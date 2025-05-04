import os
import json
import re
from pwncollege import PWNClient
from bs4 import BeautifulSoup, NavigableString
from dotenv import load_dotenv

load_dotenv()

def estrai_info_pwncollege():
    email = os.getenv("PWN_COLLEGE_EMAIL")
    password = os.getenv("PWN_COLLEGE_PASSWORD")

    client = PWNClient(email=email, password=password)
    client.do_login(email=email, password=password)

    session = client.session
    response = session.get("https://pwn.college/hacker/")
    soup = BeautifulSoup(response.text, "html.parser")

    # Nome
    nome = soup.find("h1", class_="brand-mono")
    nome = nome.text.strip() if nome else "Sconosciuto"

    # Cintura (dal title)
    cintura_span = soup.find("span", title=True)
    cintura = cintura_span["title"] if cintura_span else "Nessuna"

    # Immagine della cintura
    cintura_img_tag = soup.find("a", href="/belts").find("img", class_="scoreboard-belt")
    cintura_img_url = "https://pwn.college" + cintura_img_tag["src"] if cintura_img_tag else "Nessuna immagine"

    # Paese (flag)
    bandiera = soup.find("i", class_=lambda c: c and c.startswith("flag-"))
    paese = bandiera["class"][0].split("-")[1].upper() if bandiera else "Non disponibile"

    # Badge
    badge = []
    for badge_a in soup.find_all("a", href=True):
        badge_text = badge_a.get_text(strip=True)
        if badge_text and badge_a.find_parent("h2"):
            badge.append(badge_text)

    # Progressi challenge
    moduli = []
    containers = soup.find_all("a", class_="text-decoration-none")

    for container in containers:
        modulo = {}

        # Link al modulo
        href = container.get("href", "")
        if not href:
            continue
        modulo["link"] = f"https://pwn.college{href}"

        # Trova titolo modulo
        titolo = container.find("h2")
        if not titolo:
            continue
        modulo["titolo"] = titolo.get_text(strip=True)

        h4 = container.find("h4")
        if not h4:
            continue

        # Estrai solves
        solve_icon = h4.find("i", title="Solves")
        if solve_icon:
            solve_text = ""
            for el in solve_icon.next_siblings:
                if isinstance(el, NavigableString):
                    solve_text += el.strip()
                elif el.name:
                    solve_text += el.get_text(strip=True)
                if "/" in solve_text:
                    break
            match = re.search(r"(\d+)\s*/\s*(\d+)", solve_text)
            if match:
                modulo["challenge"] = f"{match.group(1)} / {match.group(2)}"

        # Estrai rank
        rank_icon = h4.find("i", title="Rank")
        if rank_icon:
            rank_text = ""
            for el in rank_icon.next_siblings:
                if isinstance(el, NavigableString):
                    rank_text += el.strip()
                elif el.name:
                    rank_text += el.get_text(strip=True)
                if "/" in rank_text:
                    break
            match = re.search(r"(\d+)\s*/\s*(\d+)", rank_text)
            if match:
                modulo["rank"] = f"{match.group(1)} / {match.group(2)}"

        moduli.append(modulo)

    # Stampa risultati
    print(f"Nome: {nome}")
    print(f"Immagine della cintura: {cintura_img_url}")
    print(f"Paese: {paese}")
    print(f"Badge: {badge}")
    print("Progressi challenge:")
    for m in moduli:
        print(f"- {m['titolo']}: {m.get('challenge', '?')} (Rank: {m.get('rank', '?')})")

    return {
        "nome": nome,
        "cintura_img_url": cintura_img_url,
        "paese": paese,
        "badge": badge,
        "progressi": moduli
    }

def aggiorna_json(data, filename="pwn_progress.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = {}

    existing_data.update(data)

    with open(filename, "w") as f:
        json.dump(existing_data, f, indent=4)
    print(f"✅ Dati salvati in {filename}")

if __name__ == "__main__":
    dati = estrai_info_pwncollege()
    aggiorna_json(dati)
