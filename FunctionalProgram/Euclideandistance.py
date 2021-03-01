import sys
from math import sqrt


class Distance:
    @staticmethod
    def euclideanDistance(xCoor, yCoor):
        """This function check the euclidean distance"""
        return sqrt((xCoor - 0) ** 2 + (yCoor - 0) ** 2)

try:
    if __name__ == "__main__":
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(Distance.euclideanDistance(x, y))
except:
    print("enter values")
