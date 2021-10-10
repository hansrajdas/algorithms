class Solution:
    def restoreIpAddresses(self, s):
        """This is function doc."""
        def solve(i, values, results):
            # import pdb;pdb.set_trace()
            print(i, values)
            if i == len(s) and len(values) == 4:
                results.append('.'.join(values))
                return
            for j in range(i, min(i + 3, len(s))):
                if 0 <= int(s[i:j+1]) <= 255:
                    values.append(s[i:j+1])
                    solve(j+1, values, results)
                    values.pop()

        print(len(s), s)
        results = []
        solve(0, [], results)
        print(results)
        return results

s = Solution()
print(s.restoreIpAddresses("25525511135"))  # 1
