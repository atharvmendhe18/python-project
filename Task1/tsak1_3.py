def explode_chains(encoded_list):
    for list in encoded_list:
        for i in range(2,len(list)):
            if i >= len(list):
                i = 2
            if list[i] - list[i -1] == 1 and list[i-1] - list[i-2] == 1:
                list.remove(list[i])
                list.remove(list[i-1])
                list.remove(list[i-2])
                if len(list) <= 2:
                    break

    return encoded_list


encoded_lists = [
[1, 2, 3, 4, 6],
[5, 7, 8, 9, 15],
[12, 14, 16, 18],
[10, 11,12,13,16,17,18,20]
]         

#print(explode_chains(encoded_lists))

for row in explode_chains(encoded_lists):
    print(row)

