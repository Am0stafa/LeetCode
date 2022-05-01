class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()
        listOfChar =[]
        sum = 0
        while(n not in visit):
            visit.add(n)
            while(n>9):
                listOfChar.append(n%10)
                n = n//10
            listOfChar.append(n)

            for i in listOfChar:
                sum+=i**2
            n = sum
            sum = 0
            listOfChar=[]
            if n == 1:
                return True
