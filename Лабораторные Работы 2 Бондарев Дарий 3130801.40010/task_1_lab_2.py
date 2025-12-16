money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
n=0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

for x in range (1000):
    money_capital -= spend * ((1+increase)**x) - salary
    if money_capital > 0:
        n+=1
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", n)
