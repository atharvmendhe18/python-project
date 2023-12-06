# lst = ['0001', '0011', '0101', '1011', '1101', '1111']

# new_lst = []

# for binary in lst:
#     new_lst.append(int(binary, 2))

# new_lst.sort()
# print(new_lst)
# while len(new_lst) > 2:
#     x1,x2 = new_lst[0],new_lst[1]
#     new_lst.remove(x1)
#     new_lst.remove(x2)
#     new_lst.append(x1 + x2)
#     new_lst.sort()

# print(new_lst)

# print(f"Difference: {new_lst[1] - new_lst[0]}")


import socket

host = "localhost"
port = 5000
s = socket.socket()
s.bind((host, port))
s.listen(s)
c, addr = s.accept()
print("got connection", addr)
c.send(b"Thanks")
c.close()
