class Solution(object):
    def findCenter(self, edges):
        a = edges[0][0]
        b = edges[0][1]
        if edges[1][1] == a or edges[1][0] == a:
            return a
        else:
            return b
        