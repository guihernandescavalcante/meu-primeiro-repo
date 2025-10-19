import requests
from bs4 import BeautifulSoup

url = "https://www.searchenginejournal.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
titulos = soup.find_all("h2")

#! teste 1
# print()
# print("🔎Notícias do site: ")
# print()
# for t in titulos:
#     print(t.get_text().strip())

#! teste 2
# palavras = ["Instagram", "SEO", 'AI', "Google"]

# for t in titulos:
#     texto = t.get_text().strip()
#     for p in palavras:
#         if p.lower() in texto.lower():
#             print(f"Encontrei {p} em: {texto}")

#! teste 3
# palavra = input("Informe a palavra a ser monitorada: ")
# encontrou = False

# for t in titulos:
#     if palavra.lower() in t.get_text().lower():
#         print(f"✅ Encontrei: {t.get_text().strip()}")
#         encontrou = True

# if not encontrou:
#     print("❌ Palavra não encontrada.")

#! teste 4
# resultados = []

# for t in titulos:
#     texto = t.get_text()
#     if palavra.lower() in texto.lower():
#         resultados.append(texto)

# with open("resultados.txt", "w", encoding="utf-8") as f:
#     for r in resultados:
#         f.write(r.strip() + "\n")

# print("📁 Resultados salvos em resultados.txt.")

# with open("resultados.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#! teste 5
import schedule, time

resultados = []
palavra = input("Informe a palavra a ser monitorada: ")

def rodar_bot():
    print("⏳ Verificando novos títulos...")
    for t in titulos:
        texto = t.get_text()
        if palavra.lower() in texto.lower():
            resultados.append(texto)

    with open("resultados.txt", "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(r.strip() + "\n")

    print("📁 Resultados salvos em resultados.txt.")

    with open("resultados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

schedule.every(1).hours.do(rodar_bot)

while True:
    schedule.run_pending()
    time.sleep(1)