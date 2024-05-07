# 求平均值　CALCULATE THE AVERAGE VALUE
count = 0
# 「count」是「輸入的次數」，從０開始計算
averageValue = 0
# 平均值初始值為０
while True:
    s = int(input("enter your score here: "))
    if s <= -100:
        break
    # 每當輸入「-100」的時，循環結束
    # 回頭問一下如何輸入（Ｙ／Ｎ）來結束循環——會有點麻煩,
    elif s > 100:
        print ("INVALID INPUT: TOO BIG")
    elif s < 0:
        print ("INVALID INPUT: TOO SMALL")
    elif s >= 90:
        print ("A")
    elif s >= 80:
        print ("B")
    elif s >= 70:
        print ("C")
    elif s >= 60:
        print ("D")
    else: 
        print ("F")
    count = count+1
    # 每次輸入一個數，「count」（輸入的次數）就會＋１
    averageValue = averageValue + s
print("finish")
print("count is: ", count)
print("Average Value is: ", averageValue)
