name=int(input("enter the name"))
maths=int(input("enter the marks"))
chem=int(input("enter the marks"))
hindi=int(input("enter the marks"))
average=(maths+chem+hindi)/3
print("average",average)
if(average>90):
     print("grade:A")
elif(average>75):    
    print("grade:c")
elif(average>50):
    print("grade:FAIL")
 
