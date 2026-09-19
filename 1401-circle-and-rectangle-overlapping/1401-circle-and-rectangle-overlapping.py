class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find closest x-coordinate on rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Find closest y-coordinate on rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Calculate squared distance from circle center
        # to the closest point of rectangle
        distance_squared = (
            (xCenter - closest_x) ** 2 +
            (yCenter - closest_y) ** 2
        )

        # Circle and rectangle overlap if the closest
        # point is inside or on the circle
        return distance_squared <= radius ** 2