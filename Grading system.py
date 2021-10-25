#printing the statement on the screen
print("Enter your score:")
#taking the input
sub1 = int (input())
sub2 = int (input())
sub3 = int (input())
sub4 = int (input())
sub5 = int (input())
sub6 = int (input())
sub7 = int (input())
tot = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7
print ("Total responses are:",tot)
avg = tot/5
print ("Total Average Is:",avg)
if avg>=45 and avg<=50:
    print("Need more practice")
elif avg>=50 and avg<=70:
    print("Can do better")
elif avg>=70 and avg<=85:
    print("Good")
elif avg>=85 and avg<=100:
    print("Excellent")
elif avg>=100:
    print("Outstanding")
else:
    print ("need to practice")



