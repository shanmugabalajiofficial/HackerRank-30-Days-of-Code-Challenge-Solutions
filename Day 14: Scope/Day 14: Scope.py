#Day 14: Scope


class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here
    def computeDifference(self) -> int:
        if not self.__elements:
            return 0
        self.maximumDifference = max(self.__elements) - min(self.__elements)
        return self.maximumDifference
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
