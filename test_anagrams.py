#!/usr/bin/env python3

import unittest

from find_anagrams import find_anagrams, is_anagram


class TestSingleKey(unittest.TestCase):
    def setUp(self):
        self.keys = ['abc']

    def test_key_has_one_anagram(self):
        candidates = ['foo', 'bac', 'bar']
        expected_anagrams = {
            'abc': ['bac']
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)

    def test_key_has_many_anagrams(self):
        # Also shows a string is its own anagram
        candidates = ['bac', 'abc', 'foo', 'cab']
        expected_anagrams = {
            'abc': ['cab', 'abc', 'bac']
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)

    def test_key_has_no_anagrams(self):
        candidates = ['foo', 'bar', 'baz']
        expected_anagrams = {
            'abc': []
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)

    def test_all_candidates_are_anagrams(self):
        candidates = ['bac', 'abc', 'cab', 'bca']
        expected_anagrams = {
            'abc': ['cab', 'abc', 'bac', 'bca']
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)


class TestMultipleKeys(unittest.TestCase):
    def setUp(self):
        self.keys = ['abc', 'def']

    def test_keys_no_matches(self):
        candidates = ['foo', 'bar', 'baz']
        expected_anagrams = {
            'abc': [],
            'def': []
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)

    def test_keys_one_has_matches(self):
        candidates = ['foo', 'acb', 'bar']
        expected_anagrams = {
            'abc': ['acb'],
            'def': []
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)

    def test_keys_both_have_matches(self):
        candidates = ['foo', 'acb', 'fed']
        expected_anagrams = {
            'abc': ['acb'],
            'def': ['fed']
        }
        self.assertEqual(find_anagrams(self.keys, candidates), expected_anagrams)


class TestSingleCandidate(unittest.TestCase):
    # Basically tested multiple candidates already.
    def setUp(self):
        self.candidates = ['abc']

    def test_candidate_matches_one_key(self):
        keys = ['fed', 'cab']
        expected_anagrams = {
            'fed': [],
            'cab': ['abc']
        }
        self.assertEqual(find_anagrams(keys, self.candidates), expected_anagrams)

    def test_candidate_matches_many_keys(self):
        keys = ['cab', 'bac', 'fed']
        expected_anagrams = {
            'cab': ['abc'],
            'bac': ['abc'],
            'fed': []
        }
        self.assertEqual(find_anagrams(keys, self.candidates), expected_anagrams)

    def test_candidate_matches_no_keys(self):
        keys = ['foo', 'bar', 'baz']
        expected_anagrams = dict((k, []) for k in keys)
        self.assertEqual(find_anagrams(keys, self.candidates), expected_anagrams)


class TestEmptyLists(unittest.TestCase):

    def test_candidates_empty(self):
        keys = ['abc', 'def']
        expected_anagrams = {
            'abc': [],
            'def': []
        }
        anagrams = find_anagrams(keys, [])
        self.assertEqual(anagrams, expected_anagrams)

    def test_keys_empty(self):
        candidates = ['abc', 'def', 'fed']
        anagrams = find_anagrams([], candidates)
        self.assertEqual(anagrams, {})

    def test_keys_and_candidates_empty(self):
        anagrams = find_anagrams([], [])
        self.assertEqual(anagrams, {})


class TestDuplicates(unittest.TestCase):

    def test_duplicate_keys(self):
        keys = ['abc', 'def', 'abc']
        candidates = ['abc', 'fed']
        expected_anagrams = {
            'abc': ['abc'],
            'def': ['fed']
        }
        self.assertEqual(find_anagrams(keys, candidates), expected_anagrams)

    def test_duplicate_candidates(self):
        keys = ['abc', 'def']
        candidates = ['abc', 'fed', 'fed']
        expected_anagrams = {
            'abc': ['abc'],
            'def': ['fed']
        }
        self.assertEqual(find_anagrams(keys, candidates), expected_anagrams)


class TestIsAnagram(unittest.TestCase):

    def test_true(self):
        self.assertTrue(is_anagram('foo', {'o': 2, 'f': 1}))

    def test_false_wrong_letters(self):
        self.assertFalse(is_anagram('zoo', {'o': 2, 'f': 1}))

    def test_false_too_many_letters(self):
        self.assertFalse(is_anagram('foo', {'o': 3}))

    def test_false_wrong_length(self):
        self.assertFalse(is_anagram('foo', {'o': 3, 'f': 1}))

    def test_empty_char_dict(self):
        self.assertFalse(is_anagram('abc', {}))


class TestInputUnchanged(unittest.TestCase):

    def test_keys_and_candidates_unchanged(self):
        keys = ['foo', 'bar', 'baz']
        candidates = ['abc', 'ofo', 'bar', 'oof']
        find_anagrams(keys, candidates)
        self.assertEqual(keys, ['foo', 'bar', 'baz'])
        self.assertEqual(candidates, ['abc', 'ofo', 'bar', 'oof'])

    def test_is_anagram_dict_unchanged(self):
        candidate_string = 'abc'
        char_counts = {'a': 1, 'b': 1, 'c': 1}
        is_anagram(candidate_string, char_counts)
        self.assertEqual(candidate_string, 'abc')
        self.assertEqual(char_counts, {'a': 1, 'b': 1, 'c': 1})


if __name__ == "__main__":
    unittest.main()
