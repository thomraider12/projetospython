import speedtest as st

print("Olá! Esta app mede o teu ping, download (mb/s) e upload (mb/s).\n")
input("Carrega no ENTER para começar. ")

server = st.Speedtest()
server.get_best_server()

print("Aguarda enquanto obtemos os teus resultados...\n")

ping = server.results.ping
print(f"O teu Ping: {ping}\n")

download = server.download()
download = download / 1000000
print(f"Velocidade do download: {download} mb/s\n")

upload = server.upload()
upload = upload / 1000000
print(f"Velocidade do Upload: {upload} mb/s\n")