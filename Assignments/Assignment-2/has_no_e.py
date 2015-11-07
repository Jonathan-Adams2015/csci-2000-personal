def has_no_e(string):
    if (string.count('e') == 0) and (string.count('E') == 0):
        return True
    else:
        return False

find = open("gadsby_stripped.txt")
for line in "gadsby_stripped.txt":
    if not has_no_e(find.readline()):
        find.close()
        print("e is in file")
find.close()
print("e is not in file")
