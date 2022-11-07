# Given two strings
    #   original and check
# return the minimum substring of original 
    # such that each character in check including duplicates are included in this substring
    #     the shortest substring
        
# If two substrings that satisfy the condition has the same length, the one that comes lexicographically first are smaller

#  assume that check will always be shorter that the original
# can input be empty, null, or 1
# will input always be letters
# 
#        s
input = 'c d b a e b a e c d'
#            e (len of check)
check = 'abc'

# sort which comes alphabetically first

def get_min_substring(string, check):
    left = 0
    len_count = 0
    # sort window
    # does check exist in window?
    # if true 
        # if len(window) > add to result
        # if lenwindow == len(result) and first letter of window is < first letter of result
            # then result = window
    return 'hi'

print(get_min_substring(input,check))


# let remaining = t.length;
# let left = 0,
#     right = 0,
#     minStart = 0,
#     minLen = s.length + 1;
# while (right < s.length) {
#     if (--hist[s.charCodeAt(right++)] >= 0) remaining--;
#     while (remaining === 0) {
#         if (right - left < minLen) {
#             minLen = right - left;
#             minStart = left;
#         }
#         if (++hist[s.charCodeAt(left++)] > 0) remaining++;
#     }
# }

# return minLen < s.length + 1
#     ? s.substring(minStart, minStart + minLen)
#     : "";
# };













# `from collections import Counter

# def get_minimum_window(s: str, p: str) -> str: # WRITE YOUR BRILLIANT CODE HERE

# def subset(Cw: Counter, Cp: Counter):
#     return all([Cw[x] >= Cp[x] for x in Cp.elements()])

# nw, min_len, min_str = 0, float('inf'), ""
# Cw, Cp = Counter(), Counter(p)

# for i, c in enumerate(original):
    
#     Cw[c] += 1
#     nw += 1
    
#     while Cw[s[i - nw + 1]] > Cp[s[i - nw + 1]]:
#         Cw[s[i - nw + 1]] -= 1
#         nw -= 1
        
#     if subset(Cw, Cp) and (nw < min_len or (nw == min_len and s[i - nw + 1:i + 1] < min_str)):
#         min_len = nw
#         min_str = s[i - nw + 1:i + 1]

# return min_str`