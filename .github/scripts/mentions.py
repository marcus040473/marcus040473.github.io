"""Sammelt die Discussions in henmedia/layerling, in denen @marcus040473 um etwas gebeten wird,
und schreibt sie als Markdown nach stdout."""
import json
import os
import re
import subprocess
import sys

OWNER, REPO, ME = "henmedia", "layerling", "marcus040473"
PAGES = 4  # die 100 zuletzt geänderten Discussions
ASK = re.compile(r"have a look|take a look|could you|can you|please|hand this to him|is yours|are yours", re.I)

QUERY = """query($after:String){ repository(owner:"%s", name:"%s"){ discussions(first:25, after:$after, orderBy:{field:UPDATED_AT,direction:DESC}){
 pageInfo{hasNextPage endCursor}
 nodes{ number title url updatedAt category{name} author{login} body
  comments(first:50){ nodes{ author{login} body createdAt url replies(first:30){ nodes{ author{login} body createdAt url } } } } } } } }""" % (OWNER, REPO)


def fetch():
    nodes, after = [], None
    for _ in range(PAGES):
        cmd = ["gh", "api", "graphql", "-f", "query=" + QUERY]
        if after:
            cmd += ["-f", "after=" + after]
        data = json.loads(subprocess.check_output(cmd))["data"]["repository"]["discussions"]
        nodes += data["nodes"]
        if not data["pageInfo"]["hasNextPage"]:
            break
        after = data["pageInfo"]["endCursor"]
    return nodes


def events(node):
    """Eröffnungsbeitrag zuerst, danach alle Kommentare und Antworten nach Zeit."""
    first = (node["author"] and node["author"]["login"], node["body"], "", node["url"])
    rest = []
    for c in node["comments"]["nodes"]:
        rest.append((c["author"] and c["author"]["login"], c["body"], c["createdAt"], c["url"]))
        for r in c["replies"]["nodes"]:
            rest.append((r["author"] and r["author"]["login"], r["body"], r["createdAt"], r["url"]))
    return [first] + sorted(rest, key=lambda e: e[2])


def main():
    open_asks, answered = [], 0
    for node in fetch():
        ev = events(node)
        mentions = [i for i, e in enumerate(ev) if f"@{ME}" in e[1] and e[0] != ME]
        if not mentions:
            continue
        last = mentions[-1]
        if any(e[0] == ME for e in ev[last + 1:]):
            answered += 1
            continue
        author, body, _, url = ev[last]
        if not ASK.search(body):
            continue
        text = " ".join(body.split())
        open_asks.append((node["updatedAt"], node["number"], node["title"], node["category"]["name"], author, url, text[:240]))

    open_asks.sort(reverse=True)
    print(f"_Automatisch erzeugt aus den 100 zuletzt geänderten Discussions von {OWNER}/{REPO}._\n")
    if not open_asks:
        print("Keine offenen Bitten gefunden.")
    for updated, number, title, category, author, url, text in open_asks:
        print(f"- [ ] **[#{number} {title}]({url})** ({category}, @{author}, {updated[:10]})  \n  > {text}")
    print(f"\n_{len(open_asks)} offen, {answered} Erwähnungen schon von dir beantwortet._")


if __name__ == "__main__":
    if not os.environ.get("GH_TOKEN"):
        sys.exit("GH_TOKEN fehlt")
    main()
