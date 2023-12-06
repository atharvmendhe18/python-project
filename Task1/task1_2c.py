# import random
# import copy
# new_lst = [1,3,5,11,13,15]

# min = 100


# def find_min(lst):
#     to_append = lst[0] + lst[1]
#     lst.remove(lst[0])
#     lst.remove(lst[0])
#     lst.append(to_append)
#     if len(lst) >2:
#         neww_lst = find_min(lst)
#     else:
#         return lst
#     return neww_lst


# for _ in range(50):
#     copy_of_list = copy.deepcopy(new_lst)
#     random.shuffle(copy_of_list)
#     x1, x2 = find_min(copy_of_list)
#     if abs(x1 - x2) < min:
#         min = abs(x1-x2)

# print(min)


from socket import socket

host = "localhost"
port = 5000
s = socket()
s.connect((host, port))
message = s.recv(1024)
while message:
    print(message.decode())
    message = s.recv(1024)
s.close()
