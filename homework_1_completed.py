import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Пункт 1
# Завантажте датасет за вашим вибором (наприклад, датасет "Tips" або "Planets" з Seaborn або інший публічний датасет).
# tips_dataset = sns.load_dataset("tips")
# print(tips_dataset.head())

# Пункт 2
# Побудуйте графік розподілу кількості споживачів/даних за певний параметр (наприклад, вік, вартість тощо).
# tips_dataset = sns.load_dataset("tips")
#
# sns.histplot(tips_dataset['total_bill'], kde=True)
#
# plt.title('Розподіл вартості столів')
# plt.xlabel('Вартість')
# plt.ylabel('Кількість споживачів')
#
# plt.show()

# Пункт 3
# Побудуйте графіки залежності між різними параметрами.
# tips_dataset = sns.load_dataset("tips")
#
# sns.scatterplot(x='total_bill', y='tip', data=tips_dataset)
#
# plt.title('Залежність між вартістю столу та чайовими')
# plt.xlabel('Вартість столу')
# plt.ylabel('Чайові')
#
# plt.show()

# Пункт 4
# Визначте і виведіть статистичні показники (середнє, медіану, дисперсію тощо) для вибраних параметрів.
# data = pd.DataFrame({'параметр': [10, 15, 20, 25, 30, 35, 40, 45, 50]})
#
# average = data['параметр'].mean()
# median = data['параметр'].median()
# dispersion = data['параметр'].var()
# standard_deviation = round(data['параметр'].std(), 2)
#
# print(f'Середнє: {average}')
# print(f'Медіана: {median}')
# print(f'Дисперсія: {dispersion}')
# print(f'Стандартне відхилення: {standard_deviation}')
#
# sns.histplot(data=data, x='параметр', kde=True)
#
# plt.title('Гістограма розподілу параметра')
# plt.xlabel('Значення параметра')
# plt.ylabel('Частота')
# plt.show()

# Пункт 5
# Реалізуйте програму, яка запитує користувача про введення цілого числа.
# Використовуючи конструкцію try-except, обробте виняток, якщо користувач введе не ціле число. Виведіть повідомлення про помилку та попросіть користувача ввести ціле число знову.
# Повторюйте запит користувачу до того часу, поки він не введе коректне ціле число.
# Виведіть на екран повідомлення з введеним цілим числом та подякуйте користувачу за співпрацю.

# while True:
#     try:
#         number = int(input('Будь ласка введіть число: '))
#         break
#     except ValueError:
#         print('Ви ввели не вірне число! Введіть коректне ціле число')
#
# print(f'Ви ввели коректне число: {number}')
# print('Дякуємо за співпрацю!')

# Пункт 6
# Реалізуйте програму-калькулятор, яка дозволяє користувачу вводити математичні вирази (наприклад, "2 + 3", "5 * 4", "10 / 2" тощо).
#
# Використовуючи конструкцію try-except, обробте виняток, якщо користувач введе некоректний вираз або вираз, що містить помилку.
#
# При виникненні помилки, виведіть повідомлення про помилку та попросіть користувача ввести вираз знову.

# Виконайте обчислення виразу та виведіть результат на екран.
# Повторюйте процес запиту та обчислення виразів до того часу, поки користувач не вибере вийти з програми.

# Сверху був занадто поганий калькулятор напевно писав якись недосвідчений девелопер
# ось калькулятор покраще того.
# Ps: не хочу щоб мені вінду видалили)
def accounts(example):
    try:
        symbol = "+-*/"
        operations = []
        numbers = []
        temp = ""

        for x in example:
            if x in symbol:
                operations.append(x)
                numbers.append(float(temp))
                temp = ""
            else:
                temp += x

        numbers.append(float(temp))

        result = numbers[0]
        for i in range(1, len(numbers)):
            if operations[i - 1] == "+":
                result += numbers[i]
            elif operations[i - 1] == "-":
                result -= numbers[i]
            elif operations[i - 1] == "*":
                result *= numbers[i]
            elif operations[i - 1] == "/":
                if numbers[i] == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе")
                result /= numbers[i]

        return result

    except (ValueError, ZeroDivisionError):
        raise ValueError("Помилка у виразі. Будь ласка, введіть коректний вираз.")


while True:
    try:
        user_input = input("Введіть математичний вираз (або 'вийти' для виходу): ")
        if user_input.lower() == 'вийти':
            break

        result = accounts(user_input)
        print(f"Результат: {result}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Помилка: {e}")

    except KeyboardInterrupt:
        print("\nСкасовано користувачем.")

print("Дякуємо за користування програмою калькулятор!")
