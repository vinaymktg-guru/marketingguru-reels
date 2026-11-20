import re, os, glob, asyncio
from playwright.async_api import async_playwright
B={"aca7c265850dd2ee486de2f50aa87a51":"img/prerna-blazer.jpg","90c449f20c847c4e5d6a573204358be7":"img/prerna-saree.jpg",
"bdf38b2c0384d91e00070f0ca90f3d58":"img/priyanka-crop.jpg","ccec02b2e2ac0e05c35ffe0608230e62":"img/vijaylaxmi.jpg","54ac47461b540dc6a8024f1646db7f36":"img/nisha.jpg"}
FONT="file:///home/claude/fonts/Outfit.ttf"
def conv(src):
    s=open(src).read()
    body=s[s.index('<x-dc>')+6:s.index('</x-dc>')]
    body=re.sub(r'<helmet>.*?</helmet>','',body,flags=re.S)
    for k,v in B.items(): body=body.replace('/_blob/'+k,'file:///home/claude/mbc/'+v)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>@font-face{{font-family:Outfit;src:url({FONT});font-weight:100 900}}body{{margin:0}}</style></head><body>{body}</body></html>'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for f in sorted(glob.glob('project/*.dc.html')):
            name=os.path.basename(f).replace('.dc.html','')
            h=f'render/{name}.html'; open(h,'w').write(conv(f))
            await pg.goto('file:///home/claude/mbc/'+h); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'png/{name}.png',clip={"x":0,"y":0,"width":1080,"height":1350})
        await b.close()
asyncio.run(main())
