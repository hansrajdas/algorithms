/*
 * Date: 2018-08-02
 *
 * Description:
 * There is a rod of length n and an array having lengths (l < n) where bigger
 * rod has marks and at these marks rod needs to be chopped. Cost of cutting rod
 * is equal to product of 2 smaller lengths that we got after cutting rod. So
 * task is to minimize the cost of cutting the whole rod into pieces at the
 * given lengths with minimum cost. In what sequence should this rod be chopped
 * so that it costs minimum.
 *
 * For example: length of rod, n = 10 and lengths = [2, 4, 7]
 *
 * Not clear, refer: 1st problem from https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec24.pdf
 *
 * Approach:
 *
 * Complexity:
 * O(n^3)
 */
