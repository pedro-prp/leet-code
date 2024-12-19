class Solution:
    def isHappy(self, n: int) -> bool:
        number_history = set()
        number_history.add(n)
        new_number = n

        while True:
            digits = [int(x) for x in list(str(n))]

            if new_number == 1:
                return True 

            new_number = 0

            for d in digits:
                new_number += d ** 2
            
            print(new_number)

            if new_number in number_history:
                return False
            
            number_history.add(new_number)

            n = new_number

