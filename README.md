# find_anagram.py

A program which reads a newline-separated list of words (the candidates) as input and, given another short list of words (the keys), writes out all anagrams of each key that are present in the input.

## Running the program

The program takes 2 required arguments, `--input` and `--keys`, both of which accept a file name value.

Run the program on the command line:

```
python find_anagrams.py --input input.txt --keys keys.txt
```

## Running the tests

Run the test suite on the command line:

```
python test_anagrams.py
```

## Time and space complexity

The time and space complexity for this solution are both `O(n*m*s)`, where `n` is the number of candidate strings (--input), `m` is the number of keys, and `s` is the maximum length of any string in either list.

The time complexity comes from the comparison of every key with every candidate, and each one of these string comparison costs `O(s)` time. There are smaller terms from operations such as counting the characters in each key, but those terms have been dropped.

The space complexity is because the function builds a return value mapping each key (whether or not it found matching anagrams) to a list of its matching anagrams from the input file. In the worst case, every candidate string would be an anagram of every key, so each of the `n` candidate strings of length `s` would need to be stored `m` times.

## Assumptions & alternatives considered

Assumptions made while writing this program included:
* Duplicate words in either file should be ignored.
* A list of keys are unlikely to be mostly anagrams of each other (more detail below.)

Alternative solutions/optimizations considered:
* Keeping track of keys already searched for, and if a new key is an anagram of a key already searched for, return the results of that former search. However, decided not to do that since that would involve a string comparison with time complexity `O(s)`, `m` times (1 for each existing key in the worst case), so that would add a complexity of `O(m*s)`, without any guarantee of gain.
    * There would also be the additional memory needed to store the keys already searched for, an additional term of `O(m*s)` for the space complexity.
    * Even though the smaller terms for the complexity would be dropped here, it seemed like added complication for not much gain. A list of keys that are mostly anagrams of each other would be an edge case, IMO.
* Another solution would have been to sort the keys and/or inputs, which would have a time complexity of `n*s*log(s) + m*s*log(s) = (n + m)*s*log(s)`, which is scales worse than `n*m*s`.
    * Although if, say, a list of inputs or keys was to be kept around for comparison many times in the future, it may then be worthwhile to preprocess the strings by sorting & grouping anagrams.
    * It's also worth noting that this would be the most compact soluton, code-wise, which counts for a lot. But I'm making the tradeoff for a slightly more optimal solution here.
