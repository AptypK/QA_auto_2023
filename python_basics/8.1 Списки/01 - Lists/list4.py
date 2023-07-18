# Course: QA Automation
# Week: 4
# Theme: Structured data types

# Modul 8. Structured data types
# Задача:
# Dev: Artur Kychenko
# Date: 06.04.2023

n = 5
gas_cost = []

for i in range(n):
    gas_arrears = float(input("Введіть заборгованість:"))
    gas_cost.append(round(gas_arrears, 2))

print(gas_cost)
