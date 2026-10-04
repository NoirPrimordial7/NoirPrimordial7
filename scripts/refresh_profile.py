"""Build the resume-aligned GitHub profile. Standard library only; no network."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
PAPER, INK, WINE, BLUE, GOLD = '#F1E5D0', '#20191D', '#722F48', '#7185B8', '#D5A450'
GITHUB = 'https://github.com/NoirPrimordial7/'
PROJECTS = [
    dict(id='market', name='AI-Powered Market Navigator', card='Market Navigator', verb='FORECAST', category='TIME SERIES & SENTIMENT', color=WINE,
         repo='AI-Powered-Market-Navigator', stack=['Python', 'TensorFlow / Keras', 'LSTM', 'Streamlit'], status='ML prototype',
         description='Explores stock-price trends with an LSTM model, technical indicators, and Reddit/news sentiment in an interactive Streamlit workflow.',
         detail='Historical market data is prepared with MinMax scaling and indicators including RSI, SMA, MACD, and Bollinger Bands. TensorFlow/Keras inference and VADER sentiment bring numerical and text signals into the same workflow.',
         note='A forecasting experiment. Published benchmark results and forecast accuracy are not claimed here; external data and sentiment integrations need configuration.'),
    dict(id='wildlife', name='Wildlife Recognition & Intrusion Alert System', card='Wildlife Recognition', verb='DETECT', category='COMPUTER VISION & ALERTS', color=BLUE,
         repo='wildlife_intrusion_detection_system', stack=['Python', 'TensorFlow / Keras', 'OpenCV', 'YOLOv8'], status='Desktop prototype',
         description='Combines YOLOv8 detection with species classification, then confirms danger events with confidence thresholds, repeated detections, and alert cooldowns.',
         detail='Video or webcam frames pass through YOLOv8, animal crops are classified with the existing Keras model, and confirmed danger events save evidence and detection metrics. SMS providers and registered recipients are configurable.',
         note='PC-based prototype. YOLO provides broad animal bounding boxes; the classifier identifies species from crops. SMS is disabled by default and requires provider credentials.'),
    dict(id='nearnest', name='NearNest', card='NearNest', verb='CONNECT', category='LOCAL STORES & SERVICES', color=GOLD,
         repo='nearnest-platform-2', stack=['React', 'Vite', 'Firebase Auth', 'Firestore'], status='Application foundation',
         description='A local store and service platform with account flows, store registration saved to Firestore, and separate public and admin interfaces.',
         detail='React Router organizes account, registration, and administration screens. Firebase Authentication handles identity, and the store form persists records in Firestore.',
         note='The resume-linked repository is the current portfolio reference. Admin routing exists; the current route guard checks authentication, so granular admin authorization is not claimed here.'),
    dict(id='resolvex', name='ResolveX', card='ResolveX', verb='RESOLVE', category='CUSTOMER SUPPORT & WORKFLOWS', color='#C4523E',
         repo='ResolveX', stack=['React / TypeScript', 'FastAPI', 'PostgreSQL', 'Docker'], status='Full-stack helpdesk',
         description='A customer-support ticketing system with customer, support-agent, and admin roles, JWT/RBAC, assignment, comments, filters, and reassignment workflows.',
         detail='FastAPI, SQLAlchemy, Alembic, and PostgreSQL support the ticket API. React/Vite provides role-specific screens, while Docker Compose packages the frontend, backend, and database.',
         note='The implemented scope is ticket operations and role-based access. Email notifications, attachments, SLA timers, and refresh tokens are listed as future improvements in the source repository.'),
    dict(id='tendermate', name='TenderMate AI', card='TenderMate AI', verb='ANALYZE', category='DOCUMENT AI & TENDER READINESS', color=WINE,
         repo='TenderMate-AI', stack=['Next.js', 'FastAPI', 'Supabase', 'Gemini'], status='Tender-readiness MVP',
         description='Turns tender PDFs into AI-assisted analysis with private storage, user-scoped history, text extraction, and Gemini OCR fallback for scanned documents.',
         detail='A Next.js frontend connects to FastAPI, Supabase PostgreSQL, private Supabase Storage, and Gemini. JWT authentication, rate limits, daily upload quotas, account lockout, audit logs, and trial-credit tracking support the workflow.',
         note='An MVP with separate Vercel and Render deployment flows. OCR and AI analysis depend on backend provider configuration.', live='https://tender-mate-ai.vercel.app'),
]


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def text(x, y, value, size=20, color=INK, font='Arial'):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}">{escape(value)}</text>'


def svg(path, width, height, body, title):
    write(path, f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{escape(title)}</title>{body}</svg>\n')


def icon(slug):
    paths = {
        'market': 'M10 80V18M10 80H88M20 64L38 47L53 56L78 26M63 26H78V41',
        'wildlife': 'M9 32V10H31M69 10H91V32M91 68V90H69M31 90H9V68 M30 68Q22 55 37 48Q50 32 63 48Q78 55 70 68Q62 80 50 72Q36 79 30 68 M26 36L27 31M41 27L42 22M59 27L58 22M74 36L73 31',
        'nearnest': 'M50 94Q9 56 16 31Q24 2 50 8Q84 5 85 38Q86 57 50 94Z M28 44L50 25L72 44 M34 42V65H66V42 M46 65V51H56V65',
        'resolvex': 'M15 17H84V70H57L33 90V70H15Z M31 43L44 56L68 32',
        'tendermate': 'M22 12H64L80 28V88H22Z M64 12V30H80 M35 44H66 M35 57H57 M35 70H48 M61 65L68 73L91 49',
    }
    return f'<path d="{paths[slug]}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'


def artwork():
    for index, project in enumerate(PROJECTS, 1):
        fg = INK if project['color'] in (BLUE, GOLD) else PAPER
        for mobile in (False, True):
            width, height = (600, 204) if mobile else (1000, 170)
            body = f'<rect width="{width}" height="{height}" fill="{project["color"]}"/>'
            body += f'<path d="M0 {height-6}Q90 {height} 180 {height-7}T400 {height-4}T1000 {height-6}" stroke="{fg}" stroke-width="2" fill="none" opacity=".45"/>'
            body += f'<g transform="translate(24 30) rotate(-4 44 44)"><path d="M0 0L89 2L88 94L-2 91Z" fill="{PAPER}" stroke="{INK}" stroke-width="2"/><g transform="translate(4 3) scale(.8)">{icon(project["id"])}</g></g>'
            body += text(140, 34, f'{index:02} / {project["verb"]}', 17, fg, 'monospace')
            body += text(136, 88, project['card'], 39 if mobile else 51, fg, 'Georgia')
            body += text(140, 120, project['category'], 16 if mobile else 18, fg, 'monospace')
            if mobile:
                body += text(24, 178, ' / '.join(project['stack']), 20, fg)
            else:
                body += text(140, 151, ' / '.join(project['stack']), 20, fg)
                body += f'<path d="M910 65H958M944 51L958 65L944 79" fill="none" stroke="{fg}" stroke-width="2"/>'
            svg(f'assets/projects/{project["id"]}-illustrated{"-mobile" if mobile else ""}.svg', width, height, body, project['name'] + ' | ' + ' / '.join(project['stack']))

    rows = [
        ('AI / ML', ['TensorFlow / Keras / LSTM / CNN / YOLOv8', 'OpenCV / Scikit-learn / Pandas / NumPy']),
        ('SOFTWARE', ['Python / Java / JavaScript / TypeScript / C / C++ / Dart', 'React / Vite / Next.js / Streamlit / FastAPI']),
        ('DATA / CLOUD', ['Firebase / Firestore / PostgreSQL / Supabase', 'REST APIs / JWT / RBAC / Docker / AWS fundamentals']),
    ]
    for mobile in (False, True):
        width, height = (600, 420) if mobile else (1000, 345)
        body = f'<rect width="{width}" height="{height}" fill="{PAPER}"/>'
        for index, (label, lines) in enumerate(rows):
            y = 22 + index * (136 if mobile else 107)
            body += f'<path d="M25 {y}H{width-25}" stroke="{INK}" opacity=".25"/>'
            body += text(26, y + 29, f'0{index+1} / {label}', 19, WINE, 'monospace')
            for j, line in enumerate(lines):
                body += text(26, y + 63 + j * 28, line, 17 if mobile else 23)
        svg(f'assets/graphics/system{"-mobile" if mobile else ""}.svg', width, height, body, 'AI/ML, software, data and cloud skills from Aditya Gholap’s resume')
    body = f'<rect width="1000" height="122" fill="{PAPER}"/>'
    body += text(26, 77, '04', 48, WINE, 'monospace') + text(130, 80, 'Always learning.', 47, WINE, 'Georgia')
    body += f'<path d="M102 21V102M21 112Q340 119 650 111T980 114" fill="none" stroke="{WINE}" stroke-width="2" opacity=".55"/>'
    svg('assets/graphics/illustrated-focus.svg', 1000, 122, body, '04 / Always learning')


def link(url, label):
    return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'


def section(anchor, graphic, alt):
    return f'<a id="{anchor}"></a>\n<h2><img src="assets/graphics/illustrated-{graphic}.svg" width="1000" alt="{escape(alt)}"></h2>\n'


def profile():
    content = '''<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero/illustrated-still.png">
  <img src="assets/hero/illustrated-loop.gif" width="1200" alt="Aditya Gholap / NOIR — an ink-and-paper collage with the N7 emblem.">
</picture>

<h1>Aditya Gholap <sub>/ NOIR</sub></h1>
<p><strong>AI/ML &amp; Software Engineering · Cloud Computing</strong><br>
B.Tech CSE · MIT-ADT University · Pune, India · Class of 2027</p>

<p>I turn data into predictions, images into signals, and ideas into software.<br>
My work spans machine learning, computer vision, and full-stack applications backed by cloud services.</p>

<p><a href="#selected-work">Selected work ↓</a> · <a href="#system">Toolkit ↓</a> · <a href="docs/resume.md">Résumé ↗</a> · <a href="#connect">Connect ↓</a></p>

'''
    content += section('selected-work', 'work', '01 / Selected work')
    content += '<p><strong>From models to applications.</strong> Five projects across forecasting, computer vision, local services, support workflows, and document AI.</p>\n\n'
    for project in PROJECTS:
        slug, url = project['id'], GITHUB + project['repo']
        content += f'<a href="{url}"><picture><source media="(max-width: 600px)" srcset="assets/projects/{slug}-illustrated-mobile.svg"><img src="assets/projects/{slug}-illustrated.svg" width="1000" alt="{escape(project["name"], quote=True)} — {escape(" / ".join(project["stack"]), quote=True)}"></picture></a>\n\n'
        content += f'<p><strong>{escape(project["status"])}</strong> · {escape(project["description"])}<br>\n'
        content += link(url, 'Source ↗') + ' · ' + link(f'docs/cases/{slug}.md', 'Inside the project ↗')
        if project.get('live'):
            content += ' · ' + link(project['live'], 'Live app ↗')
        content += '</p>\n\n'
    content += '<hr>\n\n' + section('system', 'system', '02 / What I build with')
    content += '''<picture><source media="(max-width: 600px)" srcset="assets/graphics/system-mobile.svg"><img src="assets/graphics/system.svg" width="1000" alt="AI/ML: TensorFlow, Keras, LSTM, CNN, YOLOv8, OpenCV, Scikit-learn, Pandas, NumPy. Software: Python, Java, JavaScript, TypeScript, C, C++, Dart, React, Vite, Next.js, Streamlit, FastAPI. Data and cloud: Firebase, Firestore, PostgreSQL, Supabase, REST APIs, JWT/RBAC, Docker, AWS fundamentals."></picture>

<details><summary>Read the toolkit as text</summary>
<p><strong>AI / ML</strong> — TensorFlow · Keras · LSTM · CNN · YOLOv8 · OpenCV · Scikit-learn · Pandas · NumPy · Data analysis &amp; visualization<br>
<strong>Programming</strong> — Python · Java · JavaScript · TypeScript · C · C++ · Dart<br>
<strong>Software / backend</strong> — React · Vite · Next.js · Streamlit · FastAPI · Firebase · Firestore · PostgreSQL · Supabase · REST APIs · JWT/RBAC · Docker · Git/GitHub<br>
<strong>Cloud / infrastructure</strong> — AWS fundamentals · Networking · Virtual machines · Storage · Cloud security · Infrastructure management</p>
</details>

<hr>

'''
    content += section('experience', 'experience', '03 / Experience — out in the field')
    content += '''<p><strong>PlaceMantra Private Ltd · Cloud Computing Intern</strong><br>
June–August 2025 · Pune</p>
<p>Project-based exposure to AWS fundamentals, networking, virtual machines, storage, cloud security, and deployment practices, with infrastructure troubleshooting and documentation.</p>

<details><summary>Education</summary>
<p><strong>MIT School of Computing, MIT-ADT University</strong><br>B.Tech CSE · Cloud Computing · 2024–2027 · CGPA: 8.0/10</p>
<p><strong>AISSMS Polytechnic College, Pune</strong><br>Diploma in Information Technology · MSBTE · 2024 · 80.31%</p>
</details>

<hr>

'''
    content += section('learning', 'focus', '04 / Always learning')
    content += '''<p>Sharpening problem-solving through <a href="https://github.com/NoirPrimordial7/-leetcode-learning-journal">my DSA learning journal ↗</a>, building on AWS fundamentals, and exploring Kubernetes.</p>

<hr>

'''
    content += section('connect', 'connect', '05 / Connect — say hello')
    content += '<p>Let’s talk about machine learning, software, or an idea worth building.</p>\n'
    content += '<p>' + ' · '.join([link(GITHUB.rstrip('/'), 'GitHub ↗'), link('https://www.linkedin.com/in/aditya-gholap-574641374', 'LinkedIn ↗'), link('mailto:adityagholap19.06@gmail.com', 'Email ↗')]) + '</p>\n\n'
    content += '<img src="assets/graphics/noir-signature.svg" width="1000" alt="Made of questions. Built with code.">\n'
    write('README.md', content)
    return content


def documents():
    for index, project in enumerate(PROJECTS, 1):
        write(f'docs/cases/{project["id"]}.md', f'# {project["name"]}\n\n**{index:02} / {project["status"]}**\n\n{project["description"]}\n\n## Inside the system\n\n{project["detail"]}\n\n**Built with:** ' + ' · '.join(project['stack']) + f'\n\n## Current scope\n\n{project["note"]}\n\n[Source repository ↗]({GITHUB + project["repo"]}) · [Back to profile](../../README.md#selected-work)\n')
    resume = '''# Aditya Gholap

AI/ML & Software Engineering · B.Tech CSE — Cloud Computing · Pune, India

[GitHub](https://github.com/NoirPrimordial7) · [LinkedIn](https://www.linkedin.com/in/aditya-gholap-574641374) · [Email](mailto:adityagholap19.06@gmail.com)

## Profile

B.Tech CSE student with hands-on experience training machine-learning models and building full-stack, cloud-connected software. Work spans LSTM forecasting, computer vision, Firebase/React applications, FastAPI/PostgreSQL backends, and AWS infrastructure fundamentals.

## Selected projects

'''
    for project in PROJECTS:
        resume += f'### [{project["name"]}]({GITHUB + project["repo"]})\n\n' + ' · '.join(project['stack']) + f'\n\n{project["description"]}\n\n{project["detail"]}\n\n'
    resume += '''## Experience

**PlaceMantra Private Ltd — Cloud Computing Intern** · Pune · June–August 2025

Completed a two-month internship covering AWS fundamentals, networking, virtual machines, storage management, cloud security, infrastructure concepts, and deployment practices. Worked through project-based infrastructure tasks involving virtualized environments, troubleshooting, documentation, and secure cloud/IT workflows.

## Education

**MIT School of Computing, MIT-ADT University** — B.Tech CSE, Cloud Computing · 2024–2027 · CGPA: 8.0/10  
**AISSMS Polytechnic College, Pune** — Diploma, Information Technology · MSBTE · 2024 · 80.31%

## Technical skills

**AI / ML:** TensorFlow · Keras · OpenCV · YOLOv8 · Scikit-learn · Pandas · NumPy · LSTM · CNN · Data analysis & visualization  
**Programming:** Python · Java · JavaScript · TypeScript · C · C++ · Dart  
**Software / backend:** FastAPI · React · Vite · Next.js · Streamlit · Firebase · Firestore · PostgreSQL · Supabase · REST APIs · JWT/RBAC · Docker · Git/GitHub  
**Cloud / infrastructure:** AWS fundamentals · Networking · Virtual machines · Storage · Cloud security · Infrastructure management

---

Adapted from the supplied résumé, with project scope clarified against the linked repositories. [Back to profile](../README.md)
'''
    write('docs/resume.md', resume.replace('  \n', '<br>\n'))
    write('design/archive.json', json.dumps({'projects': PROJECTS}, ensure_ascii=False, indent=2) + '\n')


def preview(content):
    # A base URL resolves asset paths; fragment links must retain the preview page.
    content = content.replace('href="#', 'href="preview/index.html#')
    css = '''*{box-sizing:border-box}body{margin:0;background:#0d1117;color:#f0f6fc;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}body.light{background:#fff;color:#1f2328}nav{max-width:1012px;margin:24px auto 16px;display:flex;gap:16px;align-items:center;padding:0 20px;font-size:13px}button{border:1px solid #9198a1;background:transparent;color:inherit;border-radius:6px;padding:6px 12px;cursor:pointer}article{max-width:1012px;margin:0 auto 40px;border:1px solid #3d444d;border-radius:6px;padding:32px}a{color:#4493f8;text-decoration:none}a:hover{text-decoration:underline}img{max-width:100%;height:auto;vertical-align:middle}h1{font-size:32px;line-height:1.3;border-bottom:1px solid #3d444d;padding-bottom:10px}h1 sub{font-size:16px;vertical-align:baseline;font-weight:400}h2{margin:28px 0 16px}p{margin:16px 0}hr{border:0;height:1px;background:#3d444d;margin:28px 0}summary{cursor:pointer}details p{margin-left:16px}@media(max-width:600px){article{padding:16px;border:0;border-radius:0}nav{margin:10px auto;flex-wrap:wrap;font-size:11px}h1{font-size:28px}}'''
    controls = '<nav><span>NOIR · Profile preview</span><button id="theme">Light / dark</button><button id="motion" aria-pressed="false">Still artwork</button></nav>'
    js = '''document.querySelector('#theme').onclick=()=>document.body.classList.toggle('light');document.querySelector('#motion').onclick=function(){const hero=document.querySelector('article>picture');hero.querySelector('source')?.remove();const still=this.getAttribute('aria-pressed')!=='true';hero.querySelector('img').src=still?'assets/hero/illustrated-still.png':'assets/hero/illustrated-loop.gif';this.setAttribute('aria-pressed',String(still));this.textContent=still?'Animated artwork':'Still artwork';};'''
    write('preview/index.html', f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="../"><title>Aditya Gholap / NOIR — Profile preview</title><style>{css}</style></head><body>{controls}<article>{content}</article><script>{js}</script></body></html>\n')


def build():
    artwork()
    documents()
    preview(profile())
    print('Built profile, five project cards with mobile variants, toolkit, resume, case notes, and preview.')


if __name__ == '__main__':
    build()
