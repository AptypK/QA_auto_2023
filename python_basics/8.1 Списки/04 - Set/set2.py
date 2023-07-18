# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# Задача:
# Dev: Artur Kychenko
# Date: 08.04.2023

countries = {"Ukraine", "Poland"}
print(countries)

print("Ukraine" in countries)
print("US" in countries)

if "Ukraine" in countries:
    print("Україна є в переліку країн")
else:
    print("України немає в переліку країн")

if "US" in countries:
    print("Сполучені Штати є в переліку країн")
else:
    print("Сполучених Штатів немає в переліку країн")
