"""Restore the illustrated NOIR direction; animate the existing poster, not a new identity."""
from pathlib import Path
import json,math,re,html
from PIL import Image,ImageDraw
from build_archive import symbol
R=Path(__file__).resolve().parents[1];A=R/'assets'
P='#F1E5D0';I='#20191D';W='#722F48';B='#7185B8';G='#D5A450'
projects=json.loads((R/'design/archive.json').read_text(encoding='utf-8'))['projects']
def svg(path,w,h,body,title):
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><title>{html.escape(title)}</title>{body}</svg>',encoding='utf-8')
def label(x,y,t,size,color=I,font='Georgia'):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}">{html.escape(t)}</text>'
def assets():
    # The system artwork continues directly from its blue section header.
    import xml.etree.ElementTree as ET
    for name in ('system.svg','system-mobile.svg'):
        path=A/'graphics'/name
        raw=path.read_text(encoding='utf-8');root=ET.fromstring(raw)
        w=int(root.get('width'));height=int(root.get('height'))
        if root.get('viewBox').startswith('0 0 '):
            raw=raw.replace(f'viewBox="0 0 {w} {height}"',f'viewBox="0 180 {w} {height-325}"').replace(f'height="{height}"',f'height="{height-325}"',1)
            path.write_text(raw,encoding='utf-8')
    for slug,n,title,bg,fg in [('work','01','Selected work.',I,P),('system','02','What I build with.',B,I),('experience','03','Out in the field.',G,I),('focus','04','Still figuring things out.',P,W),('connect','05','Say hello.',W,P)]:
        b=f'<rect width="1000" height="122" fill="{bg}"/>'+label(26,77,n,48,fg,'monospace')+label(130,80,title,47,fg)
        b+=f'<path d="M102 21V102M21 112Q340 119 650 111T980 114" fill="none" stroke="{fg}" stroke-width="2" opacity=".55"/>'
        b+=f'<path d="M927 20Q930 46 953 50Q930 53 927 78Q922 53 903 50Q922 45 927 20Z" fill="{fg}"/>'
        svg(A/'graphics'/f'illustrated-{slug}.svg',1000,122,b,n+' / '+title)
    for idx,p in enumerate(projects,1):
        bg=[W,B,G,'#C4523E'][idx-1];fg=P if idx in (1,4) else I
        for mobile in (False,True):
            w,h=(600,230) if mobile else (1000,195)
            b=f'<rect width="{w}" height="{h}" fill="{bg}"/><path d="M0 {h-7}Q90 {h-1} 180 {h-8}T400 {h-5}T700 {h-7}T1000 {h-6}" stroke="{fg}" stroke-width="3" fill="none" opacity=".4"/>'
            b+=f'<g transform="translate(22 24) rotate(-4 50 50)"><path d="M0 0L103 3L100 109L-3 105Z" fill="{P}" stroke="{I}" stroke-width="2"/><g transform="translate(10 9) scale(.82)">{symbol(p["id"],I)}</g></g>'
            b+=label(147,42,f'0{idx} / {p["verb"]}',18,fg,'monospace')+label(142,103,p['name'],44 if mobile else 56,fg)
            if mobile:
                b+=label(25,166,' / '.join(p['stack'][:2]),23,fg,'Arial')+label(25,204,' / '.join(p['stack'][2:]),23,fg,'Arial')
            else:b+=label(147,151,' / '.join(p['stack']),23,fg,'Arial')
            if not mobile:b+=f'<path d="M849 119Q902 153 955 102M935 99L960 98L954 121" fill="none" stroke="{fg}" stroke-width="3"/>'
            svg(A/'projects'/f'{p["id"]}-illustrated{"-mobile" if mobile else ""}.svg',w,h,b,p['name']+' / '+' / '.join(p['stack']))
def motion():
    base=Image.open(A/'hero/noir-cover.jpg').convert('RGB').resize((1200,400),Image.Resampling.LANCZOS)
    base.resize((1080,360),Image.Resampling.LANCZOS).save(A/'hero/illustrated-still.png')
    # A small paper drift in the emblem panel; the name and left-hand lettering stay still.
    frames=[];pal=base.resize((1080,360),Image.Resampling.LANCZOS).quantize(colors=128);n=96
    for k in range(n):
        t=2*math.pi*k/n
        mesh=[]
        for x in range(0,1200,20):
            weight=max(0,min(1,(x-730)/220)); dy=3*math.sin(t)*weight
            for y in range(0,400,80):
                top=y+dy*math.sin(math.pi*y/400);bottom=y+80+dy*math.sin(math.pi*(y+80)/400)
                mesh.append(((x,y,x+20,y+80),(x,top,x,bottom,x+20,bottom,x+20,top)))
        im=base.transform(base.size,Image.Transform.MESH,mesh,Image.Resampling.BICUBIC)
        # An ochre ink dot travels along the existing orbital gesture.
        d=ImageDraw.Draw(im);cx=937+224*math.cos(t);cy=172+61*math.sin(t)+.12*(cx-937)
        trail=[]
        for j in range(8):
            a=t-.10+j*.10/7;px=937+224*math.cos(a);py=172+61*math.sin(a)+.12*(px-937);trail.append((px,py))
        d.line(trail,fill=G,width=2)
        d.ellipse((cx-2.5,cy-2.5,cx+2.5,cy+2.5),fill=G)
        frames.append(im.resize((1080,360),Image.Resampling.LANCZOS).quantize(palette=pal,dither=Image.Dither.NONE))
    frames[0].save(A/'hero/illustrated-loop.gif',save_all=True,append_images=frames[1:],duration=[80,80,90]*32,loop=0,optimize=True,disposal=1)
def readme():
    s='''<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero/illustrated-still.png">
  <img src="assets/hero/illustrated-loop.gif" width="1200" alt="Aditya Gholap / NOIR — the original ink-and-paper collage, with subtle motion around the N7 emblem. Software, cloud and web.">
</picture>

**Aditya Gholap / NoirPrimordial7**<br>
Software · Cloud · Creative Technology<br>
B.Tech CSE — Cloud Computing · MIT-ADT University · Pune, India

I build systems that turn ideas into working products.

[Selected work ↓](#selected-work) · [System ↓](#system) · [Résumé ↗](docs/resume.md) · [Contact ↓](#connect)

<br>

<a id="selected-work"></a>
<h2><img src="assets/graphics/illustrated-work.svg" width="1000" alt="01 / Selected work"></h2>

'''
    for p in projects:
        s+=f'''<a href="https://github.com/NoirPrimordial7/{p['repo']}"><picture><source media="(max-width: 600px)" srcset="assets/projects/{p['id']}-illustrated-mobile.svg"><img src="assets/projects/{p['id']}-illustrated.svg" width="1000" alt="{p['name']} — {' / '.join(p['stack'])}"></picture></a>

{p['description']}<br>
[Source ↗](https://github.com/NoirPrimordial7/{p['repo']}) · [Case notes ↗](docs/cases/{p['id']}.md)'''
        if p.get('live'):s+=f" · [Live app ↗]({p['live']})"
        s+='\n\n<br>\n\n'
    s+='''---

<a id="system"></a>
<h2><img src="assets/graphics/illustrated-system.svg" width="1000" alt="02 / What I build with"></h2>

<picture><source media="(max-width: 600px)" srcset="assets/graphics/system-mobile.svg"><img src="assets/graphics/system.svg" width="1000" alt="Code: Python, Java, JavaScript, TypeScript, C++. Build: React, Next.js, Flutter. Backend: FastAPI, Firebase, PostgreSQL, Supabase. Cloud: AWS fundamentals, Docker. Intelligence: TensorFlow, OpenCV, Pandas, NumPy."></picture>

<details><summary>Read the stack as text</summary>

**Code** — Python · Java · JavaScript · TypeScript · C++<br>
**Build** — React · Next.js · Flutter<br>
**Backend & data** — FastAPI · Firebase · PostgreSQL · Supabase<br>
**Cloud** — AWS fundamentals · Docker<br>
**Intelligence** — TensorFlow · OpenCV · Pandas · NumPy

</details>

<br>

---

<h2><img src="assets/graphics/illustrated-experience.svg" width="1000" alt="03 / Experience — out in the field"></h2>

**PlaceMantra Private Ltd · Cloud Computing Intern**<br>
June–August 2025

Practical experience with AWS fundamentals, networking and deployment.

<br>

---

<h2><img src="assets/graphics/illustrated-focus.svg" width="1000" alt="04 / Current focus — still figuring things out"></h2>

**DSA** → [My learning journal ↗](https://github.com/NoirPrimordial7/-leetcode-learning-journal)<br>
**AWS** → Cloud fundamentals<br>
**Kubernetes** → Exploring

<br>

---

<a id="connect"></a>
<h2><img src="assets/graphics/illustrated-connect.svg" width="1000" alt="05 / Connect — say hello"></h2>

[GitHub ↗](https://github.com/NoirPrimordial7) · [LinkedIn ↗](https://www.linkedin.com/in/aditya-gholap-574641374) · [Email ↗](mailto:adityagholap19.06@gmail.com)

<img src="assets/graphics/noir-signature.svg" width="1000" alt="Made of questions. Built with code.">
'''
    (R/'README.md').write_text(s,encoding='utf-8')
if __name__=='__main__':assets();motion();readme()
