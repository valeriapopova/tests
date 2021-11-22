import unittest
from ya import *
file = 'news'


class TestYD(unittest.TestCase):

    def test_create_folder(self):
        self.assertEqual(create_folder(file), 201)

    def test_create_folder_error(self):
        self.assertEqual(create_folder(file), 409)

    def test_check_status(self):
        self.assertEqual(check_status(file), 200)


