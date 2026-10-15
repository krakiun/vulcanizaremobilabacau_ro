# Vulcanizare Mobilă Bacău – sursa Hugo

Generare site (din acest folder):

    hugo

Rezultatul ajunge în `../vulcanizaremobila.ro/` – acel folder se urcă pe hosting.
Previzualizare cu reîncărcare automată: `hugo server` → http://localhost:1313/

## Unde editezi
- `hugo.toml` – telefon, WhatsApp, meniu
- `data/services.yaml` – serviciile (Acasă, /servicii/, footer, schema)
- `data/zones.yaml` – cartiere și localități
- `data/faq.yaml` – întrebările frecvente de pe Acasă
- `content/*.md` – titluri, descrieri și texte pentru fiecare pagină
- `content/zone-deservite/*.md` – paginile de localitate (adresa vine din `url`, ex. /vulcanizare-mobila-onesti/)
- `content/blog/*.md` – articolele; `{{< cta >}}` inserează caseta „Sună acum”
- `assets/css/` – stilurile; `layouts/` – șabloanele HTML

Articol nou: copiază un fișier din `content/blog/`, schimbă numele fișierului (devine adresa),
front matter-ul (`title`, `h1`, `description`, `lead`, `excerpt`, `icon`, `date`, `weight`) și textul.

Localitate nouă: copiază un fișier din `content/zone-deservite/` și schimbă `name`, `url`, `tip`, `zona`
(`oras` sau `comuna`), `localitati`, `drumuri`, `situatii`, `faq` și textul. Dacă `name` apare și în
`data/zones.yaml`, numele devine automat link pe Acasă și pe pagina Zone deservite.

## Publicare automată (GitHub Pages)
La fiecare `git push` pe `main`, workflow-ul `.github/workflows/deploy.yml` construiește site-ul cu Hugo
și îl publică pe GitHub Pages, la https://vulcanizaremobila.ro (domeniul e în `static/CNAME`).
Rulează și zilnic la 08:00 UTC, ca articolele cu dată în viitor să apară singure.
Progresul se vede în tab-ul **Actions** al repository-ului.
