import unittest
from flask import Flask
from app import calculate

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_calculate_positive_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '4', 'c': '1'}):
            response = calculate()
            self.assertIn('Корни уравнения:', response)

    def test_calculate_zero_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '2', 'c': '1'}):
            response = calculate()
            self.assertIn('Уравнение имеет один корень:', response)

    def test_calculate_negative_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '1', 'c': '1'}):
            response = calculate()
            self.assertIn('Уравнение не имеет действительных корней', response)

    def test_calculate_invalid_input(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': 'a', 'b': 'b', 'c': 'c'}):
            response = calculate()
            self.assertIn('Пожалуйста, введите числовые значения для всех коэффициентов.', response)

    def test_calculate_zero_a_coefficient(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '0', 'b': '1', 'c': '1'}):
            response = calculate()
            self.assertIn("Коэффициент 'a' не может быть равен нулю.", response)

if __name__ == '__main__':
    unittest.main()
