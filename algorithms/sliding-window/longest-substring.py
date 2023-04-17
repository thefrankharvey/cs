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

# print(longest_substring(input))

# {p:0
#  w:5
#   k:3
#   e:4   
# }
# res = 3
#            l 
input2 = 'pwwkewokewpyr'
#              r
def longest2(s: str) -> int:
    # record indices of prev repeat chars
    # or char before first unique?
    left = right= 0
    result = 0
    tracker = {}

    while right < len(s)-1:
        right+=1
        window = s[left:right]
        print(window)
        if s[right] in tracker:
            print
            result = max(result, len(window))
            left=right
            # ans = 3

        tracker[s[right]] = right
    
    return result

print(longest2(input2))
