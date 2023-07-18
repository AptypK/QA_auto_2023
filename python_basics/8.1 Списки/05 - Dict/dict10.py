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
}
years_old = user.get("years_old")
if years_old is None:
    print("Ключ years_old відсутній")
else:
    print(years_old)

if "years_old" in user:
    print(years_old)
else:
    print("Ключ years_old відсутній")

print(years_old)
