str = "Engineering"

print("Original string: " + str)

# Removing char at pos 3
# using slice + concatenation

for i in range(len(str)):
    res_str = str[:i-1] + str[i:]
    print(res_str)

