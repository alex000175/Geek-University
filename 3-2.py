# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой

def info_about_people(name, surname, date_of_birth, city, email, phone):
    print (f"Пользователь:".ljust(17) + f"{name.title()} {surname.title()}")
    print(f"Дата рождения:".ljust(17) + f"{date_of_birth}")
    print(f"Город:".ljust(17) + f"{city.title()}")
    print(f"e-mail:".ljust(17) + f"{email}")
    print(f"телефон:".ljust(17) + f"{phone}")

info_about_people(name="Alex", surname="Black", date_of_birth = "10.10.2010", city="Moskow", email="alex@mail.ru", phone="999-888-77-66")