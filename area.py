from abc import ABC, abstractmethod
import math, unittest


class Figure(ABC):
    '''
    Абстрактный класс для последующего добавления других фигур
    '''

    @abstractmethod
    def get_area(self) -> float: ...


class Circle(Figure):
    '''
    Класс-наследник Figure для работы с кругами.
    '''

    @classmethod
    def get_area(cls, radius:float) -> float:
        '''
        Функция вычисления площади круга.
        Обязательный аргумент - радиус.
        '''
        return round(math.pi * (radius**2), 2)
    

class Triangle(Figure):

    @classmethod
    def get_area(cls, sides:list[float]) -> float:
        '''
        Функция вычисления площади треугольника.
        Обязательный аргумент - список длин сторон треугольника.
        '''

        if not cls.is_exist(sides):
            raise ValueError('Треугольника с такими сторонами не существует')

        # если треугольник прямоугольный - вычисление по упрощённой формуле
        if cls.is_rectangular(sides):
            return round((sides[0] * sides[1]) / 2, 2)
        
        per = sum(sides) / 2
        area = round(
            math.sqrt(per*(per-sides[0])*(per-sides[1])*(per-sides[2])), 2
            )
        return area
    
    @classmethod
    def is_rectangular(cls, sides:list[float]) -> bool:
        '''
        Функция проверки треугольника на прямоугольность.
        Обязательный аргумент - список длин сторон треугольника.
        '''
        sides.sort()
        return sides[2]**2 == sides[0]**2 + sides[1]**2

    @classmethod
    def is_exist(cls, sides:list[float]) -> bool:
        '''
        Внутренняя функция проверки треугольника на существование
        '''
        return (sides[0] + sides[1] >= sides[2]
                and sides[0] + sides[2] >= sides[1]
                and sides [1] + sides [2] >= sides[0])

class TestAreaMethods(unittest.TestCase):
    
    def test_circle_area(self):
        '''Проверка расчета площали круга'''
        self.assertEqual(Circle.get_area(1), 3.14)

    def test_triangle_is_rec(self):
        '''Проверка определения прямоугольного треугольника'''
        self.assertTrue(Triangle.is_rectangular([3,4,5]))

    def test_rec_triangle_area(self):
        '''Проверка расчета площади прямоугольного треугольника'''
        self.assertEqual(Triangle.get_area([4,5,3]), 6)

    def test_triangle_area(self):
        '''Проверка расчета площади непрямоугольного треугольника'''
        self.assertEqual(Triangle.get_area([4,2,3]), 2.9)

    def test_nonexisted_triangle(self):
        '''Проверка выброса исключения для несуществующего треугольника'''
        self.assertRaises(ValueError, Triangle.get_area, [2,3,10])

if __name__ == '__main__':
    unittest.main()
