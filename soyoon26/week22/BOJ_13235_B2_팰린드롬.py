import sys
word = sys.stdin.readline().rstrip()

if word == word[-1::-1]:
    print("true")
else:
    print("false")