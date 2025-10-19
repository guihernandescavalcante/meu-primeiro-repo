import requests  #? vai até a internet e traz a página
from bs4 import BeautifulSoup #? pega o HTML e transforma em uma sopa onde você consegue pegar só o pedaço que interessa, como todos os h2

# URL de um site de marketing
url = "https://www.searchenginejournal.com/"

# Pegando o conteúdo da página
resposta = requests.get(url) #? ele abre a página html
html = resposta.text #? guarda o HTML da página na variável html

# Interpretando o HTML
soup = BeautifulSoup(html, "html.parser") #? colocou o HTML numa batedeira para ficar mais fácil de pegar os pedaços

# Encontrando os títulos (usando tag h2 como exemplo)
titulos = soup.find_all("h2") #? Pede todos os titulos que tem h2 (geralmente sao os subtitulos)

# Palavras que quero encontrar
palavras_chave = ["SEO", "Google", "Instagram", "Ads"] #? defini as palvras que eu estou caçando nos subtitulos

print("🔍 Procurando palavras nos títulos do blog...")

for titulo in titulos:
    texto = titulo.get_text()
    for palavra in palavras_chave:
        if palavra.lower() in texto.lower():
            print(f"✅ Encontrado: '{palavra}' em -> {texto}")
