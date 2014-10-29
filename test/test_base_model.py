import unittest

from core.models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_criteria(self):
        data = {
            'empty': {
                'criteria': {},
                'expected': '1'
            },

            'base': {
                'criteria': {'one': 1},
                'expected': ' one = 1 '
            },

            'nested': {
                'criteria': {'OR': {'two': 2, 'one': 1}},
                'expected': ' ( two = 2 OR one = 1 ) '
            },

            'negation': {
                'criteria': {'AND': {'NOT': {'one': 1}, 'three': 3}},
                'expected': ' ( NOT ( one = 1 ) AND three = 3 ) '
            },

            'complex': {
                'criteria': {'OR': {'one': 1, 'NOT': {'two': 2}, 'AND': {'three': 3, 'four': 4, 'NOT': {'AND': {'five': 5, 'six': 6}}}}},
                'expected': ' ( NOT ( two = 2 ) OR ( four = 4 AND NOT ( ( six = 6 AND five = 5 ) ) AND three = 3 ) OR one = 1 ) '
            }
        }

        for dataSet in data:
            parsed = BaseModel.parse_criteria(data[dataSet]['criteria'])
            self.assertEqual(
                parsed, 
                data[dataSet]['expected'], 
                'Criteria set %s did not match expected:\nexpected:`%s`\nactual:  `%s`' % (dataSet, data[dataSet]['expected'], parsed))

    def test_load_dict(self):
        BaseModel.FIELDS = {
            0: 'guid',
            1: 'name',
            2: 'hats'
        }

        dict_data = {'guid': 'blah', 'name': 'sure', 'hats': False}

        test_model = BaseModel()
        test_model.load(dict_data)

        for key in dict_data:
            self.assertEqual(getattr(test_model, key), dict_data[key], 'Loaded data does not match data from source')

    def test_load_list(self):
        BaseModel.FIELDS = {
            0: 'guid',
            1: 'name',
            2: 'hats'
        }

        row_data = ['29f4de658', 'wat', False]

        test_model = BaseModel()
        test_model.load(row_data)

        self.assertEqual(test_model.guid, row_data[0], 'Loaded data does not match data from source')
        self.assertEqual(test_model.name, row_data[1], 'Loaded data does not match data from source')
        self.assertEqual(test_model.hats, row_data[2], 'Loaded data does not match data from source')

    def test_load_ignore_unknown_fields(self):
        BaseModel.FIELDS = {
            0: 'guid',
            1: 'name',
            2: 'hats'
        }

        dict_data = {'guid': 'blah', 'name': 'sure', 'hats': False, 'banana': 'hammock', 'number': 24387}

        test_model = BaseModel()
        test_model.load(dict_data)

        self.assertEqual(test_model.guid, dict_data['guid'], 'Loaded data does not match data from source')
        self.assertEqual(test_model.name, dict_data['name'], 'Loaded data does not match data from source')
        self.assertEqual(test_model.hats, dict_data['hats'], 'Loaded data does not match data from source')
        self.assertFalse(hasattr(test_model, 'banana'), 'Loaded an unknown field that we should not have')
        self.assertFalse(hasattr(test_model, 'number'), 'Loaded an unknown field that we should not have')

    def test_findOne_empty(self):
        result = BaseModel.findOne({'guid': 'notreal'})
        self.assertIsNone(result)

    def test_findAll_empty(self):
        result = BaseModel.findAll({'name': 'notreal'})
        self.assertEqual(result, [])