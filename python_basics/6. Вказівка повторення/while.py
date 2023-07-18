# Курс: Prometheus - QA Automation
# Тиждень: 3
# Тема: Вказівка повторення (Вивчення циклів)

# Задача на розрахунку терміну вкладу, для отримання бажаної суми накопичення

deposit_amount = float(input(print("Введіть суму депозиту:")))
annual_rate = float(input(print("Введіть річну відсоткову ставку:")))
desired_amound = float(input(print("Введіть бажану суму накопичення:")))

deposit_period = 0

while deposit_amount < desired_amound:
    deposit_period += 1
    deposit_amount = deposit_amount + deposit_amount * (annual_rate / 100)

print("Очікуваний термін депозиту:", deposit_period, " років")
print("сума заощаджень:", round(deposit_amount, 2), "грн")
