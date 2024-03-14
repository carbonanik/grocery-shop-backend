from typing import List

def plusOne(digits: List[int]) -> List[int]:
    new_digits = []
    for i in range(len(digits) - 1, -1, -1):
        current_digit = digits[i]
        new_digits.append(current_digit)
    return new_digits


digits = [1,2,3]
print(plusOne(digits))
# digits2 = [4,3,2,1]
# print(plusOne(digits2))
# digits = [9]
# print(plusOne(digits))

#[int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]