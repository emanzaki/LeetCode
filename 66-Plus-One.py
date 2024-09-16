class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(map(str, digits))  # Convert digits to a string
        num = int(num_str)  # Convert the string to an integer
        num += 1  # Increment by 1
        return [int(x) for x in str(num)]