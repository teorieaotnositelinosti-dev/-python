import tkinter as tk
from tkinter import messagebox
import random
import os


try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("Библиотека Pillow не найдена. Фон будет черным.")

try:
    import pygame
    HAS_AUDIO = True
except ImportError:
    HAS_AUDIO = False
    print("Библиотека pygame не найдена. Музыки не будет.")

class BulletstormKeygen:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulletstorm - Skillshot Edition Keygen")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        
        self.color_bg = "#1a1a1a"       
        self.color_fg = "#ff5e00"       
        self.color_text = "#ffffff"     
        self.color_btn = "#333333"      
        
        
        self.canvas = tk.Canvas(root, width=600, height=450, bg=self.color_bg, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.load_background()
        self.play_music()

        
        
        
        self.canvas.create_text(300, 40, text="BULLETSTORM", font=("Impact", 32), fill=self.color_fg)
        self.canvas.create_text(300, 75, text="KEY GENERATOR v1.0", font=("Arial", 10, "bold"), fill="white")

        
        self.lbl_input = tk.Label(root, text="ENTER 6 DIGITS (DEC):", bg="black", fg=self.color_fg, font=("Consolas", 10, "bold"))
        self.lbl_input_window = self.canvas.create_window(300, 270, window=self.lbl_input)
        
        self.entry_code = tk.Entry(root, font=("Consolas", 16), justify='center', bg="#111", fg="white", insertbackground='orange')
        self.entry_window = self.canvas.create_window(300, 300, window=self.entry_code, width=200)
        
        
        self.key_var = tk.StringVar()
        self.key_var.set("XXXXX-XXXXX XXXX")
        self.lbl_key = tk.Label(root, textvariable=self.key_var, font=("Consolas", 20, "bold"), bg="black", fg="#00ff00")
        self.lbl_key_window = self.canvas.create_window(300, 350, window=self.lbl_key)

        
        self.btn_gen = tk.Button(root, text="KILL WITH SKILL (GENERATE)", font=("Impact", 14), 
                                 bg=self.color_fg, fg="black", activebackground="white", activeforeground="black",
                                 command=self.generate_key, cursor="hand2")
        self.btn_gen_window = self.canvas.create_window(300, 400, window=self.btn_gen, width=300, height=40)

        
        self.hue = 0
        self.animate_text()

    def load_background(self):
        """Загрузка изображения bg.jpg или bg.png"""
        if not HAS_PIL:
            return

        image_path = None
        if os.path.exists("bg.jpg"): image_path = "bg.jpg"
        elif os.path.exists("bg.png"): image_path = "bg.png"

        if image_path:
            try:
                pil_image = Image.open(image_path)
                
                pil_image = pil_image.resize((600, 450), Image.Resampling.LANCZOS)
                self.bg_image = ImageTk.PhotoImage(pil_image)
                self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
                
                self.canvas.create_rectangle(50, 250, 550, 430, fill="#000000", stipple="gray50") 
            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")

    def play_music(self):
        """Запуск 8-bit музыки"""
        if HAS_AUDIO and os.path.exists("music.mp3"):
            try:
                pygame.mixer.init()
                pygame.mixer.music.load("music.mp3")
                pygame.mixer.music.play(-1) 
                pygame.mixer.music.set_volume(0.3)
            except Exception as e:
                print(f"Ошибка аудио: {e}")

    def generate_key(self):
        """
        ВАРИАНТ 10:
        Ввод: 6 цифр (DEC).
        1 блок: цифры 4,5,6 введенного числа + рандом буквы (всего 5 знаков).
        2 блок: цифры 1,2,3 введенного числа + рандом буквы (всего 5 знаков).
        3 блок: Сумма чисел, получившихся в блоке 1 и 2 (паддинг до 4 знаков).
        """
        input_str = self.entry_code.get().strip()

        
        if not input_str.isdigit() or len(input_str) != 6:
            messagebox.showerror("Error", "Введите ровно 6 цифр (0-9)!")
            return

        
        digits_block2 = input_str[0:3] 
        
        
        digits_block1 = input_str[3:6] 

        
        def get_random_letters(n):
            return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=n))

        
        part1_str = digits_block1 + get_random_letters(2)
        
        
        part2_str = digits_block2 + get_random_letters(2)

        
        val1 = int(digits_block1)
        val2 = int(digits_block2)
        total_sum = val1 + val2
        part3_str = f"{total_sum:04d}" 

        
        full_key = f"{part1_str}-{part2_str} {part3_str}"
        
        self.key_var.set(full_key)

    def animate_text(self):
        """Анимация цвета сгенерированного ключа (RGB эффект)"""
        
        colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8b00ff"]
        current_color = colors[self.hue % len(colors)]
        
        
        self.lbl_key.config(fg=current_color)
        
        self.hue += 1
        self.root.after(200, self.animate_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BulletstormKeygen(root)
    root.mainloop()