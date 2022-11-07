# Find the length of the longest substring of a given string without repeating characters
# edge cases
# 1 letter
# 2 or > 2 ALL unique? = if the window len == len of string

input = 'aaabcbbababb'

def longest_substring(string: str) -> int:
    charSet = set()
    left = 0
    result = len(string) if len(string) < 2 else 0

    for right in range(len(string)):
        while string[right] in charSet:
            charSet.remove(string[left])
            left += 1

        charSet.add(string[right])
        right+=1
        window_size = right - left
        result = max(result, window_size)

    return result

print(longest_substring(input))
