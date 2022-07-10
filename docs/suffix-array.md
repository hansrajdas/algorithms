## Suffix arrays (SA)
- A SA is an array which contains all the sorted suffixes of a string
- For eg. SA of “camel” is
  1. Index and suffix of string

      idx|suffix
      ---|------
      0|camel
      1|amel
      2|mel
      3|el
      4|l

  2. SORTED by suffix

      idx|suffix
      ---|------
      1|amel
      0|camel
      3|el
      4|l
      2|mel

  3. So SA of “camel” is __[1, 0, 3, 4, 2]__

- The SA provides space efficient alternative to suffix trees which itself is compressed version of trie
- SA can do everything suffix trees can, with some additional information such as _longest common prefix (LCP) array_

### LCP array
- The LCP array is an array in which every index tracks _how many characters two sorted adjacent suffixes have in common_
- By convention LCP[0] is undefined, but for most purposes it's fine to set it to 0
- There exists many methods for efficiently constructing LCP array in _O(nlogn) and O(n)_

### Applications of SA and LCP arrays
#### Finding and counting unique substrings of a string
- The _naive_ approach generates all substrings and places them in a set resulting in `O(n^2)` algorithm
- A _better_ approach is to use LCP array. This is not only quick but space efficient also
  - Total number of unique substrings in a string is `X - Y`, where
  - X = Total number of substrings, which is `n(n + 1) / 2`
  - Y = Number of duplicate strings, which is `SUM(LCP[i]); 1 <= i <= n`

#### Longest common substring (LCS)
- In general form, also known as `k-common substring` problem
- Problem statement: Suppose we have N strings, how do we find the __LCS__ that appears in at least `2 <= k <= n` of the strings
- One approach is to use DP running in `O(n1 x n2 x ... nm)`, where `ni` are the lengths of the strings. This works OK with smaller number of strings but rapidly gets unwieldly
- An alternative approach is to use SA and LCP array which can find the solution is `O(n1 + n2 + ... nm)` time

#### Longest repeated substring (LRS)
- LRS of a string is a string which is repeated in given string. For eg, LRS of string `ABRACADABRA` will be `ABRA` which repeates at least twice
- The brute force method requires `O(n^2)` time and lots of space. Using the information inside `LCP` array saves time and space.
- LRS is simply __max value in LCP array__

### References
- WilliamFiset suffix array lectures: https://www.youtube.com/playlist?list=PLDV1Zeh2NRsCQ_Educ7GCNs3mvzpXhHW5
