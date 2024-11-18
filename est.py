"""Адамның жасы мен бойына қарап, оның баскетбол командасына қабылдануын анықтау.
Қабылдау шарты: жас 18-ден жоғары және бойы 180 см-ден жоғары.
"""
"""zhas = int(input("Zhas engiz"))
boyi = int(input("Бойын енгіз"))

if zhas > 18 and boyi > 180:
    print("Сіз командаға қабылдандаңыз")
else:
    print("Сіз кабылданбадыныз")
"""

# integer, floating num, string


"""Берілген сан тақ па, жұп па екенін анықтаңыз."""
"""
san = int(input("San engiz"))
if san % 2 == 0:
    print("Zhup san")
else:
    print("Tak san")
"""



"""Үш сан берілген. Егер олардың қосындысы жұп сан болса, қосындыны шығарыңыз. Әйтпесе, әр санның квадратының қосындысын шығарыңыз."""


"""san1 = int(input("San1 engiz"))
san2 = int(input("San2 engiz"))
san3 = int(input("San3 engiz"))
summa = san1 + san3 + san2
if (san3 + san1 + san2) % 2 == 0:
    print(summa)
else:
    print( (san1 ** 2) + (pow(san2, 2)) + (san3 ** 2))
"""

"""Пайдаланушы енгізген екі сан арасындағы тақ сандарды шығарыңыз."""
"""san1 = int(input("San engiz"))
san2 = int(input("San engiz"))

for i in range(san1,san2+1):
    if i % 2 == 1:
        print(i, end = ' ')
"""

#Берілген санның факториалын есептеңіз.
# 5! = 1*2*3*4*5 -> 120

"""summa_factorial = 1
факториал_шегі = int(input("Шегін еңгіз"))"""
"""for i in range(1,факториал_шегі+1):
    summa_factorial = summa_factorial *  i
print(summa_factorial)
"""
"""i = 1

while i <= факториал_шегі:
    summa_factorial = summa_factorial * i
    i += 1
print(summa_factorial)
"""

#Пайдаланушы 0 енгізгенге дейін сандарды қосып отырыңыз.
"""summa = 0
san = int(input("San engiz"))

while san != 0:
    summa += san
    san = int(input("San engiz, тоқтату үшін 0 болсын"))

print(summa)
"""




#Пайдаланушы енгізген санның цифрларының қосындысын есептеңіз.

"""san = int(input("San engiz"))#1234
summa = 0#сумма
""""""while san > 0:
    summa  = summa + (san % 10)
    san = san //  10
print(summa)
"""


#Пайдаланушы енгізген санның кері санын шығарыңыз (мысалы, 123 -> 321).

"""san = int(input("San engiz"))#1234
reversed_summa = 0#сумма
"""



#1-ден 10-ға дейінгі сандарды шығарып, 5-ке жеткенде циклді тоқтатыңыз.

"""for i in range(1,11):
    if i == 5:
        break
    else:
        print(i)
"""


#1-ден 20-ға дейінгі сандарды шығарыңыз, бірақ 3-ке бөлінетін сандарды өткізіп жіберіңіз.
"""i = 1
while i < 21:
    if i % 3 == 0:
        i+=1
        continue
    print(i)
    i+=1
"""


#Циклдің көмегімен 1-ден 100-ге дейінгі сандардың ішінен 7-ге бөлінетін бірінші санды табыңыз. Егер табылмаса, "Мұндай сан жоқ" деп шығарыңыз.

"""for i in range(1,101):
    print(i)
    if i % 7 == 0:
        print("7-ге бөлінетін саны табылды")
        break
else:
    print("Ондай сан жоқ")"""

#Массивтің ішіндегі барлық тақ сандарды шығарыңыз.
"""tizim = [1,2,3,4,5,6,7,8,9]

for i in range(len(tizim)):
    if tizim[i] % 2 == 1:
        print(tizim[i])
"""


#Массивтегі бірінші және соңғы элементтің орнын ауыстырыңыз.
"""bastapky = 0
songy = 0
kosm = tizim[0]
tizim[0] = tizim[-1]
tizim[-1] = kosm
print(tizim)"""
"""
for i in range(len(tizim)):
    if i == 0:
        bastapky = tizim[i]
        tizim[-1] = bastapky
    elif i == 8:
        songy = tizim[i]
        tizim[0] = songy

print(tizim)"""
#Массивтің ішінен берілген санды алып тастаңыз.
"""tizim = [1,2,3,4,5,6,7,8,9]
san = int(input("San alyp tastau"))

for i in tizim:
    if i == san:
        tizim.append(i)
        break
print(tizim)
"""

#Файлға "Сәлем, әлем!" мәтінін жазыңыз.
"""file = open('focus.txt', 'w')

file.write("Salem, Alem")

file.close()"""

"""with open('focus.txt', 'a') as file:
    file.write("Bekzhan")"""

#Файлдан сандарды оқып, олардың қосындысын есептеңіз.
"""file = open('focus.txt')
sandar = file.readlines()
print(sandar)
summa = 0
for i in sandar:
    summa = summa + int(i)
print(summa)
"""
#2x3 массивтің барлық элементтерінің қосындысын есептеңіз.

"""a = [[1,2,3],
     [4,5,6]]
summa = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        summa += a[i][j]
print(summa)"""