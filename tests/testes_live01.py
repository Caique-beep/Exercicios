from unittest import TestCase, main
from numbers import Number


def validate_cache(func):
    def validate(self, x, y):
        if isinstance(x, Number) and isinstance(y, Number):
            func(self, x, y)
        else:
            raise Exception('insira somente numeros')
    return validate


class Calc:
    def soma(self, x, y):
        if isinstance(x, Number) and isinstance(y, Number):
            return x + y
        else:
            raise Exception('insira somente numeros')

    @validate_cache
    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x*y


class Testes(TestCase):
    def setUp(self) -> None:
        self.calc = Calc()
        
    def teste_soma(self):
        self.assertEqual(self.calc.soma(1, 2), 3)

    def teste_soma_float(self):
        self.assertEqual(self.calc.soma(2.0, 3.0), 5.0)

    def teste_soma_neg(self):
        self.assertEqual(self.calc.soma(-5, -2), -7)

    def teste_soma_string(self):
        with self.assertRaises(Exception):
            self.calc.soma("Caique", "Cardoso")

if __name__ == '__main__':
    main()