#!/usr/bin/env python3

import argparse


def calculate_char_counts(key):
    """Returns a dict of character: count for each character in key."""
    char_counts = {}
    for c in key:
        char_counts[c] = char_counts.get(c, 0) + 1

    return char_counts


def find_anagrams(keys, candidates_file):
    """Finds all anagrams in candidates_file, for all strings in keys.

    Arguments:
        keys (list): List of strings to look for anagrams for.
        candidates_file (string): Name of the file containing candidate strings.

    Returns:
        A dict of key: list_of_anagrams.
    """
    keys = set(keys)
    # key_counts is a dict of key: {character: count}
    key_counts = {k: calculate_char_counts(k) for k in keys}

    # Results dict
    key_anagrams = {k: set() for k in keys}

    with open(candidates_file) as f:
        for candidate in f:
            candidate = candidate.strip() # Remove newline char
            candidate_char_counts = calculate_char_counts(candidate)

            # Loop through keys to check for anagrams
            for k, v in key_counts.items():
                if len(k) != len(candidate):
                    # Strings of different lengths can't be anagrams.
                    # (Just a little shortcut because len() is O(1).)
                    continue

                if candidate_char_counts == v:
                    key_anagrams[k].add(candidate)

    return key_anagrams


def parse_args():
    """Just your basic arg parser.

    Arguments are --input <input_file> and --keys <key_file>, both required.
    """
    parser = argparse.ArgumentParser(
        description=('Input a file of strings & a file of keys to find all '
                     'anagrams of the keys in the list of strings.')
    )

    parser.add_argument('--input', required=True,
        help=('Text file containing a list of candidate strings in which to '
              'search for anagrams.')
    )

    parser.add_argument('--keys', required=True,
        help=('Text file containing a list of keys (strings) to look for in '
              'the list of candidate strings.')
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    with open(args.keys) as f:
        keys = f.readlines()
    keys = [x.strip() for x in keys]

    anagrams = find_anagrams(keys, args.input)

    for k, v in anagrams.items():
        print('{0}: {1}'.format(k, ', '.join(v)))
