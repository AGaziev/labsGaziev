string = 'aaaaadggggggggggggggghtyiklooooop'


def RLE(a: str):
    a = splitter(a)  # делит на подстроки ['aaaaa', 'd', 'ggggggggggggggg', 'h', 't', 'y', 'i', 'k', 'l', 'ooooo', 'p']
    result = ''
    i = 0
    while i < len(a):
        part = ''
        if len(a[i]) > 1:  # если в подстроке больше одного символа
            part = f' {len(a[i])} {a[i][0]}'
            result += part  # итог в результат
            i += 1
        else:  # если ровно один символ
            counter = 0
            while i < len(a) and len(a[i]) == 1:  # то находим еще идущие следом подстроки с одним символом
                counter += 1  # увеличиваем счетчик этих подстрок
                part += ' ' + a[i][0]  # и добавляем их в список "неповторяющихся данных"
                i += 1
            result += f' 0 {counter}{part}'  # итог в результат
    print(result)


def splitter(a: str):
    result = []
    string = ''
    for i in range(len(a)):
        string += a[i]
        if (i + 1) == len(a) or a[i] != a[i + 1]:
            result.append(string)
            string = ''
    return result


RLE(string)
