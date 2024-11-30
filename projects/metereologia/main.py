import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()
    api_key = "f8384fde9ec0f3edba0b8d0244ec8c8d" #go to openweather 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt"

    # Show loading state
    weather_label.config(text="A carregar...")
    icon_label.config(image='')

    response = requests.get(url)
    weather_data = response.json()
    if "message" in weather_data:
        messagebox.showerror("Erro", weather_data["message"])
    else:
        weather_text = f"Cidade: {city}\n"
        weather_text += f"Temperatura: {weather_data['main']['temp']}°C\n\n"
        weather_text += f"Pressão: {weather_data['main']['pressure']} hPa\n"
        weather_text += f"Humidade: {weather_data['main']['humidity']}%\n"
        weather_text += f"Min Temp: {weather_data['main']['temp_min']}°C\n"
        weather_text += f"Máx Temp: {weather_data['main']['temp_max']}°C\n"
        weather_text += f"Vento: {weather_data['wind']['speed']} m/s\n"
        weather_text += f"Descrição: {weather_data['weather'][0]['description']}\n"
        weather_text += f"Nascer do Sol: {weather_data['sys']['sunrise']}\n"
        weather_text += f"Pôr do Sol: {weather_data['sys']['sunset']}\n"
        weather_label.config(text=weather_text, font="Monocraft")
        

        #update icon
        icon_name = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_name}@2x.png"
        icon_data = requests.get(icon_url)
        with open("icon.png", "wb") as f:
           f.write(icon_data.content)
        icon_image = ImageTk.PhotoImage(Image.open("icon.png"))
        icon_label.config(image=icon_image)
        icon_label.image = icon_image


root = tk.Tk()
root.title("Metereologia")
root.geometry("1200x900")

# Create gradient image
gradient = Image.new("RGBA", (1, root.winfo_height()), "#8EC5FC")
pixels = gradient.load()
for y in range(gradient.size[1]):
    color = int(y / gradient.size[1] * 255), 140, 255
    for x in range(gradient.size[0]):
        pixels[x, y] = color
gradient = gradient.resize((root.winfo_width(), root.winfo_height()))
gradient = ImageTk.PhotoImage(gradient)


#Set gradient image as background
bg_label = tk.Label(root, image=gradient)
bg_label.place(relx=0, rely=0, relheight=1, relwidth=1)

# Frame
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Entry
city_entry = tk.Entry(frame, font=("Courier", 14))
city_entry.place(relwidth=0.65, relheight=1)
city_entry.insert(0, "")

# Get Weather button
get_weather_button = tk.Button(frame, text="Obter Previsão", font=("Courier", 12), command=get_weather)
get_weather_button.place(relx=0.7, relwidth=0.3, relheight=1)

# Weather label
weather_frame = tk.Frame(root, bg='#80c1ff', bd=10)
weather_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.5, anchor='n')
weather_label = tk.Label(weather_frame, font=("Courier", 14), justify='left', bd=5)
weather_label.place(relwidth=1, relheight=1)

# Weather icon
icon_frame = tk.Frame(weather_frame, bg='#80c1ff')
icon_label = tk.Label(icon_frame)
icon_label.place(relx=0.5, rely=0.5, anchor='center')
icon_frame.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4, anchor='n')

root.mainloop()