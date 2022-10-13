from unittest import TestCase, main      # Добавление библиотеки unittests
from main import _min                    #
from main import _max                    # добавление функций из файла main.py
from main import _sum                    #
from main import _mult                   #


class PyTest(TestCase):
    def test_min(self):
        self.assertEqual(_min([56.5, 5.0, 1.0, -4.0]), -4.0)

    def test_max(self):
        self.assertEqual(_max([-100.3, 1, 28, 1004, -12, 5555]), 5555)

    def test_mult(self):
        self.assertEqual(_mult([16.5, 44.0, 1.0, -6.0]), -4356)

    def test_sum(self):
        self.assertEqual(_sum([11, -3, 243, -10]), 241)

if __name__ == '__main__':
    main()