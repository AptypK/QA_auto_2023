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
print(user)
print(user["age"])

print(user["profession"])
user["profession"] = "Automation OA"
print(user["profession"])
key = "country"
print(user[key])
user[key] = "Ukraine, Poland"
print(user[key])
print(user.get(key))
