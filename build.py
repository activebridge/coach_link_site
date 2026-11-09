#!/usr/bin/env python3
"""Builds index.html (EN), uk/index.html (UA) and privacy pages from the strings below. No dependencies."""
import os, html

# Set to a form backend URL (Formspree, Basin, own Rails endpoint). Empty = demo mode, nothing is sent.
FORM_ENDPOINT = os.environ.get("FORM_ENDPOINT", "")
EVENT_DATE = "TBA"  # put the real launch-event date here
INSTAGRAM = "https://instagram.com/coachlink"  # TODO real handle
EMAIL = "hello@coachlink.app"  # TODO real address

T = {
"en": dict(
 lang="en", prefix="", other="uk/", other_label="UA", title="Coach Link — see how your client feels, live",
 desc="Coach Link turns your client's Garmin, Apple Watch or Amazfit into a live coaching dashboard on your phone. Free for clients. Apply for the beta.",
 nav_event="Launch event", nav_cta="Apply for the beta",
 h1="See how your client feels — live, from the watch they already wear.",
 sub="Coach Link turns your client's Garmin, Apple Watch or Amazfit into a live coaching dashboard on your phone. Free for clients.",
 cta="Apply for the beta", demo="Watch the demo", close="Close", spots="Beta spots: 100 · 1 year free for beta coaches",
 pains_h="Sound familiar?", pains=["“Is she pushing hard or just coasting?”","“He slept 4 hours — and you find out on set three.”","“Counting reps in your head while watching their form.”"],
 how_h="How it works", steps=["Your client installs the free Coach Link app on their watch.","You scan the QR code on their watch.","Their heart rate, zones and stats appear on your phone — live."],
 how_note="No chest straps. No extra hardware. Works with many clients at once.",
 feat_h="Before, during and after the session", soon="Coming soon",
 feats=[("During","Live client view","Heart rate, zones and effort for every client in real time. Get an alert when someone goes too hard — or not hard enough.",0),
        ("Before","Readiness check","See sleep, stress and recovery before the session starts. Know when to push and when to go easy.",0),
        ("After","Session report & progress","Every workout is saved. Clients get a shareable summary; you get proof of progress: resting heart rate, recovery, consistency.",0),
        ("During","Poke","Tap once and the client's watch vibrates and glows. Get their attention without a word.",0),
        ("During","The whole body picture","Heart rate in zone colours plus stress, breathing, Body Battery, heart rate variability and blood oxygen where the watch has them.",0),
        ("During","In the gym or on camera","Stand next to your client or coach over a video call. The card is the same: you see the body, they hear your cue.",0),
        ("After","Advice from the data","Short pointers worked out from recent workouts: when to rest, how much load, how recovery is going.",0),
        ("After","Notes & trends","Keep notes on every client and workout, and see trends by week, month and year.",0),
        ("During","Sets & reps tracking","The watch counts sets and reps automatically. No more notebooks between sets.",1)],
 trust_h="Your clients will say yes", trust=["Free for your clients. Always.","Clients choose what to share and can stop anytime.","Works with the watch they already have."],
 beta_h="Become a founding coach.", beta=["1 year of Coach Link PRO free","Your own promo code — earn a share of every subscription it brings","Direct line to the founder: your feedback shapes the product","Only 100 spots"],
 price_h="Simple pricing, from $5/month",
 plans=[("PRO","$5","Up to 5 clients at the same time. All features.",True),("PRO MAX","$15","Unlimited clients at the same time. All features. Best for group classes and busy coaches.",False)],
 popular="Most popular", per="/ month", price_note="Free for clients. Beta coaches get the first year of PRO free.",
 watches_h="Works with", watches=["Garmin","Apple Watch","Amazfit","Wear OS (coming soon)"],
 faq_h="FAQ", faq=[("Which watches are supported?","Garmin, Apple Watch and Amazfit. Wear OS is coming soon."),("Does my client need to pay?","No. The app is free for clients, always."),("Does it drain the battery?","Coach Link only sends data during a session you have started together, so a normal workout is not affected noticeably. We will publish real numbers from the beta."),("How many clients can I track at once?","Up to 5 on PRO, unlimited on PRO MAX."),("Is client data private?","Clients choose what to share and can stop anytime. See our privacy policy."),("When does the beta start?","We review applications and reply within 7 days. Apply now to get a founding-coach spot.")],
 apply_h="Apply for the beta", apply_p="Takes less than a minute. We review applications by hand and reply within 7 days.",
 f=dict(name="Name",email="Email",social="Instagram / TikTok",country="Country, city",how="How do you coach?",clients="Active clients",watch="Your clients' watches",consent="I agree to the processing of my data as described in the privacy policy.",send="Send application"),
 how_opts=["1:1 in gym","Group classes","Running","Online"], watch_opts=["Garmin","Apple Watch","Amazfit","Wear OS","Other","Don't know"],
 thanks_h="You're on the list.", thanks_p="We'll review applications and reply within 7 days.", cal="Add the launch event to your calendar",
 ref="Invite another coach — applications with referrals are reviewed first.", copy="Copy your invite link", copied="Copied!",
 ev_h="Join the launch event", ev_p="Not in the beta? Come to the online launch.", ev_date="Date: ", ev_btn="Join the launch event", ev_ph="Your email",
 privacy="Privacy policy", rights="© Coach Link",
 priv_h="Privacy policy", priv=[("What we collect","The details you enter in the beta application or launch-event form: name, email, social handle, location, coaching type, number of clients and watch types. We also record which channel you came from (UTM tags) and a referral code if you used one."),("Why","To review beta applications, contact you about the beta and the launch event, and decide which watches to support first."),("Who sees it","Only the Coach Link team and the services we use to store the data and send email. We do not sell your data."),("Your rights","Write to "+EMAIL+" to see, correct or delete your data, or to withdraw consent at any time."),("Health data","This site does not collect health data. The Coach Link app only shares what a client chooses to share with their coach.")],
 back="Back to the site",
 reel_alt=dict(hero="Live heart rate of a client during training, shown on the coach's phone",zone="Zone alert on the coach's phone",ready="Sleep and readiness before the session",report="Workout history and progress",pair="Scanning the QR code to pair a Garmin watch",pairu="Pairing an Apple Watch Ultra",free="Free watch app for clients",poke_g="Poke on Garmin",poke_a="Poke on Apple Watch Ultra"),
 poke_h="Poke your client", poke_p="One tap on your phone, and it buzzes on their wrist. Works on Garmin and Apple Watch.", sound="Tap a video for sound"),
"uk": dict(
 lang="uk", prefix="../", other="../", other_label="EN", title="Coach Link — бачте, як почувається клієнт, наживо",
 desc="Coach Link перетворює Garmin, Apple Watch чи Amazfit вашого клієнта на живу панель тренера на телефоні. Для клієнтів безкоштовно. Подайте заявку на бету.",
 nav_event="Івент запуску", nav_cta="Заявка на бету",
 h1="Бачте, як почувається клієнт — наживо, з годинника, який він уже носить.",
 sub="Coach Link перетворює Garmin, Apple Watch чи Amazfit вашого клієнта на живу панель тренера на телефоні. Для клієнтів безкоштовно.",
 cta="Подати заявку на бету", demo="Дивитись демо", close="Закрити", spots="Місць у бета-версії: 100 · рік безкоштовно для бета-тренерів",
 pains_h="Знайомо?", pains=["«Вона дає максимум чи просто відбуває?»","«Він спав 4 години — а ви дізнаєтесь на третьому підході.»","«Рахуєте повтори в голові й водночас стежите за технікою.»"],
 how_h="Як це працює", steps=["Клієнт встановлює безкоштовний застосунок Coach Link на годинник.","Ви скануєте QR-код на його годиннику.","Пульс, зони й показники з'являються на вашому телефоні — наживо."],
 how_note="Без нагрудних датчиків. Без додаткового заліза. Працює з багатьма клієнтами одночасно.",
 feat_h="До, під час і після тренування", soon="Скоро",
 feats=[("Під час","Клієнти наживо","Пульс, зони й навантаження кожного клієнта в реальному часі. Сповіщення, коли хтось працює надто сильно — або надто слабко.",0),
        ("До","Готовність до тренування","Сон, стрес і відновлення ще до початку заняття. Ви знаєте, коли тиснути, а коли пожаліти.",0),
        ("Після","Звіт і прогрес","Кожне тренування зберігається. Клієнт отримує підсумок, яким можна поділитись; ви — доказ прогресу: пульс спокою, відновлення, регулярність.",0),
        ("Під час","Поштовх","Один дотик — і годинник клієнта вібрує та світиться. Привернути увагу без слів.",0),
        ("Під час","Повна картина тіла","Пульс у кольорах зон, а також стрес, дихання, Body Battery, варіабельність пульсу й кисень у крові — де це є на годиннику.",0),
        ("Під час","У залі чи на камеру","Стійте поруч або тренуйте по відеозв'язку. Картка та сама: ви бачите тіло, клієнт чує вашу підказку.",0),
        ("Після","Поради з даних","Короткі підказки з недавніх тренувань: коли відпочити, яке навантаження, як іде відновлення.",0),
        ("Після","Нотатки й тренди","Нотатки по кожному клієнту й тренуванню та тренди за тиждень, місяць і рік.",0),
        ("Під час","Підходи й повтори","Годинник сам рахує підходи й повтори. Більше жодних зошитів між підходами.",1)],
 trust_h="Клієнти скажуть «так»", trust=["Для клієнтів безкоштовно. Завжди.","Клієнт сам обирає, чим ділитись, і може зупинити будь-коли.","Працює з годинником, який у нього вже є."],
 beta_h="Станьте тренером-засновником.", beta=["Рік Coach Link PRO безкоштовно","Власний промокод — частка від кожної підписки, яку він приведе","Пряма лінія до засновника: ваш відгук формує продукт","Лише 100 місць"],
 price_h="Проста ціна, від $5 на місяць",
 plans=[("PRO","$5","До 5 клієнтів одночасно. Усі можливості.",True),("PRO MAX","$15","Без обмежень за кількістю клієнтів. Усі можливості. Для групових занять і завантажених тренерів.",False)],
 popular="Найпопулярніший", per="/ міс", price_note="Для клієнтів безкоштовно. Бета-тренери отримують перший рік PRO безкоштовно.",
 watches_h="Працює з", watches=["Garmin","Apple Watch","Amazfit","Wear OS (скоро)"],
 faq_h="Питання й відповіді", faq=[("Які годинники підтримуються?","Garmin, Apple Watch та Amazfit. Wear OS — скоро."),("Чи має клієнт платити?","Ні. Для клієнтів застосунок безкоштовний, завжди."),("Чи розряджає батарею?","Coach Link передає дані лише під час тренування, яке ви почали разом, тож звичайне заняття помітно не страждає. Реальні цифри опублікуємо після бети."),("Скількох клієнтів можна вести одночасно?","До 5 на PRO, без обмежень на PRO MAX."),("Чи приватні дані клієнта?","Клієнт сам обирає, чим ділитись, і може зупинити будь-коли. Див. політику конфіденційності."),("Коли стартує бета?","Ми переглядаємо заявки й відповідаємо протягом 7 днів. Подайте заявку, щоб отримати місце тренера-засновника.")],
 apply_h="Заявка на бету", apply_p="Менше хвилини. Ми розглядаємо заявки вручну й відповідаємо протягом 7 днів.",
 f=dict(name="Ім'я",email="Email",social="Instagram / TikTok",country="Країна, місто",how="Як ви тренуєте?",clients="Активних клієнтів",watch="Годинники ваших клієнтів",consent="Погоджуюсь на обробку даних відповідно до політики конфіденційності.",send="Надіслати заявку"),
 how_opts=["Індивідуально в залі","Групові заняття","Біг","Онлайн"], watch_opts=["Garmin","Apple Watch","Amazfit","Wear OS","Інший","Не знаю"],
 thanks_h="Ви в списку.", thanks_p="Ми розглянемо заявки й відповімо протягом 7 днів.", cal="Додати івент запуску в календар",
 ref="Запросіть ще одного тренера — заявки з рекомендацією розглядаємо першими.", copy="Скопіювати посилання-запрошення", copied="Скопійовано!",
 ev_h="Приєднуйтесь до івенту запуску", ev_p="Не пройшли в бету? Приходьте на онлайн-запуск.", ev_date="Дата: ", ev_btn="Приєднатись до івенту", ev_ph="Ваш email",
 privacy="Політика конфіденційності", rights="© Coach Link",
 priv_h="Політика конфіденційності", priv=[("Що ми збираємо","Дані, які ви вводите у формі заявки на бету чи реєстрації на івент: ім'я, email, акаунт у соцмережі, місце, тип тренувань, кількість клієнтів і типи годинників. Також фіксуємо канал, з якого ви прийшли (UTM-мітки), і реферальний код, якщо він був."),("Навіщо","Щоб розглядати заявки на бету, зв'язуватись щодо бети й івенту та визначати, які годинники підтримувати першими."),("Хто бачить","Лише команда Coach Link і сервіси, які ми використовуємо для зберігання даних і розсилки. Ми не продаємо ваші дані."),("Ваші права","Напишіть на "+EMAIL+", щоб побачити, виправити чи видалити свої дані або відкликати згоду."),("Дані про здоров'я","Цей сайт не збирає даних про здоров'я. Застосунок Coach Link передає тренеру лише те, чим клієнт вирішив поділитись.")],
 back="Назад на сайт",
 reel_alt=dict(hero="Пульс клієнта під час тренування на телефоні тренера",zone="Сповіщення про зону на телефоні тренера",ready="Сон і готовність до тренування",report="Історія тренувань і прогрес",pair="Сканування QR-коду для підключення Garmin",pairu="Підключення Apple Watch Ultra",free="Безкоштовний застосунок для клієнта",poke_g="Poke на Garmin",poke_a="Poke на Apple Watch Ultra"),
 poke_h="Підштовхніть клієнта", poke_p="Один дотик на вашому телефоні, і годинник клієнта вібрує. Працює на Garmin та Apple Watch.", sound="Торкніться відео, щоб увімкнути звук"),
}

def e(s): return html.escape(s, quote=True)

def reel(t, name, alt, eager=False):
    p = t["prefix"] + "assets/media/reels/"
    return (f'<div class="reel"><video muted loop playsinline preload="{"auto" if eager else "none"}" poster="{p}posters/{name}.jpg" aria-label="{e(alt)}"'
            f'{" data-eager" if eager else ""}><source src="{p}{name}.mp4" type="video/mp4"></video></div>')

FEAT_VIDEO = [("03-zone-alert", "zone"), ("07-readiness", "ready"), ("06-workout-history", "report"), None]

def head(t, title, desc, path):
    p = t["prefix"]
    return f'''<!doctype html>
<html lang="{t["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="{p}assets/logo.svg"><link rel="preload" href="{p}assets/fonts/Onest-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/style.css"></head><body>'''

def bar(t, home):
    p, h = t["prefix"], ("" if home else "index.html")
    cta = f'<a class="btn" href="{h}#apply">{e(t["nav_cta"])}</a>'
    return f'''<header class="bar"><div class="wrap"><a class="brand" href="{h or "./"}"><img src="{p}assets/logo.svg" alt="">Coach Link</a>
<nav><a class="hide-m" href="{h}#event">{e(t["nav_event"])}</a><a href="{t["other"]}" hreflang="{ "uk" if t["lang"]=="en" else "en"}">{t["other_label"]}</a>{cta}</nav></div></header>'''

def page(t):
    f = t["f"]
    pains = "".join(f'<div class="box">{e(x)}</div>' for x in t["pains"])
    steps = "".join(f'<div class="box step"><b>{i}</b><p>{e(x)}</p></div>' for i, x in enumerate(t["steps"], 1))
    feats = "".join(f'<div class="box"><div class="when">{e(w)}</div>{"<span class=tag>"+e(t["soon"])+"</span>" if s else ""}<h3>{e(h)}</h3><p class="muted">{e(b)}</p>{reel(t,v[0],t["reel_alt"][v[1]]) if v else ""}</div>' for (w,h,b,s),v in zip(t["feats"],FEAT_VIDEO))
    trust = "".join(f"<li>{e(x)}</li>" for x in t["trust"])
    beta = "".join(f"<li>{e(x)}</li>" for x in t["beta"])
    plans = "".join(f'<div class="plan{" main" if m else ""}">{"<span class=tag>"+e(t["popular"])+"</span>" if m else ""}<h3>{e(n)}</h3><div class="price">{p} <small>{e(t["per"])}</small></div><p class="muted">{e(d)}</p></div>' for n,p,d,m in t["plans"])
    watches = "".join(f"<span>{e(x)}</span>" for x in t["watches"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in t["faq"])
    how = "".join(f'<label><input type="checkbox" name="how" value="{e(o)}"> {e(o)}</label>' for o in t["how_opts"])
    wopts = "".join(f'<label><input type="checkbox" name="watches" value="{e(o)}"> {e(o)}</label>' for o in t["watch_opts"])
    return head(t, t["title"], t["desc"], "") + bar(t, True) + f'''
<main>
<section class="hero"><div class="wrap grid"><div>
<h1>{e(t["h1"])}</h1><p class="sub">{e(t["sub"])}</p>
<div class="cta"><a class="btn" href="#apply" data-track="cta-hero">{e(t["cta"])}</a><button class="btn ghost" type="button" id="demo-open" data-track="demo">{e(t["demo"])}</button></div>
<small>{e(t["spots"])}</small></div>
<div class="hero-reel">{reel(t,"02-live-heart-rate",t["reel_alt"]["hero"],True)}<small>{e(t["sound"])}</small></div></div></section>
<section class="pain"><div class="wrap"><h2>{e(t["pains_h"])}</h2><div class="cols3">{pains}</div></div></section>
<section style="padding-top:0"><div class="wrap"><h2>{e(t["how_h"])}</h2><div class="cols3">{steps}</div><p class="muted" style="margin-top:20px"><strong>{e(t["how_note"])}</strong></p><div class="reels2">{reel(t,"05-pairing",t["reel_alt"]["pair"])}{reel(t,"09-apple-watch-ultra-pairing",t["reel_alt"]["pairu"])}</div></div></section>
<section id="demo" style="background:var(--sunk)"><div class="wrap"><h2>{e(t["feat_h"])}</h2><div class="cols3" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">{feats}</div></div></section>
<section class="trust"><div class="wrap trust-grid"><div><h2>{e(t["trust_h"])}</h2><ul>{trust}</ul></div>{reel(t,"01-free-watch-app",t["reel_alt"]["free"])}</div></section>
<section class="beta"><div class="wrap"><h2>{e(t["beta_h"])}</h2><ul>{beta}</ul><a class="btn" href="#apply" data-track="cta-beta">{e(t["cta"])}</a></div></section>
<section><div class="wrap"><h2>{e(t["price_h"])}</h2><div class="plans">{plans}</div><p class="muted" style="margin-top:16px">{e(t["price_note"])}</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2>{e(t["watches_h"])}</h2><div class="watches">{watches}</div><div class="poke"><div><h2>{e(t["poke_h"])}</h2><p class="muted">{e(t["poke_p"])}</p></div><div class="reels2">{reel(t,"04-poke-garmin",t["reel_alt"]["poke_g"])}{reel(t,"08-poke-apple-watch-ultra",t["reel_alt"]["poke_a"])}</div></div><h2>{e(t["faq_h"])}</h2>{faq}</div></section>
<section id="apply" class="apply"><div class="wrap"><h2>{e(t["apply_h"])}</h2><p>{e(t["apply_p"])}</p>
<form id="beta-form" data-endpoint="{e(FORM_ENDPOINT)}">
<input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true">
<label>{e(f["name"])}<input type="text" name="name" required autocomplete="name"></label>
<label>{e(f["email"])}<input type="email" name="email" required autocomplete="email"></label>
<label>{e(f["social"])}<input type="text" name="social" required></label>
<label>{e(f["country"])}<input type="text" name="location" required></label>
<fieldset><legend>{e(f["how"])}</legend>{how}</fieldset>
<label>{e(f["clients"])}<select name="clients" required><option value="">—</option><option>1–5</option><option>6–15</option><option>16–30</option><option>30+</option></select></label>
<fieldset><legend>{e(f["watch"])}</legend>{wopts}</fieldset>
<label style="font-weight:400;display:flex;gap:8px"><input type="checkbox" name="consent" required> {e(f["consent"])}</label>
<button class="btn" type="submit" data-track="submit">{e(f["send"])}</button></form>
<div class="ok" id="thanks" role="status"><h3>{e(t["thanks_h"])}</h3><p>{e(t["thanks_p"])}</p><p>{e(t["ref"])}</p><button class="btn ghost" id="copy" data-done="{e(t["copied"])}">{e(t["copy"])}</button></div></div></section>
<section id="event"><div class="wrap"><h2>{e(t["ev_h"])}</h2><p>{e(t["ev_p"])} <strong>{e(t["ev_date"])}{EVENT_DATE}</strong></p>
<form id="event-form" style="grid-template-columns:1fr auto;max-width:560px" data-endpoint="{e(FORM_ENDPOINT)}"><input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="email" name="email" required placeholder="{e(t["ev_ph"])}" aria-label="{e(t["ev_ph"])}" autocomplete="email"><button class="btn" type="submit">{e(t["ev_btn"])}</button></form></div></section>
</main>
<footer><div class="wrap"><div><strong>Coach Link</strong><br>{e(t["rights"])}</div><div><a href="{INSTAGRAM}">Instagram</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="privacy.html">{e(t["privacy"])}</a></div></div></footer>
<dialog id="demo-dialog" aria-label="{e(t["demo"])}"><button type="button" id="demo-close" aria-label="{e(t["close"])}">×</button><video controls playsinline preload="none" poster="{t["prefix"]}assets/media/demo-poster.jpg"><source src="{t["prefix"]}assets/media/demo.mp4" type="video/mp4"></video></dialog>
<script src="{t["prefix"]}assets/app.js" data-lang="{t["lang"]}"></script></body></html>'''

def privacy(t):
    body = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h,p in t["priv"])
    return head(t, t["priv_h"]+" — Coach Link", t["desc"], "") + bar(t, False) + f'<main><section><div class="wrap legal"><h1>{e(t["priv_h"])}</h1>{body}<p><a href="index.html">← {e(t["back"])}</a></p></div></section></main></body></html>'

def write(path, s):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)

write("index.html", page(T["en"])); write("privacy.html", privacy(T["en"]))
write("uk/index.html", page(T["uk"])); write("uk/privacy.html", privacy(T["uk"]))
print("built")
