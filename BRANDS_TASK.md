# Weekly build for the two other brands (Mera Bachcha India, Bharat AI)

Vinay approved the plan on 14 Nov 2026. Same engine as the Marketing Guru reels: add `"brand": "mb"` or `"brand": "ba"`
to a lesson JSON and build.py switches colours, logo, handle, labels and default voice.

| | Mera Bachcha India (`mb`) | Bharat AI (`ba`) |
|---|---|---|
| Metricool blogId | 8084158 | 8084230 |
| Networks | Instagram @merabachcha_india + Facebook | Instagram @bharat_ai3110 + Facebook |
| Post time (IST) | 11:30 | 19:00 |
| Reel voice | hf_alpha (Hindi female), speed 1.08 | hm_omega (Hindi male), speed 1.12 |
| Labels | AAJ KI BAAT / AKSAR GALTI / YEH KAREIN / KYUN ZAROORI HAI | AI TIP / PURANA TAREEKA / YEH PROMPT LIKHO / FAYDA |
| Slug prefix | `mb-NNN-…` | `ba-NNN-…` |

## Week pattern (Mon to Sat, Sunday rest)
Mera Bachcha: Mon reel parenting habit · Tue poster health checklist · Wed reel growth milestone · Thu carousel myth vs fact · Fri reel health awareness · Sat poster mother's wellbeing.
Bharat AI: Mon reel AI for sales · Tue carousel 5 prompts · Wed reel AI for marketing · Thu reel tool in 30 sec · Fri carousel before vs after AI · Sat reel sales + AI.

## Reels (3 a week for mb, 4 for ba)
1. `bash setup.sh`. Number reels from the highest existing `lessons/mb-*.json` / `lessons/ba-*.json` (start at 001).
2. Write the lesson JSON like lessons/001-just-checking-in.json plus `"brand"`. On-screen text Hinglish in Roman script (max ~14 words a scene),
   `vo` in Devanagari, `"lang": "hi"`. Target 22 to 30 seconds. Keys caption, first_comment as in the reference (no yt_ keys: these brands have no YouTube).
   For `ba` the "fix" scene shows the exact prompt to type (short), "mistake" shows the slow old way.
3. `python3 build.py lessons/<file>.json --preview`, look at reels/<slug>_preview.png (no overflow, nothing cut), then build fully.
4. Commit and push; use COMMIT-PINNED raw URLs (https://raw.githubusercontent.com/vinaymktg-guru/marketingguru-reels/<sha>/reels/<slug>.mp4 and _cover.jpg); check HTTP 200.
5. createScheduledPost: providers instagram + facebook, instagramData {"type":"REEL","showReelOnFeed":true,"isAiGenerated":true}, facebookData {"type":"REEL"}, media = mp4 URL, videoThumbnailUrl = cover URL, autoPublish true.

## Posters and carousels (Canva)
1080x1440. Poster = 1 page, carousel = 5 slides. Same look every time for each brand.
- mb: deep plum #400A2C background, pink #FF96C4 accents, white text, friendly rounded bold headlines, simple flat illustrations (toys, books, clock, plate, a parent with a school-age child seen from behind). Footer "@merabachcha_india". Top-left wordmark "MERA BACHCHA INDIA".
- ba: navy #091830 background, saffron #FF8A1F accents with a little green #1FA971, white text, bold condensed caps headlines, prompts shown inside a rounded "chat box". Footer "@bharat_ai3110". Top-left wordmark "BHARAT AI".
- ba logo: every ba post/carousel uses the new logo top-left (Canva asset MAHbO23fsAQ = assets/ba_header_transparent.png), not typed "Bharat AI" text.
Check every page in the thumbnail (text exact, nothing overflows, straight quotes), export png, schedule as instagramData {"type":"POST"} + facebookData {"type":"POST"}.

## Captions
Hinglish. Hook line, 1 to 2 lines of value, a save line and a share line, exactly 5 hashtags.
mb always starts #MeraBachchaIndia (mix #ParentingTipsHindi #BachchonKiParvarish #ParentingIndia #MomLife); ends health posts with "Apne doctor se salah zaroor lein."
ba always starts #BharatAI (mix #AITipsHindi #ChatGPTHindi #SalesTips #AIForBusiness). firstCommentText = one question.

## Rules
mb (STRICT, IMS Act and safety): never infant formula, feeding bottles, baby food, breastfeeding or feeding advice, supplements, medicines, any company or product; no babies under 2 in pictures and no mother-with-infant imagery; health topics only as general awareness that matches public guidance from WHO, IAP or the Ministry of Health (check with WebSearch, name the source in the email); no diagnosis, dose or treatment; no fear hooks; no real child or parent names.
ba: check every tool name, feature and price on the tool's official page before writing it; no "free forever" or earnings claims; prompts must be ones you have reasoned through as sensible; AI content labelled.
Both: no politics, no religion, never name British Life Sciences or its products, no invented statistics, no real customer/doctor/colleague names.

## Bharat AI carousels: CINEMATIC style (from 22 Nov 2026, Vinay: "I like this kind of Carousel for Bharat AI")
Replaces the navy chat-box look for ba carousels. Full-bleed cinematic AI picture, same hero every time, two-line headline at the bottom.
- Hero: field salesman, early 30s, short black hair, neat beard, white shirt rolled sleeves, dark trousers, brown leather satchel, vintage black motorcycle,
  plus a small glowing saffron-orange orb of light beside him (the orb = AI). Reference image Canva asset MAHblMTeBq4: pass it in imageReferences on every
  generate-image call (PORTRAIT_3_4) and write "Same man, same white shirt..., same orb". Painterly, golden hour, brown/amber, subject in upper two thirds,
  lower third dark. Always add "No temples, no religious buildings or symbols. No text, no letters, no logos."
- Template: copy-design DAHblDlwzPw (6 slides; add slides with merge-designs insert_pages, ONE operation per call). Each page = image rect (update_fill),
  white line (condensed font, 88 px; 72 if over 24 characters), saffron #FF8A1F line (88 px for a slogan, 58 px for a 2-line prompt, top 1135-1140),
  small "@bharat_ai3110" line, "Visual AI se bana hai", logo top-left. Element ids differ on every page and in every copy: read design_content first.
- Slide plan: cover, one idea per slide (white = label or "Pehle: ...", saffron = the prompt to copy), last slide "Follow @bharat_ai3110".
  Tue = 5 prompts (7 slides), Fri = before vs after AI (6 slides). Caption line: "Is post ke visuals AI se bane hain."
- Check every thumbnail for religious buildings/symbols in the background and regenerate if any (the first hilltop image MAHblNayL1I has a spire: do not use).
