import random


class Coupon:

    limit = 0

    def __init__(self,limit):
        self.limit = limit

    def getRandom(limit):
        """returns random number from o to limit
           :return:returns the random numbers"""
        return random.randint(0,limit)

    def getCoupon(self):
        """function to get new coupon
        :return:returns no of random numbers generated to get N distinct coupon"""

        result = 0
        couponNumbers = []
        distinct = 0
        noOFRandomNumbers = 0
        while distinct < self.limit:
            result = Coupon.getRandom(limit = self.limit)
            noOFRandomNumbers += 1
            if result not in couponNumbers:
                couponNumbers.append(result)
                distinct += 1
        print(couponNumbers)
        return noOFRandomNumbers

class ValueTooSmallError(Exception):
    """raised when the input value is too small"""
    pass
value = 1
while value == 1:
    try:
        limit = int(input("Enter the limit"))
        if limit <= 0:
            raise ValueTooSmallError
        coupon = Coupon(limit)
        print(coupon.getCoupon(),"random numbers generated")
        break
    except ValueTooSmallError:
        print("enter large number")