# def average(*args):
#
#
# print(average(1, 2, 4, 6, 23))

def naoborot(words="Hello"):
    reverse = words[::-1]
    if words == reverse:
        return True
    else:
        return False

print(naoborot())
