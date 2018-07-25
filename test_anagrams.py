#!/usr/bin/env python3

import unittest
from unittest.mock import patch, mock_open

from find_anagrams import calculate_char_counts, find_anagrams


def run_find_anagrams(keys, candidates):
    """Runs find_anagrams with the file open function mocked out.

    Arguments:
        keys (list): List of strings to look for anagrams for.
        candidates (list): List of candidate strings.

    Returns:
        A dict of key: list_of_anagrams.
    """
    m = mock_open(read_data='\n'.join(candidates))
    m.return_value.__iter__ = lambda self: self
    m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
    with patch('builtins.open', m):
        anagrams = find_anagrams(keys, 'dummy_candidate_file')
    return anagrams


class TestSingleKey(unittest.TestCase):
    def setUp(self):
        self.keys = ['abc']

    def test_key_has_one_anagram(self):
        candidates = ['foo', 'bac', 'bar']
        expected_anagrams = {
            'abc': set(['bac'])
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_key_has_many_anagrams(self):
        # Also proves that a string is its own anagram
        candidates = ['bac', 'abc', 'foo', 'cab']
        expected_anagrams = {
            'abc': set(['abc', 'bac', 'cab'])
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_key_has_no_anagrams(self):
        candidates = ['foo', 'bar', 'baz']
        expected_anagrams = {
            'abc': set()
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_all_candidates_are_anagrams(self):
        candidates = ['bac', 'abc', 'cab', 'bca']
        expected_anagrams = {
            'abc': set(['abc', 'bac', 'cab', 'bca'])
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)


class TestMultipleKeys(unittest.TestCase):
    def setUp(self):
        self.keys = ['abc', 'def']

    def test_keys_no_matches(self):
        candidates = ['foo', 'bar', 'baz']
        expected_anagrams = {
            'abc': set(),
            'def': set()
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_keys_one_has_matches(self):
        candidates = ['foo', 'acb', 'bar']
        expected_anagrams = {
            'abc': set(['acb']),
            'def': set()
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_keys_both_have_matches(self):
        candidates = ['foo', 'acb', 'fed']
        expected_anagrams = {
            'abc': set(['acb']),
            'def': set(['fed'])
        }
        self.assertEqual(run_find_anagrams(self.keys, candidates), expected_anagrams)

    def test_email_example_just_because(self):
        keys = ['foo', 'bar']
        candidates = ['ofo', 'oof', 'bar', 'baz', 'jig']
        expected_anagrams = {
            'bar': set(['bar']),
            'foo': set(['ofo', 'oof'])
        }
        self.assertEqual(run_find_anagrams(keys, candidates), expected_anagrams)


class TestSingleCandidate(unittest.TestCase):
    # Basically tested multiple candidates already.
    def setUp(self):
        self.candidates = ['abc']

    def test_candidate_matches_one_key(self):
        keys = ['fed', 'cab']
        expected_anagrams = {
            'fed': set(),
            'cab': set(['abc'])
        }
        self.assertEqual(run_find_anagrams(keys, self.candidates), expected_anagrams)

    def test_candidate_matches_many_keys(self):
        keys = ['cab', 'bac', 'fed']
        expected_anagrams = {
            'cab': set(['abc']),
            'bac': set(['abc']),
            'fed': set()
        }
        self.assertEqual(run_find_anagrams(keys, self.candidates), expected_anagrams)

    def test_candidate_matches_no_keys(self):
        keys = ['foo', 'bar', 'baz']
        expected_anagrams = dict((k, set()) for k in keys)
        self.assertEqual(run_find_anagrams(keys, self.candidates), expected_anagrams)


class TestEmptyLists(unittest.TestCase):

    def test_candidates_empty(self):
        keys = ['abc', 'def']
        expected_anagrams = {
            'abc': set(),
            'def': set()
        }
        self.assertEqual(run_find_anagrams(keys, []), expected_anagrams)

    def test_keys_empty(self):
        candidates = ['abc', 'def', 'fed']
        self.assertEqual(run_find_anagrams([], candidates), {})

    def test_keys_and_candidates_empty(self):
        self.assertEqual(run_find_anagrams([], []), {})


class TestDuplicates(unittest.TestCase):

    def test_duplicate_keys(self):
        keys = ['abc', 'def', 'abc']
        candidates = ['abc', 'fed']
        expected_anagrams = {
            'abc': set(['abc']),
            'def': set(['fed'])
        }
        self.assertEqual(run_find_anagrams(keys, candidates), expected_anagrams)

    def test_duplicate_candidates(self):
        keys = ['abc', 'def']
        candidates = ['abc', 'fed', 'fed']
        expected_anagrams = {
            'abc': set(['abc']),
            'def': set(['fed'])
        }
        self.assertEqual(run_find_anagrams(keys, candidates), expected_anagrams)


class TestCalculateCharCounts(unittest.TestCase):

    def test_different_letters(self):
        expected_char_counts = {
            'f': 1,
            'o': 1,
            'g': 1
        }
        self.assertEqual(calculate_char_counts('fog'), expected_char_counts)

    def test_same_letters(self):
        expected_char_counts = {
            'f': 1,
            'o': 2
        }
        self.assertEqual(calculate_char_counts('foo'), expected_char_counts)

    def test_one_char(self):
        self.assertEqual(calculate_char_counts('f'), {'f': 1})

    def test_empty_string(self):
        # Should never run into this in the program, but it's good to check.
        self.assertEqual(calculate_char_counts(''), {})


class TestInputUnchanged(unittest.TestCase):

    def test_keys_and_candidates_unchanged(self):
        keys = ['foo', 'bar', 'baz']
        candidates = ['abc', 'ofo', 'bar', 'oof']
        run_find_anagrams(keys, candidates)
        self.assertEqual(keys, ['foo', 'bar', 'baz'])
        self.assertEqual(candidates, ['abc', 'ofo', 'bar', 'oof'])


if __name__ == '__main__':
    unittest.main()
