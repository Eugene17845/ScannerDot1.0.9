import tkinter as tk
from tkinter import messagebox
from PIL.ImageChops import difference


def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        if num2 > num1:
            difference_gz = num2 - num1
            average_gz = min(num1,num2) + (difference_gz/2)
            lambda_gz = 299792458 / (average_gz * 1000000)
            points = num3 / round(lambda_gz / 2, 3)
            points_gz = difference_gz / num4

            result_label.config(text=f"Расстояние(М): {round(4 * lambda_gz, 3)}")
            result_points.config(text=f"Точки(поле): {round(points, 1)}")
            result_points_gz.config(text=f"Точки(частота): {round(points_gz, 1)}")
        else:
            difference_gz = num1 - num2
            average_gz = min(num1, num2) + (difference_gz / 2)
            lambda_gz = 299792458 / (average_gz * 1000000)
            points = num3 / round(lambda_gz / 2, 3)
            points_gz = num4 / lambda_gz

            result_label.config(text=f"Расстояние(М): {round(4 * lambda_gz, 3)}")
            result_points.config(text=f"Точки(поле): {round(points, 1)}")
            result_points_gz.config(text=f"Точки(частота): {round(points_gz, 1)}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа")


root = tk.Tk()
root.title("СканерТЧК")
root.resizable(width=False, height=False)

tk.Label(root, text="Первая частота(МГц):").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Вторая частота(МГц):").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Поле(М):").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Шаг(МГц):").grid(row=3, column=0, padx=10, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=5)

subtract_button = tk.Button(root, text="Вычислить", command=subtract)
subtract_button.grid(row=4, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Расстояние(М): ")
result_label.grid(row=5, column=0, columnspan=1)

result_points = tk.Label(root, text="Точки(поле): ")
result_points.grid(row=6, column=0, columnspan=1)

result_points_gz = tk.Label(root, text="Точки(частота): ")
result_points_gz.grid(row=7, column=0, columnspan=1)


root.mainloop()