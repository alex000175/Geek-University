p = float(input("Введите число размер выручки в рублях:"))
m = float(input("Введите число размер издержек в рублях:"))

if p > m:
    print(f"прибыль — выручка больше издержек на {p - m:.2f} руб.")
    print(f"рентабельность {(p - m) / p*100:.2f} %")
    с = int(input("Введите число сотрудников:"))
    print(f"прибыль из расчета на 1 сотрудника составляет {(p - m) / с:.2f} руб.")
else:
    print(f"убыток — издержки больше выручки на {m - p:.2f} руб.")

