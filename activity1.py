print ("enter the marks obtained in 3 subjects : ")

markOne = int(input())
markTwo = int(input())
markThree = int (input())

total = markOne+markThree+markThree
avg = total/3

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<=91:
    print("Your Grade is A2")
elif avg>=71 and avg<=81 :
    print ("your grade is B1")
elif avg>=61 and avg<=70 :
    print ("your grade is b2")
elif avg>=50 and avg<=60 :
    print ("your grade is c1")
elif avg>=41 and avg<=49 :
    print ("your grade is c2")
elif avg>=30 and avg<=40 :
    print ("your grade is d1")
elif avg>=21 and avg<=29 :
    print ("your grade is d2")
elif avg>=11 and avg<=20 :
    print ("your grade is e1")
elif avg>=1 and avg<=10 :
    print ("your grade is e2")
else :
    print ("invalid input")


 








