"""Check delivery integrity without network access: python scripts/validate_assets.py."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops, ImageStat

root = Path(__file__).resolve().parents[1]
readme = (root / 'README.md').read_text(encoding='utf-8-sig')
for ref in re.findall(r'(?:src|srcset)="([^"]+)"', readme):
    assert (root / ref).is_file(), f'Missing asset: {ref}'
for asset in (root / 'assets').rglob('*.svg'):
    tree = ET.parse(asset)
    assert tree.getroot().get('viewBox'), asset
    assert not any(n.tag.split('}')[-1] in ('script', 'foreignObject', 'image') for n in tree.iter())
gif = Image.open(root / 'assets/hero/illustrated-loop.gif')
assert gif.size == (1080, 360)
assert gif.n_frames == 96
assert gif.info.get('loop') == 0
assert len(list((root / 'assets/projects').glob('*-illustrated.svg'))) == 4
assert (root / 'assets/identity/noir-avatar.jpg').stat().st_size < 1_000_000
assert 'hero-loop.gif' not in readme
assert 'A8E66A' not in readme
assert (root / 'assets/hero/illustrated-loop.gif').stat().st_size < 5_000_000
assert '| What' not in readme
for ref in re.findall(r'\]\(([^)]+)\)',readme):
    if not ref.startswith(('https://','mailto:','#')):
        assert (root/ref.split('#')[0]).exists(),ref
if (root/'docs/index.html').exists():
    for ref in re.findall(r'(?:src|href)="([^"]+)"',(root/'docs/index.html').read_text(encoding='utf-8')):
        if not ref.startswith(('https://','mailto:','#')):assert (root/'docs'/ref).exists(),ref
duration = 0
frames = []
for i in range(gif.n_frames):
    gif.seek(i)
    duration += gif.info['duration']
    frames.append(gif.convert('RGB'))
assert duration == 8000
diffs = [sum(ImageStat.Stat(ImageChops.difference(frames[i],frames[(i+1)%96])).mean)/3 for i in range(96)]
assert max(diffs) > 0, 'Animation is static'
assert diffs[-1] < max(diffs[:-1])*1.5, 'Loop seam is unusually large'
print(f'PASS: assets, local links, SVG safety, 96 moving frames, {duration} ms, infinite loop, size budget.')
print(f'Frame change: mean={sum(diffs)/96:.3f}; seam={diffs[-1]:.3f}; maximum={max(diffs):.3f}')

