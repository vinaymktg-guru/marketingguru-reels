# The Marketing Guru – Daily Sales Lesson reels

Animated 9:16 reels (kinetic text, AI voiceover, original music, VP logo) for @marketingguru_vp (Instagram + Facebook), posted 1:00 PM IST daily after weekly approval.

- `setup.sh` – install deps + voice model (run once per fresh machine)
- `build.py lessons/NNN-slug.json [--preview]` – renders `reels/NNN-slug.mp4` and `_cover.jpg`
- `lessons/` – one JSON spec per reel (see build.py docstring). Lesson number = file prefix.
- `TOPICS.md` – topic bank; mark topics as used.
- `reels/` – published files. Public raw URL: `https://raw.githubusercontent.com/vinaymktg-guru/marketingguru-reels/main/reels/<file>`

Format (from research on viral reels, Nov 2026): 1) hook in the first 2 seconds with a specific promise, payoff at the end, 18-28 s; 2) kinetic word-by-word text + narration, scene change every ~3-5 s; 3) concrete, save/share-able lesson: Mistake -> exact line to say -> why it works -> "send this to a teammate who..." + comment keyword.
