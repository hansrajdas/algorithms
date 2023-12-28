# List of Algorithms
All programs are categorized in level 1 to 4(1 being easiest)
## Sorting
- [Bubble sort (Python)](Level-2/bubble_sort.py): Implement bubble sort in Python | O(n^2) | Level 2.
- [Bubble sort (Go)](Level-2/bubble-sort.go): Implement bubble sort in Golang | O(n^2) | Level 2.
- [Selection sort](Level-2/selection_sort.py): Implement selection sort in python | O(n^2) | Level 2.
- [Selection sort](Level-2/selection_sort.c): Implement selection sort in C| O(n^2) | Level 2.
- [Insertion sort](Level-2/insertion_sort.py): Implement insertion sort | O(n^2) | Level 2.
- [Heap sort using max heap](Level-3/heap_sort_using_max_heap.c): Build a max heap and sort array in ascending order | Level 3.
- [Heap sort using max heap - python](Level-3/heap_sort_using_max_heap.py): Build a max heap and sort array in ascending order | Level 3.
- [Heap sort using min heap](Level-3/heap_sort_using_min_heap.c): Build a min heap and sort array in descending order | Level 3.
- [Heap sort using min heap - python](Level-3/heap_sort_using_min_heap.py): Build a min heap and sort array in descending order | Level 3.
- [Merge sort](Level-3/merge_sort.c): Implement merge sort | O(nlogn) | Level 3.
- [Merge sort - python](Level-3/merge_sort.py): Implement merge sort in python | O(nlogn) | Level 3.
- [Quick sort](Level-3/quick_sort.c): Implement quick sort(C) for array of random numbers | O(nlogn) | Level 3.
- [Quick sort - python](Level-3/quick_sort.py): Implement quick sort(python) for array of random numbers | O(nlogn) | Level 3.
- [Counting sort](Level-2/counting_sort.c): Implement count sort | O(n + k) | Level 2.
- [Counting sort - python](Level-2/counting_sort.py): Implement count sort in python | O(n + k) | Level 2.
- [Radix sort](Level-4/radix_sort.c): Implement radix sort | O(digits * (n + base)) | Level 4.

## Trie
- [Trie implementation](Level-3/trie_insert_search_delete.py): Implement trie and perform insert, search and delete operations | O(L) | Level 3.
- [Trie autocomplete](Level-3/trie_autocomplete.py): Implement word autocomplete feature using trie | O(ALPHABET_SIZE * N * L) | Level 3.
- [Trie, sorted strings](Level-2/trie_words_in_sorted_order.py): Print all words in trie, in sorted order | O(ALPHABET_SIZE * N * L) | Level 2.
- [Trie, longest prefix matching](Level-2/trie_longest_prefix_matching.py): Given a string, find a word from trie which matches longest prefix | O(n) | Level 2.
- [Pattern matching using suffix tries](Level-3/pattern_matching_using_suffix_tries.py): Implement suffix tries for pattern matching | O(m) | Level 3.

## Graphs
- [DFS traversal](Level-2/graph_depth_first_search.py): Create a directed graph and performs depth first search(DFS) traversal | O(V + E) | Level 2.
- [BFS traversal](Level-2/graph_breadth_first_search.py): Breadth first search(BFS) traversal of directed graph | O(V + E) | Level 2.
- [Connected components](Level-2/find_connected_components.py): Find all connected components in a graph | O(V + E) | Level 2.
- [Shortest path in unweighted graph](Level-2/shortest_path_of_unweighted_graph.py): Find shortest path from src to dst in an unweighted graph | O(V + E) | Level 2.
- [Cycle in graph](Level-3/cycle_in_graph.py): Check if there is cycle in a directed graph, uses DFS | O(V + E) | Level 3.
- [Topological sort](Level-3/topological_sort.py): Topological order of directed acyclic graph(DAG) using DFS | O(V + E) | Level 3.
- [Shortest path of DAG](Level-3/shortest_path_for_DAG.py): Find shortest in a directed acyclic graph from a source vertex to all reachable vertex | O(V + E) | Level 3.
- [Dijkstras shortest path](Level-3/dijkstras_shortest_path.py): Implement Dijkstras shortest path algo | O(E * log(V)) | Level 3.
- [Bellman ford](Level-3/bellman_ford.py): Bellman ford algo to find shortest path in a graph | O(VE) | Level 3.
- [Triagles in graph](Level-2/triangles_in_graph.py): Given a graph(directed or undirected), count the number of triagles present | O(N^3) | Level 2.

## Union find(disjoint sets)
- [Implement disjoint sets](Level-2/union_find.py): Implement union find data structure with path compression and rank | O(1) | Level 2.
- [Undirected graph cycle detection](Level-2/graph_cycle_detection_union_find.py): Check if undirected graph has cycle or not using union find | O(V + E) | Level 2.
- [Kruskals algo - MST](Level-3/kruskals_algo_min_spanning_tree.py): Kruskals algorithm to find minimum spanning tree(MST) of undirected graph | O(ElogE) | Level 3.
- [Job sequencing problem](Level-4/job_scheduling_problem_using_disjoint_set.py): Given set of jobs with deadline and profit, find seq for max profit | O(N) | Level 4.

## Segment tree
- [Segment Tree - iterative](Level-3/segment-tree.py): Implement segment tree (iterative approach) | O(n) | Level 3.

## Binary indexed (Fenwick) tree
- [Binary indexed (Fenwick) tree](Level-3/binary-indexed-tree.py): Implement BIT (fenwick tree) | O(n) | Level 3.

## Cracking the coding interview(6th edition)
### 1. Arrays and strings
- [Check strings has unique characters](Level-1/unique_characters_check_in_string.c): Check if a string has all unique characters or not | Level 1.
- [2 strings are permutations](Level-2/strings_permutation_check.c): Check if 2 strings are permutations of each other or not | Level 2.
- [Update input string](Level-2/url_formatter.c): Update(in-place) input string to have space replaced with %20 | O(n) | Level 2.
- [Is permutation palindrome](Level-2/is_any_permutation_palindrome.c): Check if any permutation of given string is palindrome or not | Level 2.
- [Check 2 strings, one edit away](Level-2/are_two_strings_one_edit_away.c): Check if 2 strings are max one edit away or not | O(n) | Level 2.
- [String compression](Level-2/string_compression.c): Compress string, show count for consecutive repeating characters | O(n) | Level 2.
- [Rotate square matrix](Level-3/rotate_matrix.c): Rotate square matrix clockwise by 90 degrees | O(n) | Level 3.
- [Clear row and column if 0 found](Level-3/clear_matrix_rows_and_coulmns.c): If an element in a matrix is 0, its entire row and column are set to 0 | O(MxN) | Level 3.
- [2 strings are rotations](Level-2/are_2_strings_rotations.c): Check if 2 strings are rotations of each other or not | O(n) | Level 2.

### 2. Linked list
- [Remove duplicates from linked list](Level-2/remove_duplicates_from_linked_list.py): Remove duplicates from a linked list | O(n) time and space | Level 2.
- [kth from last in linked list](Level-3/kth_from_last_in_linked_list.py): Find kth element from last of a singly linked list | O(n) | Level 3.
- [Delete node from linked list](Level-2/delete_node_from_linked_list.py): Given only reference to an arbitary node of a linked list, delete that node | O(1) | Level 2.
- [Partition linked list](Level-2/partition_linked_list.py): Partition a linked lists with respect to a given value | O(n) | Level 2.
- [Sum digits of 2 linked list, digits in reverse order](Level-2/sum_of_linked_lists_reverse_order.py): Add 2 numbers stored in linked list in reverse order(12 is 2->1) | O(n) | Level 2.
- [Sum digits of 2 linked list, digits in forward order](Level-3/sum_of_linked_list_same_order.py): Add 2 numbers stored in linked list in forward order(12 is 1->2) | O(n) | Level 3.
- [Is linked list palindrome](Level-2/is_linked_list_palindrome.py): Check if linked list is palindrome or not | O(n) | Level 2.
- [Linked list intersection](Level-2/linked_list_intersection.py): Find if two linked list intersect each other | O(m + n) | Level 2.
- [Starting node of loop in linked list](Level-4/starting_of_loop_in_linked_list.py): Detect loop in linked list and find starting node of loop | O(n) | Level 4.

### 3. Stacks and queues
- Skipped code, mostly theoritical/design questions

### 4. Trees and graphs
- [Route between 2 nodes](Level-2/route_between_2_vertices.py): Given a directed graph, check if there is a route b/w 2 nodes | O(V + E) | Level 2.
- [Sorted array to BST](Level-3/sorted_list_to_bst.py): Given a sorted array, create binary search tree(BST) with minimal height | O(N) | Level 3.
- [List of depths](Level-2/list_of_depths.py): Binary tree to linked list for each level | O(N) | Level 2.
- [Is tree balanced](Level-2/check_tree_balanced.py): Check if a binary tree is balanced | O(N) | Level 2.
- [Is BST valid](Level-3/is_valid_bst.py): Check if a tree is valid BST or not | O(N) | Level 3.
- [BST inorder successor](Level-2/bst_inorder_successor.py): Find inorder successor of a node in binary search tree | O(h) | Level 2.
- [Project build order](Level-2/project_build_order.py): Given projects and there dependent projects, find build order. Graph topological sort problem | O(P + D) | Level 2.
- [LCA in binary tree](Level-3/lowest_common_ancestor_in_binary_tree.py): Find lowest common ancestor in binary tree | O(n) | Level 3.
- [LCA in BST](Level-2/lowest_common_ancestor_in_bst.py): Find lowest common ancestor in binary search tree | O(logn) | Level 2.
- BST sequence: Skipped, not clear
- [Check subtree](Level-2/check_subtree.py): Given 2 trees, check if one tree is exact subtree of another | O(n + km) | Level 2.
- [Check subtree - using preorder](Level-2/check_subtree_using_preorder.py): Given 2 trees, check if one tree is exact subtree of another | O(n + m) | Level 2.
- Get random node: Skipped, not clear
- [Paths with sum](Level-3/paths_with_sum_in_bst.py): Count number of paths in binary tree having given sum | O(nlogn) | Level 3.

### 5. Bit manipulation
- [Insert M into N](Level-2/insert_bits_from_M_into_N.c): Insert bits in M to N at positions between i and j | Level 2.
- [Decimal fraction to binary](Level-1/decimal_fraction_to_binary.c): Convert binary fraction number between 0 and 1 to binary representation | Level 1.
- [Flip a bit, get max sequence of 1s](Level-2/flip_a_bit_to_get_max_seq_of_ones.c): Flip a bit to get maximum sequence of 1s in sequence | O(b) | Level 2.
- [Next largest number, same set bits](Level-4/next_largest_same_num_of_bits_set.c): Given a positive integer, find next largest number having same number of set bits | O(b) | Level 4.
- [Previous number, same set bits](Level-4/previous_num_having_same_num_of_bits_set.c): Given a positive integer, find previous number having same number of set bits | O(b) | Level 4.
- Debugger: Explain what `((n & (n - 1)) == 0)` does
- [Bit flips required to convert](Level-2/bits_flipped_to_convert.c): Determine the number of bits need to flip to convert integer A to B | Level 2.
- [Swap odd and even bits](Level-2/swap_odd_even_bits.c): Program to swap odd and even bits in an integer | Level 2.
- [Update screen array, draw line](Level-3/draw_line.c): Update pixels array based on input pixel points to draw a line | Level 3.

### 6. Math and logic puzzles
- Skipped, puzzles and mathematical questions

### 7. Object oriented design
- LLD questions

### 8. Recursion and dynamic programming
- [Count ways to run n steps](Level-2/count_steps.py): Count the number of ways possible to run stairs having n steps (can take 1, 2 or 3 steps) | O(n) | Level 2.
- [Path of robot in grid](Level-3/robot_in_a_grid.py): Find path traversed by robot to reach from 0, 0 to row - 1, col - 1 | O(rc) | Level 3.
- [Find magic index](Level-2/magic_index.c): Find magic index from an sorted array having distinct elements | O(log(n)) | Level 2.
- [Find magic index, duplicates allowed\*](Level-3/magic_index_with_duplicates.c): Find magic index from an sorted array (having duplicates) | O(log(n)) | Level 3.
- [Generate all subsets of a set](Level-2/generate_all_subsets.py): Generate all subsets of a given set | O(n * 2^n) | Level 3.
- [Generate all subsets, binary method\*](Level-2/generate_all_subsets_binary_method.py): Generate all subsets of a given set, binary representation method | O(n * 2^n) | Level 2.
- [Multiply 2 integers](Level-2/multiply_integers.c): Multiply 2 positive integers without using multiply operator | O(log(s)) | Level 2.
- [Tower of hanoi](Level-3/tower_of_hanoi.c): Print steps to solve tower of hanoi problem for n disks | O(2^n) | Level 3.
- [Compute all permutations - Unique chars\*](Level-3/compute_all_permutations_unique_chars.py): Compute all permutations of a given string having unique characters | O(n^2 * n!) | Level 3.
- [Compute all permutations - Repeated chars](Level-4/compute_all_permutations_non_unique_chars.py): Compute all permutations of a given string having repeated characters | O(n^2 * n!) | Level 4.
- [Pair of valid parens](Level-3/pair_of_parens.py): Print all valid combinations of n pairs of parentheses | O(2^n) | Level 3.
- [Paint fill](Level-2/paint_fill.py): Fill surrounding area with new color | O(r * c) | Level 2.
- [Ways to represent n cents](Level-4/ways_to_represent_n_cents.c): Find number of ways to represent n cents using quarters, dimens, nickels and pennies | O(n * NUM_OF_DENOMS) | Level 4.
- [Place 8 queens on 8x8](Level-4/place_eight_queens.py): Print all ways to arrange 8 queens on a 8x8 chessboard so that none attack any other | O(GRID_SIZE^3) | Level 4.
- [Stack boxes to maximize height](Level-4/stack_boxes.py): Stack boxes to to have maximum height | O(n) | Level 4.
- [Boolean evaluation ways](Level-3/boolean_evaluation_ways.py): Total number of ways to get expected boolean result from a boolean expression | O(n) | Level 3.

### 9. System design and scalability
- System design questions

### 10. Sorting and searching
- [Merge 2 sorted arrays, in place](Level-2/merge_2_sorted_arrays_in_place.c): Merge 2 sorted arrays, in place | O(A + B) | Level 2.
- [Groups anagrams](Level-2/group_anagrams.py): Write a method to sort an array of strings so that all the anagrams are next to each other. | O(MxNxlog(N)) | Level 2.
- [Search element in rotated sorted array](Level-3/search_in_rotated_sorted_array.c): Search an element from rotated sorted array | Level 3.
- [Sorted search, no size](Level-2/search_in_infinite_sorted_array.c): Search an element from an infinite sized(size of array not given) sorted array | O(log(p)) | Level 2.
- [Search in sparse array](Level-2/search_string_in_sparse_array.py): Search a string from sparsely populated array of strings (other places has empty string) | O(log(n)) | Level 2.
- Sort big file: Skipped code, conceptual
- Missing int: Skipped code, conceptual
- [Find all duplicates in array](Level-2/find_duplicates_in_4k_space.c): Find all duplicates in array (range 1 to 32,000) with memory 4k | O(n) | Level 2.
- [Search in sorted matrix](Level-2/sorted_matrix_search.c): Search for an element in a matrix having each row and each column sorted | O(M + N) | Level 2.
- [Rank from stream](Level-3/rank_from_stream.c): Find rank of an element from a stream of data | O(logn) | Level 3.
- [Rank from stream - python](Level-3/rank_from_stream.py): Find rank of an element from a stream of data | O(logn) | Level 3.
- [Peaks and valleys, sorting method](Level-2/peaks_and_valleys_O_nlogn.py): Arrange an unsorted in alternating sequence of peaks and valleys | O(NlogN) | Level 2.
- [Peak and valley, O(n) method\*](Level-3/peaks_and_valleys_O_n.py): Arrange an unsorted array in alternating sequence of peaks and valleys | O(n) | Level 3.

### 11. Testing
- Skipped

### 12. C and C++
- Skipped

### 13. Java
- Skipped

### 14. Databases
- General DB concepts and questions

### 15. Threads and locks
- Questions on thread and concurrency issues

### 16. Moderate
- [Swap 2 numbers](Level-1/swap_2_numbers.py): Swap 2 numbers, inplace | O(1) | Level 1.
- [Word frequency](Level-2/word_frequency.py): Find frequency of words in list of words | O(N) | Level 2.
- Intersection: Skipped, mathematical
- Tic tac win: Skipped code, design
- [Factorial zeros](Level-2/factorial_zeros.py): Compute number of trailing 0s in n factorial | log(n) | Level 2.
- [Smallest difference](Level-2/smallest_difference.py): Find smallest difference b/w pair of elements from 2 arrays | O(Alog(A) + Blog(B)) | Level 2.
- Number max: Skipped, do in C language
- English int: Skipped code
- Arithmetic operations: Skipped code
- [Year with max population](Level-3/year_with_max_population.py): Given birth and death years, find year with max population | O(Y + P) | Level 3.
- [Diving board](Level-2/diving_board.py): Find number of lengths possible using 2 lengths k times | O(2^k) | Level 2.
- [Diving board - optimized](Level-3/diving_board_optimized.py): Find number of lengths possible using 2 lengths k times | O(k) | Level 3.
- XML encoding: Skipped, uses some predefined methods - refer random/practice/xml_encoding.py
- Bisect squares: Skipped, not clear
- Best line: Skipped code
- [Master mind](Level-2/master_mind_game.py): Given solution and guess for 4 slots of RGBY string, find hits and pseudo hits | O(n) | Level 2.
- [Sub sort](Level-3/sub_sort.py): Find indices of array which needs to be sorted to make whole array sorted | O(N) | Level 3.
- [Largest sum of subarray](Level-3/largest_sum_of_subarray.c): Given an unsorted array(+ve and -ve numbers), find max sum possible of a subarray | Kadane's algo | O(N) | Level 3.
- Pattern matching: Skipped, not clear
- [Pond sizes](Level-2/pond_sizes.py): Given matrix having water(0) and land, find the size of ponds | O(MN) | Level 2.
- T9 number to string: Skipped code
- [Sum swap](Level-3/sum_swap.py): Find pair of elements from 2 given array to make sum of 2 arrays same | O(A + B) | Level 3.
- Langton's Ant: Skipped code
- [Rand7 from rand5](Level-3/rand7_using_rand5.py): Implement rand7 using rand5 | Level 3.
- [Pairs having given sum](Level-2/pairs_having_given_sum.c): Given an array and required sum, find pairs in array that sums to required sum | O(n) time and space | Level 2.
- [Pairs with sum - python](Level-2/pairs_with_sum.py): Find all pairs of integers with an array which sum to specified sum | O(N) | Level 2.
- [LRU cache impelementation](Level-3/lru_cache.py): Put and Get operations implemented in LRU cache | Level 3.
- [Evaluate expression](Level-3/evaluate_expression.py): Evaluate arithmetic expression(without parentheses) | O(N) | Level 3.

### 17. Hard
- [Add 2 numbers](Level-2/add_2_numbers.py): Add 2 numbers without arithmatic operations | OlogN) | Level 2.
- [Shuffle cards](Level-2/shuffle_cards.py): Given deck of cards, shuffle it | O(N) | Level 2.
- [Random set](Level-2/random_set.py): Generate random set having m elements from an array having n elements | O(N) | Level 2.
- Missing number: Skipped, not clear
- [Letters and numbers](Level-3/letter_and_numbers.py): Find longest subarry having same number of letters and numbers | O(N) | Level 3.
- Count 2's: Skipped, not clear
- [Baby names](Level-3/baby_names_synonyms.py): Get count of synonym names | O(B + P) | Level 3.
- [Circus tower](Level-3/max_circus_tower.py): Given list of pair of words, find longest increasing sequence | O(nlogn) | Level 3.
- [Kth multiple - 3, 5 and 7](Level-3/kth_multiple_3_5_7.py): Find kth number such that the only factors are 3, 5 and 7 | O(k) | Level 3.
- [Majority element from array](Level-2/majority_element_in_array.c): Find majority(more than n/2 times) element from an array | Moore's voting algo | O(N) | Level 2.
- [Majority element from array - python](Level-2/majority_element.py): Find majority(more than n/2 times) element from an array | Moore's voting algo | O(N) | Level 2.
- [Word distance](Level-2/word_distance.py): Given list of words, find shortest distance b/w 2 given words | O(A + B) | Level 2.
- [Binary tree to doubly linked list](Level-3/binary_tree_to_doubly_linked_list.py): Convert a binary tree to doubly linked list | O(N) | Level 3.
- [Re-space](Level-4/re-space-sentence.py): Add spaces in sentence to have min unrecognized chars | O(N^2) | Level 4.
- [Smallest K numbers](Level-3/find_k_smallest_nums.py): Given unsorted array find k smallest numbers | O(N) | Level 3.
- [Longest word](Level-3/longest_word.py): Given list of words, find longest word that can be found using other words | O(nlogn + L^2) | Level 3.
- [The masseuse](Level-2/max_minutes.py): Given list of meetings, find max meeting minutes without taking any adjacent meetings | O(N) | Level 2.
- [The masseuse - space optimized](Level-3/max_minutes_space_optimized.py): Given list of meetings, find max meeting minutes without taking any adjacent meetings | O(N) | Level 3.
- [Multi search](Level-3/multi_search.py): Given a string and list of smaller strings, search all smaller strings in bigger string - trie using dict | O(b^2 + kt) | Level 3.
- [Multi search - optimal](Level-3/multi_search_optimal.py): Given a string and list of smaller strings, search all smaller strings in bigger string | O(kt + bk) | Level 3.
- [Shortest supersequence](Level-2/shortest_supersequence.py): Find smallest subarray of bigger array having all elements of smaller array | O(SB^2) | Level 2.
- [Missing number](Level-2/find_missing_number.py): Given an array having numbers from 1 to N but one missing, find missing | O(N) | Level 2.
- [Missing 2 numbers](Level-2/find_2_missing_numbers.py): Given an array having numbers from 1 to N but 2 numbers missing, find missing numbers | O(N) | Level 2.
- [Track median, stream of numbers](Level-4/track_median_stream_of_nums.py): Keep track of median from stream of numbers | O(logn) track and O(1) get median | Level 4.
- [Volume of histogram](Level-3/volume_of_histogram_optimized.py): Given set of histogram bars, find max water logged | O(N) | Level 3.
- Word transform: Skipped, not clear
- Max black square: Skipped, not clear
- [Max submatrix](Level-2/max_submatrix.py): Given NxN matrix having +ve and -ve numbers, find submtrix having max sum | O(N^6) | Level 2.
- Word rectangle: Skipped code
- [Sparse similarity](Level-2/sparse_similarity.py): Given list of documents, find similarity b/w pairs | O(D^2 * W) | Level 2.

## Uncategorised
- [Karatsuba algo](Level-4/karatsuba.py): Efficient way to multiply 2 numbers, karatsuba algo | O(n^1.58) | Level 4.
- [Level order tree traversal](Level-2/level_order_tree_traversal.c): Level order traversal of a tree | O(n^2) | Level 2.
- [Level order tree traversal - python](Level-2/level_order_tree_traversal.py): Level order traversal of a tree | O(n^2) | Level 2.
- [Level order tree traversal using queue\*](Level-2/level_order_tree_traversal_using_queue.c): Level order traversal of a tree using queue | O(n) time and space | Level 2.
- [Level order tree traversal using queue - python\*](Level-2/level_order_tree_traversal_using_queue.py): Level order traversal of a tree using queue | O(n) time and space | Level 2.
- [Edit distance - O(3^m)](Level-2/edit_distance.py): Find minimum operations required to convert a source string to target string | O(3^m) | Level 3.
- [Edit distance DP approach](Level-3/edit_distance_dp.c): Find minimum operations required to convert a source string to target string | O(MxN) | Level 3.
- [Edit distance DP approach - python](Level-3/edit_distance_dp.py): Find minimum operations required to convert a source string to target string | O(MxN) | Level 3.
- [Flip your caps](Level-3/flip_your_cap.c): You all will conform | flip your cap(s) puzzle | Level 3.
- [Find 1-D peak](Level-2/find_peak_element.c): Find 1-D peak from an array | Level 2.
- [Find 2-D peak](Level-3/find_2d_peak.c): Find 2-D peak from a 2-D array | Level 3.
- [Find second largest number](Level-1/second_largest_in_array.c): Find second largest number from an array | Level 1.
- [Find element with rank k](Level-2/rank_k_element_in_2_sorted_array_O_k.c): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted | O(k) | Level 1.
- [Find element with rank k - python](Level-2/rank_k_element_in_2_sorted_arrays_O_k.py): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted | O(k) | Level 2.
- [Find element with rank k - log(k)\*](Level-3/rank_k_element_in_2_sorted_array_log_k.c): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted having distinct elements | O(log(k)) | Level 3.
- [Find element with rank k - log(k), python\*](Level-3/rank_k_element_in_2_sorted_array_log_k.py): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted having distinct elements | O(log(k)) | Level 3.
- [Longest increainng subsequence - O(n^2)](Level-3/longest-increasing-subsequence.c): Find length of longest increasing subsequence from an unsorted array | O(n^2) | Level 3.
- [Longest increainng subsequence - O(nlogn)\*](Level-3/longest-increasing-subsequence-nlogn.c): Find length of longest increasing subsequence from an unsorted array | O(nlogn) | Level 3.
- [Binary representation](Level-1/binary_representation.c): Print binary representation of an integer | Level 1.
- [Knapsack problem](Level-4/knapsack.c): Given a knapsack (bag with capacity W), and N items having weights and values, select items such that value is maximized | O(nxW) | Level 4.
- [Knapsack problem - python](Level-4/knapsack.py): Given a knapsack (bag with capacity W), and N items having weights and values, select items such that value is maximized | O(nxW) | Level 4.
- [Knapsack problem, Maximize weight](Level-4/knapsack_maximize_weight.c): Given a knapsack, maximize weights that can be carried in given knapsack, No item values given | O(nxW) | Level 4.
- [Knapsack problem, Maximize weight - python](Level-4/knapsack_maximize_weight.py): Given a knapsack, maximize weights that can be carried in given knapsack, No item values given | O(nxW) | Level 4.
- [Min from sorted rotated](Level-3/min_in_sorted_rotated_array.c): Find min element from sorted rotated array | O(log(n)) | Level 3.
- [Tree level with max width](Level-2/level_with_max_width.c): Find tree level having max width/nodes | O(n) | Level 2.
- [Tree level with max width - python](Level-2/level_with_max_width.py): Find tree level having max width/nodes | O(n) | Level 2.
- [Print fibonacci numbers](Level-1/fibonacci.c): Print first n fibonacci numbers | O(n) | Level 1.
- [Print prime numbers](Level-4/print_all_prime_numbers.py): Print all prime numbers from 1 to n, sieve of eratosthenes method | O(sqrt(n)log(log(n))) | Level 3.
- [Find min range, k sorted arrays](Level-3/min_range_k_sorted_arrays.c): Find min range which will have elements from all k arrays | O(n * k) | Level 3.
- [Min positive integer missing](Level-2/smallest_positive_missing.py): Find minimum positive number missing from an array having random integers | O(n) | Level 2.
- [Min positive integer missing - O(1) space\*](Level-3/smallest_positive_num_missing_O_1_space.c): Find minimum positive number missing from an array having random integers | O(n) | Level 3.
- [Create sequence of 'a' and 'b'](Level-3/three_non_consecutive_ab.py): Given 2 numbers A and B, create sequence with at max 2 consecutive 'a' and 'b' | O(A + B) | Level 3.
- [Check strings same](Level-1/case_insensitive_strcmp.c): Write a function to check if 2 strings are same, ignoring case | Level 1.
- [Multiple of 4](Level-1/check_multiple_of_4.c): Check if a number of 4 or not | Level 1.
- [Find 7n/8](Level-1/find_7by8_of_n.c): Find 7n/8 without using * and / operators | Level 1.
- [Clear both elements](Level-1/unset_both.c): Clear both array elements having at least a 0 and 1 | Level 1.
- [Binary palindrom](Level-2/is_num_binary_palindrdom.c): Check if a numbers binary representation is palindrome or not | Level 2.
- [Product of elements](Level-2/product_array_elements_except_self.c): Create a array having product of all elements except element at self index | Level 2.
- [Next word in dictionary](Level-2/next_word_in_dictionary.py): Given a string, find next dictionary word | Level 2.
- [Find log(n)](Level-1/find_log_n.c): Write one liner program to find log(n) with some base | O(n/b) | Level 1
- [Binary search tree](Level-2/binary_search_tree.c): BST insert, traverse, delete operations | Level 2.
- [Binary search tree - python](Level-2/binary_search_tree.py): BST insert, traverse, delete operations | Level 2.
- [AVL trees](Level-3/avl_balanced_tree.c): Implement AVL balanced trees - Insert, delete, search | Level 3.
- [AVL trees - python](Level-3/avl_balanced_tree.py): Implement AVL balanced trees - Insert, delete, search | Level 3.
- [Linked list in python](Level-1/linked_list.py): Implement linked list in python.
- [Reverse linked list](Level-3/reverse_linked_list.py): Reverse a linked list | O(n) | Level 3.
- [Happy number](Level-2/is_happy_number.c): Check if a given number is happy or not | O(n) | Level 2.
- [Median in 2 sorted arrays](Level-4/median_in_2_sorted_arrays.py): Find median from 2 sorted arrays | O(log(min(m + n))) | Level 4.
- [Longest palindrome](Level-3/longest_palindrome_in_a_string.py): Find longest palindrome from a given string | O(n^2) | Level 3.
- [Spiral matrix](Level-3/spiral_matrix.py): Given a number N, create matrix having values from 1 to N^2 in spiral form | O(N^2) | Level 3.
- [Print matrix in spiral](Level-3/print_matrix_in_spiral.py): Given a matrix, print its elements in clockwise spiral form | O(MxN) | Level 3.
- [Print matrix in spiral reverse](Level-3/print_matrix_in_spiral_reverse.py): Given a matrix, print its elements in anticlockwise spiral form | O(MxN) | Level 3.
- [Look and say sequence](Level-2/look_and_say_seq.py): Print look and say sequence for given number of input lines | O(N) | Level 2.
- [LCM and HCF](Level-1/gcd_and_lcm.py): Find GCD(or HCF) and LCM of 2 numbers | Level 1.
- [Separate positives and negatives](Level-2/separate_positive_and_negative_nums.c): Move all positive to start and negative to end of array, 2 pointer problem, problem adapted from sort array of 0s and 1s | O(n) | Level 2.
- [Track kth largest, stream of numbers](Level-2/track_kth_largest_stream_of_nums.py): Keep track of kth largest number from a stream of numbers | O(k) | Level 2.
- [Check prime](Level-2/is_prime.go): Check if a given number is prime or not | O(sqrt(n)) | Level 2.
- [Find square root](Level-4/babylonian_square_root.go): Find square root of a number using babylonian convergence method | Level 4.
- [Substring matching, Rabin karp](Level-3/rabin_karp.c): Implement rabin karp algo for substring matching | O(m + n) | Level 4.
- [Substring matching, Rabin karp - python](Level-3/rabin_karp.py): Implement rabin karp algo for substring matching | O(m + n) | Level 4.
- [Connections in matrix](Level-2/connections_in_matrix.py): Count possible connections in matrix of 0s and 1s | O(MxN) | Level 2.
- [Next power of 2](Level-1/next_pow_of_2.c): Find next power of 2 for a given number | Level 1.
- [Round off float](Level-1/round_off.c): Round off a float number to nearest integer | Level 1.
- [Sum of digits](Level-1/sum_num.c): Find sum of digits of a given integer | Level 1.
- [Generic linked list](Level-3/generic_linked_list.c): Generic linked list in C language | Level 3.
- [Count frequency of numbers](Level-1/frequency_of_elements.c): Count frequency of numbers in array | O(N) time and space | Level 1.
- [Count frequency, without space](Level-2/frequency_of_elements_without_space.c): Count frequency of numbers in array | O(N) time and O(1) space | Level 2.
- [Repeating numbers](Level-2/find_repeating_elements.c): Find all repeating numbers in a array | O(N) | Level 2.
- [Inversion of 3](Level-2/inversion_of_3.c): Find number of combinations which follows: a[i] > a[j] > a[k] with i < j < k in a unsorted array | O(N^2) | Level 2.
- [Equilibrium index](Level-2/find_equilibrium_index.c): Find equilibrium index in a array(Equal sum of left and right sub array) | O(N) | Level 2.
- [Leaders in array](Level-1/leaders_in_array.c): Print all leaders in array(greater than all elements right to that) | O(N) | Level 1.
- [Odd occurring numberr](Level-2/find_2_odd_occurring_numbers.c): A array has all numbers occurring even numbers of times and 2 occurring odd number of times, find these 2 numbers | O(N) | Level 2.
- [Even occurring numbers](Level-3/find_2_even_occurring_numbers.c): Find 2 numbers in array(numbers from 1 to n - 2) occurring even number of times, other all occur odd number of times | O(N) | Level 3.
- [Common in 3 sorted arrays](Level-1/common_elements_in_3_sorted_array.c): Find common elements in 3 sorted arrays | O(n1 + n2 + n3) | Level 1.
- [Sorted subsequence of size 3](Level-3/sorted_subsequence_of_size_3.c): Find sorted subsequence of size 3 in an unsorted array | O(N) time and space | Level 3.
- [Sorted subsequence of size 3, O(1) space](Level-4/sorted_subsequence_of_size_3_without_space.c): Find sorted subsequence of size 3 in an unsorted array | O(N) time | Level 4.
- [Max average of len K](Level-2/max_average_of_len_k.c): Find sub array of len K having maximum average | O(N) | Level 2.
- [Subarray having given sum](Level-3/subarray_having_given_sum.c): Find a sub array(positive numbers) having sum | O(N) | Level 3.
- [Triplets in GP](Level-2/find_triplets_in_gp.c): Given a sorted array, print triplets in GP | O(N^2) | Level 2.
- [ASCII to int](Level-2/atoi_using_bitwise.c): Given an ascii string convert it to integer, atoi conversion | O(N) | Level 2.
- [Largest sum of rotated subarray](Level-3/largest_sum_of_rotated_subarray.c): Find max sum of rotated subarray | O(N) | Level 3.
- [Triplet having given sum](Level-2/triplets_with_given_sum.c): Find triplets in a sorted array which sums to a given sum | O(N^2) | Level 2.
- [Triplet having smaller sum](Level-2/triplets_with_smaller_sum.c): Find triplets in a sorted array which sums less than given sum | O(N^2) | Level 2.
- [Distinct pairs](Level-4/number_of_distinct_pairs.c): Find number of distinct pairs in unsorted array | O(N) | Level 4.
- [Is array subset](Level-1/is_subset_of_array.c): Given 2 sorted arrays, check if arr2 is subset of arr1 | O(N) | Level 1.
- [Count 0s in sorted array](Level-2/count_num_of_zeros.c): Given a sorted array of 1s and 0s, find number of 0s in that array | O(logn) | Level 2.
- [Merge required to make palindrome](Level-2/num_of_merges_to_make_palindrome.c): Number of merge operations required to make an unsorted array palindrome | O(N) | Level 2.
- [Jolly jumper sequence](Level-2/is_jolly_jumper_sequence.c): Check if an unsorted array is jolly jumper sequence | O(N) | Level 2.
- [Min number not possible](Level-4/min_number_not_possible.c): Find the min num not possible as any subset of sorted array | O(N) | Level 4.
- [Subarray with equal 0 and 1](Level-2/subarray_with_equal_0_and_1.c): Find max subarray having equal 0s and 1s | O(N^2) | Level 2.
- [Max diff btwn elements](Level-2/max_diff_btwn_2_elements.c): Find max diff btwn 2 elements in array such that larger appears later | O(N) | Level 2.
- [Maximize index diff](Level-3/maximize_index_diff.c): Find max(j - i) such that A[j] > A[i] | O(N) | Level 3.
- [Max subarray len, arrange contiguous](Level-2/max_contiguous_subarray_len.c): Max subarray len whose elements can be arranged in contiguous sequence | O(N^2) | Level 2.
- [String anagram having given md5 hash](Level-3/anagram_having_given_hash.py): Given an input string, md5 hashes and long list of words, find anagram of given string which has given hash | Level 3.
- [JSON parser](Level-2/json_parser.py): Partial JSON parser, Ecko question | Level 2.
- [Max product of subarray, size k](Level-2/max_product_of_subarray_size_k.c): Find max product of a subarray, size k | O(N) | Level 2.
- [Max and min product of subset](Level-2/max_and_min_prod_of_subset.c): Find max and min product of subset in array | O(N) | Level 2.
- [Max subarray product, 2 traversal](Level-3/max_subarray_product_2_traversal.c): Find max subarray product, 2 traversals used | O(N) | Level 3.
- [Max subarray product, single traversal\*](Level-3/max_subarray_product.c): Find max subarray product, single traversal | O(N) | Level 3.
- [Triplet with max product](Level-2/triplet_with_max_product.c): Find triplet in array with max product | O(N) | Level 2.
- [Max product - index diff and min](Level-2/max_product_of_indx_diff_and_min.c): Find max value of abs(i - j) * MIN(a[i], a[j]) from unsorted array | O(N) | Level 2.
- [Max product of increasing triplet](Level-2/max_prod_of_increasing_triplet.c): Find max product of increasing triplet from unsorted array | O(N^2) | Level 3.
- [Max min, value index pair](Level-2/max_min_value_index_pair.c): Find max value of (a[i] - i) - (a[j] - j) from an unsorted array | O(N) | Level 2.
- [Min unique array sum](Level-2/min_unique_array_sum.py): Increment array elements until all elements become unique and find sum of all unique elements | O(N) | Level 2.
- [Max K such that K elements >= K](Level-2/max_k_having_k_greater_elements.c): Find max k such that array has k elements greater than equal to k | O(N) | Level 2.
- [Min subarray len, sum > X](Level-2/min_subarray_len_with_sum_greater_than_x.c): Min subarray len having sum greater than X | O(N) | Level 2.
- [Max sum with no elements adjacent](Level-3/max_sum_with_no_elements_adjacent.c): Find max sum with no 2 elements adjacent | O(N) | Level 3.
- [Longest bitonic subsequence](Level-3/longest_bitonic_subsequence.c): Find longest bitonic subsequence in a array | O(N) | Level 3.
- [Rotations to maximize sum(i * a[i])](Level-2/num_of_rotations_to_maximize_sum.c): Find number of right rotations required to maximize sum(i * a[i]) | O(N) | Level 2.
- [RGB merging, get min count](Level-2/RGB_merging_min_count.c): Array has RGBs, merge different element and get min elements left O(N) | Level 2.
- [Count strictly increasing subarrays](Level-2/count_strictly_increasing_subarrays.c): Count the number of strictly increasing subarrays possible | O(N) | Level 2.
- [Count subarrays with even sum](Level-3/count_subarrays_with_even_sum.c): Given an unsorted array, count the number of subarrays with even sum | O(N) | Level 3.
- [Smallest number missing](Level-2/find_smallest_num_missing.c): Given a sorted array - size n, elements 0 to n - 1. Find smallest number missing | O(logn) | Level 2.
- [Max sum path, 2 sorted arrays](Level-3/max_sum_path_of_2_sorted_arrays.c): Given 2 sorted arrays, find max sum path | O(M + N) | Level 3.
- [Min distance between 2 elements - O(N^2)](Level-2/min_distance_bw_2_nums_O_n2.c): Find min distance 2 elements in unsorted array | O(N^2) | Level 2.
- [Min distance between 2 elements - O(N)](Level-2/min_distance_bw_2_nums_O_n.c): Find min distance 2 elements in unsorted array | O(N) | Level 2.
- [Min distance between 2 elements, python - O(N)](Level-2/min_dist_bw_2_nums_O_n.py): Find min distance 2 elements in unsorted array | O(N) | Level 2.
- [Stock buy sell to maximize profit](Level-3/stock_buy_sell_max_profit.c): Given stock prices, find days to buy and sell so that profit can be maximized | O(N) | Level 3.
- [Merge 2 sorted arrays as contiguous sorted](Level-4/merge_2_sorted_array_as_contigous_sorted.c): Given 2 sorted arrays, merge them as contiguous sorted arrays | O(M * N) | Level 4.
- [Steps to get given array](Level-2/steps_to_get_given_array.c): Find the number of steps required to get given array from all 0s array | O(K * N) | Level 2.
- [Index of 0 flipped to get max 1 seq](Level-3/indx_of_0_for_max_1_seq.c): Find the index of 0 to be changed to 1 to get max 1s sequence | O(N) | Level 3.
- [Max sum after k negations](Level-2/max_sum_after_k_negations.c): Find max sum of array elements after k negations | O(K * N) | Level 2.
- [Max 0s after flipping subarray - O(N^2)](Level-2/max_0s_in_array_after_subarray_flip_n2.c): Find max 0s in binary array after flipping a subarray | O(N^2) | Level 2.
- [Max 0s after flipping subarray - O(N)](Level-3/max_0s_in_array_after_subarray_flip_n.c): Find max 0s in binary array after flipping a subarray | O(N) | Level 3.
- [Find floor and ceil in array - O(N)](Level-1/find_ceil_n_floor_in_array_O_n.c): Find floor and ceil of X from sorted array | O(N) | Level 1.
- [Find floor and ceil in array](Level-2/find_ceil_n_floor_in_array_logn.c): Find floor and ceil of X from sorted array | O(logn) | Level 2.
- [Find floor and ceil in array - python](Level-2/find_ceil_and_floor_in_sorted_array.py): Find floor and ceil of X from sorted array | O(logn) | Level 2.
- [Convert integer to comma format](Level-2/format_nums.cc): Given an integer, convert it to string with comma notation - Indian and US | O(N) | Level 2.
- [Reverse sentence](Level-2/reverse_sentence.cc): Given a sentence, reverse it's individual words | O(N) | Level 2.
- [Reverse sentence - python](Level-2/reverse_sentence.py): Given a sentence, reverse it's individual words | O(N) | Level 2.
- [Is symmetric tree](Level-2/is_tree_symmetric.py): Check if a given tree is symmetric/self mirror image or not | O(N) | Level 2.
- [Find mirror image](Level-2/find_tree_mirror.py): Find mirror image of a given binary tree | O(N) | Level 2.
- [Left and right views of tree](Level-2/left_right_views_of_tree.py): Print left and right views of binary tree | O(N) | Level 2.
- [Left/right rotate array](Level-3/rotate_array.py): Rotate array left or right by given number of times | O(N) | Level 3.
- [Knight's shortest path](Level-3/knights_shortest_path.py): Find shortest path from source to destination for a knight on NxN board | BFS | O(N^2) | Level 3.
- [Tree inorder iterative](Level-2/tree_inorder_traversal_iterative.py): Tree inorder traversal without recursion, iterative approach using stack | O(N) | Level 2.
- [Tree preorder iterative](Level-2/tree_preorder_traversal_iterative.py): Tree preorder traversal without recursion, iterative approach using stack | O(N) | Level 2.
- [Tree postorder iterative](Level-2/tree_postorder_traversal_iterative.py): Tree postorder traversal without recursion, iterative approach using stack | O(N) | Level 2.
- [Vertical level order tree traversal](Level-2/vertical_level_order_tree_traversal.py): Perform vertical level order tree traversal | O(n) | Level 2.
- [Top view of binary tree](Level-2/top_view_binary_tree.py): Print elements seen from top view of a binary tree | O(N) | Level 2.
- [Bottom view of binary tree](Level-2/bottom_view_binary_tree.py): Print elements seen from bottom view of a binary tree | O(N) | Level 2.
- [Tree nodes level by level](Level-2/print_tree_level_by_level.py): Print binary tree nodes level by level in separate lines | O(N) | Level 2.
- [Nodes with distance K in binary tree](Level-4/node_with_k_distance_in_tree.py): Print all nodes which are K distance away from given node in binary tree | O(N) | Level 4.
- [Tree spiral level order](Level-3/tree_spiral_level_order.py): Print tree nodes in spiral level order | O(N) | Level 3.
- [Find diameter(width) of tree](Level-2/diameter_of_tree.py): Find diameter(or max width) of a tree | O(N) | Level 2.
- [Nodes with K distance from leaf](Level-3/tree_nodes_with_k_distance_from_leaf.py): Nodes with k distance from leaf in tree | O(N) | Level 3.
- [Sort array of 0s, 1s and 2s](Level-2/sort_array_of_0s_1s_and_2s.py): Sort array having 0s, 1s and 2s | O(N) | Level 2.
- [Kth largest number, Heap method](Level-2/find_kth_largest_num.py): Find Kth largest number from an unsorted array | O(k + (n-k)logk) | Level 2.
- [Kth smallest number, QuickSort method](Level-3/find_kth_smallest_num.py): Find Kth smallest number from an unsorted array | O(N) | Level 3.
- [Longest common subsequence](Level-3/longest_common_subsequence.py): Find LCS in given 2 strings | O(M * N) | Level 3.
- [Subset having equal sum](Level-3/subset_equal_sum.py): Given an array, check if it can be partitioned in 2 subsets having equal sum | O(N * SUM) | Level 3.
- [Kth smallest from BST](Level-3/kth_smallest_from_bst.py): Find Kth smallest number from a BST | O(K) | Level 3.
- [Next greater element](Level-3/next_greater_element.py): Print NGEs for all elements in given array | O(N) | Level 3.
- [Cut rod to have max profit](Level-3/cut_rod_to_max_profit.py): Find max profit obtainable by cutting up the rod and selling the pieces | O(N^2) | Level 3.
- [Max product, rope cutting](Level-3/max_product_cutting.py): Find max product obtained by cutting rope of different sizes | O(N^2) | Level 3.
- [Custom split string](Level-2/custom_split.py): Split string with substrings enclosed in quotes as single | O(N) | Level 2.
- [Infix to postfix expression converter](Level-3/infix_to_postfix.c): Convert infix expression into postfix | O(N * N) | Level 3.
- [Job sequencing problem](Level-3/job_scheduling_problem.py): Given set of jobs with deadline and profit, find seq for max profit | O(N^2) | Level 3.
- [Subarray sum less than K](Level-3/subarrays_sum_less_than_k.py): Count subarrays having sum less that k | O(N) | Level 3.
- [Smallest num not subset sum](Level-3/not_subset_sum.py): Given sorted array, find min num which is not subset sum of array | O(N) | Level 3

## Other problems
- https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
