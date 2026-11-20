# Mera Bachcha design kit (new brand, 20 Nov 2026)

Setup: mkdir -p /home/claude/mbc /home/claude/fonts && cp -r mb-kit/* /home/claude/mbc/ && cp mb-kit/Outfit.ttf /home/claude/fonts/

- gen.py: helpers for the brand look (MARK logo svg, MAA illustration svg, header/footer/tag/page, icons, CHECK/CROSS) and the launch designs. Import the top part (everything before `files={}`) to reuse helpers.
- project/*.dc.html: the launch designs as HTML (1080x1350). Use them as the visual reference for new posts.
- render.py: turns project/*.dc.html into png/*.png with Playwright + /usr/bin/google-chrome (blob URLs mapped to img/*.jpg).
- img/: expert photos (prerna-saree, prerna-blazer, priyanka-crop, vijaylaxmi, nisha).
- Palette: plum #6D1B4F, gold #F2A33A, blush #FBF4F1, grey #6E5A63, cream #F7E3C7, ink #3A1029. Font Outfit.
