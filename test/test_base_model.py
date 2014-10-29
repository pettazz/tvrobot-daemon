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