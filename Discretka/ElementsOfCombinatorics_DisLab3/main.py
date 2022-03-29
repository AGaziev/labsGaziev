n, m = 13, 16
ways = 0


def numberOfWays():
    arr = [[0 for i in range(m + 1)] for j in range(n + 1)]  # матрица количества путей
    arr[1][1] = 1  # в ячейку 1,1 можно прийти одним путем
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # пропускаем первый элемент
                continue
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]  # динамически заполняем матрицу
    return arr


def numberOfWaysWithCond():
    arr = [[0 for i in range(m + 1)] for j in range(n + 1)]
    arr[1][1] = 1
    arr[1][0] = 1  # корректировка количества путей в 2,1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # пропускаем первый элемент
                continue
            arr[i][j] = arr[i - 1][j - 1] + arr[i][j - 1]  # динамически заполняем матрицу
    return arr


def combinationsNum():
    word = "КОМБИНАТОРИКА"
    word = list(word)  # разделяем слово на буквы
    combination = set()  # множество трехбуквенных слов (неповторяющихся)
    for i in range(len(word)):
        for j in range(len(word)):
            for k in range(len(word)):
                if i == k or i == j or j == k:  # исключаем излишнее повторение букв
                    continue
                combination.add(word[i] + word[j] + word[k])  # составляем слова из трех букв перебором
    print('Без повторений букв: ', len(combination))


def recurrentGet(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return int(4 * recurrentGet(n - 1) - 13 * recurrentGet(n - 2))


def getByFormula(n):
    return 1 / 2 * ((2 + 3j) ** n + (2 - 3j) ** n)


def main():
    print(f"Общее решение: {getByFormula(100)}")
    print(f"Реккурентная формула: {getByFormula(100)}")
    combinationsNum()
    arr = numberOfWays()
    for i in reversed(arr[1:]):
        for j in i[1:]:
            print(j, end=" ")
        print()
    arr = numberOfWaysWithCond()
    for i in reversed(arr[1:]):
        for j in i[1:]:
            print(j, end=" ")
        print()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
