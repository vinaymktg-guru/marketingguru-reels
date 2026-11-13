#!/usr/bin/env python3
"""The Marketing Guru – daily sales-lesson reel builder.

Usage:  python3 build.py lessons/<file>.json            -> reels/<slug>.mp4
        python3 build.py lessons/<file>.json --preview  -> reels/<slug>_preview.png (no audio, fast)

Spec (JSON):
{ "slug": "2026-11-14-just-checking-in", "n": 1, "theme": "bokeh|grid|streaks", "chords": 0-3,
  "hook":    {"text": "Stop saying *\"just checking in.\"*", "vo": "Stop saying just checking in."},
  "mistake": {"label": "THE MISTAKE", "text": "\"Just checking in, sir.\"", "vo": "..."},
  "fix":     {"label": "SAY THIS INSTEAD", "text": "...", "vo": "..."},
  "why":     {"label": "WHY IT WORKS", "text": "...", "vo": "..."},
  "cta":     {"share": "Send this to a teammate who ...", "keyword": "VALUE", "vo": "..."} }
Words wrapped in *asterisks* are drawn in gold. Use straight quotes.
"""
import json, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
NAVY = (11, 31, 58); GOLD = (245, 179, 1); WHITE = (255, 255, 255); RED = (226, 58, 58)
FONTS = {'bebas': 'bebas.ttf', 'cinzel': 'cinzel.ttf', 'pb': 'playfairb.ttf', 'pi': 'playfairi.ttf',
         'pop': 'Poppins-Medium.ttf', 'popb': 'Poppins-Bold.ttf'}
_fc = {}
def font(n, s):
    if (n, s) not in _fc: _fc[(n, s)] = ImageFont.truetype(os.path.join(ROOT, 'fonts', FONTS[n]), s)
    return _fc[(n, s)]
def clamp(x, a=0., b=1.): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def smooth(x): x = clamp(x); return x * x * (3 - 2 * x)
_D = ImageDraw.Draw(Image.new('RGB', (1, 1)))
def tw(t, f): b = _D.textbbox((0, 0), t, font=f); return b[2] - b[0]

# ------------------------------------------------------------------ kinetic text
def parse(text):
    words, gold = [], False
    for raw in text.split():
        w = raw; g0 = gold
        if w.startswith('*'): w = w[1:]; g0 = True; gold = True
        end = w.endswith('*') or w.endswith('*.') or w.endswith('*,')
        w = w.replace('*', '')
        words.append((w, g0 or gold))
        if end: gold = False
    return words

def layout(text, fname, size, maxw=900, maxlines=4, minsize=60):
    words = parse(text)
    while True:
        f = font(fname, size); sp = tw(' ', f) + 4; lines = [[]]; cur = 0
        for w, g in words:
            ww = tw(w, f)
            if lines[-1] and cur + sp + ww > maxw: lines.append([]); cur = 0
            lines[-1].append((w, g, ww)); cur += (sp if cur else 0) + ww
        if (len(lines) <= maxlines and max(sum(x[2] for x in l) + sp * (len(l) - 1) for l in lines) <= maxw) or size <= minsize:
            asc, desc = f.getmetrics(); lh = int((asc + desc) * (0.92 if fname == 'bebas' else 1.15))
            return dict(lines=lines, f=f, sp=sp, lh=lh, h=lh * len(lines), n=len(words))
        size -= 6

def draw_kinetic(layer, L, top, u, t0=0.0, stagger=0.09, base=WHITE, accent=GOLD, shadow=True):
    """Reveal words one by one starting at local time t0. Returns time when last word is in."""
    d = ImageDraw.Draw(layer); k = 0
    for li, line in enumerate(L['lines']):
        lw = sum(x[2] for x in line) + L['sp'] * (len(line) - 1); x = (W - lw) // 2; y = top + li * L['lh']
        for w, g, ww in line:
            a = ease((u - t0 - k * stagger) / 0.28)
            if a > 0.01:
                dy = int(28 * (1 - a)); col = (accent if g else base) + (int(255 * a),)
                if shadow: d.text((x + 3, y + dy + 5), w, font=L['f'], fill=(0, 0, 0, int(150 * a)))
                d.text((x, y + dy), w, font=L['f'], fill=col)
            x += ww + L['sp']; k += 1
    return t0 + k * stagger + 0.28

def pill(layer, cy, label, col, filled=False, a=1.0):
    d = ImageDraw.Draw(layer); f = font('cinzel', 34); w = tw(label, f) + 70; x = (W - w) // 2
    if filled: d.rounded_rectangle((x, cy - 32, x + w, cy + 32), radius=32, fill=col + (int(255 * a),))
    else: d.rounded_rectangle((x, cy - 32, x + w, cy + 32), radius=32, outline=col + (int(255 * a),), width=4)
    d.text((W // 2, cy + 2), label, font=f, fill=(NAVY if filled else col) + (int(255 * a),), anchor='mm')

# ------------------------------------------------------------------ backgrounds
def vgrad(stops):
    ys = np.linspace(0, 1, H); col = np.zeros((H, 3))
    for c in range(3): col[:, c] = np.interp(ys, [s[0] for s in stops], [s[1][c] for s in stops])
    return np.repeat(col[:, None, :], W, axis=1)

def make_bg(theme, seed):
    rnd = random.Random(seed)
    yy, xx = np.mgrid[0:H, 0:W]
    vig = np.clip(1 - 0.5 * np.clip(np.sqrt(((xx - W / 2) / (W * .75)) ** 2 + ((yy - H / 2) / (H * .7)) ** 2) - .35, 0, 1) ** 1.3, 0, 1)[..., None]
    if theme == 'grid':
        arr = vgrad([(0, (5, 10, 24)), (0.55, (11, 31, 58)), (0.62, (70, 45, 20)), (0.66, (12, 22, 42)), (1, (4, 8, 18))])
    elif theme == 'streaks':
        arr = vgrad([(0, (8, 16, 34)), (0.5, (14, 34, 64)), (1, (5, 9, 20))])
    else:
        arr = vgrad([(0, (6, 14, 30)), (0.45, (11, 31, 58)), (1, (40, 12, 22))])
    base = Image.fromarray(np.clip(arr * vig, 0, 255).astype(np.uint8)).convert('RGBA')
    # readability scrim in the text zone
    sc = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sc).ellipse((-200, 380, W + 200, 1500), fill=(3, 8, 18, 120))
    sc = sc.filter(ImageFilter.GaussianBlur(120))
    if theme == 'bokeh':
        sprites = {}
        for r in (18, 30, 46, 70):
            s = Image.new('RGBA', (r * 4, r * 4), (0, 0, 0, 0)); ImageDraw.Draw(s).ellipse((r, r, r * 3, r * 3), fill=GOLD + (255,))
            sprites[r] = s.filter(ImageFilter.GaussianBlur(r * 0.45))
        parts = [(rnd.random() * W, rnd.random() * H, rnd.choice(list(sprites)), 0.15 + rnd.random() * 0.45, 25 + rnd.random() * 60, rnd.random() * 6) for _ in range(34)]
        def bg(t):
            img = base.copy()
            for x, y, r, a, sp, ph in parts:
                py = (y - sp * t) % (H + 300) - 150; px = x + 30 * math.sin(t * 0.5 + ph)
                spr = sprites[r]; al = spr.getchannel('A').point(lambda v, a=a * (0.75 + 0.25 * math.sin(t + ph)): int(v * a))
                s2 = spr.copy(); s2.putalpha(al); img.alpha_composite(s2, (int(px - r * 2), int(py - r * 2)))
            img.alpha_composite(sc); return img
    elif theme == 'grid':
        HZ = int(H * 0.62)
        def bg(t):
            img = base.copy(); lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
            for i in range(-12, 13):
                d.line((W / 2 + i * 14, HZ, W / 2 + i * 260, H), fill=GOLD + (60,), width=2)
            for i in range(14):
                z = ((i + t * 0.9) % 14) / 14; y = HZ + (H - HZ) * z ** 2.4
                d.line((0, y, W, y), fill=GOLD + (int(20 + 70 * z),), width=2)
            img.alpha_composite(lay); img.alpha_composite(sc); return img
    else:
        st = Image.new('RGBA', (1600, 60), (0, 0, 0, 0)); ImageDraw.Draw(st).rounded_rectangle((0, 18, 1600, 42), radius=12, fill=GOLD + (255,))
        st = st.filter(ImageFilter.GaussianBlur(9)).rotate(28, expand=True)
        lines = [(rnd.random() * 2400 - 1200, rnd.random() * H, 0.35 + rnd.random() * 0.35, 120 + rnd.random() * 160) for _ in range(9)]
        def bg(t):
            img = base.copy()
            for x, y, a, sp in lines:
                px = (x + sp * t) % 2600 - 1500; s2 = st.copy(); s2.putalpha(st.getchannel('A').point(lambda v, a=a: int(v * a)))
                img.alpha_composite(s2, (int(px), int(y - st.height / 2 + 0.3 * px * 0.5) % H - 300))
            img.alpha_composite(sc); return img
    return bg

def logo():
    L = Image.new('RGBA', (W, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(L); x, y = 70, 110
    d.ellipse((x, y, x + 96, y + 96), outline=GOLD + (255,), width=4)
    f = font('cinzel', 44); b = d.textbbox((0, 0), 'VP', font=f)
    d.text((x + 48 - (b[2] + b[0]) / 2, y + 50 - (b[3] + b[1]) / 2), 'VP', font=f, fill=GOLD + (255,))
    d.line((x + 74, y + 30, x + 86, y + 14), fill=GOLD + (255,), width=4)
    d.polygon([(x + 90, y + 8), (x + 78, y + 13), (x + 88, y + 22)], fill=GOLD + (255,))
    d.text((x + 116, y + 18), 'THE MARKETING GURU', font=font('cinzel', 26), fill=GOLD + (255,))
    d.text((x + 116, y + 54), 'Vinay Pandey  ·  @marketingguru_vp', font=font('pop', 22), fill=(255, 255, 255, 230))
    L.putalpha(L.getchannel('A').point(lambda v: int(v * 0.9))); return L

# ------------------------------------------------------------------ scenes
def scene_fns(spec):
    S = {}; U = ui(spec)
    h = layout(spec['hook']['text'], 'bebas', 170, maxlines=4)
    def hook(lay, u, d):
        top = 900 - h['h'] // 2
        pill(lay, top - 90, spec['hook'].get('label', U['lesson'].format(n=spec['n'])), GOLD, a=ease(u / 0.3))
        draw_kinetic(lay, h, top, u, 0.1, stagger=0.11)
    S['hook'] = hook
    m = layout(spec['mistake']['text'], 'bebas', 130, maxlines=4)
    def mistake(lay, u, d):
        top = 920 - m['h'] // 2
        pill(lay, top - 100, spec['mistake'].get('label', U['mistake']), RED, filled=True, a=ease(u / 0.3))
        end = draw_kinetic(lay, m, top, u, 0.15, base=(225, 225, 225), accent=RED)
        s = ease((u - end - 0.25) / 0.45); dr = ImageDraw.Draw(lay)
        for li, line in enumerate(m['lines']):
            lw = sum(x[2] for x in line) + m['sp'] * (len(line) - 1); x0 = (W - lw) // 2
            yc = top + li * m['lh'] + int(m['lh'] * 0.45)
            if s > 0: dr.line((x0 - 10, yc, x0 - 10 + (lw + 20) * s, yc), fill=RED + (255,), width=12)
    S['mistake'] = mistake
    fx = layout(spec['fix']['text'], 'bebas', 125, maxw=820, maxlines=5)
    def fix(lay, u, d):
        top = 930 - fx['h'] // 2; a = ease(u / 0.35)
        pill(lay, top - 120, spec['fix'].get('label', U['fix']), GOLD, filled=True, a=a)
        dr = ImageDraw.Draw(lay); bw = 940
        dr.rounded_rectangle(((W - bw) // 2, top - 40, (W + bw) // 2, top + fx['h'] + 30), radius=28,
                             fill=(11, 31, 58, int(200 * a)), outline=GOLD + (int(255 * a),), width=5)
        draw_kinetic(lay, fx, top, u, 0.25, stagger=0.08, shadow=False)
    S['fix'] = fix
    wy = layout(spec['why']['text'], 'bebas', 120, maxlines=5)
    def why(lay, u, d):
        top = 920 - wy['h'] // 2
        pill(lay, top - 100, spec['why'].get('label', U['why']), WHITE, a=ease(u / 0.3))
        draw_kinetic(lay, wy, top, u, 0.15, stagger=0.08)
    S['why'] = why
    sh = layout(spec['cta']['share'], 'pop', 42, maxw=840, maxlines=3, minsize=32)
    def cta(lay, u, d):
        dr = ImageDraw.Draw(lay); a = ease(u / 0.35)
        sv = layout(U['save'], 'bebas', 190)
        draw_kinetic(lay, sv, 470, u, 0.0, stagger=0.15)
        draw_kinetic(lay, sh, 720, u, 0.5, stagger=0.04, shadow=False)
        b = ease((u - 1.0) / 0.4); kw = spec['cta']['keyword']; f = font('bebas', 110); pw = tw(kw, f) + 120
        top = 960 + int(40 * (1 - b))
        dr.rounded_rectangle((90, top - 30, W - 90, top + 300), radius=40, fill=(11, 31, 58, int(215 * b)), outline=GOLD + (int(130 * b),), width=3)
        dr.text((W // 2, top + 20), U['comment'], font=font('cinzel', 34), fill=GOLD + (int(255 * b),), anchor='mm')
        dr.rounded_rectangle(((W - pw) // 2, top + 55, (W + pw) // 2, top + 195), radius=70, fill=GOLD + (int(255 * b),))
        dr.text((W // 2, top + 128), kw, font=f, fill=NAVY + (int(255 * b),), anchor='mm')
        dr.text((W // 2, top + 245), spec['cta'].get('ask', U['ask']), font=font('pop', 30), fill=(255, 255, 255, int(220 * b)), anchor='mm')
        c = ease((u - 1.6) / 0.4)
        dr.text((W // 2, 1390), 'FOLLOW @marketingguru_vp', font=font('cinzel', 36), fill=GOLD + (int(255 * c),), anchor='mm')
        dr.text((W // 2, 1440), U['tag'], font=font('pop', 28), fill=(255, 255, 255, int(200 * c)), anchor='mm')
    S['cta'] = cta
    return S

ORDER = ['hook', 'mistake', 'fix', 'why', 'cta']
UI = {'en': dict(lesson='SALES LESSON #{n}', mistake='THE MISTAKE', fix='SAY THIS INSTEAD', why='WHY IT WORKS', save='SAVE *THIS.*',
                 comment='COMMENT', ask='if you will try this today', tag='25 years of field lessons. One a day.'),
      'hi': dict(lesson='AAJ KA MANTRA #{n}', mistake='GALTI', fix='YEH BOLO', why='KYUN KAAM KARTA HAI', save='SAVE *KARO.*',
                 comment='COMMENT KARO', ask='agar aaj try karoge', tag='25 saal ka field experience. Roz ek sabak.')}
def ui(spec): return UI['hi' if spec.get('lang', 'en').startswith('hi') else 'en']
MIN = {'hook': 2.8, 'mistake': 3.0, 'fix': 3.6, 'why': 3.0, 'cta': 4.5}

# ------------------------------------------------------------------ audio
def tts(spec, outdir):
    from kokoro_onnx import Kokoro
    import soundfile as sf
    k = Kokoro(os.path.join(ROOT, 'models', 'kokoro.onnx'), os.path.join(ROOT, 'models', 'voices-v1.0.bin'))
    hi = spec.get('lang', 'en').startswith('hi'); voice = spec.get('voice', 'hm_omega' if hi else 'am_michael'); clips = {}
    for s in ORDER:
        a, sr = k.create(spec[s]['vo'], voice=voice, speed=spec.get('speed', 1.05), lang='hi' if hi else 'en-us')
        nz = np.where(np.abs(a) > 0.01)[0]; clips[s] = a[max(nz[0] - 200, 0): nz[-1] + 1200]
    return clips, 24000

def music(dur, ci, bpm=88):
    from scipy.signal import lfilter
    SR = 44100; CH = [[[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]], [[50, 53, 57], [46, 50, 53], [53, 57, 60], [48, 52, 55]],
                      [[52, 55, 59], [48, 52, 55], [55, 59, 62], [50, 54, 57]], [[48, 52, 55], [45, 48, 52], [53, 57, 60], [55, 59, 62]]][ci % 4]
    def midi(n): return 440 * 2 ** ((n - 69) / 12)
    t = np.arange(int(dur * SR)) / SR; out = np.zeros_like(t); spb = 60 / bpm; cl = spb * 4
    for i in range(int(dur / cl) + 1):
        ch = CH[i % 4]; s0 = i * cl; seg = (t >= s0 - .3) & (t < s0 + cl + .6); tt = t[seg] - s0
        env = np.clip((tt + .3) / .6, 0, 1) * np.clip((cl + .6 - tt) / .6, 0, 1); pad = np.zeros_like(tt)
        for n in ch:
            for de in (-.08, .08): pad += 2 * ((midi(n + de) * tt) % 1) - 1
        out[seg] += lfilter([.04], [1, -.96], pad) * env * .05 + np.sin(2 * np.pi * midi(ch[0] - 12) * tt) * env * .16
        idx = np.where(seg)[0]
        for j in range(8):
            ps = j * spb / 2; m = (tt >= ps) & (tt < ps + 1.2); p = tt[m] - ps; f = midi(ch[[0, 1, 2, 1, 0, 2, 1, 2][j]] + 12)
            out[idx[m]] += (np.sin(2 * np.pi * f * p) + .35 * np.sin(4 * np.pi * f * p)) * np.exp(-p * 5) * .06
    b = 2.5
    while b < dur - .2:
        m = (t >= b) & (t < b + .45); p = t[m] - b; f = 45 + 80 * np.exp(-p * 25)
        out[m] += np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-p * 9) * .3; b += spb
    n = int(SR * 2.2); ir = np.random.default_rng(7).standard_normal(n) * np.exp(-np.linspace(0, 7, n)); ir /= np.abs(ir).sum() / 6
    N = 1 << (len(out) + n - 1).bit_length(); wet = np.fft.irfft(np.fft.rfft(out, N) * np.fft.rfft(ir, N), N)[:len(out)]
    out = out * .7 + wet * .3; out *= np.clip(t / 1, 0, 1) * np.clip((dur - t) / 1.5, 0, 1); out /= np.abs(out).max() + 1e-9
    return np.stack([out, out], 1) * .8, SR

# ------------------------------------------------------------------ main
def main():
    path = sys.argv[1]; preview = '--preview' in sys.argv
    spec = json.load(open(path)); slug = spec['slug']; outdir = os.path.join(ROOT, 'reels'); os.makedirs(outdir, exist_ok=True)
    S = scene_fns(spec); bg = make_bg(spec.get('theme', 'bokeh'), spec['n']); LOGO = logo()
    if preview:
        durs = {s: MIN[s] + 0.6 for s in ORDER}; clips = None
    else:
        clips, VSR = tts(spec, outdir)
        durs = {s: max(MIN[s], 0.35 + len(clips[s]) / VSR + 0.6) for s in ORDER}
    starts = {}; acc = 0.0
    for s in ORDER: starts[s] = acc; acc += durs[s]
    total = round(acc, 2)

    def frame(t):
        img = bg(t); lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for s in ORDER:
            u = t - starts[s]; d = durs[s]
            if -0.01 <= u <= d:
                L2 = Image.new('RGBA', (W, H), (0, 0, 0, 0)); S[s](L2, u, d)
                fo = 1 - smooth((u - (d - 0.25)) / 0.25) if s != 'cta' else 1
                if fo < 0.999: L2.putalpha(L2.getchannel('A').point(lambda v: int(v * fo)))
                lay.alpha_composite(L2)
        img.alpha_composite(lay); img.alpha_composite(LOGO); return img.convert('RGB')

    if preview:
        pts = [starts[s] + durs[s] * 0.8 for s in ORDER]
        sheet = Image.new('RGB', (5 * 300 + 40, 534), (0, 0, 0))
        for i, tt in enumerate(pts): sheet.paste(frame(tt).resize((300, 534)), (i * 310, 0))
        sheet.save(os.path.join(outdir, slug + '_preview.png')); frame(pts[2]).save(os.path.join(outdir, slug + '_fix.jpg'), quality=85)
        print('preview', total); return

    import soundfile as sf
    vo = np.zeros(int(total * VSR) + VSR)
    for s in ORDER:
        i0 = int((starts[s] + 0.35) * VSR); a = clips[s]; vo[i0:i0 + len(a)] += a
    vo = vo[:int(total * VSR)]; vo = vo / (np.abs(vo).max() + 1e-9) * 0.9
    tmpd = '/tmp/mgreel'; os.makedirs(tmpd, exist_ok=True)
    sf.write(f'{tmpd}/vo.wav', vo, VSR); mu, MSR = music(total, spec.get('chords', spec['n'])); sf.write(f'{tmpd}/mu.wav', mu, MSR)
    vid = f'{tmpd}/v.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', vid], stdin=subprocess.PIPE)
    for i in range(int(total * FPS)): p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close(); assert p.wait() == 0
    out = os.path.join(outdir, slug + '.mp4'); tmp = out[:-4] + '.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vid, '-i', f'{tmpd}/vo.wav', '-i', f'{tmpd}/mu.wav', '-filter_complex',
                    '[1:a]aresample=44100,aformat=channel_layouts=stereo,volume=1.6,asplit=2[vo][sc];[2:a]volume=0.3[m];'
                    '[m][sc]sidechaincompress=threshold=0.04:ratio=8:attack=15:release=350[md];[vo][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', tmp], check=True)
    os.replace(tmp, out)
    # cover image = fix scene frame
    frame(starts['hook'] + durs['hook'] * 0.85).save(os.path.join(outdir, slug + '_cover.jpg'), quality=90)
    print(json.dumps({'out': out, 'duration': total}))

if __name__ == '__main__':
    main()
