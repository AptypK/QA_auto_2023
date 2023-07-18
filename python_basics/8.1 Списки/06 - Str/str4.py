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

print(
    "Користувач з ім'ям {}, віком {} проживає у країні {}".format(
        user["name"], user["age"], user["country"]
    )
)
