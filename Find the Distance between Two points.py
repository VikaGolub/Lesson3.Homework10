'''
Codewars: Find The Distance Between Two Points
'''
import math

def distance(x1, y1, x2, y2):
    x = (x2 - x1) * (x2 - x1)
    y = (y2 - y1) * (y2 - y1)
    return round(math.sqrt(x + y), 2)