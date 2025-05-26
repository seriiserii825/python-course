def matreshka():
    def test(n): 
        if n == 1:
            print("Matreoshka")
        else:
            print(f"Вверх матрешки {n}")
            test(n - 1)
            print(f"Низ матрешки {n}")

    n = int(input("Введите количество матрешек: "))
    if n <= 0:
        print("Количество матрешек должно быть положительным числом.")
    else:
        test(n)
