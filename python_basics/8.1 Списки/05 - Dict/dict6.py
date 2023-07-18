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

key_list = user.keys()
print(key_list)
print("age" in key_list)

del user["age"]
print(key_list)
print("age" in key_list)
