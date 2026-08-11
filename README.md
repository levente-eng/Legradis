# LEGRADI weboldal – statikus bemutatóverzió

Ez a csomag egy teljes, reszponzív, többoldalas HTML/CSS/JavaScript weboldal.

## Megnyitás

1. Csomagold ki a ZIP-fájlt.
2. Nyisd meg az `index.html` fájlt, vagy töltsd fel a teljes mappát egy tárhelyre.
3. Helyi fejlesztői előnézethez a mappában futtatható:

```bash
python3 -m http.server 8000
```

Ezután: `http://localhost:8000`

## Oldalak

- Főoldal
- Üzletberendezések
- Egyedi bútorok
- Design lépcsők
- Tervezés
- Technológia és 3D nyomtatás
- Referenciák szűrhető galériával
- Blog + 4 mintabejegyzés
- Rólunk
- Kapcsolat
- Bútorok készletről
- Adatkezelés / Impresszum sablon
- 404 oldal

## Beépített funkciók

- mobilmenü
- reszponzív elrendezés
- referencia-szűrők
- képnagyító lightbox
- scroll animációk
- kapcsolatfelvételi űrlap kliensoldali ellenőrzéssel
- hírlevél/készletértesítő demó
- SEO metaadatok, `sitemap.xml`, `robots.txt`

## Élesítés előtt módosítandó

- Kapcsolati e-mail: jelenleg `office@legradis.com`.
- A kapcsolatfelvételi űrlap jelenleg a felhasználó levelezőprogramját nyitja meg. Éles oldalon ajánlott Formspree, Netlify Forms, saját backend vagy WordPress űrlapkezelő bekötése.
- Az impresszum és adatkezelési oldal jogi adatait ki kell tölteni.
- A hírlevél- és készletértesítő űrlapot valódi rendszerhez kell kapcsolni.
- A `build_site.py` elején lévő `SITE_URL`, `EMAIL` és `LOCATION` értékek módosíthatók, majd a script újra futtatható.

## Telepítési lehetőségek

A csomag feltölthető hagyományos tárhelyre, Netlifyra, Cloudflare Pagesre vagy GitHub Pagesre. WordPress-be a megjelenés egyedi sablonként átültethető.
