# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# 111112222334445 => 5142233415 / AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

a = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
rle = ''
count = 0
for i in range(0, len(a)):
    count += 1
    if i == (len(a)-1):
        rle += str(count)
        rle += a[i]
        break
    elif a[i] != a[i+1]:
        rle += str(count)
        rle += a[i]
        count = 0
 
print(a)
print(rle)
