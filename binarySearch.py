# search target number in the list.
# the list must be sorted before comparison.

class BinarySearch :

    def __init__(self,target, data):
        self.data = data
        self.target = target
        startIdx = 0
        lastIdx = len(self.data) - 1
        print(self.doSearch(startIdx, lastIdx))


    def doSearch(self, startIdx, lastIdx):
        midIdx = (startIdx + lastIdx) / 2
        midIdx = int(midIdx)
        success = 0
        
        if midIdx == startIdx :
            if self.data[startIdx] == self.target or self.data[lastIdx] == self.target:
                return 1
            else :
                return 0
        if self.data[midIdx] == self.target :
            return 1
        elif self.data[midIdx] < self.target:
            success = self.doSearch(midIdx, lastIdx)
        else:
            success = self.doSearch(startIdx, midIdx)
            
        return success

        
        
BinarySearch(55,[1,2,3,4,5,6,7,8,9,10])
BinarySearch(3,[1,2,3,4,5,6,7,8,9,10])
BinarySearch(6,[1,2,3,4,5,6,7,8,9,10])
BinarySearch(8,[1,2,3,4,5,6,7,8,9,10])
BinarySearch(1,[1,2,3,4,5,6,7,8,9,10])
BinarySearch(3,[1,2,3,4])
BinarySearch(4,[1,2,3,4])


