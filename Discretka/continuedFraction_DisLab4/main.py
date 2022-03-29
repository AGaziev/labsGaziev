import math


def nod(m, n):
    return m if n == 0 else nod(n, m % n)


def EuclidToLinear(a, b, c):
    assert c != 0  # проверка на неправильные данные
    nodAB = nod(abs(a), abs(b))  # наибольший общий делитель
    if c % nodAB:
        print("Уравнение не имеет решений")
    else:
        a //= nodAB  # получаем целочисленные значения от деления на НОД
        b //= nodAB
        c //= nodAB
        for k in range(abs(a)):  # перебор всех целых значений а
            if (c - b * k) % a == 0:  # можно ли подобрать b целое
                y = k
                x = (c - b * y) // a
                print("x =", x, "y =", y)
                break
        else:
            print("Неудача")


def solvePell(n):
    x = int(math.sqrt(n))
    y, z, r = x, 1, x << 1
    print(y,z,r,x)
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z
        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r
        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return a, b


def main():
    print("Solve Ax+By=C in integers:")
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))
    EuclidToLinear(a, b, c)
    print(solvePell(10612))


if __name__ == '__main__':
    main()
