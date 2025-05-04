import json
import os
import re

def formatta_pwncollege_section(data):
    nome = data["nome"]
    cintura_url = data["cintura_img_url"]
    paese = data["paese"]
    badge = " ".join(data["badge"]) if data["badge"] else "Nessuno"

    header = (
        '<!-- PWN_START -->\n'
        '<hr/>\n'
        '<h2 align="left" style="color:#00bcd4;">🔐 pwn.college Progress</h2>\n'
        '<div align="left" style="margin-bottom:10px;">\n'
        f'  <strong style="font-size:1.2em;">👤 {nome}</strong><br/>\n'
        f'  🌍 <em>{paese}</em> &nbsp;|&nbsp; 🏅 <strong>Badges:</strong> {badge}<br/>\n'
        f'  <img src="{cintura_url}" alt="Belt" width="90" style="margin-top:5px;"/>\n'
        '</div>\n\n'
        '<table>\n'
        '  <thead>\n'
        '    <tr>\n'
        '      <th align="left">📘 Module</th>\n'
        '      <th align="center">📈 Progress</th>\n'
        '      <th align="center">🏅 Rank</th>\n'
        '    </tr>\n'
        '  </thead>\n'
        '  <tbody>\n'
    )

    body = ""
    for modulo in data["progressi"]:
        titolo = modulo.get("titolo", "Unknown")
        link = modulo.get("link", "#")
        titolo_linkato = f'<a href="{link}">{titolo}</a>'
        progress = modulo.get("challenge", "? / ?")
        rank = modulo.get("rank", "? / ?")
        body += f'    <tr>\n'
        body += f'      <td>{titolo_linkato}</td>\n'
        body += f'      <td align="center">{progress}</td>\n'
        body += f'      <td align="center">{rank}</td>\n'
        body += f'    </tr>\n'

    footer = (
        '  </tbody>\n'
        '</table>\n'
        '<hr/>\n'
        '<!-- PWN_END -->\n'
    )

    return header + body + footer

def aggiorna_readme_da_json(json_path="pwn_progress.json", readme_path="README.md"):
    with open(json_path, "r") as f:
        data = json.load(f)

    nuova_sezione = formatta_pwncollege_section(data)

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            contenuto = f.read()
    else:
        contenuto = ""

    # Se esiste già una sezione PWN, sostituiscila
    if "<!-- PWN_START -->" in contenuto and "<!-- PWN_END -->" in contenuto:
        contenuto = re.sub(
            r"<!-- PWN_START -->.*?<!-- PWN_END -->",
            nuova_sezione,
            contenuto,
            flags=re.DOTALL
        )
    else:
        # Altrimenti aggiungila alla fine
        contenuto += "\n\n" + nuova_sezione

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(contenuto)

    print(f"✅ README.md aggiornato con i dati di pwn.college")

if __name__ == "__main__":
    aggiorna_readme_da_json()
