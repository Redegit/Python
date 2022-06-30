class Field():
    def __init__(self):
        self.screen = [['.'] * 20 for _ in range(20)]

    def draw(self, screen):
        new_screen = [['.'] * 20 for _ in range(20)]
        for y in range(len(screen)):
            x = 0
            for i, j in zip(self.screen[y], screen[y]):
                if i == "*" or j == "*":
                    new_screen[y][x] = "*"
                x += 1
        self.screen = new_screen

    def print_screen(self):
        for line in self.screen:
            for symb in line:
                print(symb, end='')
            print()


class Sharp(Field):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'Это точка с координатами ({self.x};{self.y})'

    def area(self):
        return 0


# sh = Sharp(1, 19)
# sh.draw()
# sh.__str__()
# sh.area()


class Rectangle(Sharp):
    def __init__(self, *parameter):
        self.__x = parameter[0]
        self.__y = parameter[1]
        self.__width = parameter[2]
        self.__height = parameter[3]

    def draw(self):  # отрисовка границы прямоугольника
        self.screen = [['.'] * 20 for _ in range(20)]
        for i in range(self.__y, self.__y + self.__height):
            self.screen[i][self.__x] = '*'
        for i in range(self.__y, self.__y + self.__height):
            self.screen[i][self.__x + self.__width - 1] = '*'
        for i in range(self.__x, self.__x + self.__width):
            self.screen[self.__y][i] = '*'
        for i in range(self.__x, self.__x + self.__width):
            self.screen[self.__y + self.__height - 1][i] = '*'
        return self.screen

    def draw1(self, master):  # отрисовка с заполнением
        self.screen = [['.'] * 20 for _ in range(20)]
        for j in range(self.__x, self.__x + self.__width):
            for i in range(self.__y, self.__y + self.__height):
                self.screen[i][j] = '*'
        master.draw(self.screen)


field1 = Field()
rectangle = Rectangle(1, 10, 3, 4)
rectangle1 = Rectangle(10, 1, 5, 4)
# field1.draw(rectangle.draw())
rectangle1.draw1(field1)
field1.print_screen()
print()

# field2 = Field()
# rectangle3 = Rectangle(2, 8, 13, 4)
# field2.draw(rectangle3.draw())
# field2.print_screen()


# class Sharp(object):
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#         self.screen=[['.']*20 for _ in range(20)]

#     def print_screen(self):
#         for line in self.screen:
#             for symb in line:
#                 print(symb, end='')
#             print()

#     @property
#     def x(self):
#         return self.__x

#     @property
#     def y(self):
#         return self.__y

#     def draw(self):
#         self.screen=[['.']*20 for _ in range(20)]
#         self.screen[self.__y][self.__x]='*'
#         self.print_screen()

#     def __str__(self):
#         return f'Это точка с координатами ({self.x};{self.y})'

#     def area(self):
#         return 0

# class Sharp(object):
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#         self.screen=[['.']*20 for _ in range(20)]

#     def print_screen(self):
#         for line in self.screen:
#             for symb in line:
#                 print(symb, end='')
#             print()

#     @property
#     def x(self):
#         return self.__x

#     @property
#     def y(self):
#         return self.__y

#     def draw(self):
#         self.screen=[['.']*20 for _ in range(20)]
#         self.screen[self.__y][self.__x]='*'
#         self.print_screen()

#     def __str__(self):
#         return f'Это точка с координатами ({self.x};{self.y})'

#     def area(self):
#         return 0