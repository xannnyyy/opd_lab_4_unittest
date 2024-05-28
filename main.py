import unittest
from flask import Flask, request
from app import calculate

class TestQuadraticEquation(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_calculate_with_positive_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '4', 'c': '1'}):
            result = calculate()
            self.assertEqual(result, 'Корни уравнения: x1 = -0.2679491924311228, x2 = -3.732050807568877')

    def test_calculate_with_zero_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '2', 'c': '1'}):
            result = calculate()
            self.assertEqual(result, 'Уравнение имеет один корень: x = -1.0')

    def test_calculate_with_negative_discriminant(self):
        with self.app.test_request_context('/calculate', method='POST', data={'a': '1', 'b': '1', 'c': '1'}):
            result = calculate()
            self.assertEqual(result, 'Уравнение не имеет действительных корней')

if __name__ == '__main__':
    unittest.main()
