sym = ['С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш']
code = ['000000', '010101', '100110', '110011', '111000', '101101', '011110', '001011']


def checkDistance(a: str, b: str):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return str(distance)


distances = []
distances.append(['+'] + sym)  # первая строка (верхняя часть рамки таблицы
for i in range(len(sym)):
    distances.append([sym[i]] + ['-'] * len(sym))  # следующие строки (боковая часть рамки таблицы + пустые '-')

for i in range(len(sym)):
    for j in range(i + 1, len(sym)):
        distances[i + 1][j + 1] = checkDistance(code[i], code[j])  # заполняем таблицу расстояниями

for i in range(len(distances)):  # вывод таблицы
    print(distances[i])



def findDistancesWith(given: str):
    for i in range(len(code)):
        d = checkDistance(code[i], given)
        print(f'{sym[i]}: d({code[i]}, {given}) = {d}')

findDistancesWith('011100')
