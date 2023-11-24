import unittest
import tkinter as tk

class TestCanvasFunctions(unittest.TestCase):
    def test_add_and_remove_circle(self):
        root = tk.Tk()
        width, height = 700, 450
        canvas = tk.Canvas(root, width=width, height=height, bg='white')
        canvas.pack()

        radius = 50  # Пример радиуса окружности

        # Добавление окружности
        circle_id = canvas.create_oval(width // 2 - radius, height // 2 - radius,
                                       width // 2 + radius, height // 2 + radius, outline="black")

        self.assertTrue(circle_id is not None)  # Проверка, что объект окружности создан

        # Удаление окружности
        canvas.delete(circle_id)

        # Проверка, что окружность удалена
        self.assertEqual(len(canvas.find_all()), 0)  # Проверка, что на холсте больше нет объектов

        root.destroy()  # Закрытие окна

if __name__ == '__main__':
    unittest.main()
