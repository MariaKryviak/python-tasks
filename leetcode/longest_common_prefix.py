from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for c in first_word:
            flag = []
            for word in strs:
                flag.append(word.startswith(first_word))
            if all(flag):
                return first_word
            else:
                first_word = first_word[0:-1]
        return ""


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([""]))
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
