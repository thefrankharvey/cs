import re
str1 = 'Do geese see God?'
# str2 = 'aa'
# nums1 = 33

def val_pal(chars: str) -> bool:
    pure_chars = re.sub(r'[^A-Za-z0-9]+', '', str(chars)).lower()
    for idx, left_char in enumerate(pure_chars):
        right_char = pure_chars[(len(pure_chars)-1)-idx]
        if left_char != right_char:
            return False
    return True

print(val_pal(str1))
