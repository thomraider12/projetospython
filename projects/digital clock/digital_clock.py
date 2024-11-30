import tkinter as tk
import time

# Create the main window
relogio = tk.Tk()

# Create a label to display the clock
texto_relogio = tk.Label(relogio, font=('Monocraft', 180), fg='#000', bg='#cae000')
texto_relogio.pack(fill='both', expand=True)

# Function to update the clock
def atualizar_relógio():
    tempo_atual = time.strftime('%H:%M:%S')
    texto_relogio.config(text=tempo_atual)
    relogio.after(1, atualizar_relógio)

# Make the window full screen
relogio.attributes('-fullscreen', True)

# Start the clock
atualizar_relógio()

# Run the application
relogio.mainloop()