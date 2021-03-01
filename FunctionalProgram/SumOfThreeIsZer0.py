import logging
logging.basicConfig(level=logging.INFO)
logging.info("this is info message")

def triplet(arr,arr_len,sum):
    """This function check the sum of three integer is zero"""
    for i in range(0,arr_len-2):
        for j in range(i+1,arr_len-1):
            for k in range(j+1,arr_len):
                if(arr[i]+arr[j]+arr[k] == sum):
                    print(arr[i], arr[j], arr[k])
                    break
    else:
     print("Triplet series not generated")

try:

    arr = list(map(int,input("enter values").split()))
    arr_len=len(arr)
    sum = 0
    triplet(arr,arr_len,sum)
except:
    print("enter only number")



