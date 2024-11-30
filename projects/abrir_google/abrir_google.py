import webbrowser

url = "https://www.google.pt/search?q="
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def create_query():
    query = input("Digite sua pesquisa: ")
    return query.replace(" ", "+")

def create_url():
    query = create_query()
    if not query:
        print("Erro: Por favor, insira uma pesquisa válida.")
    else:
        final_url = url + query
        webbrowser.get(chrome_path).open(final_url)

create_url()