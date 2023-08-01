class Solution:

    def romanToInt(self, s: str) -> int:
        sum_roman = 0
        all_rome = {"CD": 400, "CM": 900, "XC": 90, "XL": 40, "IV": 4, "IX": 9,
                    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        counter = 0
        while counter < len(s):
            for key, value in all_rome.items():
                if key in s:
                    sum_roman = sum_roman + value
                s = s.replace(key, '', 1)
        return sum_roman


if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("MCMXCIV"))
