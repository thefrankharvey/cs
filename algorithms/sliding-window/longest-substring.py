# Find the length of the longest substring of a given string without repeating characters


# start  s
input = 'abcdbea'
# end       e
 
# Output: 3

def longest_substring(string: str) -> int:
    result = []
    start, end = 0, 0
    while end < len(string)-1:
        end+=1
        window = string[start:end]
        if string[end] in window and len(window) > len(result):
            result=window
            start=end

    return (len(result))

print(longest_substring(input))