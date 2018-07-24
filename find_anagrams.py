#!/usr/bin/env python3

import argparse
import copy

"""
Keep it:
* READABLE
* UNIT TESTABLE

Use the right tools!!!
"""

def parse_args():
    """Just your basic arg parser.

    Arguments are --input <input_file> and --keys <key_file>, both required.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Input a file of strings & a file of keys to find all anagrams of "
            "the keys in the list of strings."
        )
    )

    parser.add_argument("--input", required=True,
        help=("Text file containing a list of candidate strings in which to "
              "search for anagrams.")
    )

    parser.add_argument("--keys", required=True,
        help=("Text file containing a list of keys (strings) to look for in "
              "the list of candidate strings.")
    )

    return parser.parse_args()


def is_anagram(candidate_string, char_counts, key_length=None):
    """Returns True if candidate_string is an anagram of a string with
    character counts represented in char_counts.

    Arguments:
        candidate_string: String to check if is anagram of char_counts.
        char_counts: Dict of character: character_count, for each character
            in the original key string.
        key_length (optional): Length of original key string. (Just because
            it's faster than always summing the values in char_counts.)
    """
    if not key_length:
        key_length = sum(char_counts.values())

    if len(candidate_string) != key_length:
        # Words of different lengths cannot be anagrams.
        return False

    # This looks a bit ugly, but it saves us from having to count the characters
    # in the key multiple times.
    key_char_counts = copy.deepcopy(char_counts)

    is_ag = True
    # Loop through the letters of candidate_string
    for c in candidate_string:
        if c in key_char_counts:
            key_char_counts[c] -= 1
            if key_char_counts[c] < 0:
                # Too many of character c
                is_ag = False
                break
        else:
            # Character c not in key
            is_ag = False
            break

    return is_ag


def find_anagrams(keys, candidates):
    """Finds all anagrams in candidates, for all strings in keys.

    Arguments:
        keys: List of strings to look for anagrams for.
        candidates: List of candidate strings.

    Returns:
        A dict of string: list_of_anagrams, as key: value.
    """
    key_anagrams = dict.fromkeys(keys)

    # Ignore case, duplicates
    keys = set([x.lower() for x in keys])
    candidates = set([x.lower() for x in candidates])

    for key in keys:
        anagrams_found = []

        # Calculate character counts for this key
        # TODO: would it be better & more readable to just do this for every damn candidate?
        calculated_char_counts = dict((c, key.count(c)) for c in key)

        for candidate in candidates:
            if is_anagram(candidate, calculated_char_counts, len(key)):
                anagrams_found.append(candidate)

        key_anagrams[key] = anagrams_found

    return key_anagrams


if __name__ == "__main__":
    args = parse_args()

    with open(args.keys) as f:
        keys = f.readlines()
    keys = [x.strip() for x in keys]

    with open(args.input) as f:
        ag_candidates = f.readlines()
    ag_candidates = [x.strip() for x in ag_candidates]

    anagrams = find_anagrams(keys, ag_candidates)

    for k, v in anagrams.items():
        print("{0}: {1}".format(k, ", ".join(v)))
