import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def pinch(hand):
    # thumb (4) + index (8)
    return distance(hand[4], hand[8]) < 40

def grab(hand):
    palm = hand[0]
    avg = sum(distance(palm, hand[i]) for i in [8,12,16,20]) / 4
    return avg < 80
