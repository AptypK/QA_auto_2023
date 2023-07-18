# Course: QA Automation
# Week: 4
# Theme: Structured data types
# Modul 8. Structured data types
# Cotrol task: 8.11
# Dev: Artur Kychenko
# Date: 09.04.2023


text_input = input("Введіть текст:")

# your code goes here
if (
    "Ы" in text_input.upper()
    or "Ъ" in text_input.upper()
    or "Ё" in text_input.upper()
    or "Э" in text_input.upper()
):
    print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
else:
    print("Дякуємо за замовлення!")
