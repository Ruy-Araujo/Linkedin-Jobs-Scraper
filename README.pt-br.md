[![en](https://img.shields.io/badge/lang-EN-blue?style=for-the-badge&logo=googletranslate&logoColor=4285F4)](/README.md)

# Linkedin Jobs Scraper

Este repositório contém um scraper de empregos do LinkedIn escrito em Python que extrai dados de vagas de emprego e salva em arquivos JSON.

## Como usar

1. Clone o repositório para a sua máquina local:

    ```bash
    git clone https://github.com/Ruy-Araujo/Linkedin-Jobs-Scraper
    ```

2. Instale as dependências:

    ```bash
    cd Linkedin-Jobs-Scraper
    pip install -r requirements.txt
    ```

3. Configure o arquivo exemple.env:  

    1. Preencha os parametros _LINKEDIN_COOKIES_ e _CSRF_TOKEN_ com os da plataforma vide [como gerar os cookies e o csrf-token](#cookies)

    2. O campo _KEYWORDS_ é uma string com as palavras-chave que serão utilizadas para filtrar as vagas de emprego.  

    3. O campo _LOCATION_ é uma string com o local onde as vagas serão buscadas.

4. Excute o script main.py

    ```python3
    python main.py
    ```

O scraper irá extrair dados das vagas de emprego do LinkedIn Jobs e salvar em um arquivo JSON no diretório do projeto.

## <a id="cookies"></a>Como gerar os cookies do LinkedIn

1. Acesse o site [LinkedIn Jobs](https://www.linkedin.com/jobs/).

2. Abra o console do navegador (F12) e vá para a aba Network.

3. Na aba Network aperte CTRL+F para realizar uma busca e digite "csrf-token".

4. Selecione qualquer item e verá os campos "cookie" e "csrf-token" no cabeçalho da requisição.

## Detalhes técnicos

O scraper usa o framework [Scrapy](https://scrapy.org/) para fazer o parsing do HTML da página de empregos do LinkedIn e extrair informações como título da vaga, nome da empresa, localização, descrição da vaga e data de publicação.

Os dados brutos estão disponiveis [aqui](data/)

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
