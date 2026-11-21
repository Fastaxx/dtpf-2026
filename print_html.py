"""Make the copy of the rendered deck used for the PDF: every animation frozen on a chosen frame.
The four <video> elements (in deck order: rising bubble, tin, dissolving body, boiling bubble) lose their source and show a
chosen frame as poster; the swarm GIF becomes a chosen PNG frame. The frames are in figures/print/.
    python3 print_html.py talk.html talk-print.html"""
import base64, os, re, sys
src, dst = sys.argv[1], sys.argv[2]
H = os.path.dirname(os.path.abspath(__file__))
def uri(name):
    return "data:image/png;base64," + base64.b64encode(open(os.path.join(H, "figures", "print", name), "rb").read()).decode()
s = open(src, encoding="utf-8").read()
videos = list(re.finditer(r"<video\b[^>]*>\s*</video>", s))
assert len(videos) == 4, f"expected 4 videos, found {len(videos)}"
for m, name in reversed(list(zip(videos, ("hysing3d.png", "gal_tin.png", "gal_disk.png", "boiling.png")))):
    tag = m.group(0)
    tag = re.sub(r'\ssrc="[^"]*"', "", tag)
    tag = re.sub(r'\sposter="[^"]*"', "", tag)
    tag = re.sub(r"\sdata-autoplay\b", "", tag)
    tag = tag.replace("<video", f'<video poster="{uri(name)}" preload="none"', 1)
    s = s[:m.start()] + tag + s[m.end():]
gifs = re.findall(r'src="data:image/gif;base64,[^"]*"', s)
assert len(gifs) == 1, f"expected 1 GIF, found {len(gifs)}"
s = s.replace(gifs[0], f'src="{uri("swarm.png")}"')
open(dst, "w", encoding="utf-8").write(s)
print(f"{dst}: 4 videos and 1 GIF frozen")
