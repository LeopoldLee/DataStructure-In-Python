# search target number in the list.

class LinearSearch :

    def __init__(self,target, data):
        self.data = data
        self.target = target
        print(self.doSearch())


    def doSearch(self):

        for current in self.data :
            if current == self.target :
                return "Target Number %s is in the list" % str(self.target)
        return "Target Number %s is not in the list" % str(self.target)


LinearSearch(7,[1,2,3,4,5])

# How many comparison occurs here in works case?
# T(n) = n

