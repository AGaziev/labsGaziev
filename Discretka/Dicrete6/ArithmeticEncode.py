def floatToBin(x, eps=1e-9): # перевод в бинарный вид
    res = ''
    while x > eps:
        x *= 2
        res += str(int(x))
        x -= int(x)
    return res


def binToFloat(x): # перевод из бинарного
    return sum(2 ** (-i - 1) for i, digit in enumerate(x) if digit == '1')


def findCode(a, b):
    i = 0
    a += '0' * (len(b) - len(a))
    while a[i] == b[i]:
        i += 1
    res = a[:i] + '0'
    cnt = 0
    while a[i] == 1:
        i += 1
        cnt += 1
    res += '1' * (cnt + 1)
    return res


def encoding(word, alphabet, p):
    left, right = 0, 1
    for letter in word:
        i = alphabet.index(letter)
        left, right = (left + (right - left) * sum(p[:i]), left + (right - left) * sum(p[:i + 1]))
    return findCode(*map(floatToBin, (left, right)))


def decoding(code, length, alphabet, freq):
    code = binToFloat(code)
    word = ''
    left, right = 0, 1
    for _ in range(length):
        for i, letter in enumerate(alphabet):
            interval = (left + (right - left) * sum(freq[:i]), left + (right - left) * sum(freq[:i + 1]))
            if interval[0] <= code < interval[1]:
                word += letter
                code = (code - interval[0]) / (interval[1] - interval[0])
                break
    return word


alphabet = 'aecdfb'
freq = (0.05, 0.10, 0.05, 0.55, 0.15, 0.10)
word = 'eacdbf'
code = encoding(word, alphabet, freq)
print(code)
print(decoding(code, len(word), alphabet, freq))
