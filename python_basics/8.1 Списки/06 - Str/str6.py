# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# Задача:
# Dev: Artur Kychenko
# Date: 08.04.2023

str1 = "Слава Україні!"
ch = input("Символ або слово для перевірки наявності ")

if ch in str1:
    print(f"Символ або слово {ch} присутній У рядку {str1}")
else:
    print(f"Символ або слово {ch} відсутній у рядку {str1}")
