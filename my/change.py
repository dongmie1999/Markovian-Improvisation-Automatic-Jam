import musthe


# def change(num, key, mode, count=3):
#     d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
#     result = []
#     if type(num) == int and 0 < num < 8:
#         s = musthe.Scale(musthe.Note(key), mode)
#         scale = []
#         for i in range(len(s)):
#             scale.append(str(s[i]))
#         for i in range(count):
#             result.append(d[scale[(num - 1 + 2 * i) % 7]])
#     else:
#         raise TypeError('num should be int from 1~7.')
#     return result

def change(num, key, mode, count=3):
    """
    change the chord from number to str.
    example: in C major, 1 change to ['C', 'E', 'G']
    :param num: the progression number, should be int from 1~7.
    :param key: char, the first note of scale，could be C D E F G A B.
    :param mode: see doc of class Impromptu.
    :param count: default 3, could be 3, 4 or 5, corresponding triad， seventh chord and hord of the ninthc.
    :return:
    """
    d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
    result = []
    try:
        if type(num) == int and 0 < num < 8:
            s = musthe.Scale(musthe.Note(key), mode)
            scale = []
            for i in range(len(s)):
                scale.append(str(s[i]))
            for i in range(count):
                result.append(d[scale[(num - 1 + 2 * i) % 7]])
        else:
            raise TypeError('num should be int from 1~7.')
    except NameError:
        return change(num, key, mode='aeolian', count=count)
    return result

print(change(4, 'C', 'major'))
