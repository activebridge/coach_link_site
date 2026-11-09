# Coach Link — landing site

Static landing page (EN + UA) for Coach Link. Structure follows the "Coach Link — структура лендінгу" doc. Design tokens/fonts come from the main `coach_link` app.

```bash
python3 build.py              # regenerates index.html, privacy.html, uk/*
python3 -m http.server 8000   # http://localhost:8000  (UA: /uk/)
FORM_ENDPOINT=https://... python3 build.py   # wire the forms to a backend
```

Edit copy in `build.py` (dictionary `T`), styles in `assets/style.css`. Without `FORM_ENDPOINT` the forms run in demo mode (nothing is sent).

TODO before publishing: real `EVENT_DATE`, `INSTAGRAM`, `EMAIL`; hero video + feature screenshots; form backend; privacy policy review; analytics.
