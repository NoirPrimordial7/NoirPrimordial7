"""NOIR v2: original vector project marks and hand-drawn motion strip.
No network. Run with Python + Pillow. Uses Windows Georgia / Consolas.
AI-created identity/cover files are preserved separately, not regenerated here.
"""
from pathlib import Path
from math import sin, cos, pi
import json, random
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'
P={'paper':'#F1E5D0','ink':'#20191D','wine':'#722F48','blue':'#7185B8','red':'#C4523E','gold':'#D5A450','rose':'#D8AAA7'}
INK=P['ink']; PAPER=P['paper']

def star(cx,cy,r,fill):
    return f'<path d="M{cx} {cy-r}Q{cx+3} {cy-3} {cx+r} {cy}Q{cx+3} {cy+3} {cx} {cy+r}Q{cx-3} {cy+3} {cx-r} {cy}Q{cx-3} {cy-3} {cx} {cy-r}Z" fill="{fill}"/>'

def mark(n, c=INK, accent=P['red']):
    # Each mark is drawn in a 100 × 100 coordinate space.
    if n=='nearnest':
        return f'''<g fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M50 94C39 76 15 56 16 35C18 5 79 2 84 34C88 57 60 82 50 94Z"/>
        <path d="M30 43L50 25L71 43M34 40V62H66V40M46 61V48H56V61"/>
        </g><path d="M32 75Q49 88 69 74" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>'''
    if n=='market':
        return f'''<g stroke="{c}" stroke-linecap="round" stroke-linejoin="round" fill="none">
        <path d="M50 7C74 6 94 26 92 51C90 77 75 93 49 93C22 92 7 74 8 49C7 25 25 8 50 7Z" stroke-width="4"/>
        <path d="M50 1V13M99 50H87M50 99V87M1 50H13" stroke-width="4"/>
        <path d="M24 68L39 51L49 61L74 30M59 31L75 28L73 44" stroke-width="6"/>
        </g><path d="M27 76L50 68L43 61Z" fill="{accent}"/>'''
    if n=='wildlife':
        return f'''<g stroke="{c}" stroke-width="4" fill="none" stroke-linecap="round">
        <path d="M7 31V8H30M70 8H93V31M93 69V92H70M30 92H7V69"/>
        <path d="M16 50Q49 12 84 50Q51 89 16 50Z"/>
        </g><path d="M35 62C28 51 38 46 42 43C45 37 54 37 58 43C62 47 71 52 65 62C62 68 55 65 50 65C44 65 39 70 35 62Z" fill="{c}"/>
        <ellipse cx="32" cy="40" rx="5" ry="7" fill="{accent}" transform="rotate(-25 32 40)"/>
        <ellipse cx="46" cy="31" rx="5" ry="7" fill="{accent}"/>
        <ellipse cx="60" cy="34" rx="5" ry="7" fill="{accent}" transform="rotate(20 60 34)"/>
        <ellipse cx="70" cy="45" rx="4" ry="6" fill="{accent}" transform="rotate(30 70 45)"/>'''
    return f'''<g fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M70 13C96 28 99 63 79 82C61 101 24 92 12 70C-1 46 10 19 31 10"/>
    <path d="M50 5V13M93 50H85M50 94V86M8 50H16M48 70L71 76"/>
    <path d="M35 66C20 34 48 22 76 24C76 55 60 71 35 66Z"/>
    <path d="M28 81Q42 55 63 37"/>
    </g><path d="M45 55Q44 36 65 33Q65 49 45 55Z" fill="{accent}"/>'''

def svg(path,w,h,body,title):
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{title}</title>{body}</svg>',encoding='utf-8')

projects=[('nearnest','NearNest','01 / LOCAL STORES &amp; SERVICES',P['red'],PAPER,P['gold']),
          ('market','Market Navigator','02 / DATA, TRENDS &amp; CURIOSITY',P['gold'],INK,P['wine']),
          ('wildlife','Wildlife Recognition','03 / A CLOSER LOOK AT NATURE',P['blue'],INK,P['wine']),
          ('eco-watch','Eco Watch','04 / WILDLIFE &amp; AWARENESS',P['wine'],PAPER,P['gold'])]

def build_vectors():
    for name,title,label,bg,fg,accent in projects:
        svg(A/'projects'/f'{name}-logo.svg',100,100,mark(name,INK,accent),title+' — custom project mark')
        # Brand plate is intentionally a single row, readable on mobile, not a 2-column table.
        b=f'<rect width="1200" height="164" fill="{bg}"/><path d="M0 155L29 158L51 154L81 160L114 156L160 159L195 155L250 160L300 156L350 159L410 155L460 160L520 156L570 159L630 155L680 160L730 156L790 159L850 155L910 160L970 156L1040 160L1110 156L1200 158V164H0Z" fill="{fg}" opacity=".32"/>'
        b+=f'<path d="M34 25L151 17L161 137L42 144Z" fill="{PAPER}" stroke="{INK}" stroke-width="2"/><g transform="translate(48 29) scale(1.02)">{mark(name,INK,accent)}</g>'
        b+=f'<text x="196" y="49" font-family="monospace" font-size="14" letter-spacing="1" fill="{fg}">{label}</text><text x="190" y="115" font-family="Georgia,serif" font-size="59" font-weight="700" letter-spacing="-2" fill="{fg}">{title}</text>'
        b+=f'<path d="M1055 101Q1110 130 1154 77M1132 78L1158 74L1152 99" fill="none" stroke="{fg}" stroke-width="3" stroke-linecap="round"/>'
        b+=star(1100,44,20,fg)
        for y in range(12,145,9):
            for x in range(1190-int((y/8)**1.35),1200,9):b+=f'<circle cx="{x}" cy="{y}" r="1.1" fill="{fg}" opacity=".3"/>'
        svg(A/'projects'/f'{name}-plate.svg',1200,164,b,title)
    b=f'<rect width="1200" height="112" fill="{PAPER}"/><text x="24" y="35" fill="{P["wine"]}" font-family="monospace" font-size="14">THE TOOLBOX / ALWAYS EXPANDING</text><text x="21" y="86" fill="{INK}" font-family="Georgia,serif" font-size="49" font-style="italic">A little logic. A lot of curiosity.</text>'
    b+=f'<path d="M896 27L867 54L897 82M942 19L923 90M972 27L1002 54L972 82" fill="none" stroke="{P["red"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    b+=star(1080,52,28,P['wine'])
    svg(A/'graphics'/'noir-toolbox.svg',1200,112,b,'The toolbox — a little logic, a lot of curiosity')
    b=f'<rect width="1200" height="110" fill="{P["wine"]}"/><text x="28" y="38" fill="{P["gold"]}" font-family="monospace" font-size="14">NOIRPRIMORDIAL7 / PUNE, INDIA</text><text x="26" y="85" fill="{PAPER}" font-family="Georgia,serif" font-size="38" font-style="italic">Made of questions. Built with code.</text>'
    b+=f'<path d="M916 63Q955 15 1007 52T1140 51M1120 42L1146 49L1133 70" fill="none" stroke="{P["gold"]}" stroke-width="3" stroke-linecap="round"/>'
    svg(A/'graphics'/'noir-signature.svg',1200,110,b,'NoirPrimordial7 — made of questions, built with code')

def motion():
    S=2; W,H=1200,100
    serif=ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf',33*S)
    small=ImageFont.truetype('C:/Windows/Fonts/consola.ttf',12*S)
    frames=[]
    for i in range(72):
        t=2*pi*i/72
        im=Image.new('RGB',(W*S,H*S),PAPER);d=ImageDraw.Draw(im)
        def ln(points,c=INK,w=2): d.line([(x*S,y*S) for x,y in points],fill=c,width=round(w*S),joint='curve')
        d.text((28*S,15*S),'THE NOIR LOOP',font=small,fill=P['wine'])
        for j,word in enumerate(['BUILD','BREAK','LEARN','REPEAT']):
            x=221+j*228
            d.text((x*S,34*S),word,font=serif,fill=INK)
            # Each phase briefly underlines one stage; hand-drawn underline flows smoothly.
            power=max(0,cos(t-j*pi/2))**4
            if power>.01:
                yy=78
                ln([(x,yy),(x+50*power,yy+2*sin(t+j)),(x+135*power,yy-2)],P['red'],3)
            if j<3:
                x+=174; yy=51+2*sin(t+j)
                ln([(x-7,yy),(x+20,yy-3),(x+14,yy-10)],P['wine'],2)
                ln([(x+20,yy-3),(x+12,yy+6)],P['wine'],2)
        # A small ochre asterisk turns at the margin; name never moves.
        cx,cy=158,59
        for k in range(6):
            a=k*pi/3+t/6
            ln([(cx+7*cos(a),cy+7*sin(a)),(cx+20*cos(a),cy+20*sin(a))],P['gold'],4)
        ln([(20,98),(310,97),(570,99),(900,97),(1180,99)],P['ink'],.6)
        im=im.resize((W,H),Image.Resampling.LANCZOS)
        if i==0:
            im.save(A/'graphics'/'noir-loop-still.png')
            pal=im.quantize(colors=64)
        frames.append(im.quantize(palette=pal,dither=Image.Dither.NONE))
    frames[0].save(A/'graphics'/'noir-loop.gif',save_all=True,append_images=frames[1:],duration=[80,80,90]*24,loop=0,optimize=True,disposal=1)

if __name__=='__main__':
    (A/'projects').mkdir(exist_ok=True)
    build_vectors();motion()
    (ROOT/'design'/'palette.json').write_text(json.dumps({'name':'NOIR — Ink & Curiosity','colors':P,'typography':{'display':'Expressive editorial serif / Georgia','labels':'Consolas / monospace','body':'GitHub native UI font'},'principles':['No faces or portraits','No neon green','Black ink, torn paper, comic halftone','Legible names and selectable project copy']},indent=2),encoding='utf-8')
    print('Built 4 project logos, 4 brand plates, 2 sections, 6-second motion loop and palette.json.')
