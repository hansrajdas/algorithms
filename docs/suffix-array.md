## Suffix arrays (SA)
WilliamFiset lectures [starting 42](https://www.youtube.com/watch?v=zqKlL3ZpTqs&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=42) to 47
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
- Finding and counting unique substrings of a string