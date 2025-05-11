from collections import Counter

points = [[1,1],[2,3],[3,2]]

st=True
points.sort()

if points[1][0]-points[0][0]==points[2][0]-points[1][0] and points[1][0]-points[0][0]==points[2][0]-points[1][0]