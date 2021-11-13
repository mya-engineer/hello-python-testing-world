import unittest
from unittest.mock import patch
from Employee import Employee


class TestEmployee(unittest.TestCase):
    # starts at the beginning of tests
    @classmethod
    def setUpClass(cls):
        print(f'Starting {cls.__name__} tests')

    # starts at the end of all tests
    @classmethod
    def tearDownClass(cls):
        print(f'Finishing {cls.__name__} tests')

    # starts before every test
    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # starts after every test
    def tearDown(self):
        del self.emp_1
        del self.emp_2

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'corey.schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'john.schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('Employee.requests.get') as mocked_get:
            # testing ok response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.montly_schedule('May')
            # called with correct URL
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success!')

            # testing bad response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.montly_schedule('June')
            # called with correct URL
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
