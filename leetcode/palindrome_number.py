class Solution:

    def isPalindrome(self, x: int) -> bool:
        counter = 0
        num_to_str = str(x)
        bool_list = []
        last_index = 1
        while counter < len(num_to_str):
            bool_list.append(num_to_str[counter] == num_to_str[-last_index])
            counter = counter + 1
            last_index = last_index + 1
        return all(bool_list)


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
