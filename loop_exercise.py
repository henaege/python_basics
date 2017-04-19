for i in range(11):
    print (i)

# start = int(input("Start from: \n"))
# end = int(input("End on: \n"))
# for i in range(start, end+1):
#     print (i)

for i in range(1, 10, 2):
    print (i)

star = "*"
for i in range(5):
    print (star*5)

square_num = int(input("How big is the square?\n"))
for i in range(square_num):
    print (star * square_num)

blank = " "
width = int(input("Width?\n"))
height = int(input("Height?\n"))
for i in range(height):
    if i == 0:
        print (star * width)
    print (star + blank * (width - 2) + star)
    if i == height - 1:
        print (star * width)

# triangle
stars = 1
for i in range(height):
    print(blank*((height + height - 1 - stars) // 2) + star * stars \
          + blank*((height + height - 1 - stars) // 2))
    stars += 2

# table
for i in range(1, 11):
    for n in range(1, 11):
        total = i * n
        print("%d x %d = %d" % (i, n, total))

# Banner
words_on_banner = input("Text?\n")
print (star * (len(words_on_banner) + 2))
print (star + words_on_banner + star)
print (star * (len(words_on_banner) + 2))

# Triangle num
for i in range(100):
    n = (i*(i+1)) / 2
    print (n)

# Factor num
num_fac = 16
for i in range(1, num_fac + 1):
    if (num_fac % i == 0):
        print (i)
