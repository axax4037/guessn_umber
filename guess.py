import random
print("猜數字遊戲，請輸入數字範圍 A~B ")
a = int(input("請輸入起始數字 A : "))
b = int(input("請輸入結尾數字 B : ")) 
x = random.randint(a, b)
y = 0
print("猜數字遊戲,遊戲開始")
while True:
    c = int(input("你猜的數字： "))
    if x == c:
        print("恭喜你答對了")
        print("THE NUMBER IS ", x)
        print("你猜了", y,"次")
        break
    elif c > x:
        print("你的數字比答案大")
    elif c < x:
        print("你的數字比答案小")
    y = y + 1
    print("你猜了", y,"次")
        
