import requests
from bs4 import BeautifulSoup

def get_noticias():
    url = 'https://www.globo.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    noticias = soup.find_all('a')
    tgt_class1 = 'post__title'  # Exemplo de classe para o nome do país
    tgt_class2 = 'post__link'  # Exemplo de classe para o número de noticias

    quadronoticias = {}
    for noticia in noticias:
        if (noticia.h2 != None) and (noticia.h2.get('class') != None):
            if  tgt_class1 in noticia.h2.get('class'):
                quadronoticias[noticia.h2.text] = noticia.get('href')
            if  tgt_class2 in noticia.h2.get('class'):
                quadronoticias[noticia.h2.text] = noticia.get('href')

    return quadronoticias 

def enviar_noticias(noticias):
    url = 'http://localhost:8080/news/add'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=noticias, headers=headers)
    
    if response.status_code == 201:
        print("Notícias enviadas com sucesso!")
    else:
        print(f"Falha ao enviar notícias: {response.status_code}")

noticias = get_noticias()
enviar_noticias(noticias)
