import random
answer=random.randint(1,100)
count=0
while True:
    guess=int(input("猜一个1-100的数: "))
    count+=1
    if guess>answer:
        print("猜大了")
    elif guess<answer:
        print("猜小了")
    else:
        print("猜对了")
        break
print(count)