a=int(input("Enter the terms: ")) #Enter the number of terms to be seen in output
f=0
s=1

if a<=0:
    print("The requested series is\n",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next