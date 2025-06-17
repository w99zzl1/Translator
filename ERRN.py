import tkinter as tk
from tkinter import scrolledtext, messagebox

eng_to_rus = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '?': ',', '&': '?',
}

rus_to_eng = {v: k for k, v in eng_to_rus.items()}

def convert_text(text, table):
    result = []
    for c in text:
        lower = c.lower()
        if lower in table:
            conv_char = table[lower]
            if c.isupper():
                result.append(conv_char.upper())
            else:
                result.append(conv_char)
        else:
            result.append(c)
    return ''.join(result)

def on_translate():
    text = txt_input.get("1.0", tk.END).rstrip()
    if not text.strip():
        messagebox.showwarning("Внимание", "Введите текст для перевода")
        return
    translated = convert_text(text, eng_to_rus)
    show_result(translated)

def on_reverse():
    text = txt_input.get("1.0", tk.END).rstrip()
    if not text.strip():
        messagebox.showwarning("Внимание", "Введите текст для перевода")
        return
    translated = convert_text(text, rus_to_eng)
    show_result(translated)

def show_result(text):
    result_window = tk.Toplevel(root)
    result_window.title("Перевод")
    result_window.geometry("600x400")
    result_window.configure(bg=bg_color)

    txt_output = scrolledtext.ScrolledText(result_window, wrap=tk.WORD,
                                           bg=bg_color, fg=text_color,
                                           insertbackground=text_color,
                                           font=font_text, relief=tk.FLAT,
                                           highlightthickness=4)
    txt_output.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    txt_output.insert(tk.END, text)
    txt_output.config(state=tk.DISABLED)

    animate_glow(txt_output, glow_colors_text)

# Цвета и шрифты (неоновый голубо-бирюзовый стиль)
bg_color = '#0f2027'
accent_color = '#00fff7'
text_color = '#a0f0f0'
button_color = '#04c9c9'
button_hover = '#00ffff'
font_title = ("Consolas", 14, "bold")
font_text = ("Consolas", 12)

root = tk.Tk()
root.title("Переводчик раскладки")
root.geometry("700x500")
root.configure(bg=bg_color)

lbl = tk.Label(root, text="Введите текст:", bg=bg_color, fg=accent_color, font=font_title)
lbl.pack(pady=(15,5))

txt_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15,
                                     bg='#001f27', fg=text_color,
                                     insertbackground=text_color,
                                     font=font_text, relief=tk.FLAT,
                                     highlightthickness=4)
txt_input.pack(expand=True, fill=tk.BOTH, padx=15)

btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(fill=tk.X, pady=15)

btn_translate = tk.Button(btn_frame, text="Перевести →",
                          font=font_title,
                          bg=button_color, fg=bg_color,
                          activebackground=button_hover,
                          activeforeground=bg_color,
                          relief=tk.FLAT, padx=20, pady=8,
                          cursor="hand2", command=on_translate)
btn_translate.pack(side=tk.RIGHT, padx=(5, 15))

btn_reverse = tk.Button(btn_frame, text="← Поменять",
                        font=font_title,
                        bg=button_color, fg=bg_color,
                        activebackground=button_hover,
                        activeforeground=bg_color,
                        relief=tk.FLAT, padx=20, pady=8,
                        cursor="hand2", command=on_reverse)
btn_reverse.pack(side=tk.RIGHT)

def on_enter(e):
    e.widget['background'] = button_hover

def on_leave(e):
    e.widget['background'] = button_color

btn_translate.bind("<Enter>", on_enter)
btn_translate.bind("<Leave>", on_leave)
btn_reverse.bind("<Enter>", on_enter)
btn_reverse.bind("<Leave>", on_leave)

glow_colors_text = ['#0ff7f7', '#00ffff', '#1af3f3', '#00ffff']

def animate_glow(widget, colors, delay=400, index=0, direction=1):
    widget.config(highlightbackground=colors[index], highlightcolor=colors[index])
    next_index = index + direction
    if next_index == len(colors) or next_index < 0:
        direction *= -1
        next_index = index + direction
    widget.after(delay, animate_glow, widget, colors, delay, next_index, direction)

animate_glow(txt_input, glow_colors_text, delay=500)

root.mainloop()
root.iconbitmap("icon.ico")