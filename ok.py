import random
while True:
    a=random.randint(0,1000)
    b=int(input("Введіть число 0 від 1000;"))
    if b>a:
        print("Введене число більше ніж рандомне:")
    else:
        print("Введеене число менше ніж рандомне:")
    if b==a:
        print("Ви вгадали число!")
        break