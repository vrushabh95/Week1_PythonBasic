
try:

    m,n = [int(number)for number in input("enter number of rows and coloumn").split()]
    user_data_type = input("enter data type")



    data_types = {
        "int": int,
         "float": float,
        "string": str
    }
    import random
    List = []
    for row in range(m):
        inner_list = []
        for column in range(n):
            data = random.random()*3
            data_type = data_types.get(user_data_type)
            inner_list.append(data_type(data))
        List.append(inner_list)
    print(List)
except:
    print("enter correct data type")



