## Assumption:
# 1. Here I use "start" instead of "from" as a variable because "from" is one of the python keywords.
# 2. "start" is always less than "to".
# 3. I define set_value() function instead of set() because set() is a built-in function.
# 4. If "amount" is 0, no action will be taken for add() function, and it will return early.

## Evaluation:
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# final_cleanup(): O(n)
# process_middle_points(): O(n)
# find_pos_and_add_missing(): O(log n)
# add(): O(n)
# set_value(): O(n)


from sortedcontainers import SortedDict
from bisect import bisect_left


class IntensityBySegment:
    def __init__(self):
        self.points = SortedDict()


    def final_cleanup(self):
        if not self.points:
            return []

        intensity_dist = []
        prev_intensity = None

        for key, curr_intensity in self.points.items():
            if curr_intensity != 0 or (prev_intensity != 0 and prev_intensity is not None):
                intensity_dist.append([key, curr_intensity])
            
            prev_intensity = curr_intensity

        return intensity_dist
        
        
    def process_middle_points(self, start, to, amount, operation):
        inclusive_start = True if operation == "set" else False
        middle_keys = list(self.points.irange(start, to, inclusive=(inclusive_start, False)))

        if operation == "add":
            for key in middle_keys:
                self.points[key] += amount
        elif operation == "set":
            for key in middle_keys:
                self.points[key] = amount


    def find_pos_and_add_missing(self, x):
        pos = self.points.bisect_left(x)
        if pos == len(self.points) or self.points.keys()[pos] != x:
            self.points[x] = 0
        return pos


    def add(self, start, to, amount):
        if amount == 0:
            return
        if amount > 0:
            print("Add {} segment(s) from {} to {}..".format(amount, start, to))
        else:
            print("Delete {} segment(s) from {} to {}..".format(abs(amount), start, to))


        # Handle start point
        start_index = self.find_pos_and_add_missing(start)
        
        if amount < 0 and (self.points and start in self.points):
            curr_intensity = self.points[start]
        else:
            prev_key = self.points.keys()[start_index - 1] if start_index > 0 else None
            curr_intensity = self.points[prev_key] if prev_key else 0

        if start in self.points:
            self.points[start] += amount
        else:
            self.points[start] = curr_intensity + amount


        # Handle end point and middle points
        to_index = self.find_pos_and_add_missing(to)
        self.process_middle_points(start, to, amount, operation="add")


        # Final cleanup
        intensity_distribution = self.final_cleanup()

        print("Intensity Distribution: ", intensity_distribution)


    def set_value(self, start, to, amount):
        print("Set {} segment(s) from {} to {}..".format(amount, start, to))


        # Update points
        self.find_pos_and_add_missing(start)
        self.find_pos_and_add_missing(to)
        self.process_middle_points(start, to, amount, operation="set")


        # Final cleanup
        intensity_distribution = self.final_cleanup()
        print("Intensity Distribution: ", intensity_distribution)
