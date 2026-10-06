class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1

            else:
                if five == 0:
                    return False

                if ten == 0 and five < 3:
                    return False

                if ten > 0:
                    ten -= 1
                    five -= 1
                
                else:
                    five -= 3

        return True