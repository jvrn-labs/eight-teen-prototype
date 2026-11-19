# EIGHT TEEN · MVP 1 prototype

A clickable prototype of the EIGHT TEEN app (PRD v1.3): a verified, campus-only social feed for Thai university students. There's no backend. Everything runs in the browser, and the data stays on the device.

**Open it:** https://jvrn-labs.github.io/eight-teen-prototype/

## Use it like an app on your phone

- **iPhone (Safari):** Share → **Add to Home Screen**.
- **Android (Chrome):** ⋮ menu → **Install app** (or **Add to Home screen**).

It then opens full screen from its own icon and keeps working offline.

Phone support: works from 320px (iPhone SE) up to large phones, keeps inputs above the keyboard, follows the iPhone text-size setting (or Settings › Theme & text › Text size), and asks you to turn the phone upright in landscape.

## Testing

- On the sign-in step, use one of the test accounts, or type any email:
  - `@student.chula.ac.th` gets in.
  - Another university's domain (`.ac.th`, `.edu`) puts you on that university's waitlist.
  - Gmail or Outlook is refused.
- Test tools on a phone: **Prototype test tools** on the welcome screen, or **Me → ⚙ → Prototype test tools** after sign-up. On a desktop they show beside the phone. You can jump to any screen, simulate events, reset the demo and watch the analytics event log there.
- To try the AI moderation, type one of these in a post: `โอนเงินก่อน` (blocked as a scam), `อยากตาย` (shows the support sheet), `ขายต่อ` (published with reduced reach).

## Files

- `eight-teen-prototype.html`: the app source (an HTML fragment, also published as a claude.ai artifact)
- `build.py`: wraps the source into `index.html` and generates `sw.js` (`python3 build.py`)
- `manifest.webmanifest`, `icons/`, `sw.template.js`: what makes it installable and work offline
- `img/`: sample photos

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
