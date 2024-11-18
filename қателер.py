tizim = [1,2,3,4,5,6,7,8]

for i in range(len(tizim)):
    if i == 0:
        tizim[0], tizim[-1] = tizim[-1], tizim[0]
        break
print(tizim)