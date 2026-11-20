import sys; sys.argv=['x']
src=open('gen.py').read(); src=src[:src.index('files={}')]
exec(src)
IMG="file:///home/claude/mbc/img/"
experts=[("prerna-saree.jpg","Dt. Prerna Sharma","Main face · Picky eating","center 15%"),
         ("priyanka-crop.jpg","Dt. Priyanka Sharma","Kids nutrition · Pehla khana","center 20%"),
         ("vijaylaxmi.jpg","Dt. Vijaylaxmi","Maa ka khana","center 20%"),
         ("nisha.jpg","Dt. Nisha Das","Immunity · Sardi","center 25%")]
ex="".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px;width:220px"><img src="{IMG}{f}" style="width:150px;height:150px;border-radius:999px;object-fit:cover;object-position:{pos};border:6px solid {GOLD}"><div style="font-size:26px;font-weight:700;color:#FFFFFF;text-align:center;line-height:1.15">{n}</div><div style="font-size:20px;color:#F3DCE7;text-align:center">{a}</div></div>' for f,n,a,pos in experts)
series=[("Parvarish Lab","Har expert, ek asli sawaal (reel)"),("Ek Maa Ki Diary","Dil chhoo lene wali kahaniyan"),("Dadi vs Doctor","Myths, pyaar aur izzat se"),("Pehla Niwala Week","Har mahine ek theme + free chart"),("Mera Bachcha Moms","Maaon ki apni kahaniyan")]
se="".join(f'<div style="background:#FFFFFF;border-radius:20px;padding:20px 24px;display:flex;gap:18px;align-items:center"><div style="flex:none;width:52px;height:52px;border-radius:999px;background:{PLUM};color:{GOLD};font-size:26px;font-weight:800;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div style="font-size:30px;font-weight:700;color:{PLUM}">{t}</div><div style="font-size:22px;color:{GREY}">{d}</div></div></div>' for i,(t,d) in enumerate(series))
tl=[("27 Nov","Ek Maa Ki Diary"),("28 Nov","Dadi vs Doctor"),("29 Nov","“2 baje” poster"),("30 Nov","Parvarish Lab teaser"),("4 Dec","Pehla Niwala chart")]
tle="".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px"><div style="width:26px;height:26px;border-radius:999px;background:{GOLD};border:5px solid #FFFFFF"></div><div style="font-size:24px;font-weight:800;color:{PLUM}">{d}</div><div style="font-size:19px;color:{INK};text-align:center;line-height:1.2">{t}</div></div>' for d,t in tl)
role=[("Accept karein","Har Collab invite turant accept karein"),("Share karein","Pehle 1 ghante mein apni Story par"),("Reply karein","Comments mein maaon ke sawaal ka jawaab"),("Record karein","Mahine mein 1 Parvarish Lab reel")]
ro="".join(f'<div style="display:flex;gap:16px;align-items:flex-start"><svg width="40" height="40" viewBox="0 0 64 64" style="flex:none"><circle cx="32" cy="32" r="32" fill="{GOLD}"></circle><path d="M18 33 L28 43 L47 22" fill="none" stroke="{PLUM}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"></path></svg><div><span style="font-size:28px;font-weight:700;color:{PLUM}">{t}</span><span style="font-size:24px;color:{GREY}"> &#183; {d}</span></div></div>' for t,d in role)
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>@font-face{{font-family:Outfit;src:url(file:///home/claude/fonts/Outfit.ttf);font-weight:100 900}}body{{margin:0}}</style></head><body>
<div style="width:1080px;font-family:Outfit,sans-serif;background:{BLUSH};display:flex;flex-direction:column">
<div style="background:{PLUM};padding:64px 70px 56px;display:flex;flex-direction:column;gap:22px">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="display:flex;align-items:center;gap:14px">{MARK("#FFFFFF",GOLD,64)}<div style="font-size:40px;font-weight:500;color:#FFFFFF;letter-spacing:-1px">mera bachcha</div></div><div style="border:3px solid {GOLD};color:{GOLD};border-radius:999px;padding:10px 24px;font-size:22px;font-weight:700;letter-spacing:3px">GAME PLAN</div></div>
<div style="font-size:84px;line-height:1.02;font-weight:800;color:#FFFFFF;letter-spacing:-3px;margin-top:20px">Saath milkar,<br><span style="color:{GOLD}">har maa tak.</span></div>
<div style="font-size:30px;line-height:1.4;color:#F3DCE7;max-width:900px">India ki har maa tak science-backed, pyaar bhari jaankari. Unki apni zubaan, Hinglish mein.</div>
<div style="margin-top:26px;font-size:22px;font-weight:700;color:{GOLD};letter-spacing:4px">HUMARA EXPERT PANEL</div>
<div style="display:flex;justify-content:space-between">{ex}</div>
</div>
<div style="padding:50px 70px 0;display:flex;flex-direction:column;gap:16px">
<div style="font-size:22px;font-weight:700;color:{GOLD};letter-spacing:4px">5 SIGNATURE SERIES</div>
{se}
</div>
<div style="padding:46px 70px 0">
<div style="font-size:22px;font-weight:700;color:{GOLD};letter-spacing:4px">LAUNCH CALENDAR</div>
<div style="position:relative;margin-top:26px"><div style="position:absolute;left:10%;right:10%;top:12px;height:4px;background:{PLUM};opacity:0.25"></div><div style="display:flex;position:relative">{tle}</div></div>
</div>
<div style="padding:46px 70px 0">
<div style="background:#FFFFFF;border-radius:28px;padding:34px 36px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:22px;font-weight:700;color:{GOLD};letter-spacing:4px">AAPKA ROLE, SIRF 4 KAAM</div>{ro}
<div style="margin-top:6px;font-size:24px;line-height:1.4;color:{INK}">Har post <b style="color:{PLUM}">aapke profile par bhi</b> aayegi: aapki pehchaan, aapke naye followers.</div>
</div></div>
<div style="padding:40px 70px 0;display:flex;gap:20px">
<div style="flex:1;background:{GOLD};border-radius:28px;padding:30px"><div style="font-size:64px;font-weight:800;color:{PLUM};line-height:1">+1,000</div><div style="font-size:24px;color:{PLUM};font-weight:600;margin-top:8px">followers, 30 din mein</div></div>
<div style="flex:1;background:{PLUM};border-radius:28px;padding:30px"><div style="font-size:64px;font-weight:800;color:{GOLD};line-height:1">10K+</div><div style="font-size:24px;color:#FFFFFF;font-weight:600;margin-top:8px">views wali pehli reel</div></div>
</div>
<div style="padding:34px 70px 0;display:flex;justify-content:space-between;font-size:24px;font-weight:600;color:{PLUM}"><span>Science pehle (WHO, IAP, ICMR)</span><span>Koi brand nahi</span><span>Pyaar se, izzat se</span></div>
<div style="margin-top:44px;background:{PLUM};padding:34px 70px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:26px;letter-spacing:4px;color:{GOLD};font-weight:600">MAA KI GOD SE SAPNO TAK</div><div style="font-size:28px;color:#FFFFFF;font-weight:500">@merabachcha_india</div></div>
</div></body></html>'''
open('render/gameplan.html','w').write(html)
