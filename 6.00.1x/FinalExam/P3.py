__author__ = 'ThanhNam'
import unittest

def dict_invert(d):
    reverse_dictionary = {}
    original_relationships = []
    for key in d:
        original_relationships.append((key, d[key]))
    for original in original_relationships:
        try:
            reverse_dictionary[original[1]].append(original[0])
        except KeyError:
            reverse_dictionary[original[1]] = [original[0]]
    for key in reverse_dictionary:
        unsort = reverse_dictionary[key]
        issort = sorted(unsort)
        reverse_dictionary[key] = issort
    return reverse_dictionary




class TestCasesForFinalProblem3(unittest.TestCase):

    def test_reverse_dictionary(self):
        self.assertEqual(
            dict_invert(
                {1:10, 2:20, 3:30}
            ),
            {10: [1], 20: [2], 30: [3]}
        )
        self.assertEqual(
            dict_invert(
                {1:10, 2:20, 3:30, 4:30}
            ),
            {10: [1], 20: [2], 30: [3, 4]}
        )
        self.assertEqual(
            dict_invert(
                {4:True, 2:True, 0:True}
            ),
            {True: [0, 2, 4]}
        )

if __name__ == '__main__':
    unittest.main()