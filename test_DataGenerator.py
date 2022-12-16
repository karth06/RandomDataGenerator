from unittest import TestCase
from DataGenerator import RandomDataGenerator


class TestRandomDataGenerator(TestCase):

    def test_get_users_list(self):
        data = RandomDataGenerator.get_users(data_type="list", length=2)
        self.assertTrue(len(data) == 2)
        print(data)

    def test_get_users_set(self):
        data = RandomDataGenerator.get_users(data_type="set", length=2)
        self.assertTrue(len(data) == 2)
        print(data)

    def test_data_length(self):
        with self.assertRaises(ValueError) as context:
            RandomDataGenerator.get_users(length=11)
        self.assertEqual("The size of the collection must be greater than 0 and less than 10", str(context.exception))

    def test_data_type_list(self):
        data = RandomDataGenerator.get_users(data_type="list")
        self.assertTrue(isinstance(data, list))
        print(data)

    def test_data_type_set(self):
        data = RandomDataGenerator.get_users(data_type="set")
        self.assertTrue(isinstance(data, set))
        print(data)

    def test_data_type_dict(self):
        data = RandomDataGenerator.get_users(data_type="dict", length=1)
        self.assertTrue(isinstance(data, dict))
        print(data)

    def test_data_type_list_of_dict(self):
        data = RandomDataGenerator.get_users(data_type="dict", length=5)
        print(data)

    def test_invalid_data_type(self):
        with self.assertRaises(ValueError) as context:
            RandomDataGenerator.get_users(data_type="listsetdict")
        self.assertEqual("Invalid data_type, the data type must be a List or a Set", str(context.exception))
