import vlc
import tkinter as tk
from tkinter import messagebox

# Lista de rádios com nome e URL
radios = {
    "Rádio Comercial": "https://stream-icy.bauermedia.pt/comercial.aac",
    "RFM": "https://playerservices.streamtheworld.com/api/livestream-redirect/RFMAAC_SC",
    "Fama Rádio": "http://famaradio.mywire.org:8000/digitalfm64",
    "Observador": "https://playerservices.streamtheworld.com/api/livestream-redirect/OBSERVADORAAC.aac?dist=web-popup&devicename=aac",
    "TSF": "http://tsfdirecto.tsf.pt/tsfdirecto.mp3",
    "M80": "https://stream-icy.bauermedia.pt/m80.aac",
    "Rádio Voz Santo Tirso": "https://radios.justweb.pt/8024/stream",
    "MegaHits": "http://25703.live.streamtheworld.com/MEGA_HITS_SC",
    "Nova Era": "http://centova.radios.pt:9478/stream/1/",
    "MEO Sudoeste": "http://centova.radio.com.pt:8495/stream/1/",
    "Orbital": "https://centova.radios.pt/proxy/401?mp=/stream/",
    "Nove3Cinco": "https://centova.radios.pt/proxy/522?mp=/stream/1/",
    "Cidade FM": "https://stream-icy.bauermedia.pt/cidade.aac",
    "Cidade Hoje": "http://centova.radio.com.pt:8119/;",
    "Tuga FM": "https://tugafm.stream.laut.fm/tugafm",
    "Truckers FM": "https://live.truckers.fm/"
}


class RadioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Player de Rádios")
        self.root.geometry("200x680")  # Exemplo de resolução: 300x400 pixels
        self.player = None
        self.current_radio = None
        
        # Frame para os botões de rádio
        radio_frame = tk.Frame(root)
        radio_frame.pack(padx=10, pady=10)

        # Botões para cada rádio
        for i, (name, url) in enumerate(radios.items()):
            btn = tk.Button(radio_frame, text=name, command=lambda url=url, name=name: self.play_radio(url, name))
            btn.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        # Botão para parar a rádio
        stop_button = tk.Button(root, text="Parar", command=self.stop_radio, fg="red")
        stop_button.pack(pady=10)

        # Label para mostrar qual rádio está tocando
        self.playing_label = tk.Label(root, text="A tocar: Nenhuma rádio", fg="blue")
        self.playing_label.pack(pady=5)

    def play_radio(self, url, name):
        # Parar rádio atual, se estiver tocando
        if self.player:
            self.player.stop()

        # Iniciar nova rádio
        self.player = vlc.MediaPlayer(url)
        self.player.play()
        self.current_radio = name
        self.playing_label.config(text=f"A tocar: {name}")
        messagebox.showinfo("Play", f"A tocar: {name}")

    def stop_radio(self):
        if self.player:
            self.player.stop()
            messagebox.showinfo("Pause", f"Reprodução da {self.current_radio} encerrada.")
            self.playing_label.config(text="A tocar: Nenhuma rádio")
            self.current_radio = None


if __name__ == "__main__":
    root = tk.Tk()
    app = RadioApp(root)
    root.mainloop()
