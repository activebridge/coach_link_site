#!/usr/bin/env python3
"""Builds index.html (EN), uk/index.html (UA) and privacy pages from the strings below. No dependencies."""
import os, html

# Set to a form backend URL (Formspree, Basin, own Rails endpoint). Empty = demo mode, nothing is sent.
FORM_ENDPOINT = os.environ.get("FORM_ENDPOINT", "")
EVENT_DATE = "TBA"  # launch-event date, still to be set; beta itself starts Dec 1
INSTAGRAM = "https://instagram.com/coachlink"  # TODO real handle
EMAIL = "hello@coachlink.app"  # TODO real address

T = {
"en": dict(
 lang="en", prefix="", other="uk/", other_label="UA", title="Coach Link — see how your client feels, live",
 desc="Coach Link turns your client's Garmin watch into a live coaching dashboard on your phone. Free for clients. The beta starts December 1 — apply now.",
 nav_event="Launch event", nav_cta="Apply for the beta",
 h1="See how your client feels — live, from the watch they already wear.",
 sub="Coach Link turns your client's Garmin watch into a live coaching dashboard on your phone. Apple Watch and Amazfit are next. Free for clients.",
 cta="Apply for the beta", demo="Watch the 60-sec demo", spots="Beta starts Dec 1 · 100 spots · 1 year free for beta coaches",
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
 watches_h="Works with the watch your client already wears", devices=[("Garmin",1),("Apple Watch",0),("Amazfit",0),("Wear OS",0)], live="In the beta",
 faq_h="FAQ", faq=[("Which watches are supported?","Garmin works in the beta. Apple Watch and Amazfit are next, Wear OS after that."),("Does my client need to pay?","No. The app is free for clients, always."),("Does it drain the battery?","Coach Link only sends data during a session you have started together, so a normal workout is not affected noticeably. We will publish real numbers from the beta."),("How many clients can I track at once?","Up to 5 on PRO, unlimited on PRO MAX."),("Is client data private?","Clients choose what to share and can stop anytime. See our privacy policy."),("When does the beta start?","The beta starts on December 1. We review applications and reply within 7 days, so apply now to get a founding-coach spot.")],
 apply_h="Apply for the beta", apply_p="Takes less than a minute. We review applications by hand and reply within 7 days.",
 f=dict(name="Name",email="Email",social="Instagram / TikTok",country="Country, city",how="How do you coach?",clients="Active clients",watch="Your clients' watches",consent="I agree to the processing of my data as described in the privacy policy.",send="Send application"),
 how_opts=["1:1 in gym","Group classes","Running","Online"], watch_opts=["Garmin","Apple Watch","Amazfit","Wear OS","Other","Don't know"],
 thanks_h="You're on the list.", thanks_p="We'll review applications and reply within 7 days.", cal="Add the launch event to your calendar",
 ref="Invite another coach — applications with referrals are reviewed first.", copy="Copy your invite link", copied="Copied!",
 ev_h="Join the launch event", ev_p="Not in the beta? Come to the online launch.", ev_date="Date: ", ev_btn="Join the launch event", ev_ph="Your email",
 privacy="Privacy policy", rights="© Coach Link",
 priv_h="Privacy policy", priv=[("What we collect","The details you enter in the beta application or launch-event form: name, email, social handle, location, coaching type, number of clients and watch types. We also record which channel you came from (UTM tags) and a referral code if you used one."),("Why","To review beta applications, contact you about the beta and the launch event, and decide which watches to support first."),("Who sees it","Only the Coach Link team and the services we use to store the data and send email. We do not sell your data."),("Your rights","Write to "+EMAIL+" to see, correct or delete your data, or to withdraw consent at any time."),("Health data","This site does not collect health data. The Coach Link app only shares what a client chooses to share with their coach.")],
 back="Back to the site",
 nav=[("story","How it works"),("features","Features"),("pricing","Pricing"),("faq","FAQ")],
 stats=[(100,"","founding spots"),(7," days","to get a reply"),(12," months","of PRO free in the beta"),(0,"","chest straps needed")],
 story_h="From the first rep to your phone — in real time",
 story=[("Your client trains","The watch they already wear is on their wrist. Nothing else to put on."),("Data takes off","Heart rate, zones and stats fly out in real time."),("You see it all","Everything lands on your phone. You adjust the session on the spot.")],
 steps_h="Three steps. About a minute.", bento_h="Everything you need around the session", bento_p="Before, during and after — in one calm dashboard.",
 plan_name="PRO", plan_price="$5", plan_per="/ month", plan_who="per coach account",
 plan_list=["Up to 5 clients at the same time","All features","Free for every client"], plan_more="Need unlimited clients? PRO MAX is $15 / month.",
 final_h="See how your client feels — live.", final_p="Apply for the beta. We review applications by hand and reply within 7 days.",
 demo_phone="Coach", client_zone="Zone", live_lbl="Live"),
"uk": dict(
 lang="uk", prefix="../", other="../", other_label="EN", title="Coach Link — бачте, як почувається клієнт, наживо",
 desc="Coach Link перетворює Garmin вашого клієнта на живу панель тренера на телефоні. Для клієнтів безкоштовно. Бета стартує 1 грудня — подайте заявку.",
 nav_event="Івент запуску", nav_cta="Заявка на бету",
 h1="Бачте, як почувається клієнт — наживо, з годинника, який він уже носить.",
 sub="Coach Link перетворює Garmin вашого клієнта на живу панель тренера на телефоні. Apple Watch і Amazfit — наступні. Для клієнтів безкоштовно.",
 cta="Подати заявку на бету", demo="Дивитись демо за 60 с", spots="Бета стартує 1 грудня · 100 місць · рік безкоштовно для бета-тренерів",
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
 watches_h="Працює з годинником, який клієнт уже носить", devices=[("Garmin",1),("Apple Watch",0),("Amazfit",0),("Wear OS",0)], live="У бета-версії",
 faq_h="Питання й відповіді", faq=[("Які годинники підтримуються?","У бета-версії працює Garmin. Apple Watch і Amazfit — наступні, Wear OS — після них."),("Чи має клієнт платити?","Ні. Для клієнтів застосунок безкоштовний, завжди."),("Чи розряджає батарею?","Coach Link передає дані лише під час тренування, яке ви почали разом, тож звичайне заняття помітно не страждає. Реальні цифри опублікуємо після бети."),("Скількох клієнтів можна вести одночасно?","До 5 на PRO, без обмежень на PRO MAX."),("Чи приватні дані клієнта?","Клієнт сам обирає, чим ділитись, і може зупинити будь-коли. Див. політику конфіденційності."),("Коли стартує бета?","Бета стартує 1 грудня. Ми переглядаємо заявки й відповідаємо протягом 7 днів, тож подайте заявку, щоб отримати місце тренера-засновника.")],
 apply_h="Заявка на бету", apply_p="Менше хвилини. Ми розглядаємо заявки вручну й відповідаємо протягом 7 днів.",
 f=dict(name="Ім'я",email="Email",social="Instagram / TikTok",country="Країна, місто",how="Як ви тренуєте?",clients="Активних клієнтів",watch="Годинники ваших клієнтів",consent="Погоджуюсь на обробку даних відповідно до політики конфіденційності.",send="Надіслати заявку"),
 how_opts=["Індивідуально в залі","Групові заняття","Біг","Онлайн"], watch_opts=["Garmin","Apple Watch","Amazfit","Wear OS","Інший","Не знаю"],
 thanks_h="Ви в списку.", thanks_p="Ми розглянемо заявки й відповімо протягом 7 днів.", cal="Додати івент запуску в календар",
 ref="Запросіть ще одного тренера — заявки з рекомендацією розглядаємо першими.", copy="Скопіювати посилання-запрошення", copied="Скопійовано!",
 ev_h="Приєднуйтесь до івенту запуску", ev_p="Не пройшли в бету? Приходьте на онлайн-запуск.", ev_date="Дата: ", ev_btn="Приєднатись до івенту", ev_ph="Ваш email",
 privacy="Політика конфіденційності", rights="© Coach Link",
 priv_h="Політика конфіденційності", priv=[("Що ми збираємо","Дані, які ви вводите у формі заявки на бету чи реєстрації на івент: ім'я, email, акаунт у соцмережі, місце, тип тренувань, кількість клієнтів і типи годинників. Також фіксуємо канал, з якого ви прийшли (UTM-мітки), і реферальний код, якщо він був."),("Навіщо","Щоб розглядати заявки на бету, зв'язуватись щодо бети й івенту та визначати, які годинники підтримувати першими."),("Хто бачить","Лише команда Coach Link і сервіси, які ми використовуємо для зберігання даних і розсилки. Ми не продаємо ваші дані."),("Ваші права","Напишіть на "+EMAIL+", щоб побачити, виправити чи видалити свої дані або відкликати згоду."),("Дані про здоров'я","Цей сайт не збирає даних про здоров'я. Застосунок Coach Link передає тренеру лише те, чим клієнт вирішив поділитись.")],
 back="Назад на сайт",
 nav=[("story","Як це працює"),("features","Можливості"),("pricing","Ціна"),("faq","Питання")],
 stats=[(100,"","місць для засновників"),(7," днів","до відповіді"),(12," місяців","PRO безкоштовно в бета"),(0,"","нагрудних датчиків")],
 story_h="Від першого повтору до вашого телефона — в реальному часі",
 story=[("Клієнт тренується","Годинник, який він і так носить, на зап'ясті. Більше нічого вдягати не треба."),("Дані вилітають","Пульс, зони й показники летять у реальному часі."),("Ви бачите все","Усе з'являється на вашому телефоні. Ви коригуєте тренування одразу.")],
 steps_h="Три кроки. Приблизно хвилина.", bento_h="Усе, що потрібно навколо тренування", bento_p="До, під час і після — в одній спокійній панелі.",
 plan_name="PRO", plan_price="$5", plan_per="/ міс", plan_who="за акаунт тренера",
 plan_list=["До 5 клієнтів одночасно","Усі можливості","Безкоштовно для кожного клієнта"], plan_more="Потрібно без обмежень? PRO MAX — $15 / міс.",
 final_h="Бачте, як почувається клієнт — наживо.", final_p="Подайте заявку на бету. Ми розглядаємо заявки вручну й відповідаємо протягом 7 днів.",
 demo_phone="Тренер", client_zone="Зона", live_lbl="Наживо"),
}

def e(s): return html.escape(s, quote=True)

ART = {
 "en": dict(sleep="Sleep", battery="Body Battery", stress="Stress", breath="Breath", poke="Poke", tip1="Rest day tomorrow", tip2="Load +10% this week", tip3="Recovery is on track", day=["M","T","W","T","F","S","S"], live="Live", gym="In the gym", call="Video call", set="Set 3 · 8 reps", alert="Push harder"),
 "uk": dict(sleep="Сон", battery="Body Battery", stress="Стрес", breath="Дихання", poke="Поштовх", tip1="Завтра день відпочинку", tip2="Навантаження +10% цього тижня", tip3="Відновлення йде за планом", day=["П","В","С","Ч","П","С","Н"], live="Наживо", gym="У залі", call="Відеозв'язок", set="Підхід 3 · 8 повторів", alert="Додай темпу"),
}
ECG = '<svg viewBox="0 0 200 30" preserveAspectRatio="none"><path d="M0 15H40l6 0 6-11 6 22 6-11h46l6 0 6-11 6 22 6-11h66"/></svg>'
ZONES = [(171, 5), (152, 4), (133, 3), (114, 2), (0, 1)]
def zone_of(hr): return next(z for lim, z in ZONES if hr >= lim)

def live_card(t, name, hr, phase, amp=14, cls=""):
    z = zone_of(hr)
    return (f'<div class="live-card {cls}" data-live data-base="{hr}" data-amp="{amp}" data-phase="{phase}" style="--zc:var(--z{z})">'
            f'<div class="lc-top"><span class="lc-name">{e(name)}</span><span class="lc-live"><i></i>{e(t["live_lbl"])}</span></div>'
            f'<div class="lc-mid"><b class="lc-hr">{hr}</b><span class="lc-unit">bpm<br><em class="lc-zone">{e(t["client_zone"])} {z}</em></span></div>'
            f'<div class="ecg" aria-hidden="true"><div class="ecg-track">{ECG}{ECG}</div></div></div>')

def watch(hr, extra=""):
    z = zone_of(hr)
    return (f'<div class="watch {extra}" data-live data-base="{hr}" data-amp="12" data-phase="1.7" style="--zc:var(--z{z})">'
            f'<svg class="w-ring" viewBox="0 0 120 120"><circle class="w-track" cx="60" cy="60" r="52"/><circle class="w-val" cx="60" cy="60" r="52" pathLength="100" stroke-dasharray="100" stroke-dashoffset="{round(100-hr/190*100,1)}"/></svg>'
            f'<div class="w-in"><b class="lc-hr">{hr}</b><span class="w-bpm">bpm</span><span class="w-zone lc-zone">Z{z}</span></div></div>')

def head(t, title, desc, path):
    p = t["prefix"]
    return f'''<!doctype html>
<html lang="{t["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#0e151b">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="{p}assets/logo.svg" type="image/svg+xml">
<link rel="preload" href="{p}assets/fonts/Onest-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/Unbounded-Variable.woff2" as="font" type="font/woff2" crossorigin>
<script>if(!matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("anim")</script>
<link rel="stylesheet" href="{p}assets/style.css"></head><body><div class="grain" aria-hidden="true"></div>'''

def bar(t, home):
    p, h = t["prefix"], ("" if home else "index.html")
    links = "".join(f'<a class="nl" href="{h}#{k}" data-nav="{k}">{e(v)}</a>' for k, v in t["nav"])
    return f'''<header class="bar" id="bar"><div class="wrap bar-in"><a class="brand" href="{h or "./"}"><img src="{p}assets/logo.svg" alt="" width="28" height="28"><span>Coach Link</span></a>
<nav class="nav" aria-label="Main">{links}</nav>
<div class="bar-r"><a class="lang" href="{t["other"]}" hreflang="{ "uk" if t["lang"]=="en" else "en"}">{t["other_label"]}</a><a class="btn sm" href="{h}#apply" data-magnetic>{e(t["nav_cta"])}</a></div></div></header>'''

def words(s):
    return " ".join(f'<span class="w"><span style="--i:{i}">{e(w)}</span></span>' for i, w in enumerate(s.split(" ")))

def page(t):
    f, A = t["f"], ART[t["lang"]]
    h1 = words(t["h1"])
    stats = "".join(f'<div class="stat"><b><span data-count="{n}">{n}</span>{e(u)}</b><span>{e(l)}</span></div>' for n, u, l in t["stats"])
    pains = "".join(f'<blockquote class="pain" data-reveal><span class="q">“</span>{e(x.strip("“”«»\" "))}</blockquote>' for x in t["pains"])
    caps = "".join(f'<li class="cap"><span class="cap-n">0{i}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(t["story"], 1))
    steps = "".join(f'<li class="step" data-reveal><span class="step-n">{i}</span><p>{e(x)}</p></li>' for i, x in enumerate(t["steps"], 1))

    def card(i, w, h, b, soon, art, cls):
        tag = f'<span class="tag">{e(t["soon"])}</span>' if soon else ""
        return f'<article class="bento-card {cls}" data-reveal data-spot><div class="bc-art" aria-hidden="true">{art}</div><div class="bc-txt"><span class="when">{e(w)}</span>{tag}<h3>{e(h)}</h3><p>{e(b)}</p></div></article>'
    F = t["feats"]
    arts = [
      f'<div class="art-live">{live_card(t,"Anna",162,0.3,16,"mini")}{live_card(t,"Marcus",138,1.9,14,"mini")}{live_card(t,"Dana",118,3.4,12,"mini")}</div>',
      f'<div class="art-meters"><div style="--v:86"><span>{A["sleep"]}</span><b>86</b><i></i></div><div style="--v:82"><span>{A["battery"]}</span><b>82</b><i></i></div><div style="--v:33"><span>{A["stress"]}</span><b>33</b><i></i></div></div>',
      '<svg class="art-spark" viewBox="0 0 200 70" preserveAspectRatio="none"><path class="area" d="M0 60C20 55 30 58 50 46S85 40 105 32 140 28 160 18 190 10 200 8V70H0Z"/><path class="line" pathLength="100" d="M0 60C20 55 30 58 50 46S85 40 105 32 140 28 160 18 190 10 200 8"/></svg>',
      f'<div class="art-poke"><span class="ring r1"></span><span class="ring r2"></span><button type="button" tabindex="-1">{A["poke"]}</button></div>',
      '<div class="art-chips"><span>HR <b>138</b></span><span>Stress <b>33</b></span><span>Breath <b>19</b></span><span>Battery <b>74</b></span><span>HRV <b>52</b></span><span>SpO₂ <b>97%</b></span></div>',
      f'<div class="art-call"><div class="call-frame"><span>{A["call"]}</span></div><div class="call-card"><i></i>138 bpm</div></div>',
      f'<ul class="art-tips"><li>{A["tip1"]}</li><li>{A["tip2"]}</li><li>{A["tip3"]}</li></ul>',
      '<div class="art-bars">' + "".join(f'<i style="--h:{h}%"><s>{d}</s></i>' for h, d in zip([35,50,42,64,58,80,92], A["day"])) + '</div>',
      f'<div class="art-sets"><b>{A["set"]}</b><span><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span></div>',
    ]
    cls = ["c-live","c-ready","c-report","c-poke","c-body","c-call","c-tips","c-notes","c-soon"]
    bento = "".join(card(i, *F[i][:4], arts[i], cls[i]) for i in range(len(F)))
    devices = "".join(f'<div class="dev{" on" if on else ""}" data-reveal><span class="dev-n">{e(n)}</span><span class="dev-s">{"<i></i>"+e(t["live"]) if on else e(t["soon"])}</span></div>' for n, on in t["devices"])
    trust = "".join(f'<li data-reveal><span class="ck"></span>{e(x)}</li>' for x in t["trust"])
    beta = "".join(f"<li>{e(x)}</li>" for x in t["beta"])
    plist = "".join(f"<li>{e(x)}</li>" for x in t["plan_list"])
    faq = "".join(f"<details data-reveal><summary>{e(q)}</summary><div class='ans'><p>{e(a)}</p></div></details>" for q, a in t["faq"])
    how = "".join(f'<label class="opt"><input type="checkbox" name="how" value="{e(o)}"><span>{e(o)}</span></label>' for o in t["how_opts"])
    wopts = "".join(f'<label class="opt"><input type="checkbox" name="watches" value="{e(o)}"><span>{e(o)}</span></label>' for o in t["watch_opts"])
    return head(t, t["title"], t["desc"], "") + bar(t, True) + f'''
<main id="main">
<section class="hero" id="top"><div class="hero-bg" aria-hidden="true"></div>
<div class="wrap hero-grid"><div class="hero-copy">
<span class="eyebrow h-in" style="--d:.05s"><i></i>{e(t["spots"])}</span>
<h1 class="split">{h1}</h1>
<p class="sub h-in" style="--d:.55s">{e(t["sub"])}</p>
<div class="cta h-in" style="--d:.7s"><a class="btn lg" href="#apply" data-track="cta-hero" data-magnetic>{e(t["cta"])}</a><a class="btn ghost lg" href="#story">{e(t["nav"][0][1])}</a></div>
</div>
<div class="stage h-in" style="--d:.35s" aria-hidden="true" data-parallax>
<div class="phone" data-depth="14"><div class="ph-top"><b>Coach Link</b><span class="lc-live"><i></i>{e(t["live_lbl"])}</span></div>
{live_card(t,"Anna",162,0.3,16)}{live_card(t,"Marcus",138,1.9,14)}{live_card(t,"Dana",104,3.4,12)}</div>
{watch(162,"hero-watch")}</div></div></section>

<section class="stats"><div class="wrap stats-in">{stats}</div></section>

<section class="pains"><div class="wrap"><h2 data-reveal>{e(t["pains_h"])}</h2><div class="pain-grid">{pains}</div></div></section>

<section class="story" id="story" data-story><div class="story-pin">
<div class="wrap"><h2 class="story-h">{e(t["story_h"])}</h2>
<div class="story-stage"><div class="s-watch">{watch(146)}<span class="s-tag">{e(t["story"][0][0])}</span></div>
<svg class="s-path" aria-hidden="true"><path class="sp-base"/><path class="sp-glow"/><g class="sp-dots"><circle r="5"/><circle r="5"/><circle r="5"/><circle r="5"/><circle r="5"/></g></svg>
<div class="s-phone"><div class="ph-top"><b>Coach Link</b><span class="lc-live"><i></i>{e(t["live_lbl"])}</span></div>
{live_card(t,"Anna",162,0.3,16,"s-card")}<div class="s-card-wrap">{live_card(t,"Marcus",138,1.9,14,"s-card")}<button class="s-poke" type="button" tabindex="-1">{A["poke"]}</button></div>{live_card(t,"Dana",118,3.4,12,"s-card")}</div></div>
<ol class="caps">{caps}</ol>
<div class="s-prog" aria-hidden="true"><i></i></div></div></div></section>

<section class="features" id="features"><div class="wrap"><div class="sec-head" data-reveal><h2>{e(t["bento_h"])}</h2><p>{e(t["bento_p"])}</p></div><div class="bento">{bento}</div></div></section>

<section class="how"><div class="wrap"><h2 data-reveal>{e(t["steps_h"])}</h2>
<ol class="steps"><span class="steps-line" aria-hidden="true"><i></i></span>{steps}</ol>
<p class="how-note" data-reveal>{e(t["how_note"])}</p></div></section>

<section class="devices"><div class="wrap"><h2 data-reveal>{e(t["watches_h"])}</h2><div class="dev-row">{devices}</div></div></section>

<section class="trust"><div class="wrap"><h2 data-reveal>{e(t["trust_h"])}</h2><ul>{trust}</ul></div></section>

<section class="beta"><div class="wrap"><h2 data-reveal>{e(t["beta_h"])}</h2><ul data-reveal>{beta}</ul><a class="btn" href="#apply" data-track="cta-beta" data-magnetic>{e(t["cta"])}</a></div></section>

<section class="pricing" id="pricing"><div class="wrap"><h2 data-reveal>{e(t["price_h"])}</h2>
<div class="price-card" data-reveal data-spot><span class="tag solid">{e(t["plan_who"])}</span><h3>{e(t["plan_name"])}</h3>
<div class="price"><b>{e(t["plan_price"])}</b><span>{e(t["plan_per"])}</span></div>
<ul>{plist}</ul><a class="btn lg" href="#apply" data-track="cta-price" data-magnetic>{e(t["cta"])}</a>
<p class="pc-note">{e(t["price_note"])}</p><p class="pc-more">{e(t["plan_more"])}</p></div></div></section>

<section class="faq" id="faq"><div class="wrap narrow"><h2 data-reveal>{e(t["faq_h"])}</h2>{faq}</div></section>

<section class="final" id="apply"><div class="final-glow" aria-hidden="true"></div><div class="wrap">
<div class="final-head" data-reveal><h2>{e(t["final_h"])}</h2><p>{e(t["final_p"])}</p></div>
<div class="form-card" data-reveal>
<form id="beta-form" data-endpoint="{e(FORM_ENDPOINT)}" novalidate>
<input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row2"><div class="field"><label for="f-name">{e(f["name"])}</label><input id="f-name" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label for="f-email">{e(f["email"])}</label><input id="f-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row2"><div class="field"><label for="f-social">{e(f["social"])}</label><input id="f-social" type="text" name="social" required></div>
<div class="field"><label for="f-loc">{e(f["country"])}</label><input id="f-loc" type="text" name="location" required autocomplete="address-level2"></div></div>
<fieldset class="field"><legend>{e(f["how"])}</legend><div class="opts">{how}</div></fieldset>
<div class="field"><label for="f-clients">{e(f["clients"])}</label><div class="select"><select id="f-clients" name="clients" required><option value="">—</option><option>1–5</option><option>6–15</option><option>16–30</option><option>30+</option></select></div></div>
<fieldset class="field"><legend>{e(f["watch"])}</legend><div class="opts">{wopts}</div></fieldset>
<label class="consent"><input type="checkbox" name="consent" required><span class="box"></span><span>{e(f["consent"])}</span></label>
<button class="btn lg" type="submit" data-track="submit" data-magnetic>{e(f["send"])}</button></form>
<div class="ok" id="thanks" role="status"><h3>{e(t["thanks_h"])}</h3><p>{e(t["thanks_p"])}</p><p>{e(t["ref"])}</p><button class="btn ghost" id="copy" type="button" data-done="{e(t["copied"])}">{e(t["copy"])}</button></div></div>
<div class="event" id="event" data-reveal><div><h3>{e(t["ev_h"])}</h3><p>{e(t["ev_p"])} <strong>{e(t["ev_date"])}{EVENT_DATE}</strong></p></div>
<form id="event-form" data-endpoint="{e(FORM_ENDPOINT)}"><input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="email" name="email" required placeholder="{e(t["ev_ph"])}" aria-label="{e(t["ev_ph"])}" autocomplete="email"><button class="btn" type="submit">{e(t["ev_btn"])}</button></form></div>
</div></section>
</main>
<footer><div class="wrap foot"><div><strong>Coach Link</strong><br><span>{e(t["rights"])}</span></div><div class="foot-l"><a href="{INSTAGRAM}">Instagram</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="privacy.html">{e(t["privacy"])}</a></div></div></footer>
<script src="{t["prefix"]}assets/vendor/gsap.min.js" defer></script><script src="{t["prefix"]}assets/vendor/ScrollTrigger.min.js" defer></script><script src="{t["prefix"]}assets/vendor/lenis.min.js" defer></script>
<script src="{t["prefix"]}assets/app.js" data-lang="{t["lang"]}" defer></script></body></html>'''

def privacy(t):
    body = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h,p in t["priv"])
    return head(t, t["priv_h"]+" — Coach Link", t["desc"], "") + bar(t, False) + f'<main><section class="legal-s"><div class="wrap legal"><h1>{e(t["priv_h"])}</h1>{body}<p><a href="index.html">← {e(t["back"])}</a></p></div></section></main></body></html>'

def write(path, s):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)

write("index.html", page(T["en"])); write("privacy.html", privacy(T["en"]))
write("uk/index.html", page(T["uk"])); write("uk/privacy.html", privacy(T["uk"]))
print("built")
