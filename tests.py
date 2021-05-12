import unittest
from coordinates import parse_coordinates
from parce_daily import parce_daily
from parce_current import parce_current


class TestCoordinates(unittest.TestCase):

	def test_town_coordinates(self):
		self.assertEqual(parse_coordinates('Москва'), parse_coordinates('МоСкВа'))
		self.assertEqual(parse_coordinates('МОСква'), parse_coordinates('МОСКВА'))
		self.assertEqual(parse_coordinates('МоСКвА'), parse_coordinates('МОСква'))
		self.assertEqual(type(parse_coordinates('Москва')), type(list()))
class TestDaily(unittest.TestCase):

	def test_result_message(self):
		lot_lan = parse_coordinates('Москва')
		self.assertEqual(type(parce_daily(lot_lan)), type(str()))
class TestCurrent(unittest.TestCase):

	def test_current_weather(self):
		lot_lan = parse_coordinates('Москва')
		result_current = parce_current(lot_lan)
		self.assertTrue(isinstance(result_current, str))
		end_line = result_current.find('\n')
		current_temp = result_current[22:end_line]
		self.assertGreater(float(current_temp), -70)


if __name__ == '__main__':
	unittest.main()