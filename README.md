# Coach Link — landing site

Jekyll site (EN + UA) for Coach Link, deployed to GitHub Pages at `https://coachlink.ab.team/`. Structure follows the "Coach Link — структура лендінгу" doc; design tokens and fonts come from the main `coach_link` app.

## Run

```bash
bundle install              # once (github-pages gem = the engine Pages uses)
bundle exec jekyll serve    # http://localhost:4000/   (UA: /uk/)
```

Without Bundler: `JEKYLL_NO_BUNDLER_REQUIRE=1 jekyll serve`.

## Where things are

- `_config.yml` — `url`, `baseurl`, email, Instagram, `form_endpoint` (empty = demo mode, nothing is sent). The custom domain is configured with `url: "https://coachlink.ab.team"` and an empty `baseurl`.
- `_data/en.yml`, `_data/uk.yml` — all copy. Edit text here, keep both files in sync.
- `_layouts/default.html`, `_includes/` — page shell and sections (`sections/*`, feature card art in `art/*`, live card / watch mockups).
- `index.html`, `uk/index.html`, `privacy.html`, `uk/privacy.html` — thin pages that pick the language via `lang:` front matter.
- `assets/` — `style.css`, `app.js`, fonts, `vendor/` (Lenis, GSAP, ScrollTrigger, no CDN).

All URLs go through `relative_url`, so the site works under any `baseurl`.

## Motion

Smooth scroll uses Lenis, scroll-driven animation uses GSAP + ScrollTrigger. Everything is decorative and degrades: with `prefers-reduced-motion` or without JS the page is static. The hero phone/watch and the pinned story are HTML/CSS mockups with simulated heart-rate data, not screenshots.

## TODO before launch

Real `instagram`, `email`; form backend; privacy policy review; analytics; hero video and screenshots (local files live in `assets/media/`, git-ignored for now).
