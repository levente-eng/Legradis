from pathlib import Path
from html import escape
from datetime import date

ROOT = Path('/mnt/data/legradi_website')
ASSET = 'assets/images/'

SITE_NAME = 'LEGRADI'
SITE_URL = 'https://legradis.com'
EMAIL = 'office@legradis.com'
LOCATION = 'Győr, Magyarország'

nav_items = [
    ('index.html','Főoldal','home'),
    ('referenciak.html','Referenciák','references'),
    ('blog.html','Blog','blog'),
    ('rolunk.html','Rólunk','about'),
    ('kapcsolat.html','Kapcsolat','contact'),
]
service_items = [
    ('uzletberendezesek.html','Üzletberendezések','retail'),
    ('egyedi-butorok.html','Egyedi bútorok','furniture'),
    ('design-lepcsok.html','Design lépcsők','stairs'),
    ('tervezes.html','Tervezés','planning'),
    ('technologia.html','Technológia','technology'),
    ('keszletrol.html','Bútorok készletről','stock'),
]

icons = {
'arrow': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg>',
'plan': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h12v12H4zM8 4v5h8M4 12h6v4M17 3l4 4-10 10-5 1 1-5z"/></svg>',
'factory': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21V9l6 3V8l6 4V5h4v16zM7 21v-4h3v4M14 17h3"/></svg>',
'stairs': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 19h5v-4h5v-4h5V7h3M4 6l5-3 5 3"/></svg>',
'store': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9h18l-2-5H5zM5 9v11h14V9M8 20v-6h5v6M3 9c0 2 3 2 3 0 0 2 3 2 3 0 0 2 3 2 3 0 0 2 3 2 3 0 0 2 3 2 3 0"/></svg>',
'cube': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l9 5-9 5-9-5zM3 7v10l9 5 9-5V7M12 12v10"/></svg>',
'check': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 13l4 4L19 7"/></svg>',
'pin': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6 7-13a7 7 0 10-14 0c0 7 7 13 7 13zM12 11a2 2 0 110-4 2 2 0 010 4z"/></svg>',
'mail': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3zM3 6l9 7 9-7"/></svg>',
'light': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 22h4M8 14a7 7 0 118 0c-1 1-2 2-2 4h-4c0-2-1-3-2-4z"/></svg>',
'cnc': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h16v4H4zM7 8v12M17 8v12M9 12h6M12 8v8M10 16h4v4h-4z"/></svg>',
'printer': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h12v5H6zM4 9h16v9H4zM7 18h10v3H7zM9 12h6v4H9z"/></svg>',
'finish': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 17l8-13 8 13zM7 17h10v4H7zM8 13h8"/></svg>',
'blog': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h14v18H5zM8 7h8M8 11h8M8 15h5"/></svg>',
}

def icon(name):
    return f'<span class="icon">{icons[name]}</span>'

def page_header(active):
    main_nav = ''.join(
        f'<a href="{href}" class="nav-link {"is-active" if key==active else ""}">{label}</a>'
        for href,label,key in nav_items
    )
    services = ''.join(
        f'<a href="{href}" class="dropdown-link {"is-active" if key==active else ""}">{label}</a>'
        for href,label,key in service_items
    )
    return f'''<header class="site-header" data-header>
  <div class="header-inner container-wide">
    <a class="brand" href="index.html" aria-label="LEGRADI főoldal">
      <img src="{ASSET}logo-light.png" alt="LEGRADI" width="164" height="98">
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-menu-toggle>
      <span></span><span></span><span></span><span class="sr-only">Menü megnyitása</span>
    </button>
    <nav id="site-nav" class="site-nav" aria-label="Fő navigáció" data-menu>
      <a href="index.html" class="nav-link {'is-active' if active=='home' else ''}">Főoldal</a>
      <details class="nav-dropdown">
        <summary class="nav-link {'is-active' if active in [x[2] for x in service_items] else ''}">Szolgáltatások</summary>
        <div class="dropdown-panel">{services}</div>
      </details>
      {''.join(f'<a href="{href}" class="nav-link {"is-active" if key==active else ""}">{label}</a>' for href,label,key in nav_items[1:])}
      <a class="button button-small button-red nav-cta" href="kapcsolat.html">Ajánlatkérés</a>
    </nav>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="{ASSET}logo-light.png" alt="LEGRADI" width="180" height="108">
      <p>Üzletberendezések, egyedi bútorok és komplex belsőépítészeti kivitelezés Győrből, Magyarországra és Ausztriába.</p>
    </div>
    <div><h3>Szolgáltatások</h3><ul>
      <li><a href="uzletberendezesek.html">Üzletberendezések</a></li>
      <li><a href="egyedi-butorok.html">Egyedi bútorok</a></li>
      <li><a href="design-lepcsok.html">Design lépcsők</a></li>
      <li><a href="tervezes.html">Tervezés</a></li>
      <li><a href="technologia.html">Technológia</a></li>
    </ul></div>
    <div><h3>Információ</h3><ul>
      <li><a href="referenciak.html">Referenciák</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="rolunk.html">Rólunk</a></li>
      <li><a href="keszletrol.html">Bútorok készletről</a></li>
      <li><a href="kapcsolat.html">Kapcsolat</a></li>
    </ul></div>
    <div><h3>Kapcsolat</h3><ul class="contact-list">
      <li>{icon('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{icon('pin')}<span>{LOCATION}</span></li>
      <li><span class="coverage">Magyarország • Ausztria</span></li>
    </ul></div>
  </div>
  <div class="footer-bottom container">
    <span>© {date.today().year} LEGRADI. Minden jog fenntartva.</span>
    <span><a href="adatkezeles.html">Adatkezelés</a> · <a href="impresszum.html">Impresszum</a></span>
  </div>
</footer>'''

def shell(title, description, active, body, image='hero-home.webp', canonical='index.html', extra_head=''):
    page_title = f'{title} | {SITE_NAME}' if title != SITE_NAME else f'{SITE_NAME} | Üzletberendezés és egyedi bútor'
    return f'''<!doctype html>
<html lang="hu">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page_title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#080808">
  <link rel="canonical" href="{SITE_URL}/{canonical}">
  <link rel="icon" href="{ASSET}favicon.png" type="image/png">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(page_title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="{SITE_URL}/{ASSET}{image}">
  <meta property="og:url" content="{SITE_URL}/{canonical}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
  {extra_head}
</head>
<body data-page="{active}">
<a class="skip-link" href="#main">Ugrás a tartalomra</a>
{page_header(active)}
<main id="main">{body}</main>
{footer()}
<button class="back-to-top" type="button" aria-label="Vissza az oldal tetejére" data-back-to-top>↑</button>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Kép nagyítása" hidden data-lightbox>
  <button type="button" class="lightbox-close" aria-label="Bezárás">×</button>
  <img src="" alt="">
  <p></p>
</div>
<div class="cookie-banner" data-cookie-banner hidden>
  <p>Az oldal a működéshez szükséges helyi tárolást használ. További részletek az <a href="adatkezeles.html">adatkezelési tájékoztatóban</a>.</p>
  <button class="button button-small button-red" type="button" data-cookie-accept>Rendben</button>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>'''

def hero(image, eyebrow, title, lead, primary=('Referenciák','referenciak.html'), secondary=('Kapcsolat','kapcsolat.html'), cls=''):
    return f'''<section class="hero {cls}" style="--hero-image:url('{ASSET}{image}')">
  <div class="hero-content container" data-reveal>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="hero-lead">{lead}</p>
    <div class="button-row">
      <a class="button button-red" href="{primary[1]}">{primary[0]} {icons['arrow']}</a>
      <a class="button button-ghost" href="{secondary[1]}">{secondary[0]}</a>
    </div>
  </div>
  <a class="scroll-cue" href="#content" aria-label="Tovább a tartalomhoz"><span></span></a>
</section>'''

def section_title(eyebrow, title, lead=''):
    return f'''<div class="section-heading" data-reveal>
      <p class="eyebrow">{eyebrow}</p><h2>{title}</h2>{f'<p>{lead}</p>' if lead else ''}
    </div>'''

def service_card(href, image, icon_name, title, text, tag=''):
    return f'''<a class="service-card" href="{href}" data-reveal>
  <div class="card-image"><img src="{ASSET}{image}" alt="{escape(title)}" loading="lazy"></div>
  <div class="card-body">{icon(icon_name)}<div>{f'<span class="micro-tag">{tag}</span>' if tag else ''}<h3>{title}</h3><p>{text}</p></div><span class="card-arrow">{icons['arrow']}</span></div>
</a>'''

def gallery_item(image, category, title, text):
    return f'''<figure class="gallery-item" data-category="{category}" data-reveal>
  <button class="gallery-button" type="button" data-lightbox-src="{ASSET}{image}" data-lightbox-caption="{escape(title)} — {escape(text)}">
    <img src="{ASSET}{image}" alt="{escape(title)}" loading="lazy">
    <span class="gallery-overlay"><span class="micro-tag">{category}</span><strong>{title}</strong><small>{text}</small></span>
  </button>
</figure>'''

# HOME
home_body = hero('hero-home.webp','Győr • Magyarország • Ausztria','Tervezéstől a kivitelezésig.','Üzletberendezések, egyedi bútorok és belsőépítészeti megoldások több generációs szakmai tapasztalattal, modern CNC- és 3D-technológiával.','Referenciák','referenciak.html') if False else ''
# correct helper call
home_body = hero('hero-home.webp','Győr • Magyarország • Ausztria','Tervezéstől a kivitelezésig.','Üzletberendezések, egyedi bútorok és belsőépítészeti megoldások több generációs szakmai tapasztalattal, modern CNC- és 3D-technológiával.',('Referenciák','referenciak.html'),('Projekt egyeztetés','kapcsolat.html'),'hero-home')
home_body += f'''
<section id="content" class="trust-strip"><div class="container trust-grid">
  <div>{icon('store')}<strong>Fő profil: üzletberendezés</strong><span>B2B projektek teljes körű megvalósítása</span></div>
  <div>{icon('check')}<strong>Egy kézben</strong><span>Tervezés, gyártás, szállítás, szerelés</span></div>
  <div>{icon('cnc')}<strong>Modern gyártás</strong><span>CNC, felületkezelés és 3D nyomtatás</span></div>
  <div>{icon('pin')}<strong>Határokon át</strong><span>Magyarországi és ausztriai kivitelezések</span></div>
</div></section>
<section class="section section-dark"><div class="container split-grid profile-feature">
  <div class="media-frame" data-reveal><img src="{ASSET}ref-retail-denim.webp" alt="Egyedi üzletberendezés világított polcrendszerrel" loading="lazy"></div>
  <div class="split-copy" data-reveal>
    <p class="eyebrow">Meghatározó szakterületünk</p><h2>Üzletberendezések, amelyek a márkát képviselik.</h2>
    <p>Az üzletberendezések tervezése, gyártása és helyszíni kivitelezése vállalkozásunk fő profilja. Komplett berendezéseket, pultokat, display rendszereket, kirakati elemeket és egyedi fényinstallációkat készítünk.</p>
    <ul class="check-list"><li>gyártható műszaki megoldások</li><li>határidőre szervezett projektfolyamat</li><li>saját csapattal végzett telepítés</li></ul>
    <a class="text-link" href="uzletberendezesek.html">Üzletberendezések részletesen {icons['arrow']}</a>
  </div>
</div></section>
<section class="section section-light"><div class="container">
  {section_title('Szolgáltatások','Komplex megoldások egyetlen partnerrel','A lakossági egyedi bútoroktól a komplett üzlettéri kivitelezésig minden projektet a funkció, a tartósság és a részletek minősége mentén építünk fel.')}
  <div class="service-grid">
    {service_card('uzletberendezesek.html','hero-retail.webp','store','Üzletberendezések','Tervezés, gyártás és telepítés üzletek, butikok és kereskedelmi terek számára.','Fő profil')}
    {service_card('egyedi-butorok.html','hero-furniture.webp','factory','Egyedi bútorok','Konyhák, gardróbok, vitrinek és teljesen egyedi belsőépítészeti elemek.')}
    {service_card('design-lepcsok.html','hero-stairs.webp','stairs','Design lépcsők','Fa, acél és üveg összehangolásával készülő egyedi lépcsőrendszerek.')}
    {service_card('tervezes.html','hero-planning.webp','plan','Tervezés','3D látványtervek, műszaki dokumentáció és gyártási előkészítés.')}
  </div>
</div></section>
<section class="section section-black process-home"><div class="container">
  {section_title('Munkafolyamat','Az első vonaltól a helyszíni átadásig','Átlátható projektmenedzsment, pontos gyártás és saját kivitelező csapat.')}
  <div class="process-layout"><div class="process-steps" data-reveal>
    <article><span>01</span><h3>Konzultáció</h3><p>Igények, tér, funkció és ütemezés pontosítása.</p></article>
    <article><span>02</span><h3>Tervezés</h3><p>Látványtervek, csomópontok és gyártható dokumentáció.</p></article>
    <article><span>03</span><h3>Gyártás</h3><p>CNC megmunkálás, asztalosmunka és felületkezelés.</p></article>
    <article><span>04</span><h3>Kivitelezés</h3><p>Szállítás, helyszíni szerelés és minőségellenőrzés.</p></article>
  </div><div class="media-frame media-wide" data-reveal><img src="{ASSET}process-montage.webp" alt="Üzletberendezés gyártási és szerelési folyamata" loading="lazy"></div></div>
</div></section>
<section class="section section-dark"><div class="container technology-feature">
  <div class="split-copy" data-reveal><p class="eyebrow">Technológia</p><h2>Hagyományos szakértelem, korszerű gyártási háttér.</h2><p>A precíz kivitelezés mögött átgondolt tervezés, CNC megmunkálás, saját felületkezelés és többféle 3D nyomtatási technológia dolgozik.</p><div class="mini-features"><span>{icon('cnc')}CNC megmunkálás</span><span>{icon('printer')}3D nyomtatás</span><span>{icon('finish')}Felületkezelés</span></div><a class="button button-outline" href="technologia.html">Technológiai háttér</a></div>
  <div class="technology-collage" data-reveal><img src="{ASSET}technology-cnc.webp" alt="CNC marófej MDF megmunkálás közben" loading="lazy"><img src="{ASSET}technology-printer.webp" alt="Bambu Lab P1S 3D nyomtató AMS rendszerrel" loading="lazy"></div>
</div></section>
<section class="section section-light"><div class="container">
  {section_title('Kiemelt munkák','Referenciák, amelyek mögött teljes folyamat áll','Valódi projektek üzletberendezés, lépcső és egyedi bútor kategóriákból.')}
  <div class="gallery-grid gallery-featured">
    {gallery_item('ref-retail-window.webp','Üzletberendezés','Egyedi kirakati installáció','Kleider Bauer projekt')}
    {gallery_item('ref-stair-glass.webp','Design lépcső','Tölgy lépcső üvegkorláttal','Egyedi tervezés és kivitelezés')}
    {gallery_item('ref-counter.webp','Üzletberendezés','Egyedi értékesítési pult','Komplett gyártás és telepítés')}
    {gallery_item('ref-table.webp','Egyedi bútor','Tömörfa étkezőasztal','Karakteres, egyedi felület')}
    {gallery_item('ref-wardrobe.webp','Egyedi bútor','Beépített gardrób','Teljes belmagasságú megoldás')}
    {gallery_item('ref-retail-orange.webp','Üzletberendezés','Moduláris üzlettéri elem','Egyedi szín és geometria')}
  </div><div class="center"><a class="button button-dark" href="referenciak.html">Összes referencia</a></div>
</div></section>
<section class="section section-black"><div class="container split-grid about-preview">
  <div class="media-frame" data-reveal><img src="{ASSET}team-shirt.webp" alt="LEGRADI munkaruha és arculat" loading="lazy"></div>
  <div class="split-copy" data-reveal><p class="eyebrow">Rólunk</p><h2>Családi vállalkozás, értékteremtő szemlélettel.</h2><p>Győri műhelyünkben a több évtizedes asztalos tapasztalatot modern tervezési és gyártási technológiákkal ötvözzük. A helyszíni telepítést minden projektben saját csapatunk végzi.</p><a class="text-link" href="rolunk.html">Ismerjen meg bennünket {icons['arrow']}</a></div>
</div></section>
<section class="section section-light"><div class="container">
  {section_title('Blog','Műhelynapló és szakmai háttér','Tervezés, anyaghasználat, gyártástechnológia és betekintés aktuális projektjeinkbe.')}
  <div class="blog-grid">
    <article class="blog-card" data-reveal><a href="blog-uzletberendezes-folyamat.html"><img src="{ASSET}blog-retail.webp" alt="Üzletberendezés gyártási folyamata" loading="lazy"><div><span>Projektfolyamat</span><h3>Egy üzletberendezés útja a tervtől az átadásig</h3><p>Mi történik a felméréstől a helyszíni szerelésig?</p></div></a></article>
    <article class="blog-card" data-reveal><a href="blog-design-lepcso.html"><img src="{ASSET}blog-stair.webp" alt="Modern fa és üveg lépcső" loading="lazy"><div><span>Design lépcsők</span><h3>Fa, üveg és acél: hogyan lesz egységes a végeredmény?</h3><p>Anyagválasztás és csomópontok egyedi lépcsőknél.</p></div></a></article>
    <article class="blog-card" data-reveal><a href="blog-3d-nyomtatas.html"><img src="{ASSET}technology-printer.webp" alt="3D nyomtató műhelyben" loading="lazy"><div><span>Technológia</span><h3>3D nyomtatás a modern bútorgyártásban</h3><p>Prototípusok, sablonok és egyedi alkatrészek.</p></div></a></article>
  </div><div class="center"><a class="button button-dark" href="blog.html">Tovább a blogra</a></div>
</div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Új projekt</p><h2>Van egy elképzelése?</h2><p>Egyeztessük a funkciót, az ütemezést és a megvalósítás következő lépését.</p></div><a class="button button-light" href="kapcsolat.html">Projekt indítása {icons['arrow']}</a></div></section>
'''

# Retail page
retail_body = hero('hero-retail.webp','Fő szakterületünk','Üzletberendezések, amelyek erősítik a márkát.','Komplett üzlettéri bútorok, pultok, display rendszerek, kirakati elemek és helyszíni telepítés Magyarországon és Ausztriában.',('Projekt egyeztetés','kapcsolat.html'),('Referenciák','referenciak.html'))
retail_body += f'''
<section id="content" class="section section-light"><div class="container split-grid"><div class="split-copy" data-reveal><p class="eyebrow">Teljes körű B2B kivitelezés</p><h2>Az üzlettér a márka fizikai megjelenése.</h2><p>A jó üzletberendezés egyszerre támogatja a termékbemutatást, a vásárlói útvonalat és az üzemeltetést. A tervezéstől a gyártáson át a helyszíni beépítésig egy kézben tartjuk a folyamatot.</p><ul class="check-list"><li>üzletláncok és egyedi butikok</li><li>pultok, polcrendszerek és display elemek</li><li>kirakati és világító installációk</li><li>határidőre szervezett helyszíni telepítés</li></ul></div><div class="media-frame" data-reveal><img src="{ASSET}ref-retail-window.webp" alt="Egyedi kirakati fényinstalláció" loading="lazy"></div></div></section>
<section class="section section-black"><div class="container">{section_title('Kompetenciák','A koncepciótól a nyitásig','A projektet gyártható, szerelhető és fenntartható rendszerként kezeljük.')}
<div class="feature-grid four"><article>{icon('plan')}<h3>Tervezés és előkészítés</h3><p>Felmérés, részletezés, látványterv és gyártási dokumentáció.</p></article><article>{icon('factory')}<h3>Saját gyártás</h3><p>CNC, asztalosüzemi megmunkálás és prémium felületkezelés.</p></article><article>{icon('light')}<h3>Fényinstallációk</h3><p>Világító kirakati elemek és bútorba integrált LED-megoldások.</p></article><article>{icon('store')}<h3>Telepítés</h3><p>Szállítás és professzionális helyszíni szerelés saját csapattal.</p></article></div></div></section>
<section class="section section-light"><div class="container">{section_title('Referenciák','Üzlettéri megoldások különböző léptékben')}
<div class="gallery-grid">{gallery_item('ref-retail-denim.webp','Üzletberendezés','Világított farmerfal','Egyedi hajlított polcrendszer')}{gallery_item('ref-retail-window.webp','Kirakat','Fénykeretes kirakati installáció','Szezonális megjelenés')}{gallery_item('ref-retail-orange.webp','Üzlettéri elem','Moduláris sziget','Gyerekruházati display')}{gallery_item('ref-counter.webp','Pult','Értékesítési pult','Tartós, nagy igénybevételre')}{gallery_item('ref-process-install.webp','Kivitelezés','Helyszíni szerelés','Szerkezet és integrált tartók')}{gallery_item('process-montage.webp','Folyamat','Tervtől a kész üzlettérig','Gyártási folyamat montázs')}</div></div></section>
<section class="section section-dark"><div class="container split-grid"><div class="media-frame" data-reveal><img src="{ASSET}ref-retail-window.webp" alt="Világító kirakati keret" loading="lazy"></div><div class="split-copy" data-reveal><p class="eyebrow">Kirakat- és üzletvilágítás</p><h2>Egyedi fényinstallációk az üzletberendezés részeként.</h2><p>A világítást a tér, a bútor és a márkaarculat szerves részeként kezeljük. Egyedi fénykereteket, integrált LED-elemeket és különleges kirakati installációkat készítünk.</p><p class="note">A szolgáltatás nem általános villanyszerelés: a saját gyártású üzlettéri elemek világítási integrációjára fókuszál.</p></div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">B2B projekt</p><h2>Üzletnyitás, átalakítás vagy sorozatgyártás?</h2><p>Küldje el a terveket, méreteket és céldátumot; összeállítjuk a megvalósítási keretet.</p></div><a class="button button-light" href="kapcsolat.html">Egyeztetés indítása {icons['arrow']}</a></div></section>'''

# Furniture page
furniture_body = hero('hero-furniture.webp','Egyedi bútorok','Minden tér más. A bútoraink is azok.','Konyhák, gardróbok, vitrinek, fürdőszobabútorok és egyedi belsőépítészeti elemek pontosan az adott térhez tervezve.',('Ajánlatkérés','kapcsolat.html'),('Referenciák','referenciak.html'))
furniture_body += f'''
<section id="content" class="section section-light"><div class="container">{section_title('Egyedi gyártás','Funkció, arány és részletminőség','Nem katalógusból választunk kész megoldást: minden projektet az adott helyiséghez, használathoz és anyagvilághoz igazítunk.')}
<div class="feature-grid four"><article>{icon('factory')}<h3>Konyhák</h3><p>Ergonomikus elrendezés, tartós szerkezetek és részletes vasalatválasztás.</p></article><article>{icon('cube')}<h3>Gardróbok</h3><p>Beépített tárolás, teljes belmagasság és személyre szabott belső kiosztás.</p></article><article>{icon('store')}<h3>Vitrinek és szekrények</h3><p>Üveg, világítás és finom asztalos részletek egységes rendszerben.</p></article><article>{icon('plan')}<h3>Egyedi darabok</h3><p>Asztalok, pultok és különleges belsőépítészeti tárgyak.</p></article></div></div></section>
<section class="section section-black"><div class="container split-grid"><div class="media-frame" data-reveal><img src="{ASSET}ref-table.webp" alt="Tömörfa étkezőasztal" loading="lazy"></div><div class="split-copy" data-reveal><p class="eyebrow">Anyag és karakter</p><h2>Időtálló bútorok, nem rövid távú kompromisszumok.</h2><p>A szerkezetet, anyagot, felületet és vasalatot a használati terheléshez választjuk. A cél nem csak a látvány: a bútor hosszú távon is jól működjön, javítható és értékálló maradjon.</p><ul class="check-list"><li>prémium lapanyagok és tömörfa</li><li>megbízható vasalatok</li><li>egyedi felületkezelés</li><li>helyszíni beépítés</li></ul></div></div></section>
<section class="section section-light"><div class="container">{section_title('Munkáink','Egyedi bútor referenciák')}
<div class="gallery-grid">{gallery_item('ref-wardrobe.webp','Gardrób','Fekete beépített szekrény','Teljes belmagasságú kialakítás')}{gallery_item('ref-cabinet.webp','Vitrin','Klasszikus üveges vitrin','Egyedi festett kivitel')}{gallery_item('ref-table.webp','Asztal','Tömörfa étkezőasztal','Karakteres, rusztikus felület')}{gallery_item('ref-cabinet-alt.webp','Vitrin','Kétoldalas üvegezett szekrény','Finom részletképzés')}{gallery_item('render-loft.webp','Látványterv','Komplex lakótér','Bútor és tér egységes tervezése')}{gallery_item('detail-lamella.webp','Belsőépítészeti elem','Lamellás térelválasztó','Egyedi ritmus és csomópont')}</div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Egyedi igény</p><h2>Van egy nehezen berendezhető tér?</h2><p>Felmérjük a lehetőségeket, megtervezzük a funkciót, majd legyártjuk és beépítjük a megoldást.</p></div><a class="button button-light" href="kapcsolat.html">Konzultáció kérése {icons['arrow']}</a></div></section>'''

# Stairs page
stairs_body = hero('hero-stairs.webp','Design lépcsők','Több mint közlekedőelem. Az enteriőr fókuszpontja.','Egyedi fa-, acél- és üvegkombinációk a tervezéstől a helyszíni beépítésig.',('Projekt egyeztetés','kapcsolat.html'),('Lépcső referenciák','referenciak.html'))
stairs_body += f'''
<section id="content" class="section section-light"><div class="container split-grid"><div class="split-copy" data-reveal><p class="eyebrow">Egyedi szerkezet</p><h2>A lépcső az épület egyik legösszetettebb bútora.</h2><p>A geometria, a statikai rendszer, a járáskomfort, a korlát és az anyagkapcsolatok egyszerre határozzák meg a végeredményt. Minden lépcsőt az adott térhez és építészeti karakterhez igazítunk.</p><ul class="check-list"><li>lebegő és konzolos kialakítások</li><li>üvegkorlátok és fa kapaszkodók</li><li>acél–fa kombinációk</li><li>pontos helyszíni felmérés és szerelés</li></ul></div><div class="media-frame" data-reveal><img src="{ASSET}ref-stair-detail.webp" alt="Tölgy lépcső és üvegkorlát részlete" loading="lazy"></div></div></section>
<section class="section section-black"><div class="container">{section_title('Tervezési szempontok','Biztonság, arány és részletképzés')}
<div class="feature-grid four"><article>{icon('plan')}<h3>Térhez igazított geometria</h3><p>Kényelmes járásvonal és pontos csatlakozások.</p></article><article>{icon('stairs')}<h3>Karakteres szerkezet</h3><p>Lebegő, gerinces vagy falhoz rögzített megoldások.</p></article><article>{icon('cube')}<h3>Anyagkapcsolatok</h3><p>Fa, üveg és fém összehangolt részletekkel.</p></article><article>{icon('check')}<h3>Helyszíni kivitelezés</h3><p>Pontos szerelés, illesztés és átadás saját csapattal.</p></article></div></div></section>
<section class="section section-light"><div class="container">{section_title('Referenciák','Különböző szerkezeti és korlátmegoldások')}
<div class="gallery-grid">{gallery_item('ref-stair-floating.webp','Lépcső','Lebegő tölgy lépcső','Üvegkorláttal')}{gallery_item('ref-stair-glass.webp','Lépcső','Fordulós lépcső','Oldalsó üvegtartóval')}{gallery_item('ref-stair-detail.webp','Részlet','Tölgy fok és üveg','Közeli csomópont')}{gallery_item('22397.webp' if False else 'ref-stair-glass.webp','Lépcső','Fa–üveg kompozíció','Letisztult nappali tér')}{gallery_item('detail-hex.webp','Részletmegoldás','Burkolat és parketta átmenete','Egyedi csomópont')}{gallery_item('detail-lamella.webp','Belsőépítészet','Lamellás térelválasztó','Lépcsőtérhez kapcsolódó elem')}</div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Új lépcső</p><h2>A jó eredmény pontos felméréssel kezdődik.</h2><p>Küldje el az alaprajzot, metszetet vagy helyszíni fotókat; egyeztetjük a megvalósítható irányokat.</p></div><a class="button button-light" href="kapcsolat.html">Felmérés egyeztetése {icons['arrow']}</a></div></section>'''

# Planning page
planning_body = hero('hero-planning.webp','Tervezés','Minden jó projekt egy gyártható tervvel kezdődik.','3D látványtervek, műszaki részletezés és gyártási előkészítés a pontos döntésekhez és kiszámítható kivitelezéshez.',('Konzultáció kérése','kapcsolat.html'),('Munkafolyamat','index.html#content'))
planning_body += f'''
<section id="content" class="section section-light"><div class="container">{section_title('Tervezési folyamat','Az ötlettől a jóváhagyott gyártási dokumentációig','A vizuális koncepciót műszakilag megvalósítható, költség- és szerelés szempontjából is átgondolt rendszerré alakítjuk.')}
<div class="timeline"><article><span>01</span><h3>Konzultáció</h3><p>Igények, funkciók, stílus és ütemezés.</p></article><article><span>02</span><h3>Felmérés</h3><p>Méretek, csatlakozások és helyszíni adottságok.</p></article><article><span>03</span><h3>Koncepció</h3><p>Térszervezés, anyagok és formai irány.</p></article><article><span>04</span><h3>3D látványterv</h3><p>Élethű megjelenítés a döntések támogatásához.</p></article><article><span>05</span><h3>Műszaki terv</h3><p>Gyártható részletek, vasalatok és csomópontok.</p></article><article><span>06</span><h3>Gyártás</h3><p>A jóváhagyott dokumentáció alapján.</p></article></div></div></section>
<section class="section section-black"><div class="container split-grid"><div class="media-stack" data-reveal><img src="{ASSET}design-moodboard.webp" alt="Tervezési moodboard és gyártási folyamat" loading="lazy"><img src="{ASSET}design-render.webp" alt="Fotórealisztikus belsőépítészeti látványterv" loading="lazy"></div><div class="split-copy" data-reveal><p class="eyebrow">Látvány és realitás</p><h2>A látványterv akkor értékes, ha meg is valósítható.</h2><p>A design mellett már a tervezési fázisban kezeljük a gyártástechnológiát, szerelhetőséget, anyagvastagságokat, vasalatokat és karbantarthatóságot.</p><ul class="check-list"><li>fotórealisztikus 3D látvány</li><li>anyag- és színkoncepció</li><li>gyártási dokumentáció</li><li>költség- és ütemezési döntéstámogatás</li></ul></div></div></section>
<section class="section section-light"><div class="container">{section_title('Mit tervezünk?','Lakossági és üzleti terek egyedi megoldásai')}
<div class="feature-grid four"><article>{icon('factory')}<h3>Egyedi bútorok</h3><p>Konyha, gardrób, nappali, fürdő és különleges darabok.</p></article><article>{icon('store')}<h3>Üzletberendezések</h3><p>Pultok, polcrendszerek, kirakatok és display elemek.</p></article><article>{icon('stairs')}<h3>Design lépcsők</h3><p>Fa-, üveg- és acélmegoldások részletes csomópontokkal.</p></article><article>{icon('cube')}<h3>Egyedi szerkezetek</h3><p>Speciális panelek, burkolatok és 3D nyomtatott alkatrészek.</p></article></div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Tervezési megbízás</p><h2>Lássa a végeredményt még a gyártás előtt.</h2><p>Küldje el az alaprajzot, méreteket és inspirációkat; felépítjük a projekt tervezési menetét.</p></div><a class="button button-light" href="kapcsolat.html">Tervezési egyeztetés {icons['arrow']}</a></div></section>'''

# Technology page
technology_body = hero('hero-technology.webp','Technológia','Modern eszközök az egyedi megoldások mögött.','CNC megmunkálás, felületkezelés, 3D nyomtatás és gyártást támogató digitális folyamatok egy műhelyben.',('Technológiai egyeztetés','kapcsolat.html'),('Munkáink','referenciak.html'))
technology_body += f'''
<section id="content" class="section section-light"><div class="container">{section_title('Gyártási háttér','Pontosság, rugalmasság és reprodukálhatóság','A gépparkot nem önmagáért használjuk: minden technológia a minőséget, a gyorsabb iterációt és az egyedi részletek megvalósítását szolgálja.')}
<div class="technology-sections"><article class="tech-row"><div class="media-frame"><img src="{ASSET}technology-cnc.webp" alt="CNC marófej MDF megmunkálás közben" loading="lazy"></div><div><p class="eyebrow">CNC megmunkálás</p><h2>Milliméterpontos gyártás.</h2><p>Marás, furatképek, sablonok, egyedi kontúrok és ismételhető alkatrészgyártás a CAD/CAM adatok alapján.</p></div></article><article class="tech-row reverse"><div class="media-frame"><img src="{ASSET}technology-printer.webp" alt="Bambu Lab 3D nyomtató" loading="lazy"></div><div><p class="eyebrow">3D nyomtatás</p><h2>Gyors prototípus és speciális alkatrész.</h2><p>3D nyomtatóinkat főként saját munkáinkhoz használjuk sablonok, szerelési segédeszközök, prototípusok és egyedi alkatrészek készítésére. Saját ötlettel érkező külső megkereséseket is fogadunk.</p></div></article><article class="tech-row"><div class="media-frame"><img src="{ASSET}ref-process-paint.webp" alt="Festett alkatrészek szárítórácson" loading="lazy"></div><div><p class="eyebrow">Felületkezelés</p><h2>Egységes, tartós felületek.</h2><p>Festékszórással és kontrollált rétegrenddel biztosítjuk a bútorok és üzlettéri elemek prémium megjelenését.</p></div></article></div></div></section>
<section class="section section-black"><div class="container">{section_title('Egyedi megoldások','Amikor a standard alkatrész nem elég')}
<div class="feature-grid four"><article>{icon('cube')}<h3>Súlyoptimalizált panelek</h3><p>Méhsejt jellegű, egyedi szerkezeti megoldások.</p></article><article>{icon('printer')}<h3>Prototípusok</h3><p>Gyors formai és funkcionális ellenőrzés.</p></article><article>{icon('cnc')}<h3>Sablonok és segédeszközök</h3><p>Pontosabb és gyorsabb műhelyfolyamatok.</p></article><article>{icon('finish')}<h3>Különleges felületek</h3><p>Egyedi színek, rétegrendek és részletképzés.</p></article></div></div></section>
<section class="section section-light"><div class="container">{section_title('Műhelyrészletek','A végeredmény mögötti munka')}
<div class="gallery-grid">{gallery_item('ref-process-mdf.webp','Gyártás','Előkészített MDF panelek','Rajzokkal és mérőeszközökkel')}{gallery_item('ref-process-hollow.webp','Szerkezet','Könnyített panel','Egyedi belső felépítés')}{gallery_item('ref-process-paint.webp','Felületkezelés','Festett alkatrészek','Szárítás és minőségellenőrzés')}{gallery_item('technology-cnc-wide.webp','CNC','Megmunkáló központ','Digitális gyártási háttér')}{gallery_item('technology-printer.webp','3D nyomtatás','P1S AMS rendszerrel','Többanyagú gyártási lehetőség')}{gallery_item('ref-process-install.webp','Kivitelezés','Helyszíni szerelés','Egyedi üzlettéri rendszer')}</div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Speciális igény</p><h2>Van egy alkatrész vagy prototípus, ami nem kapható készen?</h2><p>Küldje el a modellt, rajzot vagy az ötlet leírását; megvizsgáljuk a gyárthatóságot.</p></div><a class="button button-light" href="kapcsolat.html">Megkeresés küldése {icons['arrow']}</a></div></section>'''

# References page
all_gallery = ''.join([
 gallery_item('ref-retail-denim.webp','uzlet','Világított farmerfal','Üzletberendezés'),
 gallery_item('ref-retail-window.webp','uzlet','Kirakati fényinstalláció','Üzletberendezés'),
 gallery_item('ref-retail-orange.webp','uzlet','Moduláris üzlettéri sziget','Üzletberendezés'),
 gallery_item('ref-counter.webp','uzlet','Egyedi értékesítési pult','Üzletberendezés'),
 gallery_item('ref-process-install.webp','uzlet','Helyszíni szerelés','Üzletberendezés'),
 gallery_item('ref-stair-floating.webp','lepcso','Lebegő tölgy lépcső','Design lépcső'),
 gallery_item('ref-stair-glass.webp','lepcso','Üvegkorlátos lépcső','Design lépcső'),
 gallery_item('ref-stair-detail.webp','lepcso','Fa–üveg részlet','Design lépcső'),
 gallery_item('ref-table.webp','butor','Tömörfa asztal','Egyedi bútor'),
 gallery_item('ref-wardrobe.webp','butor','Beépített gardrób','Egyedi bútor'),
 gallery_item('ref-cabinet.webp','butor','Festett vitrin','Egyedi bútor'),
 gallery_item('ref-cabinet-alt.webp','butor','Üvegezett szekrény','Egyedi bútor'),
 gallery_item('render-loft.webp','terv','Komplex lakótér','3D látványterv'),
 gallery_item('design-moodboard.webp','terv','Terv–gyártás–végeredmény','Tervezési folyamat'),
 gallery_item('detail-hex.webp','reszlet','Burkolati átmenet','Egyedi részlet'),
 gallery_item('detail-lamella.webp','reszlet','Lamellás térelválasztó','Belsőépítészeti elem'),
])
references_body = hero('hero-retail.webp','Portfólió','Referenciák, amelyek mögött teljes projektfolyamat áll.','Üzletberendezések, egyedi bútorok, design lépcsők, tervezési és technológiai részletek.',('Ajánlatkérés','kapcsolat.html'),('Főoldal','index.html'))
references_body += f'''<section id="content" class="section section-light"><div class="container">{section_title('Referenciák','Szűrhető projektgaléria','Kattintson a képekre a nagyításhoz.')}
<div class="filter-bar" role="group" aria-label="Referencia szűrők"><button class="filter-button is-active" data-filter="all">Összes</button><button class="filter-button" data-filter="uzlet">Üzletberendezés</button><button class="filter-button" data-filter="butor">Egyedi bútor</button><button class="filter-button" data-filter="lepcso">Lépcső</button><button class="filter-button" data-filter="terv">Tervezés</button><button class="filter-button" data-filter="reszlet">Részletmegoldás</button></div><div class="gallery-grid filter-gallery">{all_gallery}</div></div></section><section class="cta-band"><div class="container"><div><p class="eyebrow">Következő referencia</p><h2>Az Ön projektje lehet a következő.</h2><p>Beszéljük át az igényeket és a megvalósítás kereteit.</p></div><a class="button button-light" href="kapcsolat.html">Kapcsolatfelvétel {icons['arrow']}</a></div></section>'''

# Blog index
blog_body = hero('hero-blog.webp','Blog','Műhelynapló, technológia és projektismeretek.','Betekintés a tervezésbe, gyártásba és kivitelezésbe — gyakorlati szempontokkal, valódi projektekből.',('Cikkek','blog.html#articles'),('Kapcsolat','kapcsolat.html'))
blog_cards = f'''
<article class="blog-card featured" data-reveal><a href="blog-uzletberendezes-folyamat.html"><img src="{ASSET}blog-retail.webp" alt="Üzletberendezés gyártási folyamat" loading="lazy"><div><span>Projektfolyamat</span><h2>Egy üzletberendezés útja a tervtől az átadásig</h2><p>Felmérés, tervezés, gyártás, felületkezelés és helyszíni telepítés egy folyamatban.</p><time datetime="2026-08-10">2026. augusztus 10.</time></div></a></article>
<article class="blog-card" data-reveal><a href="blog-design-lepcso.html"><img src="{ASSET}blog-stair.webp" alt="Modern design lépcső" loading="lazy"><div><span>Design lépcsők</span><h3>Fa, üveg és acél: mitől lesz egységes a végeredmény?</h3><p>Anyagkapcsolatok és részletképzés egyedi lépcsőknél.</p><time datetime="2026-08-06">2026. augusztus 6.</time></div></a></article>
<article class="blog-card" data-reveal><a href="blog-3d-nyomtatas.html"><img src="{ASSET}technology-printer.webp" alt="3D nyomtató műhelyben" loading="lazy"><div><span>Technológia</span><h3>3D nyomtatás a modern bútorgyártásban</h3><p>Hol segít egy prototípus vagy egyedi alkatrész?</p><time datetime="2026-08-02">2026. augusztus 2.</time></div></a></article>
<article class="blog-card" data-reveal><a href="blog-tervezes.html"><img src="{ASSET}blog-desk.webp" alt="Tervezőasztal rajzokkal" loading="lazy"><div><span>Tervezés</span><h3>Miért nem elég egy szép látványterv?</h3><p>A gyárthatóság, szerelhetőség és költség szerepe.</p><time datetime="2026-07-29">2026. július 29.</time></div></a></article>'''
blog_body += f'''<section id="articles" class="section section-light"><div class="container">{section_title('Friss bejegyzések','Szakmai háttér érthetően')}
<div class="blog-grid blog-index">{blog_cards}</div></div></section><section class="newsletter"><div class="container"><div><p class="eyebrow">Műhelynapló</p><h2>Új projektek és technológiai részletek.</h2><p>A feliratkozási funkció élesítéskor köthető össze a választott hírlevélrendszerrel.</p></div><form class="inline-form" data-demo-form><label class="sr-only" for="newsletter-email">E-mail</label><input id="newsletter-email" type="email" placeholder="E-mail-cím" required><button class="button button-red" type="submit">Feliratkozás</button></form></div></section>'''

# About page
about_body = hero('hero-home.webp','Rólunk','Családi vállalkozás, modern gyártói szemlélettel.','Több generációs asztalos tapasztalat, saját gyártási háttér és személyes felelősség minden projektben.',('Kapcsolat','kapcsolat.html'),('Referenciák','referenciak.html'))
about_body += f'''
<section id="content" class="section section-light"><div class="container split-grid"><div class="media-frame" data-reveal><img src="{ASSET}team-shirt.webp" alt="LEGRADI csapat és munkaruha" loading="lazy"></div><div class="split-copy" data-reveal><p class="eyebrow">A LEGRADI</p><h2>Hagyomány és innováció egy műhelyben.</h2><p>Győri családi vállalkozásként egyedi bútorokat, üzletberendezéseket, design lépcsőket és belsőépítészeti elemeket készítünk. A hagyományos asztalos szakértelmet CAD/CAM tervezéssel, CNC megmunkálással, saját felületkezeléssel és 3D nyomtatással egészítjük ki.</p><p>A kivitelezést nem adjuk tovább: a helyszíni telepítést minden esetben a saját csapatunk végzi.</p></div></div></section>
<section class="section section-black"><div class="container">{section_title('Értékeink','A projektműködés alapelvei')}
<div class="feature-grid four"><article>{icon('check')}<h3>Időtálló minőség</h3><p>Tartós szerkezetek, megbízható anyagok és ellenőrzött részletek.</p></article><article>{icon('plan')}<h3>Pontos kommunikáció</h3><p>Átlátható műszaki tartalom és egyértelmű következő lépések.</p></article><article>{icon('factory')}<h3>Saját felelősség</h3><p>A tervezéstől a szerelésig egy csapat kezében marad a projekt.</p></article><article>{icon('cube')}<h3>Egyedi megoldás</h3><p>Nem a standardhoz igazítjuk a teret, hanem a térhez tervezzük a megoldást.</p></article></div></div></section>
<section class="section section-light"><div class="container split-grid"><div class="split-copy" data-reveal><p class="eyebrow">Műhely és kapacitás</p><h2>Faipari és digitális technológiák összehangolva.</h2><p>CNC gép, festőkamra, klasszikus asztalos nagygépek, korszerű kéziszerszámok és többféle FDM/kompozit 3D nyomtató támogatja a gyártást.</p><a class="text-link" href="technologia.html">Technológiai háttér {icons['arrow']}</a></div><div class="media-frame" data-reveal><img src="{ASSET}process-montage.webp" alt="LEGRADI gyártási folyamat" loading="lazy"></div></div></section>
<section class="cta-band"><div class="container"><div><p class="eyebrow">Együttműködés</p><h2>Keressen hosszú távú kivitelező partnert?</h2><p>Magánmegrendelések, üzletláncok és belsőépítészeti együttműködések számára is dolgozunk.</p></div><a class="button button-light" href="kapcsolat.html">Bemutatkozó egyeztetés {icons['arrow']}</a></div></section>'''

# Contact page
contact_body = hero('hero-contact.webp','Kapcsolat','Beszéljük át a projekt következő lépését.','Küldje el a projekt rövid leírását, helyszínét, tervezett határidejét és a rendelkezésre álló rajzokat vagy fotókat.',('Üzenet küldése','#contact-form'),('Referenciák','referenciak.html'))
contact_body += f'''
<section id="contact-form" class="section section-light"><div class="container contact-layout"><div class="contact-intro" data-reveal><p class="eyebrow">Projekt egyeztetés</p><h2>Milyen információ segíti a gyors indulást?</h2><ul class="check-list"><li>helyszín és projekt típusa</li><li>hozzávetőleges méretek vagy alaprajz</li><li>kívánt funkció és stílus</li><li>tervezett határidő</li><li>inspirációs képek vagy műszaki dokumentumok</li></ul><div class="contact-box"><p>{icon('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></p><p>{icon('pin')}<span>{LOCATION}</span></p><p>Vállalási terület: Magyarország és Ausztria.</p></div></div>
<form class="contact-form" data-contact-form data-email="{EMAIL}" data-reveal><div class="form-grid"><label>Név / cégnév<input type="text" name="name" required autocomplete="name"></label><label>E-mail<input type="email" name="email" required autocomplete="email"></label><label>Telefonszám<input type="tel" name="phone" autocomplete="tel"></label><label>Projekt típusa<select name="type"><option>Üzletberendezés</option><option>Egyedi bútor</option><option>Design lépcső</option><option>Tervezés</option><option>3D nyomtatás / technológia</option><option>Egyéb</option></select></label></div><label>Projekt rövid leírása<textarea name="message" rows="7" required placeholder="Helyszín, méret, határidő, elképzelés..."></textarea></label><label class="checkbox"><input type="checkbox" required><span>Elfogadom, hogy az üzenetemet kapcsolatfelvétel céljából kezeljék.</span></label><button class="button button-red" type="submit">Üzenet előkészítése {icons['arrow']}</button><p class="form-note">Az űrlap az alapverzióban az alapértelmezett levelezőprogramot nyitja meg. Élesítéskor közvetlen űrlapkezelő szolgáltatáshoz köthető.</p><div class="form-status" role="status" aria-live="polite"></div></form></div></section>'''

# Stock page
stock_body = hero('hero-stock.webp','Bútorok készletről','Készletről elérhető bútorok — hamarosan.','Kínálatunk hamarosan azonnal megvásárolható, gondosan kiválasztott és saját minőségi elveink szerint elkészített bútorokkal bővül.',('Értesítést kérek','#stock-form'),('Egyedi bútorok','egyedi-butorok.html'))
stock_body += f'''<section id="stock-form" class="section section-light"><div class="container narrow center-text">{section_title('Hamarosan','Elsőként szeretne értesülni?','Az értesítési funkció élesítéskor kapcsolható hírlevél- vagy webshoprendszerhez.')}
<form class="inline-form inline-form-light" data-demo-form><label class="sr-only" for="stock-email">E-mail</label><input id="stock-email" type="email" placeholder="E-mail-cím" required><button class="button button-red" type="submit">Értesítést kérek</button></form><p class="small-note">Az oldalon jelenleg még nem történik online értékesítés.</p></div></section>'''

# Legal placeholders
legal_data = '''<section class="simple-page section section-light"><div class="container narrow"><p class="eyebrow">Jogi információ</p><h1>Adatkezelési tájékoztató</h1><p>Ez az oldal a weboldal technikai mintaverziójának része. A végleges adatkezelési tájékoztatót a vállalkozás tényleges adatkezelési folyamatai, az űrlapkezelő, analitikai és hírlevélrendszer alapján szükséges elkészíteni és feltölteni.</p><h2>Kapcsolati adat</h2><p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p><h2>Technikai megjegyzés</h2><p>A jelenlegi statikus bemutatóoldal nem küld adatot szerverre. A kapcsolatfelvételi űrlap a felhasználó levelezőprogramját nyitja meg.</p></div></section>'''
legal_imprint = f'''<section class="simple-page section section-light"><div class="container narrow"><p class="eyebrow">Jogi információ</p><h1>Impresszum</h1><p>A végleges cégnév, székhely, adószám, cégjegyzékszám, tárhelyszolgáltató és felelős kiadó adatait élesítés előtt szükséges kitölteni.</p><h2>Kapcsolat</h2><p>LEGRADI<br>{LOCATION}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></section>'''

# Article helper

def article_page(title, category, image, intro, sections, active='blog'):
    body = f'''<article class="article-page"><header class="article-header" style="--article-image:url('{ASSET}{image}')"><div class="container"><p class="eyebrow">{category}</p><h1>{title}</h1><p>{intro}</p><a href="blog.html" class="text-link">← Vissza a bloghoz</a></div></header><div class="article-content container narrow">'''
    for heading, paragraphs in sections:
        body += f'<section><h2>{heading}</h2>' + ''.join(f'<p>{p}</p>' for p in paragraphs) + '</section>'
    body += f'''<aside class="article-cta"><h2>Van hasonló projektje?</h2><p>Egyeztessük a műszaki kereteket és a megvalósítás következő lépését.</p><a class="button button-red" href="kapcsolat.html">Kapcsolatfelvétel</a></aside></div></article>'''
    return body

articles = {
'blog-uzletberendezes-folyamat.html': article_page('Egy üzletberendezés útja a tervtől az átadásig','Projektfolyamat','blog-retail.webp','A látványos végeredmény mögött pontos tervezés, szervezett gyártás és fegyelmezett helyszíni kivitelezés áll.',[
 ('1. Igények és határidők rögzítése',['Az első egyeztetésen nem csak a méreteket és a formát kell tisztázni. Fontos a termékkör, a vásárlói útvonal, a napi használat, a telepítés időablaka és az üzlet nyitási dátuma is.']),
 ('2. Gyártható tervezés',['A látványtervet műszaki részletekkel kell alátámasztani: anyagvastagságokkal, vasalatokkal, kábelvezetésekkel, világítással és szerelési csomópontokkal.']),
 ('3. Gyártás és felületkezelés',['Az alkatrészek CNC megmunkálása után következik az asztalos összeállítás, próbaszerelés és felületkezelés. A csomagolási sorrendet már a helyszíni szerelés logikája határozza meg.']),
 ('4. Helyszíni telepítés',['Az üzlettéri kivitelezés gyakran szűk időablakban történik. A pontos előkészítés csökkenti a helyszíni improvizációt, és kiszámíthatóbb átadást biztosít.'])]),
'blog-design-lepcso.html': article_page('Fa, üveg és acél: mitől lesz egységes a végeredmény?','Design lépcsők','blog-stair.webp','Egy design lépcsőnél a legkisebb csomópontok is meghatározzák az egész tér minőségérzetét.',[
 ('Arányok és járáskomfort',['A fokmagasság, belépőmélység, forduló és járásvonal nem esztétikai részlet, hanem a használhatóság alapja.']),
 ('Anyagkapcsolatok',['A fa természetes mozgását, az üveg rögzítését és az acélszerkezet tűréseit egy rendszerben kell kezelni.']),
 ('Korlát és kapaszkodó',['A korlát vizuálisan könnyed lehet, de a rögzítésének merevnek, biztonságosnak és tartósnak kell maradnia.']),
 ('Helyszíni pontosság',['A falak, födémek és burkolatok valós méretei eltérhetnek a tervtől, ezért a végleges gyártás előtt pontos felmérés szükséges.'])]),
'blog-3d-nyomtatas.html': article_page('3D nyomtatás a modern bútorgyártásban','Technológia','technology-printer.webp','A 3D nyomtatás nem helyettesíti az asztalosmunkát, hanem gyorsabbá és rugalmasabbá teszi az egyedi gyártást.',[
 ('Prototípus a gyártás előtt',['Egy új csomópont, fogantyú vagy burkolati elem kis költséggel kipróbálható, mielőtt végleges anyagból elkészül.']),
 ('Sablonok és szerelési segédletek',['Az egyedi fúró-, pozicionáló- és marósablonok csökkentik a hibalehetőséget és gyorsítják az ismétlődő műveleteket.']),
 ('Pótalkatrészek és különleges elemek',['Olyan kis darabszámú alkatrészek is elkészíthetők, amelyek kereskedelmi forgalomban nem kaphatók.']),
 ('Külső megkeresések',['A nyomtatóparkot főként saját projektjeinkhez használjuk, de saját ötlettel, modellel vagy alkatrészigénnyel is meg lehet keresni bennünket.'])]),
'blog-tervezes.html': article_page('Miért nem elég egy szép látványterv?','Tervezés','blog-desk.webp','A látványterv döntéstámogató eszköz. A kivitelezéshez azonban gyártható részletek, pontos méretek és szerelési logika is szükséges.',[
 ('A látványterv szerepe',['Segít megérteni a térarányokat, anyagokat, színeket és a bútor vizuális jelenlétét.']),
 ('Műszaki részletezés',['A gyártáshoz szükséges dokumentáció tartalmazza az alkatrészek méreteit, anyagait, élzárását, vasalatait és csatlakozásait.']),
 ('Költség és döntések',['A korai részletezés megmutatja, hol érdemes prémium anyagot választani, és hol lehet egyszerűsíteni a funkció sérülése nélkül.']),
 ('Szerelhetőség',['A legjobb terv nem csak legyártható, hanem szállítható, bevihető, összeszerelhető és karbantartható is.'])]),
}

pages = {
'index.html': shell('LEGRADI','Üzletberendezések, egyedi bútorok, design lépcsők, tervezés és teljes körű kivitelezés Győrből Magyarországra és Ausztriába.','home',home_body,'hero-home.webp',''),
'uzletberendezesek.html': shell('Üzletberendezések','Egyedi üzletberendezések tervezése, gyártása és helyszíni telepítése Magyarországon és Ausztriában.','retail',retail_body,'hero-retail.webp','uzletberendezesek.html'),
'egyedi-butorok.html': shell('Egyedi bútorok','Egyedi konyhák, gardróbok, vitrinek és belsőépítészeti bútorok tervezése és gyártása.','furniture',furniture_body,'hero-furniture.webp','egyedi-butorok.html'),
'design-lepcsok.html': shell('Design lépcsők','Egyedi fa-, üveg- és acéllépcsők tervezése, gyártása és helyszíni kivitelezése.','stairs',stairs_body,'hero-stairs.webp','design-lepcsok.html'),
'tervezes.html': shell('Tervezés','3D látványtervezés, műszaki részletezés és gyártási előkészítés bútor- és belsőépítészeti projektekhez.','planning',planning_body,'hero-planning.webp','tervezes.html'),
'technologia.html': shell('Technológia','CNC megmunkálás, felületkezelés és 3D nyomtatási megoldások a LEGRADI műhelyében.','technology',technology_body,'hero-technology.webp','technologia.html'),
'referenciak.html': shell('Referenciák','LEGRADI referencia munkák: üzletberendezések, egyedi bútorok, design lépcsők és belsőépítészeti megoldások.','references',references_body,'hero-retail.webp','referenciak.html'),
'blog.html': shell('Blog','Tervezési, gyártási és kivitelezési háttéranyagok a LEGRADI műhelyéből.','blog',blog_body,'hero-blog.webp','blog.html'),
'rolunk.html': shell('Rólunk','A LEGRADI győri családi vállalkozás: több generációs asztalos tapasztalat modern gyártási technológiákkal.','about',about_body,'hero-home.webp','rolunk.html'),
'kapcsolat.html': shell('Kapcsolat','Projekt egyeztetés és ajánlatkérés üzletberendezés, egyedi bútor, lépcső, tervezés és 3D nyomtatás témában.','contact',contact_body,'hero-contact.webp','kapcsolat.html'),
'keszletrol.html': shell('Bútorok készletről','Hamarosan készletről megvásárolható LEGRADI bútorok.','stock',stock_body,'hero-stock.webp','keszletrol.html'),
'adatkezeles.html': shell('Adatkezelés','Adatkezelési tájékoztató.','',legal_data,'hero-contact.webp','adatkezeles.html'),
'impresszum.html': shell('Impresszum','A LEGRADI weboldal impresszuma.','',legal_imprint,'hero-contact.webp','impresszum.html'),
}
for filename, body in articles.items():
    pages[filename] = shell(filename.replace('.html','').replace('blog-','').replace('-',' ').title(), 'LEGRADI blogbejegyzés tervezésről, gyártásról és kivitelezésről.', 'blog', body, 'hero-blog.webp', filename)

for name, html in pages.items():
    (ROOT/name).write_text(html, encoding='utf-8')

# 404
(ROOT/'404.html').write_text(shell('Az oldal nem található','A keresett oldal nem található.','', '<section class="simple-page section section-black"><div class="container narrow center-text"><p class="eyebrow">404</p><h1>Az oldal nem található.</h1><p>Ellenőrizze a címet, vagy térjen vissza a főoldalra.</p><a class="button button-red" href="index.html">Főoldal</a></div></section>', 'hero-home.webp','404.html'), encoding='utf-8')

# Sitemap and robots
urls=['','uzletberendezesek.html','egyedi-butorok.html','design-lepcsok.html','tervezes.html','technologia.html','referenciak.html','blog.html','rolunk.html','kapcsolat.html','keszletrol.html']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE_URL}/{u}</loc></url>\n' for u in urls)+'</urlset>',encoding='utf-8')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n',encoding='utf-8')
