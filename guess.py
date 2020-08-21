import random
print("猜數字遊戲，請輸入數字範圍 A~B ")
a = int(input("請輸入起始數字 A : "))
b = int(input("請輸入結尾數字 B : ")) 
x = random.randint(a, b)
print("猜數字遊戲,遊戲開始")
while True:
    c = int(input("你猜的數字： "))
    if x == c:
        print("恭喜你答對了")
        print("THE NUMBER IS ", x)
        break
    else:
        if x != c:
            print("猜錯了，再試一次")
        
