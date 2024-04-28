# g REPRESENTS "GRADE"
g = int(input("ENTER YOUR PERCENTAGE OF YOUR SCORE TO CONVERT  "))
if g > 100:
    print("INVALID INFORMATION")
elif g >= 90:
    print("YOUR GRADE IS: A")
elif g >= 80:
    print("YOUR GRADE IS: B")
elif g >= 70:
    print("YOUR GRADE IS: C")
elif g >= 60:
    print("YOUR GRADE IS: D")
elif g >0:
    print("YOUR GRADE IS: F")
elif g < 0:
    print("INVALID INFORMATION")
else:
    print("INVALID INFORMATION")