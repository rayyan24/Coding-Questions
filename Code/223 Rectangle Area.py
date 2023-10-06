class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1=(ax2-ax1)*(ay2-ay1)
#                 |         |
#               length    breadth
#                 |         |
        area2=(bx2-bx1)*(by2-by1)
        
        # calculate x overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left

        # calculate y overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        area_of_overlap = 0
        # if the rectangles overlap each other, then calculate
        # the area of the overlap
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = x_overlap * y_overlap
        return area1 + area2 - area_of_overlap