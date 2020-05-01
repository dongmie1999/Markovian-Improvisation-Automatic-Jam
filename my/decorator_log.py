# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value < 0:
#             raise ValueError('width must be a positive number.')
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value < 0:
#             raise ValueError('height must be a positive number.')
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self.width * self.height
#
#
# s = Screen()
# s.height = 20
# s.width = 40
# print(s.resolution)
# s.resolution = 1

# recipes = {
#     'maj': ['P1', 'M3', 'P5'],
#     'min': ['P1', 'm3', 'P5'],
#     'aug': ['P1', 'M3', 'A5'],
#     'dim': ['P1', 'm3', 'd5'],
#     'dom7': ['P1', 'M3', 'P5', 'm7'],
#     'min7': ['P1', 'm3', 'P5', 'm7'],
#     'maj7': ['P1', 'M3', 'P5', 'M7'],
#     'aug7': ['P1', 'M3', 'A5', 'm7'],
#     'dim7': ['P1', 'm3', 'd5', 'd7'],
#     'm7dim5': ['P1', 'm3', 'd5', 'm7'],
#     'sus2': ['P1', 'P5', 'P8', 'M2'],
#     'sus4': ['P1', 'P5', 'P8', 'P4'],
#     'open5': ['P1', 'P5', 'P8'],
# }
# aliases = {
#     # 'M': 'maj',
#     'm': 'min',
#     '+': 'aug',
#     '°': 'dim',
#     '7': 'dom7',
#     'm7': 'min7',
#     'M7': 'maj7',
#     '+7': 'aug7',
#     '7aug5': 'aug7',
#     '7#5': 'aug7',
#     '°7': 'm7dim5',
#     'ø7': 'm7dim5',
#     'm7b5': 'm7dim5',
# }
# valid_types = list(recipes.keys()) + list(aliases.keys())

# d = {'major':       [0, 2, 2, 1, 2, 2, 2, 1],
#      'dorian':      [0, 2, 1, 2, 2, 2, 1, 2],
#      'phrygian':    [0, 1, 2, 2, 2, 1, 2, 2],
#      'lydian':      [0, 2, 2, 2, 1, 2, 2, 1],
#      'mixolydian':  [0, 2, 2, 1, 2, 2, 1, 2],
#      'minor':       [0, 2, 1, 2, 2, 1, 2, 2],
#      'locrian':     [0, 1, 2, 2, 1, 2, 2, 2]}
#
# aliases = {'Ionian': 'major'}
#
# ip = 'Ionian'
# key = ip.lower()
# try:
#     print(d[key])
# except KeyError:  # not in d
#     try:
#         print(d[aliases[key]])
#     except KeyError:  # not in aliases
#         raise KeyError('Can not find your mode. Please check your key.')

# def fun():
#     print("fun")
#     def fun_in():
#         print("fun_in")
#         return fun_in
#     return fun_in
#
# var = fun()
# var()

import logging
from functools import wraps


def decorator_log(fun):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./test.log',
                        filemode='w')

    @wraps(fun)
    def fun_in(*args, **kwargs):
        logging.debug("{} start.".format(fun.__name__))
        fun(*args, **kwargs)
        logging.debug("{} end.".format(fun.__name__))

    return fun_in


# @decorator_log
# def real_fun(content):
#     print(content)
#
#
# real_fun('aaa')
# print(real_fun.__name__)
