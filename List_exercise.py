list_numbers = [10, 8, 3, 8, 5, 3, 0]

# largest
max_num = 0
for n in list_numbers:
    if (n > max_num):
        max_num = n
print (max_num)

# Smallest
min_num = 0
for i in list_numbers:
    if (i < min_num):
        min_num = i
print (min_num)

# Even
for j in list_numbers:
    if (j % 2 == 0):
        print (j)

# Positive
new_list = []
for q in list_numbers:
    if q > 0:
        new_list.append(q)
print (new_list)

# Multiply
factor_num = 2
multi_list = []
for e in list_numbers:
    n = e * factor_num
    multi_list.append(n)
print (multi_list)

# Multi vector
v_list1 = [2, 4, 5]
v_list2 = [2, 3, 6]
v_newlist = []
for i in range(len(v_list1)):
    result = v_list1[i] * v_list2[i]
    v_newlist.append(result)
print (v_newlist)

# Matrix Addition
ma_list1 = [[2, -2], [5, 3], [3, 4]]
ma_list2 = [[5, 2], [1, 0], [5, 6]]
ma_newlist = []
for i in range(len(ma_list1)):
    temp = []
    for j in range(len(ma_list1[i])):
        total = ma_list1[i][j] + ma_list2[i][j]
        temp.append(total)
    ma_newlist.append(temp)
print (ma_newlist)

# De-dup
new_list_de = list_numbers[:]
for i in range(len(list_numbers)):
    temp = list_numbers[:]
    temp.remove(list_numbers[i])
    for j in temp:
        if list_numbers[i] == j:
            new_list_de.remove(list_numbers[i])
print (new_list_de)
