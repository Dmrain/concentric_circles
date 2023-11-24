import tkinter as tk


# функция add_circle() создает новую окружность с использованием
# метода create_oval и добавляет ее на холст в центре.
def add_circle():
    global radius
    circles.append(canvas.create_oval(center_x - radius, center_y - radius,
                                      center_x + radius, center_y + radius, outline="black"))
    radius -= min(hx, hy)

# функция remove_circle() удаляет последнюю
# нарисованную окружность с холста.
def remove_circle():
    global radius
    if circles:
        canvas.delete(circles.pop())
        radius += min(hx, hy)

# on_key_press(event) - функция-обработчик событий клавиатуры.
def on_key_press(event):
    if event.keysym == 'Return':
        add_circle()
    elif event.keysym == 'd':
        remove_circle()
    elif event.keysym == 'Escape':
        root.destroy()

root = tk.Tk()
root.title('Концентрические окружности')
width, height = 700, 450
center_x, center_y = width // 2, height // 2
radius = 200  # начальный радиус
hx, hy = 10, 10  # шаги уменьшения радиуса по x и y

canvas = tk.Canvas(root, width=width, height=height, bg='white')
canvas.pack()

circles = []

root.bind('<KeyPress>', on_key_press)

root.mainloop()
