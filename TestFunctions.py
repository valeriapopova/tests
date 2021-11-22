import unittest
from unittest.mock import patch
from main import *


class TestFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass create user')

    def setUp(self):
        print('setUp')

    def test_people(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertEqual(people(), 'Аристарх Павлов')

    def test_shelf(self):
        with unittest.mock.patch('builtins.input', return_value ='11-2'):
            self.assertEqual(shelf(), '1')

    def test_doc_list(self):
        information = ['passport, удалён, Василий Гупкин', 'invoice, 11-2, Геннадий Покемонов',
                       'insurance, 10006, Аристарх Павлов']
        self.assertEqual(doc_list(), information)

    def test_add_shelf(self):
        inf = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': [], '4': []}
        with unittest.mock.patch('builtins.input', return_value='4'):
            self.assertEqual(add_new_shelf(), inf)

    def test_move(self):
        inf = {'1': ['11-2'], '2': [], '3': ['10006'], '4': []}
        self.assertEqual(move('10006', '3'), inf)

    def test_delete(self):
        inf = ([{'name': 'Василий Гупкин', 'number': 'удалён', 'type': 'passport'},
                {'name': 'Геннадий Покемонов', 'number': '11-2', 'type': 'invoice'},
                {'name': 'Аристарх Павлов', 'number': '10006', 'type': 'insurance'}],
                {'1': ['11-2'], '2': ['10006'], '3': [], '4': []})
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            self.assertEqual(delete_doc(), inf)

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass delete user')




