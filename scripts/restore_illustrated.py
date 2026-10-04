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
if __name__ == '__main__':
    # The resume-aligned builder keeps the existing illustrated hero intact.
    from refresh_profile import build
    build()
