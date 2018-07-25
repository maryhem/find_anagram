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

The time complexity comes from the comparison of every key with every candidate, and each one of these string comparisons costs `O(s)` time. There are smaller terms from operations such as counting the characters in each key, but those terms have been dropped.

The space complexity is because the function builds a return value mapping each key (whether or not it found matching anagrams) to a list of its matching anagrams from the input file. In the worst case, every candidate string would be an anagram of every key, so each of the `n` candidate strings of length `s` would need to be stored `m` times.

## Assumptions & alternatives considered

Assumptions made while writing this program include:
* Duplicate words in either file should be ignored- BUT, having a lot of duplicates would be unusual.
* The number of anagrams in the input file for any given key will normally be much smaller than the overall size of the input file (hence my memory-conscious solution.)

Alternative solutions considered:
* Sorting the key & input strings, and then comparing the sorted strings. However, just sorting the strings would cost `n*s*log(s) + m*s*log(s) = (n + m)*s*log(s)`, and then sorting the key and/or candidate lists would cost an additional `n*log(n)` or `m*log(m)`. So, this solution would scale much worse than the solution I chose.
    * Although if, say, a list of inputs or keys was to be kept around for comparison many times in the future, it may then be worthwhile to preprocess the strings by sorting & grouping anagrams.
    * It's also worth noting that this would be the most compact soluton, code-wise, which counts for a lot. But I'm making the tradeoff for a slightly more optimal solution here.
* Reading both the key and candidate files into memory, and then, after removing duplicates, looping through all key & candidate pairs and comparing character counts. I came very close to choosing this as my solution, and really the "right" answer only depends on your priorities and what you expect your input to look like.
    * This solution would be less memory efficient because it would hold all candidate strings in memory, whereas my solution reads them in one at a time. However, thanks to the results dict, the overall space complexity would still be `O(n*m*s)` either way.
    * This solution would be slightly faster if the candidate file contained a lot of duplicates, because it would remove those duplicates before going through and doing the character counts for each string. However, one of my assumptions is that having a lot of duplicates would be unusual, so I decided to opt for the memory-efficient solution instead.
    * Last but not least, it'd be easier to test this one because you wouldn't have to mock out the file stream.
