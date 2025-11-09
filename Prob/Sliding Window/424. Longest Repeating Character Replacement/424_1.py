# O(n*26)) time | O(1) space

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l,maxr=0,0

        for r in range(len(s)):
            count[s[r]]= count.get(s[r],0)+1
            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
                if count[s[r]]==0:
                    del count[s[r]]
            maxr=max(maxr,r-l+1)
        return maxr

def main():
    inputs = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
        ("AAABBBCC", 2, 5),
    ]

    for s, k, expected in inputs:
        obj = Solution()
        result = obj.characterReplacement(s, k)

        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: s='{s}', k={k}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()