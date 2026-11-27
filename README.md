# EIGHT TEEN · prototypes

Clickable prototypes of EIGHT TEEN, a verified, campus-only social app for Thai university students. There's no backend. Everything runs in the browser, and the data stays on the device.

**Link for testers:** https://jvrn-labs.github.io/eight-teen-prototype/

This link always opens the current test build. Right now that's **v2.3 A**. The older links testers already have, `/v2.1/` and `/v2.2/`, also open the current build.

**A/B test (from 27 Nov 2026):** v2.3 A and v2.3 B are the same app with a different home feed. Give testers either the root link (A) or the B link; each version keeps its own saved data.

## Versions

| Version | Link | What it is |
| --- | --- | --- |
| v2.4 A (for founder review) | [/v2.4a/](https://jvrn-labs.github.io/eight-teen-prototype/v2.4a/) | v2.3 A restyled as a Story-style frame (rounded media with space around it, author on top, actions in a bar below) + "all of Chula hears it": every post is guaranteed its first 300 viewers (new posts get every 3rd slot in Hot), a "👁 seen by" count on every post, a live 🚀 0→300 progress chip on your own post, a reach onboarding slide, a one-question survey ("where would you have posted this?"), the daily question as a post in the feed (4th item; skip it and it returns once 6 posts later, skip twice and it is gone for the day; ⏰ in the header always opens it). Co-founder round (27 Nov): no anonymous aliases (everyone sets a name + photo), tap a name for a profile page with a Direct Message button, a Chat tab, share posts to people in the app or to other apps, comments as a list under the post (Stories-style comment timeline removed), ATE is the only reaction (🔥 + "ATE" animation), ATE breakdown by faculty/year visible to the post owner only, posts are photo or voice (GIF only in comments), a 🫧 Bubble chip/tool instead of the location pin, one mute button on the post itself (none in voice players or the header), and replies to comments (post > comment > reply) that @tag and notify the person. The first-300 guarantee is no longer shown to users (no 🚀 chip, progress bar, toast, notification or survey); ranking still gives new posts their first audience behind the scenes. Comments can be typed: the comment bar is a text field with GIF and camera inside and a hold-to-talk mic (swaps to send while typing); names in typed comments are auto-hidden |
| v2.4 B (for founder review) | [/v2.4b/](https://jvrn-labs.github.io/eight-teen-prototype/v2.4b/) | The same reach features and co-founder changes on the v2.3 B card feed (B keeps text posts) |
| **v2.3 A** (current) | [/v2.3a/](https://jvrn-labs.github.io/eight-teen-prototype/v2.3a/) | Full-bleed feed (one post per screen) + photo filters, frames and emoji stickers |
| **v2.3 B** | [/v2.3b/](https://jvrn-labs.github.io/eight-teen-prototype/v2.3b/) | Facebook-style card feed with text + voice posts first, plus the same photo filters and decorations |
| v2.2 | [/archive/v2.2/](https://jvrn-labs.github.io/eight-teen-prototype/archive/v2.2/) | User-testing round 1 fixes: speech-bubble comments, photo + voice, name or anonymous, one-tap poll and GIF answers, "same here" with faculty/year breakdown |
| v2.1 | [/archive/v2.1/](https://jvrn-labs.github.io/eight-teen-prototype/archive/v2.1/) | Stoic-style daily ritual, full-bleed feed, comment highlights |
| v2 | [/v2/](https://jvrn-labs.github.io/eight-teen-prototype/v2/) | Media pivot: voice, photo and GIF posts, anonymous-first |
| v1 | [/archive/v1/](https://jvrn-labs.github.io/eight-teen-prototype/archive/v1/) | MVP 1 (PRD v1.3, design v1.7): text-first campus feed, installable app |

## How versions work

- **Testers get one link: the root.** `index.html` at the root redirects to the current build. To switch builds, change `CURRENT` (and the `<noscript>` line) in `index.html`.
- **The current build has its own folder** (now `v2.3a/` and `v2.3b/`) with its own saved data on the phone.
- **A and B share the same code.** Near the top of each `index.html`, `const LAYOUT` is `'full'` in A and `'feed'` in B, and the storage key differs. Apply a bug fix to both folders.
- **A link that testers already have keeps working.** When a version is replaced, its build moves into `archive/` and its old folder becomes a small redirect to the root, so it follows the current build too. `v2.1/` and `v2.2/` work this way. When moving a build into `archive/`, change its `../img/` and `../icons/` paths to `../../img/` and `../../icons/`.
- **Small fixes go into the current folder. A new idea to test gets a new folder** (copy the folder, bump the version in the title, footer and storage key), so results from one test round always match one build.
- **Shared files** live at the root and are used by every version: `img/` (sample photos and GIFs), `icons/`, `brand/`.
- **`sw.js` at the root is retired.** It clears the offline cache from when v1 was installed at the root. Keep it for a few weeks after 27 Nov 2026, then delete it.

---

# v1 (archive)

**Open it:** https://jvrn-labs.github.io/eight-teen-prototype/archive/v1/

## Use it like an app on your phone

- **iPhone (Safari):** Share → **Add to Home Screen**.
- **Android (Chrome):** ⋮ menu → **Install app** (or **Add to Home screen**).

It then opens full screen from its own icon and keeps working offline.

Phone support: works from 320px (iPhone SE) up to large phones, keeps inputs above the keyboard, follows the iPhone text-size setting (or Settings › Theme & text › Text size), and asks you to turn the phone upright in landscape.

## Links to each screen

Every v1 screen has its own link (add it after `/archive/v1/`), so testers can open it directly or send it in a bug report. The link in the address bar updates as you move around the app, and **Prototype test tools → Copy link** copies it. Opening an app link skips onboarding with a test account.

| Screen | Link |
| --- | --- |
| University feed | `#/home` |
| Bubble map | `#/home/bubble` |
| New post | `#/compose` |
| Post detail | `#/post/p1` (any post id, e.g. `p8` voice post, `p9` GIF post) |
| Search | `#/search` |
| Activity | `#/activity` |
| My profile / a classmate | `#/profile` / `#/profile/u2` |
| Edit profile | `#/editProfile` |
| Settings and its pages | `#/settings`, `#/account`, `#/privacy`, `#/language`, `#/theme`, `#/help` |
| Help pages | `#/rules`, `#/privacyPolicy`, `#/support/contact`, `#/support/problem`, `#/deleteAccount`, `#/credits` |
| A place / a hashtag | `#/bubble/lib`, `#/hashtag/สามย่าน` |
| Onboarding steps | `#/onboarding/welcome`, `consent`, `sso`, `dob`, `profile`, `interests`, `location`, `push` |

## Testing

- On the sign-in step, use one of the test accounts, or type any email:
  - `@student.chula.ac.th` gets in.
  - Another university's domain (`.ac.th`, `.edu`) puts you on that university's waitlist.
  - Gmail or Outlook is refused.
- Test tools on a phone: **Prototype test tools** on the welcome screen, or **Me → ⚙ → Prototype test tools** after sign-up. On a desktop they show beside the phone. You can jump to any screen, simulate events, reset the demo and watch the analytics event log there.
- To try the AI moderation, type one of these in a post: `โอนเงินก่อน` (blocked as a scam), `อยากตาย` (shows the support sheet), `ขายต่อ` (published with reduced reach).

## Files

- `archive/v1/eight-teen-prototype.html`: the v1 app source (an HTML fragment, also published as a claude.ai artifact)
- `archive/v1/build.py`: wraps the source into `archive/v1/index.html` and generates `archive/v1/sw.js` (`python3 archive/v1/build.py`)
- `archive/v1/manifest.webmanifest`, `archive/v1/sw.template.js`: what makes v1 installable and work offline
- `img/`, `icons/`: shared by every version

## Sample photo credits (Wikimedia Commons, resized, EXIF removed)

| File | Photo | Author | License |
| --- | --- | --- | --- |
| chicken-rice.jpg | [Hainanese chicken rice](https://commons.wikimedia.org/wiki/File:Hainanese_chicken_rice.jpg) | Misaochan | CC BY 4.0 |
| library.jpg | [Chula UltimateX Library](https://commons.wikimedia.org/wiki/File:Chula_UltimateX_Library_20201124_182323.jpg) | Apiwat K. | CC BY 4.0 |
| arts-library.jpg | [Faculty of Arts Library, Chulalongkorn University](https://commons.wikimedia.org/wiki/File:Faculty_of_Arts_Library,_Chulalongkorn_University.jpg) | Geonuch | CC BY-SA 4.0 |
| auditorium.jpg | [Chulalongkorn University Auditorium](https://commons.wikimedia.org/wiki/File:Chulalongkorn_University_Auditorium.jpg) | Supanut Arunoprayote | CC BY-SA 4.0 |
| sala.jpg | [Entrance of Sala Phra Kiao](https://commons.wikimedia.org/wiki/File:Entrance_of_Sala_Phra_Kiao.jpg) | Supanut Arunoprayote | CC BY 4.0 |
| sala-night.jpg | [Event in Sala Phra Kiao at night](https://commons.wikimedia.org/wiki/File:Event_in_Sala_Phra_Kiao_at_night.jpg) | Supanut Arunoprayote | CC BY 4.0 |
| samyan.jpg | [Samyan Mitrtown (back)](https://commons.wikimedia.org/wiki/File:Samyan_Mitrtown_Back.jpg) | Chainwit. | CC BY-SA 4.0 |

### Profile pictures (v1.5)

The 12 sample profile pictures in `img/av/` are Unsplash photos served by Picsum. They are free to use under the [Unsplash License](https://unsplash.com/license). They were cropped to 256×256 with EXIF removed. Photographers: Ryan Mcguire (cat), André Spieker (dog), Alexander Shustov (golden hour), Ilham Rahmansyah (sneakers), Daniel Robert (concert), Steven Spassov (petals), Sebastian Muller (bokeh), Coley Christine (dandelion), Rula Sibai (blossom), Nicola Perantoni (camera), Sonja Langford (tea), J Duclos (sky). The in-app credits screen has the links.
