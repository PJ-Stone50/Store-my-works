class FindSubset:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


length = len(FindSubset().sub_sets([1,2,3]))
result = FindSubset().sub_sets([1,6,3,0,7,0,8,3,5,0])


print("number of set :",length)
print("Subset :",result)