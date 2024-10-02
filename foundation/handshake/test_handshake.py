from unittest import TestCase, main
from .exam_python import no_of_handshakes, InvalidInput


class TestHandShakeFunction(TestCase):

    def test_handshake_positive_integer(self):
        expected = 190
        result = no_of_handshakes(20)
        self.assertEqual(expected, result)

    def test_zero(self):
        expected = 0
        result = no_of_handshakes(0)
        self.assertEqual(expected, result)

    def test_float_error_raised(self):
        my_input = 2.5
        with self.assertRaises(InvalidInput):
            no_of_handshakes(my_input)

    def test_negative_error_raised(self):
        my_input = -1
        with self.assertRaises(InvalidInput):
            no_of_handshakes(my_input)

    def test_string_error_raised(self):
        my_input = '2'
        with self.assertRaises(AttributeError):
            no_of_handshakes(my_input)

if __name__ == '__main__':
    main()

