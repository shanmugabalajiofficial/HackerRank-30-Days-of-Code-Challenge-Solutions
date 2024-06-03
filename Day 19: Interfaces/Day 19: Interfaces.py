#Day 19: Interfaces


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        l = []
        if n==1:
            l.append(1)
        for i in range(1, n//2):
            if n % i==0:
                p = n//i
                if i not in l:
                    l.append(i)
                if p not in l:
                    l.append(p)
        return sum(l)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
