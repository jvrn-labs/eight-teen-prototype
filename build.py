"""Build the GitHub Pages site (index.html) from the artifact page fragment.

The artifact source (eight-teen-prototype.html) has no <html>/<head>/<body>
because claude.ai wraps it at publish time. This script adds that shell plus
the web-app meta tags, manifest link and service worker for mobile installs.
Run:  python3 build.py
"""
from pathlib import Path
import hashlib

root = Path(__file__).parent
frag = (root / "eight-teen-prototype.html").read_text(encoding="utf-8")
_h = hashlib.sha1(frag.encode())
for _p in sorted(list((root / "icons").glob("*")) + list((root / "img").rglob("*.jpg")) + list((root / "img").rglob("*.gif")) + [root / "build.py", root / "sw.template.js", root / "manifest.webmanifest"]):
    _h.update(_p.read_bytes())
version = _h.hexdigest()[:8]

head = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,interactive-widget=resizes-content">
<meta name="description" content="EIGHT TEEN MVP 1 clickable prototype: verified campus social for Thai university students.">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b1026" media="(prefers-color-scheme: dark)">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="EIGHT TEEN">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html,body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
@media (max-width:520px){html,body{overflow:hidden;overscroll-behavior:none}}
</style>
</head>
<body>
"""
tail = f"""
<script>
if ('serviceWorker' in navigator) {{
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js?v={version}').catch(() => {{}}));
}}
</script>
</body>
</html>
"""
(root / "index.html").write_text(head + frag + tail, encoding="utf-8")

sw = (root / "sw.template.js").read_text(encoding="utf-8").replace("__VERSION__", version)
(root / "sw.js").write_text(sw, encoding="utf-8")
print("built index.html and sw.js, version", version)
