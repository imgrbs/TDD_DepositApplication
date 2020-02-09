import datetime
import unittest

import deposit_money


class TestDepositLimitAmount(unittest.TestCase):

    def test_check_deposit_amount_per_time_when_amount_is_25000_THB_should_return_True(self):
        expected_result = True
        deposit_amount = 25000.00

        actual_result = deposit_money.check_deposit_amount_per_time(deposit_amount)

        self.assertEqual(expected_result, actual_result)

    def test_check_deposit_amount_per_time_when_amount_is_30000_THB_should_return_True(self):
        expected_result = True
        deposit_amount = 30000.00

        actual_result = deposit_money.check_deposit_amount_per_time(deposit_amount)

        self.assertEqual(expected_result, actual_result)

    def test_check_deposit_amount_per_time_when_amount_is_31000_THB_should_return_False(self):
        expected_result = False
        deposit_amount = 31000.00

        actual_result = deposit_money.check_deposit_amount_per_time(deposit_amount)

        self.assertEqual(expected_result, actual_result)


class TestDepositFeeFromAge(unittest.TestCase):

    def test_calculate_age_when_DOB_is_8_FEB_2005_should_return_age_is_equal_to_15(self):
        expected_result = 15
        DOB = datetime.datetime(2005, 2, 8)
        current_date = datetime.datetime(2020, 2, 8)

        actual_result = deposit_money.calculate_age(DOB, current_date)

        self.assertEqual(expected_result, actual_result)

    def test_calculate_deposit_fee_from_age_when_age_is_15_should_return_deposit_fee_is_equal_to_0(self):
        expected_result = 0.00
        age = 15

        actual_result = deposit_money.calculate_deposit_fee_from(age)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
