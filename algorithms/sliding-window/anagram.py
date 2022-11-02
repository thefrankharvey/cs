from typing import List

original = 'cbaebabacd'
original2 = 'abab'
check = 'abc'
check2 = 'ab'

def check_anagram(original: str, check:str) -> List[int]:
    result = []
    start, end = 0, len(check)

    while end <= len(original):
        curr_window = original[start:end]
        start+=1
        end+=1
        sorted_window = ''.join(sorted(curr_window))
        if sorted_window == check:
            result.append(start-1)

    return result

print(check_anagram(original2, check2))