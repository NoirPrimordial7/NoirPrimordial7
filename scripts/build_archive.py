"""Build the NOIR editorial assets. Python + Pillow; no network required."""
from pathlib import Path
import json, math, re, html, base64
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'
PAPER='#F1E5D0'; INK='#20191D'; WINE='#722F48'; GOLD='#D5A450'; BLUE='#7185B8'
projects=json.loads((ROOT/'design/archive.json').read_text(encoding='utf-8'))['projects']
def txt(x,y,s,size=20,fill=INK,family='Arial',extra=''):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" {extra}>{html.escape(s)}</text>'
def svg(path,w,h,body,title):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{html.escape(title)}</title><rect width="{w}" height="{h}" fill="{PAPER}"/>{body}</svg>',encoding='utf-8')
def rule(y,w=1000): return f'<path d="M32 {y}H{w-32}" stroke="{INK}" stroke-opacity=".3"/>'
def emblem(x,y,size):
    data=base64.b64encode((A/'identity/noir-n7-emblem.png').read_bytes()).decode()
    return f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="data:image/png;base64,{data}"/>'
def symbol(pid,color=INK):
    base=f'fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
    paths={
      'tendermate':'M22 12H64L80 28V88H22Z M64 12V30H80 M35 44H66 M35 57H57 M35 70H48 M61 65L68 73L91 49',
      'resolvex':'M15 17H84V70H57L33 90V70H15Z M32 35L67 56 M67 35L32 56',
      'kumbh':'M50 8L88 23V49Q86 78 50 94Q14 78 12 49V23Z M28 52Q50 24 72 52 M33 68Q50 48 67 68',
      'nearnest':'M50 94Q9 56 16 31Q24 2 50 8Q84 5 85 38Q86 57 50 94Z M28 44L50 25L72 44 M34 42V65H66V42 M46 65V51H56V65'}
    return f'<g {base}><path d="{paths[pid]}"/></g>'
def logo(name,x,y,size,color):
    raw=(A/'tech'/f'{name}.svg').read_text(encoding='utf-8')
    view=re.search(r'viewBox="([^"]+)"',raw)
    body=re.sub(r'^.*?<svg[^>]*>|</svg>\s*$','',raw,flags=re.S)
    if name=='nextjs':
        # Preserve the official white N cutout against the dark circular field.
        body=body.replace('<circle ',f'<circle fill="{color}" ').replace('#fff',PAPER)
        return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 128 128">{body}</svg>'
    # Flatten the official silhouettes into controlled ink modules; keep alpha.
    fid='mono'+name.replace('-','')
    rgb=tuple(int(color[i:i+2],16)/255 for i in (1,3,5))
    filt=f'<filter id="{fid}" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 {rgb[0]} 0 0 0 0 {rgb[1]} 0 0 0 0 {rgb[2]} 0 0 0 1 0"/></filter>'
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="{view.group(1) if view else "0 0 128 128"}">{filt}<g filter="url(#{fid})">{body}</g></svg>'

def build():
    for i,p in enumerate(projects,1):
        svg(A/'projects'/f'{p["id"]}-mark.svg',100,100,symbol(p['id']),p['name']+' original NOIR mark')
        for mobile in (False,True):
            w,h=(600,310) if mobile else (1000,256)
            b=f'<rect x="0" width="9" height="{h}" fill="{p["color"]}"/>'
            b+=txt(32,38,f'CASE / 0{i}     {p["verb"]}',18,WINE,'monospace')+rule(56,w)
            b+=txt(32,125,p['name'],49 if mobile else 65,INK,'Georgia')
            b+=txt(34,161 if mobile else 170,p['category'],15 if mobile else 19,WINE,'monospace')
            if mobile:
                b+=txt(32,227,' / '.join(p['stack'][:2]),22)+txt(32,266,' / '.join(p['stack'][2:]),22)
            else: b+=txt(34,224,'  /  '.join(p['stack']),22)
            sz=80 if mobile else 130
            b+=f'<g transform="translate({w-sz-30} {195 if mobile else 78}) scale({sz/100})">{symbol(p["id"],p["color"])}</g>'
            svg(A/'projects'/f'{p["id"]}-case{"-mobile" if mobile else ""}.svg',w,h,b,f'CASE {i:02}: {p["name"]}. '+', '.join(p['stack']))
    rows=[('01','CODE',[('python','Python'),('java','Java'),('javascript','JS'),('typescript','TS'),('cplusplus','C++')]),
      ('02','BUILD',[('react','React'),('nextjs','Next.js'),('flutter','Flutter')]),
      ('03','BACKEND + DATA',[('fastapi','FastAPI'),('firebase','Firebase'),('postgresql','PostgreSQL'),('supabase','Supabase')]),
      ('04','CLOUD',[('amazonwebservices','AWS'),('docker','Docker')]),
      ('05','INTELLIGENCE',[('tensorflow','TensorFlow'),('opencv','OpenCV'),('pandas','Pandas'),('numpy','NumPy')])]
    for mobile in (False,True):
        w=600 if mobile else 1000; y=180
        b=txt(32,40,'02 / SYSTEM',18,WINE,'monospace')+txt(32,100,'What I build with.',40 if mobile else 57,INK,'Georgia')+txt(34,142,'Code. Cloud. Systems. Intelligence.',22)
        for idx,label,items in rows:
            b+=rule(y,w)+txt(32,y+37,idx+' / '+label,19,WINE,'monospace')
            if mobile:
                for j,(name,display) in enumerate(items):
                    xx=32+(j%3)*185; yy=y+61+(j//3)*69
                    b+=logo(name,xx,yy,30,INK)+txt(xx+39,yy+23,display,21)
                y+=70+69*math.ceil(len(items)/3)
            else:
                for j,(name,display) in enumerate(items):
                    xx=260+j*141
                    b+=logo(name,xx,y+24,31,INK)+txt(xx,y+84,display,19)
                y+=116
        b+=rule(y,w)+txt(32,y+40,'CURRENT FOCUS →',18,WINE,'monospace')
        b+=txt(32,y+82,'DSA / AWS / KUBERNETES',26,INK,'Arial')+txt(32,y+116,'Practice  /  Fundamentals  /  Exploring',18)
        svg(A/'graphics'/f'system{"-mobile" if mobile else ""}.svg',w,y+145,b,'System components: '+ '; '.join(label+': '+', '.join(d for _,d in items) for _,label,items in rows)+'. Current focus: DSA practice, AWS fundamentals, exploring Kubernetes.')
    b=txt(32,40,'03 / EXPERIENCE — FIELD LOG',18,WINE,'monospace')+rule(60)+txt(32,115,'PlaceMantra',45,INK,'Georgia')+txt(32,155,'Cloud Computing Intern',25)+txt(32,200,'JUN — AUG 2025',19,WINE,'monospace')+txt(32,235,'AWS · Networking · Deployment',24)
    svg(A/'graphics/field-log.svg',1000,268,b,'PlaceMantra — Cloud Computing Intern. June–August 2025. AWS, networking and deployment.')
    for name,label,path in [('github','GITHUB ↗','M12 5Q0 7 3 21L8 24V17Q3 14 6 9L6 4L11 7L17 7L22 4V10Q25 15 20 18V24'),('linkedin','LINKEDIN ↗','M4 11V25M4 5V6M12 25V11M12 17Q23 5 23 18V25'),('email','EMAIL ↗','M2 6H27V25H2Z M2 7L15 18L27 7')]:
        b=f'<g transform="translate(23 21) scale(1.3)" fill="none" stroke="{WINE}" stroke-width="2"><path d="{path}"/></g>'
        svg(A/'graphics'/f'contact-{name}.svg',80,80,b,label)
    hero()

def hero():
    W,H=1200,400
    mono=lambda s:ImageFont.truetype('C:/Windows/Fonts/consola.ttf',s)
    serif=lambda s:ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf',s)
    mark=Image.open(A/'identity/noir-n7-emblem.png').convert('RGBA'); mark.thumbnail((278,278))
    # Fixed grain, a few registration marks, and a warm paper field.
    import random
    rng=random.Random(7); bg=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(bg)
    for _ in range(16000):
        x,y=rng.randrange(W),rng.randrange(H); d.point((x,y),fill=rng.choice(['#E9DCC8','#EEDFCC','#F5EADA']))
    d.line((36,58,1164,58),fill=WINE,width=1)
    d.text((36,22),'00 / INTRO',font=mono(19),fill=WINE)
    d.text((853,22),'NOIR ARCHIVE / N7',font=mono(19),fill=WINE)
    d.text((30,67),'NOIR',font=serif(151),fill=INK)
    d.text((38,247),'ADITYA GHOLAP',font=mono(30),fill=INK)
    d.text((38,294),'SOFTWARE / CLOUD / CREATIVE TECHNOLOGY',font=mono(20),fill=WINE)
    d.line((36,346,1164,346),fill=INK,width=1)
    d.text((38,362),'BUILD. BREAK. LEARN. REPEAT.',font=mono(20),fill=INK)
    d.text((900,362),'PUNE, INDIA',font=mono(20),fill=WINE)
    frames=[]
    for i in range(84):
        im=bg.copy(); t=i/12; layer=Image.new('RGBA',(W,H)); ld=ImageDraw.Draw(layer)
        # Opening construction and closing dispersal share the same continuous envelope.
        progress=min(1,t/1.4,(7-t)/.7); progress=max(0,progress)
        for k in range(14):
            y0=round(k*mark.height/14); y1=round((k+1)*mark.height/14)
            part=mark.crop((0,y0,mark.width,y1)); displacement=round((1-progress)**2*(65 if k%2 else -65))
            layer.alpha_composite(part,(864+displacement,65+y0))
        if progress<1: layer.putalpha(layer.getchannel('A').point(lambda a:int(a*progress)))
        im=Image.alpha_composite(im.convert('RGBA'),layer).convert('RGB')
        dr=ImageDraw.Draw(im)
        # One measured travelling registration line; no flashing.
        x=40+int(730*((i/84)%1)); dr.line((x,338,x+32,338),fill=GOLD,width=4)
        frames.append(im)
    frames[36].save(A/'hero/archive-still.png',optimize=True)
    palette=frames[36].quantize(colors=96)
    q=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    q[0].save(A/'hero/archive-loop.gif',save_all=True,append_images=q[1:],duration=[80,80,90]*28,loop=0,optimize=True,disposal=1)
if __name__=='__main__': build()
