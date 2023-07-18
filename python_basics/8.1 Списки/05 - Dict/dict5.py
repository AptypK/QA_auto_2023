# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# Задача:
# Dev: Artur Kychenko
# Date: 08.04.2023
user = {
    "name": "Sergii",
    "age": 100500,
    "profession": "Golf Player",
    "country": "Ukraine",
}

if "name" in user:
    print(user["name"])
else:
    print("Ключа не має в словнику")

if "company" in user:
    print(user["company"])
else:
    print("Ключа не має в словнику")
