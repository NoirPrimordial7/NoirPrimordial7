# Illustrated NOIR profile

The current README uses the original collage header with an eight-second loop, colored project plates and distinct section dividers. Essential descriptions remain native Markdown.

Update factual project content in `design/archive.json`. With Pillow installed and Windows Georgia/Consolas fonts available:

```sh
python scripts/build_archive.py
python scripts/restore_illustrated.py
python scripts/validate_assets.py
```

Run both builders in this order: the second restores the illustrated direction and crops the system diagram beneath its section header. The original `assets/hero/noir-cover.jpg` is the animation source. Reduced-motion readers receive the still version.

Technology logo sources and attribution are included in `assets/tech/`.
