import tkinter as tk
from tkinter import ttk, filedialog, PhotoImage, messagebox

channels = []

def update_channel_info():
    channel_info.delete(1.0, tk.END)
    for channel in reversed(channels):
        info = f"Channel Name: {channel['nome_canal']}\n" \
               f"Channel Link: {channel['link_canal']}\n"
        if channel['titulo_grupo']:
            info += f"Group Title: {channel['titulo_grupo']}\n"
        if channel['tvg_id']:
            info += f"Tvg ID: {channel['tvg_id']}\n"
        if channel['tvg_name']:
            info += f"Tvg Name: {channel['tvg_name']}\n"
        if channel['tvg_shift']:
            info += f"Tvg shift: {channel['tvg_shift']}\n"
        if channel['logo_link']:
            info += f"Logo Link: {channel['logo_link']}\n"
        if channel['license_type']:
            info += f"License Type: {channel['license_type']}\n"
        if channel['license_key']:
            info += f"License Key: {channel['license_key']}\n"
        if channel['manifest_type']:
            info += f"Manifest Type: {channel['manifest_type']}\n"
        info += "\n"
        channel_info.insert(tk.END, info)

    channel_count_var.set(f"Channels Added: {len(channels)}")

def on_add_channel():
    nome_canal = entry_nome_canal.get()
    titulo_grupo = entry_titulo_grupo.get()
    link_canal = entry_link_canal.get()
    license_type = license_type_var.get()
    license_key = entry_license_key.get()

    if not nome_canal or not titulo_grupo or not link_canal:
        tk.messagebox.showerror("Erro", "Não definido: Nome canal, Título Grupo, Link Canal")
        return

    if license_type and not license_key:
        tk.messagebox.showerror("Error", "Enter License key")
        return

    channel = {
        "nome_canal": nome_canal,
        "link_canal": link_canal,
        "titulo_grupo": titulo_grupo,
        "tvg_id": entry_tvg_id.get(),
        "tvg_name": entry_tvg_name.get(),
        "tvg_shift": combo_tvg_shift.get(),
        "logo_link": entry_logo_link.get(),
        "license_type": license_type,
        "license_key": license_key,
        "manifest_type": manifest_type_var.get(),
    }
    channels.append(channel)
    update_channel_info()

def on_clear_fields():
    clear_entries()

def on_generate_m3u():
    file_path = filedialog.asksaveasfilename(defaultextension=".m3u", filetypes=[("M3U files", "*.m3u"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for channel in channels:
                if channel['license_type'] and channel['license_key']:
                    f.write(f'#KODIPROP:inputstream=inputstream.adaptive\n')
                    f.write(f'#KODIPROP:inputstream.adaptive.license_type={channel["license_type"]}\n')
                    f.write(f'#KODIPROP:inputstream.adaptive.license_key={channel["license_key"]}\n')
                if channel['manifest_type']:
                    f.write(f'#KODIPROP:inputstream.adaptive.manifest_type={channel["manifest_type"]}\n')
                
                entry_info = '#EXTINF:-1 '
                entry_info += f'tvg-id="{channel["tvg_id"]}" ' if channel['tvg_id'] else ''
                entry_info += f'tvg-name="{channel["tvg_name"]}" ' if channel['tvg_name'] else ''
                entry_info += f'tvg-shift="{channel["tvg_shift"]}" ' if channel['tvg_shift'] else ''
                entry_info += f'tvg-logo="{channel["logo_link"]}" ' if channel['logo_link'] else ''
                entry_info += f'group-title="{channel["titulo_grupo"]}",' if channel['titulo_grupo'] else ''
                entry_info += f'{channel["nome_canal"]}\n'

                f.write(entry_info)
                f.write(f'{channel["link_canal"]}\n')

def clear_entries():
    entry_nome_canal.delete(0, tk.END)
    entry_link_canal.delete(0, tk.END)
    entry_titulo_grupo.delete(0, tk.END)
    entry_tvg_id.delete(0, tk.END)
    entry_tvg_name.delete(0, tk.END)
    combo_tvg_shift.set("")  
    entry_logo_link.delete(0, tk.END)
    license_type_var.set("")  
    entry_license_key.delete(0, tk.END)
    manifest_type_var.set("")  

window = tk.Tk()
window.title("Criador de Playlist's M3U")
window.iconbitmap(r'favicon.ico')
window.resizable("false", "false")

def show_right_click_menu(event):
    right_click_menu.post(event.x_root, event.y_root)

right_click_menu = tk.Menu(window, tearoff=0)
right_click_menu.add_command(label="Cortar", command=lambda: window.focus_get().event_generate("<<Cut>>"))
right_click_menu.add_command(label="Copiar", command=lambda: window.focus_get().event_generate("<<Copy>>"))
right_click_menu.add_command(label="Colar", command=lambda: window.focus_get().event_generate("<<Paste>>"))

window.bind("<Button-3>", show_right_click_menu)

main_frame = tk.Frame(window, borderwidth=2, relief="groove")
main_frame.pack(padx=10, pady=10)

label_nome_canal = tk.Label(main_frame, text="Nome do Canal:")
label_nome_canal.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nome_canal = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_nome_canal.grid(row=0, column=1, padx=5, pady=5, ipady=6)

label_titulo_grupo = tk.Label(main_frame, text="Título do Grupo:")
label_titulo_grupo.grid(row=0, column=2, padx=5, pady=5, sticky="w")
entry_titulo_grupo = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_titulo_grupo.grid(row=0, column=3, padx=5, pady=5, ipady=6)

label_tvg_name = tk.Label(main_frame, text="EPG TVG Nome:")
label_tvg_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_tvg_name = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_tvg_name.grid(row=1, column=1, padx=5, pady=5, ipady=6)

label_tvg_shift = tk.Label(main_frame, text="EPG TVG Shift:")
label_tvg_shift.grid(row=1, column=2,padx=5, pady=5, sticky="W")
tvg_shift_values = ["", "-12", "-11", "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
combo_tvg_shift = ttk.Combobox(main_frame, values=tvg_shift_values,textvariable=tvg_shift_values, font=("Arial", 17), width=15, state="readonly")
combo_tvg_shift.grid(row=1, column=3, padx=5, pady=5)

label_tvg_id = tk.Label(main_frame, text="EPG TVG ID:")
label_tvg_id.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_tvg_id = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_tvg_id.grid(row=2, column=1, padx=5, pady=5, ipady=6)

label_logo_link = tk.Label(main_frame, text="Logo Link:")
label_logo_link.grid(row=2, column=2, padx=5, pady=5, sticky="w")
entry_logo_link = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_logo_link.grid(row=2, column=3, padx=5, pady=5, ipady=6)

label_link_canal = tk.Label(main_frame, text="Canal Link:")
label_link_canal.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_link_canal = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_link_canal.grid(row=3, column=1, padx=5, pady=5, ipady=6)
label_license_type = tk.Label(main_frame, text="License Type:")
label_license_type.grid(row=4, column=2, padx=5, pady=5, sticky="w")
license_types = ["", "clearkey", "com.widevine.alpha", "com.microsoft.playready", "org.w3.clearkey"]
license_type_var = tk.StringVar()
license_type_combobox = ttk.Combobox(main_frame, values=license_types, textvariable=license_type_var, font=("Arial", 10), width=28, state="readonly")
license_type_combobox.grid(row=4, column=3, padx=5, pady=5, ipady=6)
license_type_combobox.set("")
label_license_key = tk.Label(main_frame, text="Chave_Licensa:")
label_license_key.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_license_key = tk.Entry(main_frame, font=("Arial", 10), width=30)
entry_license_key.grid(row=4, column=1, padx=5, pady=5, ipady=6)
label_manifest_type = tk.Label(main_frame, text="Manifest Type:")
label_manifest_type.grid(row=3, column=2, padx=5, pady=5, sticky="w")
manifest_types = ["", "hls", "dash", "smooth", "progressive", "wv", "ismt", "rtmp", "m3u8", "mpd", "mp4", "ts", "flv"]
manifest_type_var = tk.StringVar()
manifest_type_combobox = ttk.Combobox(main_frame, values=manifest_types, textvariable=manifest_type_var, font=("Arial", 10), width=28, state="readonly")
manifest_type_combobox.grid(row=3, column=3, padx=5, pady=5, ipady=6)
manifest_type_combobox.set("")
button_add_channel = tk.Button(main_frame, text="        Adiconar Canal        ", command=on_add_channel)
button_add_channel.grid(row=5, column=1, padx=5, pady=10)

button_clear_fields = tk.Button(main_frame, text="Limpar", fg="red", command=on_clear_fields)
button_clear_fields.grid(row=5, column=3, padx=5, pady=10)

channel_info = tk.Text(window, height=15, width=79)
channel_info.pack(padx=10, pady=10)

channel_count_var = tk.StringVar()
channel_count_label = tk.Label(window, textvariable=channel_count_var, font=("Arial", 11))
channel_count_label.pack(pady=10)

button_generate_m3u = tk.Button(window, text="             Gerar  Playlist M3U             ", command=on_generate_m3u)
button_generate_m3u.pack(padx=10)

# Start the GUI event loop
window.mainloop()