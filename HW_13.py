

import math


class Point:
    _x = None
    _y = None

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'==' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'!=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.x != other.x or self.y != other.y

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f'`x_coord` argument must be an integer (got {type(value)})')
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f'`y_coord` argument must be an integer (got {type(value)})')
        self._y = value


class Line:
    _begin = None
    _end = None

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    def __str__(self):
        return f'Line({self.begin}, {self.end})'

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'<' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length < other.length

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'<=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length <= other.length

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'==' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length == other.length

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'!=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length != other.length

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'>' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length > other.length

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'>=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.length >= other.length

    @property  # getter
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'`begin_point` argument must be a Point object (got {type(value)})')
        self._begin = value

    @property  # getter
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'`end_point` argument must be a Point object (got {type(value)})')
        self._end = value

    @property
    def length(self):
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:
    _point1 = None
    _point2 = None
    _point3 = None

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3

    def __str__(self):
        return f'Triangle({self.point1}, {self.point2}, {self.point3})'

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"'<' not supported between instances of '{self.__class__.__name__}' and '{type(other)}'")
        return self.area < other.area

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'<=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.area <= other.area

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'==' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.area == other.area

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'!=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.area != other.area

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'>' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"'>=' not supported between instances of '{self.__class__.__name__}' and '{type(other).__name__}'")
        return self.area >= other.area

    @property  # getter
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'`point_1` argument must be a Point object (got {type(value)})')
        self._point1 = value

    @property  # getter
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'`point_2` argument must be a Point object (got {type(value)})')
        self._point2 = value

    @property  # getter
    def point3(self):
        return self._point3

    @point3.setter
    def point3(self, value):
        if not isinstance(value, Point):
            raise TypeError(f'`point_3` argument must be a Point object (got {type(value)})')
        self._point3 = value

    @property
    def area(self):
        """
        Ініціалізація трикутника з прийнятих точокю
        Розрахунок площини за теоремою Герона
        """
        line1 = Line(self.point1, self.point2)
        line2 = Line(self.point2, self.point3)
        line3 = Line(self.point3, self.point1)
        line_A = line1.length
        line_B = line2.length
        line_C = line3.length

        half_perim = (line_A + line_B + line_C) / 2
        return math.sqrt(half_perim * (half_perim - line_A) * (half_perim - line_B) * (half_perim - line_C))
    
# Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=)
# print() обʼєкту классу Triangle показує координати його вершин
# print(triangle1)
# > (Point(1,0) Point(5,9) Point(3,3))

if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = Point(4, 5)
    point3 = Point(1, 6)
    point4 = Point(0, 14)
    point5 = Point(8, 2)
    point6 = Point(1, 6)
    print(point1)
    print(f'point1 != point4: {point1 != point4}')
    print(f'point3 == point6: {point3 != point6}', end='\n\n')

    line1 = Line(point1, point2)
    line2 = Line(point6, point4)
    print(line1, f'length: {line1.length}')
    print(line2, f'length: {line2.length}')
    print(f'line2 > line1: {line2 > line1}', end='\n\n')

    triangle1 = Triangle(point1, point2, point3)
    triangle2 = Triangle(point4, point5, point6)
    print(triangle1, f'area: {triangle1.area}')
    print(triangle2, f'area: {triangle2.area}')
    print(f'triangle2 > triangle1: {triangle2 > triangle1}')