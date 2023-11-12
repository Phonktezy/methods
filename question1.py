#1
# class Robot:
#
#     COORDS_MAX = 20
#     COORDS_MIN = -20
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def left(self):
#         if self.x > Robot.COORDS_MIN:
#             self.x -= 1
#             print(f'x = {self.x}, y = {self.y}')
#
#     def right(self):
#         if self.x < Robot.COORDS_MAX:
#             self.x += 1
#             print(f'x = {self.x}, y = {self.y}')
#
#     def up(self):
#         if self.y > Robot.COORDS_MIN:
#             self.y -= 1
#             print(f'x = {self.x}, y = {self.y}')
#
#     def down(self):
#         if self.y < Robot.COORDS_MAX:
#             self.y += 1
#             print(f'x = {self.x}, y = {self.y}')
#
#     def move(self, message):
#         for i in message:
#             if i == 'N':
#                 self.up()
#             elif i == 'S':
#                 self.down()
#             elif i == 'W':
#                 self.left()
#             else:
#                 self.right()
#2
# class Snow:
#
#     def __init__(self, num):
#         self.num = num
#
#     def makeSnow(self, snow):
#
#         for i in range(self.num // snow ):
#             print('*' * snow)
#
#         print('*' * (self.num % snow))
#
#     def __add__(self, other):
#         if not isinstance(other, (Snow, int)):
#             raise TypeError('error')
#         if not isinstance(other, int):
#             return Snow(self.num + other)
#         else:
#             return Snow(self.num + other.num)
#
#     def __sub__(self, other):
#         if not isinstance(other, (Snow, int)):
#             raise TypeError('error')
#         if not isinstance(other, int):
#             return Snow(self.num - other)
#         else:
#             return Snow(self.num - other.num)
#
#     def __mul__(self, other):
#         if not isinstance(other, (Snow, int)):
#             raise TypeError('error')
#         if not isinstance(other, int):
#             return Snow(self.num * other)
#         else:
#             return Snow(self.num * other.num)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, (Snow, int)):
#             raise TypeError('error')
#         if not isinstance(other, int):
#             return Snow(self.num / other)
#         else:
#             return Snow(self.num / other.num)
#
# num = Snow(112)
# num.makeSnow(10)
# num = num + 100
# num.makeSnow(10)
# pip = Snow(15)
# num = num + pip
# num.makeSnow()
# num.makeSnow(13)
#3
# class SnowFlake:
#
#     def __init__(self, number):
#         self.number = number
#
#     def snow(self):
#         k = 0
#         st = ''
#         for i in range(self.number):
#             for j in range(self.number):
#                 if j == k or j == k + 1:
#                     st += '*'
#                 elif self.number - j == k + 1 or self.number - j == k + 2:
#                     st += '*'
#                 elif j == self.number // 2:
#                     st += '*'
#                 elif i == self.number // 2:
#                     st += '*'
#                 else:
#                     st += ' '
#             print(st)
#             st = ''
#             k += 1
#
#     def thaw(self):
#         self.number = self.number - 2
#
#     def frezee(self):
#         self.number = self.number * 2
#
# s = SnowFlake(11)
# s.snow()
# s.thaw()
# s.frezee()
#4
class Talking:

  def __init__(self, name, yes_count = 0, no_count = 0):
   self.name = name
   self.yes_count = 0
   self.no_count = 0

  def to_answer(self):
     if self.yes_count > self.no_count:
        self.no_count += 1
        return "meow-meow"
     else:
           self.yes_count += 1
           return "moore-moore"

  def number_yes(self):
       return self.yes_count

  def number_no(self):
       return self.no_count

tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')





