import json, datetime, os
R="/home/claude/mbc/project"
PLUM="#6D1B4F"; GOLD="#F2A33A"; BLUSH="#FBF4F1"; GREY="#6E5A63"; CREAM="#F7E3C7"; INK="#3A1029"
W,H=1080,1350

MARK=lambda body,dot=GOLD,s=56:f'''<svg width="{s}" height="{s}" viewBox="0 0 100 100" aria-hidden="true"><path d="M77.98 41 A30 30 0 1 1 34.79 31.42" fill="none" stroke="{body}" stroke-width="12" stroke-linecap="round"></path><circle cx="36" cy="17" r="11" fill="{body}"></circle><circle cx="52" cy="58" r="11" fill="{dot}"></circle></svg>'''

def MAA(s=360, badge="heart", uid="a"):
    SK="#A86B4A"; SKB="#C68B63"; HAIR="#2B1B17"
    b=""
    if badge=="heart":
        b=f'<circle cx="342" cy="342" r="50" fill="{GOLD}" stroke="#FFFFFF" stroke-width="8"></circle><path d="M342 366 C312 346 316 322 330 320 C337 319 341 324 342 328 C343 324 347 319 354 320 C368 322 372 346 342 366 Z" fill="{PLUM}"></path>'
    elif badge=="spoon":
        b=f'<circle cx="342" cy="342" r="50" fill="{GOLD}" stroke="#FFFFFF" stroke-width="8"></circle><ellipse cx="342" cy="326" rx="13" ry="17" fill="{PLUM}"></ellipse><rect x="338" y="338" width="8" height="34" rx="4" fill="{PLUM}"></rect>'
    return f'''<svg width="{s}" height="{s}" viewBox="0 0 400 400" role="img" aria-label="Illustration of an Indian mother holding her baby"><defs><clipPath id="c{uid}"><circle cx="200" cy="200" r="200"></circle></clipPath></defs>
<circle cx="200" cy="200" r="200" fill="{CREAM}"></circle><g clip-path="url(#c{uid})">
<circle cx="261" cy="99" r="29" fill="{HAIR}"></circle>
<rect x="105" y="225" width="195" height="245" rx="90" fill="{PLUM}"></rect>
<ellipse cx="206" cy="215" rx="18" ry="25" fill="{SK}"></ellipse>
<ellipse cx="201" cy="148" rx="51" ry="56" fill="{SK}"></ellipse>
<path d="M146 142 A56 56 0 0 1 258 142 Z" fill="{HAIR}"></path>
<ellipse cx="156" cy="148" rx="10" ry="27" fill="{HAIR}"></ellipse>
<circle cx="202" cy="131" r="5" fill="{GOLD}"></circle>
<path d="M170 154 Q180 162 190 154" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round"></path>
<path d="M212 154 Q222 162 232 154" fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round"></path>
<path d="M190 173 Q202 183 214 173" fill="none" stroke="#7A3030" stroke-width="4" stroke-linecap="round"></path>
<polygon points="118,260 260,222 300,262 140,330" fill="{GOLD}"></polygon>
<ellipse cx="215" cy="306" rx="85" ry="44" fill="#FFFFFF"></ellipse>
<circle cx="167" cy="291" r="29" fill="{SKB}"></circle>
<path d="M140 286 A27 27 0 0 1 194 286 Z" fill="{HAIR}"></path>
<path d="M152 296 Q158 301 164 296" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"></path>
<path d="M172 296 Q178 301 184 296" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"></path>
<rect x="150" y="330" width="170" height="42" rx="21" fill="{PLUM}"></rect>
<ellipse cx="310" cy="348" rx="20" ry="22" fill="{SK}"></ellipse></g>
<circle cx="200" cy="200" r="196" fill="none" stroke="{CREAM}" stroke-width="8"></circle>{b}</svg>'''

def page(title, body, bg, preview=(W,H)):
    return f'''<!doctype html>
<html lang="hi-Latn">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:{GOLD}}}a:hover{{color:#FFFFFF}}
</style>
</helmet>
<div style="width: {preview[0]}px; height: {preview[1]}px; box-sizing: border-box; background: {bg}; font-family: Outfit, sans-serif; position: relative; overflow: hidden; display: flex; flex-direction: column; padding: 72px 80px 64px">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{preview[0]},"height":{preview[1]}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

def header(onplum, counter=None, pill=None):
    c="#FFFFFF" if onplum else PLUM
    right=""
    if counter:
        right=f'<div style="font-size: 26px; font-weight: 500; color: {c}; opacity: 0.75; letter-spacing: 1px">{counter}</div>'
    if pill:
        right=f'<div style="border: 3px solid {GOLD}; color: {GOLD if onplum else PLUM}; border-radius: 999px; padding: 10px 26px; font-size: 24px; font-weight: 600; letter-spacing: 2px">{pill}</div>'
    return f'''<div style="display: flex; justify-content: space-between; align-items: center">
<div style="display: flex; align-items: center; gap: 14px">{MARK("#FFFFFF" if onplum else PLUM)}<div style="font-size: 36px; font-weight: 500; color: {c}; letter-spacing: -1px">mera bachcha</div></div>{right}</div>'''

def footer(onplum, left="@merabachcha_india", right=None):
    c="#FFFFFF" if onplum else GREY
    r=f'<div style="font-size: 22px; color: {c}; opacity: 0.85; text-align: right; max-width: 600px; line-height: 1.35">{right}</div>' if right else ""
    return f'<div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 30px; margin-top: auto"><div style="flex: none; font-size: 26px; font-weight: 500; color: {GOLD if onplum else PLUM}">{left}</div>{r}</div>'

def tag(t, onplum):
    return f'<div style="display: inline-block; background: {GOLD}; color: {PLUM}; border-radius: 999px; padding: 12px 30px; font-size: 28px; font-weight: 700; letter-spacing: 4px">{t}</div>'

ICONS={
"hand": f'<svg width="280" height="280" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96" fill="{CREAM}"></circle><path d="M40 120 C60 100 90 96 118 104 L150 112 C160 115 160 128 150 129 L120 126" fill="none" stroke="{PLUM}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"></path><path d="M40 138 C70 150 110 152 140 140" fill="none" stroke="{PLUM}" stroke-width="9" stroke-linecap="round"></path><circle cx="120" cy="82" r="20" fill="{GOLD}"></circle><path d="M108 96 C112 112 128 112 132 96" fill="none" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"></path></svg>',
"moon": f'<svg width="280" height="280" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96" fill="{CREAM}"></circle><path d="M120 50 A52 52 0 1 0 150 128 A42 42 0 1 1 120 50 Z" fill="{PLUM}"></path><path d="M146 58 l5 12 12 5 -12 5 -5 12 -5 -12 -12 -5 12 -5 Z" fill="{GOLD}"></path><circle cx="66" cy="62" r="5" fill="{GOLD}"></circle></svg>',
"bowl": f'<svg width="280" height="280" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96" fill="{CREAM}"></circle><path d="M44 100 H156 C156 132 132 152 100 152 C68 152 44 132 44 100 Z" fill="{PLUM}"></path><ellipse cx="100" cy="100" rx="56" ry="10" fill="{GOLD}"></ellipse><ellipse cx="146" cy="58" rx="12" ry="16" fill="none" stroke="{PLUM}" stroke-width="7" transform="rotate(30 146 58)"></ellipse><path d="M138 72 L118 104" stroke="{PLUM}" stroke-width="7" stroke-linecap="round"></path></svg>',
"bubble": f'<svg width="280" height="280" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96" fill="{CREAM}"></circle><path d="M46 62 H154 A12 12 0 0 1 166 74 V118 A12 12 0 0 1 154 130 H92 L66 152 V130 H46 A12 12 0 0 1 34 118 V74 A12 12 0 0 1 46 62 Z" fill="{PLUM}"></path><text x="100" y="108" text-anchor="middle" font-family="Outfit, sans-serif" font-size="36" font-weight="700" fill="{GOLD}">Maa!</text></svg>',
"candle": f'<svg width="280" height="280" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96" fill="{CREAM}"></circle><rect x="48" y="112" width="104" height="44" rx="10" fill="{PLUM}"></rect><rect x="48" y="112" width="104" height="12" rx="6" fill="{GOLD}"></rect><rect x="94" y="72" width="12" height="40" rx="4" fill="{GOLD}"></rect><path d="M100 44 C110 56 108 66 100 68 C92 66 90 56 100 44 Z" fill="{GOLD}"></path><text x="100" y="148" text-anchor="middle" font-family="Outfit, sans-serif" font-size="22" font-weight="700" fill="#FFFFFF">1</text></svg>',
}

files={}
# ---------- Story carousel ----------
cover=f'''{header(True, pill="EK MAA KI DIARY")}
<div style="display: flex; flex-direction: column; align-items: center; margin-top: 70px; gap: 0">{MAA(420, "heart", "s1")}</div>
<h1 style="margin: 56px 0 0; font-size: 150px; line-height: 1; font-weight: 700; color: #FFFFFF; letter-spacing: -4px; text-align: center">Pehla saal.</h1>
<p style="margin: 32px auto 0; max-width: 820px; font-size: 42px; line-height: 1.35; font-weight: 400; color: #F3DCE7; text-align: center">Kisi ne nahi bataya tha ki yeh itna <span style="color: {GOLD}; font-weight: 600">khoobsurat</span> hoga... aur itna mushkil bhi.</p>
<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center"><div style="font-size: 30px; color: #F3DCE7">Shayad yeh aapki kahani ho</div><div style="font-size: 34px; font-weight: 600; color: {GOLD}">Swipe karein &#8594;</div></div>'''
files["Main.dc.html"]=page("Ek Maa Ki Diary – cover", cover, PLUM)

diary=[
 ("DIN 1","hand","Usne meri ungli pakdi.","Aur maine apni neend chhod di.",None,BLUSH),
 ("MAHINA 3","moon","Pehli muskaan.","Raat ke 3 baje. Sirf mere liye.",None,BLUSH),
 ("MAHINA 6","bowl","Pehla niwala.","Aadha muh mein, aadha mere kapdon par.","6 mahine pe shuru karein: masla hua dal-chawal, ragi ya kela. Pehle 2&#8211;3 chammach se.",BLUSH),
 ("MAHINA 9","bubble","Usne “Maa” bola.","...ya shayad “Ma-ma”. Maine poore khandaan ko phone kar diya.",None,BLUSH),
]
for i,(lab,ic,big,sub,tip,bg) in enumerate(diary, start=2):
    tipbox=""
    if tip:
        tipbox=f'<div style="margin-top: 44px; background: #FFFFFF; border-radius: 28px; padding: 30px 36px; display: flex; gap: 22px; align-items: flex-start"><img src="/_blob/90c449f20c847c4e5d6a573204358be7" alt="Prerna Sharma" style="flex: none; width: 96px; height: 96px; border-radius: 999px; object-fit: cover; object-position: center 15%; border: 4px solid {GOLD}"><div><div style="font-size: 24px; font-weight: 700; color: {PLUM}; letter-spacing: 1px">DT. PRERNA SHARMA KI TIP &#183; MSc Food &amp; Nutrition</div><div style="margin-top: 8px; font-size: 32px; line-height: 1.4; color: {INK}">{tip}</div></div></div>'
    body=f'''{header(False, counter=f"{i}/7")}
<div style="margin-top: 90px">{tag(lab, False)}</div>
<div style="margin-top: 50px">{ICONS[ic]}</div>
<h2 style="margin: 50px 0 0; font-size: 104px; line-height: 1.02; font-weight: 700; color: {PLUM}; letter-spacing: -3px">{big}</h2>
<p style="margin: 26px 0 0; font-size: 50px; line-height: 1.3; font-weight: 400; color: {GREY}">{sub}</p>
{tipbox}
{footer(False, right="Ek Maa Ki Diary")}'''
    files[f"story-{i}.dc.html"]=page(f"Ek Maa Ki Diary – {lab.title()}", body, bg)

s6=f'''{header(True, counter="6/7")}
<div style="margin-top: 90px">{tag("SAAL 1", True)}</div>
<div style="margin-top: 50px">{ICONS["candle"]}</div>
<p style="margin: 56px 0 0; font-size: 58px; line-height: 1.25; font-weight: 400; color: #F3DCE7">Log kehte hain, bachcha ek saal ka ho gaya.</p>
<h2 style="margin: 30px 0 0; font-size: 96px; line-height: 1.05; font-weight: 700; color: #FFFFFF; letter-spacing: -3px">Main kehti hoon, ek <span style="color: {GOLD}">maa</span> bhi ek saal ki ho gayi.</h2>
{footer(True, right="Ek Maa Ki Diary")}'''
files["story-6.dc.html"]=page("Ek Maa Ki Diary – Saal 1", s6, PLUM)

def action(label, svg):
    return f'<div style="display: flex; flex-direction: column; align-items: center; gap: 14px"><div style="width: 120px; height: 120px; border-radius: 999px; background: {PLUM}; display: flex; align-items: center; justify-content: center">{svg}</div><div style="font-size: 30px; font-weight: 600; color: {PLUM}">{label}</div></div>'
SEND=f'<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2 11 13"></path><path d="M22 2 15 22l-4-9-9-4 20-7z"></path></svg>'
SAVE=f'<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>'
CMT=f'<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.8-.9L3 21l1.9-5.2A8.4 8.4 0 1 1 21 11.5z"></path></svg>'
s7=f'''{header(False, counter="7/7")}
<div style="display: flex; justify-content: center; margin-top: 60px">{MAA(300, "heart", "s7")}</div>
<h2 style="margin: 50px 0 0; font-size: 84px; line-height: 1.08; font-weight: 700; color: {PLUM}; letter-spacing: -2px; text-align: center">Har us maa ko bhejiye jo aaj raat bhi jaag rahi hai.</h2>
<p style="margin: 26px 0 0; font-size: 44px; line-height: 1.3; color: {GREY}; text-align: center">Use bataiye, woh akeli nahi hai.</p>
<div style="margin-top: 56px; display: flex; justify-content: center; gap: 70px">{action("Bhejiye", SEND)}{action("Save", SAVE)}{action("Comment", CMT)}</div>
<div style="margin-top: 50px; background: #FFFFFF; border-radius: 28px; padding: 28px 36px; font-size: 36px; line-height: 1.35; color: {INK}; text-align: center">Comment mein likhiye: aapke bachche ka <span style="color: {PLUM}; font-weight: 700">pehla</span> kya tha?</div>
{footer(False, right="Maa ki god se sapno tak")}'''
files["story-7.dc.html"]=page("Ek Maa Ki Diary – share", s7, BLUSH)

# ---------- Myth carousel ----------
m1=f'''{header(True, pill="DADI vs DOCTOR")}
<h1 style="margin: 140px 0 0; font-size: 158px; line-height: 0.98; font-weight: 700; color: #FFFFFF; letter-spacing: -5px">Dadi ki<br><span style="color: {GOLD}">6 baatein.</span></h1>
<p style="margin: 40px 0 0; font-size: 50px; line-height: 1.3; color: #F3DCE7">3 bilkul sahi thi.<br>3 ab badal gayi hain.</p>
<div style="margin-top: 80px; display: flex; gap: 28px">
<div style="flex: 1; background: {GOLD}; border-radius: 32px; padding: 36px; display: flex; align-items: center; gap: 22px"><div style="font-size: 96px; font-weight: 800; color: {PLUM}; line-height: 1">3</div><div style="font-size: 36px; font-weight: 600; color: {PLUM}; line-height: 1.15">Sahi thi<br>Dadi</div></div>
<div style="flex: 1; border: 4px solid {GOLD}; border-radius: 32px; padding: 32px; display: flex; align-items: center; gap: 22px"><div style="font-size: 96px; font-weight: 800; color: {GOLD}; line-height: 1">3</div><div style="font-size: 36px; font-weight: 600; color: #FFFFFF; line-height: 1.15">Ab badal<br>gaya hai</div></div>
</div>
<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center"><div style="font-size: 30px; color: #F3DCE7">Pyaar se, izzat se</div><div style="font-size: 34px; font-weight: 600; color: {GOLD}">Swipe karein &#8594;</div></div>'''
files["myth-1.dc.html"]=page("Dadi ki 6 baatein – cover", m1, PLUM)

CHECK=f'<svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="32" fill="{GOLD}"></circle><path d="M18 33 L28 43 L47 22" fill="none" stroke="{PLUM}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
CROSS=f'<svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="none" stroke="{GOLD}" stroke-width="4"></circle><path d="M22 22 L42 42 M42 22 L22 42" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"></path></svg>'
def rows(items, onplum):
    out=""
    for t,s in items:
        tc="#FFFFFF" if onplum else PLUM; sc="#F3DCE7" if onplum else GREY
        out+=f'<div style="display: flex; gap: 30px; align-items: flex-start"><div style="flex: none; margin-top: 6px">{CHECK if not onplum else CROSS}</div><div><div style="font-size: 52px; font-weight: 700; color: {tc}; line-height: 1.12; letter-spacing: -1px">{t}</div><div style="margin-top: 12px; font-size: 36px; color: {sc}; line-height: 1.35">{s}</div></div></div>'
    return out
m2=f'''{header(False, counter="2/5")}
<div style="margin-top: 80px">{tag("SAHI THI DADI", False)}</div>
<div style="margin-top: 70px; display: flex; flex-direction: column; gap: 64px">{rows([("Pehle 6 mahine sirf maa ka doodh","WHO bhi aaj yahi kehta hai."),("Ghar ka bana pehla khana","Khichdi, ragi, dal: sabse achha shuruaat ka khana."),("Roz ki maalish","Pyaar aur bonding, dono badhte hain.")], False)}</div>
{footer(False, right="Source: WHO, IAP")}'''
files["myth-2.dc.html"]=page("Dadi ki 6 baatein – sahi", m2, BLUSH)
m3=f'''{header(True, counter="3/5")}
<div style="margin-top: 80px">{tag("AB BADAL GAYA HAI", True)}</div>
<div style="margin-top: 70px; display: flex; flex-direction: column; gap: 64px">{rows([("Janam ke baad ghutti ya shahad","1 saal tak shahad bilkul nahi. Ek gambhir infection (botulism) ka khatra hai."),("Aankhon mein kajal","Kajal mein lead ho sakta hai, aur aankh mein infection ka darr."),("Garmi mein paani (6 mahine se pehle)","Maa ka doodh hi kaafi hai. Paani ki zaroorat nahi.")], True)}</div>
{footer(True, right="Source: WHO, IAP")}'''
files["myth-3.dc.html"]=page("Dadi ki 6 baatein – badal gaya", m3, PLUM)
m4=f'''{header(False, counter="4/5")}
<h2 style="margin: 110px 0 0; font-size: 104px; line-height: 1.02; font-weight: 700; color: {PLUM}; letter-spacing: -3px">Dadi se kaise baat karein?</h2>
<p style="margin: 28px 0 0; font-size: 46px; color: {GREY}">Behas nahi. Pyaar se.</p>
<div style="margin-top: 70px; display: flex; flex-direction: column; gap: 30px">
<div style="background: #FFFFFF; border-radius: 28px; padding: 32px 40px; display: flex; gap: 28px; align-items: center"><div style="flex: none; font-size: 64px; font-weight: 800; color: {GOLD}">1</div><div style="font-size: 40px; line-height: 1.3; color: {INK}">“Aapne humein itne pyaar se paala hai...”</div></div>
<div style="background: #FFFFFF; border-radius: 28px; padding: 32px 40px; display: flex; gap: 28px; align-items: center"><div style="flex: none; font-size: 64px; font-weight: 800; color: {GOLD}">2</div><div style="font-size: 40px; line-height: 1.3; color: {INK}">“...ab doctor nayi research ke saath yeh kehte hain.”</div></div>
<div style="background: #FFFFFF; border-radius: 28px; padding: 32px 40px; display: flex; gap: 28px; align-items: center"><div style="flex: none; font-size: 64px; font-weight: 800; color: {GOLD}">3</div><div style="font-size: 40px; line-height: 1.3; color: {INK}">Aur yeh post unhe pyaar se dikhaiye.</div></div>
</div>
{footer(False)}'''
files["myth-4.dc.html"]=page("Dadi ki 6 baatein – kaise baat karein", m4, BLUSH)
m5=f'''{header(True, counter="5/5")}
<div style="display: flex; justify-content: center; margin-top: 70px">{MAA(320, "heart", "m5")}</div>
<h2 style="margin: 60px 0 0; font-size: 92px; line-height: 1.05; font-weight: 700; color: #FFFFFF; letter-spacing: -3px; text-align: center">Yeh post family group mein bhejiye.</h2>
<p style="margin: 30px 0 0; font-size: 48px; line-height: 1.3; color: {GOLD}; text-align: center; font-weight: 500">Dadi bhi samjhengi, maa bhi.</p>
<div style="margin-top: 50px; display: flex; justify-content: center; align-items: center; gap: 20px"><img src="/_blob/90c449f20c847c4e5d6a573204358be7" alt="Prerna Sharma" style="width: 84px; height: 84px; border-radius: 999px; object-fit: cover; object-position: center 15%; border: 4px solid {GOLD}"><div style="font-size: 28px; color: #F3DCE7; line-height: 1.35">Reviewed by <span style="color: #FFFFFF; font-weight: 600">Dt. Prerna Sharma</span>, MSc Food &amp; Nutrition<br>Apne doctor se salah zaroor lein.</div></div>
{footer(True, right="Source: WHO, IAP")}'''
files["myth-5.dc.html"]=page("Dadi ki 6 baatein – share", m5, PLUM)

# ---------- Posters ----------
p1=f'''{header(True)}
<div style="margin-top: 150px; display: flex; flex-direction: column; gap: 24px">
<div style="font-size: 92px; line-height: 1.08; font-weight: 600; color: #F3DCE7; letter-spacing: -2px">Woh raat 2 baje uthta hai.</div>
<div style="font-size: 92px; line-height: 1.08; font-weight: 600; color: #F3DCE7; letter-spacing: -2px">Main bhi 2 baje uthti hoon.</div>
<div style="margin-top: 30px; font-size: 118px; line-height: 1.02; font-weight: 700; color: {GOLD}; letter-spacing: -4px">Isi ko toh pyaar kehte hain.</div>
</div>
<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end"><div style="display: flex; flex-direction: column; gap: 10px"><div style="font-size: 30px; color: #F3DCE7">Tag karein us maa ko</div><div style="font-size: 30px; font-weight: 500; color: {GOLD}">@merabachcha_india</div></div>{MAA(260, "heart", "p1")}</div>'''
files["poster-quote.dc.html"]=page("Poster – 2 baje", p1, PLUM)

rowsdata=[("6 mahine","Patla, masla hua","Dal-chawal, ragi, kela","2&#8211;3 chammach se shuru, din mein 1&#8211;2 baar"),
          ("7&#8211;8 mahine","Gaadha, masla hua","Khichdi, sooji, sabzi","Din mein 2&#8211;3 baar"),
          ("9&#8211;11 mahine","Chhote naram tukde","Paneer, roti ke tukde, phal","3&#8211;4 meal + 1&#8211;2 snack"),
          ("12 mahine +","Ghar ka khana","Family ka khana, bina extra namak-cheeni","3&#8211;4 meal + 1&#8211;2 snack")]
tbl=""
for k,(age,tex,food,freq) in enumerate(rowsdata):
    bgc="#FFFFFF" if k%2==0 else "#F6E7EE"
    tbl+=f'<div style="display: grid; grid-template-columns: 210px minmax(0, 1fr) 270px; gap: 24px; align-items: center; background: {bgc}; border-radius: 22px; padding: 28px 30px"><div style="font-size: 36px; font-weight: 700; color: {PLUM}; line-height: 1.1">{age}</div><div><div style="font-size: 32px; font-weight: 600; color: {INK}; line-height: 1.2">{food}</div><div style="margin-top: 6px; font-size: 26px; color: {GREY}">{tex}</div></div><div style="font-size: 27px; color: {INK}; line-height: 1.3">{freq}</div></div>'
p2=f'''{header(False, pill="SAVE KAREIN")}
<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 60px; gap: 30px">
<div><div style="font-size: 30px; font-weight: 600; color: {GOLD}; letter-spacing: 4px">6&#8211;12 MAHINE</div><h1 style="margin: 12px 0 0; font-size: 104px; line-height: 1; font-weight: 700; color: {PLUM}; letter-spacing: -3px">Pehla Niwala<br>Chart</h1></div>
{MAA(220, "spoon", "p2")}</div>
<div style="margin-top: 50px; display: grid; grid-template-columns: 210px minmax(0, 1fr) 270px; gap: 24px; padding: 0 30px 14px; font-size: 22px; font-weight: 700; color: {GREY}; letter-spacing: 2px"><div>UMAR</div><div>KYA DEIN</div><div>KITNI BAAR</div></div>
<div style="display: flex; flex-direction: column; gap: 14px">{tbl}</div>
<div style="margin-top: 30px; font-size: 28px; color: {INK}; line-height: 1.4"><span style="font-weight: 700; color: {PLUM}">Maa ka doodh jaari rakhein.</span> 1 saal tak shahad aur namak-cheeni nahi.</div>
{footer(False, right="Reviewed by Dt. Prerna Sharma, MSc Food &amp; Nutrition &#183; Source: WHO, ICMR-NIN")}'''
files["poster-chart.dc.html"]=page("Poster – Pehla Niwala chart", p2, BLUSH)

p3=f'''<div style="display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 14px">{MARK(PLUM)}<div style="font-size: 36px; font-weight: 500; color: {PLUM}; letter-spacing: -1px">mera bachcha</div></div><div style="background: {PLUM}; color: {GOLD}; border-radius: 999px; padding: 12px 28px; font-size: 26px; font-weight: 700; letter-spacing: 3px">PARVARISH LAB &#183; EP 01</div></div>
<h1 style="margin: 70px 0 0; font-size: 96px; line-height: 1.04; font-weight: 700; color: {PLUM}; letter-spacing: -3px">Bachcha khana nahi khaata?<br><span style="background: {PLUM}; color: {GOLD}; padding: 0 16px; border-radius: 12px">Kab chinta karein?</span></h1>
<div style="margin-top: auto; position: relative; height: 760px; display: flex; justify-content: center; align-items: flex-end">
<div style="width: 640px; height: 720px; border-radius: 320px 320px 40px 40px; background: {CREAM}; overflow: hidden; border: 8px solid #FFFFFF; box-sizing: border-box"><img src="/_blob/aca7c265850dd2ee486de2f50aa87a51" alt="Prerna Sharma, nutritionist" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block"></div>
<div style="position: absolute; left: 0; bottom: 120px; background: #FFFFFF; border-radius: 20px; padding: 22px 30px; box-shadow: 0 8px 30px rgba(109,27,79,0.15)"><div style="font-size: 36px; font-weight: 700; color: {PLUM}">Dt. Prerna Sharma</div><div style="font-size: 26px; color: {GREY}">MSc Food &amp; Nutrition</div><div style="margin-top: 4px; font-size: 24px; font-weight: 600; color: {GOLD}">@nutrieezen</div></div>
</div>'''
p3=p3
files["poster-parvarish-lab.dc.html"]=page("Parvarish Lab – reel cover template", p3, GOLD)

# write files
for k,v in files.items():
    open(os.path.join(R,k),"w").write(v)

order=["Main.dc.html"]+[f"story-{i}.dc.html" for i in range(2,8)]+[f"myth-{i}.dc.html" for i in range(1,6)]+["poster-quote.dc.html","poster-chart.dc.html","poster-parvarish-lab.dc.html"]
titles={"Main.dc.html":"Diary 1 · Cover"}
for i in range(2,8): titles[f"story-{i}.dc.html"]=f"Diary {i}"
for i in range(1,6): titles[f"myth-{i}.dc.html"]=f"Dadi vs Doctor {i}"
titles.update({"poster-quote.dc.html":"Poster · 2 baje","poster-chart.dc.html":"Poster · Pehla Niwala chart","poster-parvarish-lab.dc.html":"Parvarish Lab · reel cover template"})
boards={}
for i in range(7): boards[order[i]]={"x":i*1160,"y":0,"w":W,"h":H,"title":titles[order[i]]}
for i in range(5): boards[order[7+i]]={"x":i*1160,"y":1850,"w":W,"h":H,"title":titles[order[7+i]]}
for i in range(3): boards[order[12+i]]={"x":i*1160,"y":3700,"w":W,"h":H,"title":titles[order[12+i]]}
canvas={"v":3,"createdOnFiles":{"v":1,"at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")},"title":"Mera Bachcha – Super-Brand Launch Designs","launch":{"view":"canvas"},"pages":[],"boards":boards,"order":order,
 "notes":{"t1":{"x":0,"y":-320,"text":"Ek Maa Ki Diary · emotional story carousel (7 slides)","kind":"title1","maxW":7960},
          "t2":{"x":0,"y":1530,"text":"Dadi vs Doctor · myth carousel (5 slides)","kind":"title1","maxW":5720},
          "t3":{"x":0,"y":3380,"text":"Posters · quote, save-worthy chart, expert series template","kind":"title1","maxW":3400}},"designSystems":[]}
json.dump(canvas, open(os.path.join(R,"canvas.json"),"w"), ensure_ascii=False, indent=1)
print(len(files))
