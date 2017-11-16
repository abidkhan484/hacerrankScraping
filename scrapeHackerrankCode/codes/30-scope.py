# Accepted
# Python 3

    def computeDifference(self):
        check = 0
        self.maximumDifference = -1000
        length = len(self.__elements)

        for i in range(length):
            for j in range (i+1, length):
                check = a[i] - a[j]
                
                
                if check < 0:
                    check = -check

                if check > self.maximumDifference:
                    self.maximumDifference = check

        return self.maximumDifference


