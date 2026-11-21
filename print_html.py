"""Make the copy of the rendered deck used for the PDF: every animation frozen on a chosen frame.
The five <video> elements (in deck order: rising bubble, tin, dissolving body, boiling bubble, appendix boiling split) lose their source and show a
chosen frame as poster; the swarm GIF becomes a chosen PNG frame (frames in figures/print/); slide 10, whose loop diagram and
convergence plot share one column, is printed twice.
    python3 print_html.py talk.html talk-print.html"""
import base64, os, re, sys
src, dst = sys.argv[1], sys.argv[2]
H = os.path.dirname(os.path.abspath(__file__))
def uri(name):
    return "data:image/png;base64," + base64.b64encode(open(os.path.join(H, "figures", "print", name), "rb").read()).decode()
s = open(src, encoding="utf-8").read()
videos = list(re.finditer(r"<video\b[^>]*>\s*</video>", s))
assert len(videos) == 5, f"expected 5 videos, found {len(videos)}"
for m, name in reversed(list(zip(videos, ("hysing3d.png", "gal_tin.png", "gal_disk.png", "boiling.png", "boiling_split.png")))):
    tag = m.group(0)
    tag = re.sub(r'\ssrc="[^"]*"', "", tag)
    tag = re.sub(r'\sposter="[^"]*"', "", tag)
    tag = re.sub(r"\sdata-autoplay\b", "", tag)
    tag = tag.replace("<video", f'<video poster="{uri(name)}" preload="none"', 1)
    s = s[:m.start()] + tag + s[m.end():]
gifs = re.findall(r'src="data:image/gif;base64,[^"]*"', s)
assert len(gifs) == 2, f"expected 2 GIFs, found {len(gifs)}"
for g, name in zip(gifs, ("frank.png", "swarm.png")):          # deck order: Frank sphere (slide 10), swarm (closing)
    s = s.replace(g, f'src="{uri(name)}"')
# slide 10 stacks the loop diagram and the convergence plot in one column (one per click): print it twice,
# the diagram first, then the plot
sid = 'id="moving-the-interface-one-residual-a-newton-iteration"'
i = s.rfind("<section", 0, s.index(sid))
j = s.index("</section>", i) + len("</section>")
sec = s[i:j]
loop = (sec.replace(sid, 'id="newton-loop-print"')
        .replace('class="nwplot fragment"', 'class="nwplot fragment" style="display:none"')
        .replace('class="nwloop2 fragment current-visible"', 'class="nwloop2"'))
plot = (sec.replace(sid, sid + ' data-visibility="uncounted"')
        .replace('class="nwloop2 fragment current-visible"', 'class="nwloop2 fragment current-visible" style="display:none"'))
assert loop != sec and plot != sec, "slide 10 markup changed"
s = s[:i] + loop + plot + s[j:]
open(dst, "w", encoding="utf-8").write(s)
print(f"{dst}: 5 videos and 2 GIFs frozen")
