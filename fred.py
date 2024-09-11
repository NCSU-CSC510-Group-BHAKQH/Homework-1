"""
Simple program for hw1.
"""
N = 10
NUM1 = 0
NUM2 = 1
NEXT_NUMBER = NUM2
COUNT = 1

while COUNT <= N:
    print(NEXT_NUMBER, end=" ")
    COUNT += 1
    NUM1, NUM2 = NUM2, NEXT_NUMBER
    NEXT_NUMBER = NUM1 + NUM2
    print()
