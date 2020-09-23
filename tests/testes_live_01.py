from unittest import TestCase, main


def eh_par(val: int) -> bool:
    try:
        return True if val % 2 == 0 else False
    except TypeError:
        return False


class Testes(TestCase):
    def test_par(self):
        self.assertEqual(eh_par(2), True)

    def test_imp(self):
        self.assertEqual(eh_par(3), False)

    def test_string(self):
         self.assertEqual(eh_par('string'), False)




if __name__ == '__main__':
    main()