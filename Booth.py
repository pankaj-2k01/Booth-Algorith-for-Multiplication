'''
Here I am implementing The Booths algorithm for multiplying the two No and finding the result of them 
I am implementing Booths Algorithm in Python and throuth the help of file handling I store the result 
in a file "FINAL.TXT"

Name : Pankaj Kumar
Computer Organization
'''
max_number=0
max_bit=0
check=False
open('final.txt', 'w').close()
f = open("final.txt","a")
#Main Driver Function
def main():
    global max_number,max_bit
    num1=input("enter 1st no ")
    num2 =input("enter 2nd no ")
    max_number=max(abs(int(num1)),abs(int(num2)))
    max_bit=len("{0:b}".format(int(max_number)))+1

    num1_bin=convert(num1)
    num2_bin=convert(num2)
    checker(int(num1),int(num2))
    boothplusplus(num1_bin,num2_bin)
#Function Just for providing spaces
def spacer():
    global max_bit
    space=" "
    for i in range(max_bit+4):
        space+=" "
    return space
#Function Performing Booth Algorithm
def boothplusplus(M0,Q0):
    r=max_bit
    Q_='0'
    AC=[]
    for i in range(r):
        AC.append('0')
    c=1
    print("Steps:  "+"\tAccumulator"+"\t"+" Q "+spacer()+"\t"+" Q-1")
    f.write("Steps: "+spacer()+"Accumulator"+spacer()+"Q"+spacer()+"Q-1")
    for i in range(r):
        print(console(i,AC,Q0,Q_))
        f.write("\n")
        f.write(console(i,AC,Q0,Q_))
        #f.write("\n")
        if((Q0[len(Q0)-1]=='0'and Q_=='0') or (Q0[len(Q0)-1]=='1'and Q_=='1')):
            temp1=AC[0]
            temp2=AC[len(AC)-1]
            Q_=Q0[len(Q0)-1]
            Q0=rightshift(Q0)
            AC=rightshift(AC)
            AC[0]=temp1
            Q0[0]=temp2
            
        elif Q0[len(Q0)-1]=='0' and Q_=='1':
            AC=addBinary(AC,M0)
            temp1=AC[0]
            temp2=AC[len(AC)-1]
            Q_=Q0[len(Q0)-1]
            Q0=rightshift(Q0)
            AC=rightshift(AC)
            AC[0]=temp1
            Q0[0]=temp2
            
        elif(Q0[len(Q0)-1]=='1' and Q_=='0'):
            AC=subtraction(AC,M0)
            temp1=AC[0]
            temp2=AC[len(AC)-1]
            Q_=Q0[len(Q0)-1]
            Q0=rightshift(Q0)
            AC=rightshift(AC)
            

            AC[0]=temp1
            Q0[0]=temp2
    final_result=""
    for i in AC:
        final_result+=i
    for j in Q0:
        final_result+=j
    if(check== False):
        print("Binary result: :  "+final_result)
        f.write("\n")

        f.write("Binary result: :  "+final_result)
        print("Decimal result: :  "+str(int(final_result,2)))
        f.write("\n")
        f.write("Binary result: :  "+str(int(final_result,2)))

    else:
        print("Binary result: :  "+str(final_result))
        f.write("\n")
        f.write("Binary result: :  "+str(final_result))
        temp=solution(final_result)
        print("Decimal result: :  -"+str(temp))
        f.write("\n")
        f.write("Decimal result: :  -"+str(temp))
#Function for converting List to String
def convetstring(num):
    number=""
    for i in num:
        number+=i
    return number
#Function for Providing Column 
def console(steps,accu,Q,Q__):
    Line=str(steps)+spacer()+"\t"+convetstring(accu)+spacer()+convetstring(Q)+spacer()+Q__
    return Line
#Function for finding the differnce between -ve no and its 2's complement
def solution(num):
    maxint=2**len(num)
    temp=int(num,2)
    return maxint-temp
#Rightshifting of all list elements
def rightshift(num):
    L=[]
    L.append(num[0])
    for i in range(len(num)-1):
        L.append(num[i])
    return L
#Adding two list containing Binary No
def addBinary(num1,num2):
    added = []
    carry = 0
    for x in range(len(num1)-1, -1, -1):
        if num1[x] == '0' and num2[x] == '0':
            if carry == 1:
                added.append('1')
                carry = 0
            else:
                added.append('0')                
        elif (num1[x] == '0' and num2[x] == '1') or (num1[x] == '1' and num2[x] == '0'):
            if carry == 1:
                added.append('0')
            else:
                added.append('1')
        elif num1[x] == '1' and num2[x] == '1':
            if carry == 1:
                added.append('1')
            else:
                added.append('0')
                carry = 1
    added.reverse()

    return added
#Subtraction of tw0 list containing Binary no
def subtraction(product,mcand):
    carry = 0
    answer =[]
    for i in range(len(product)-1,-1,-1):
        if (mcand[i] == "1" and product[i] == "0"):
            if (carry == 1):
                answer.insert(0,"0")
            else:
                answer.insert(0,"1")
                carry = 1
        elif (mcand[i] == "1" and product[i] == "1"):
            if (carry == 1):
                answer.insert(0,"1")
                carry = 1

            else:
                answer.insert(0,"0")
        elif (mcand[i] == "0" and product[i] == "1"):
            if (carry == 1):
                answer.insert(0,"0")
                carry = 0
            else:
                answer.insert(0,"1")

        elif (mcand[i] == "0" and product[i] == "0"):
            if (carry == 1):
                answer.insert(0,"1")
            else:
            	answer.insert(0,"0")
    return answer
#Function For Calculating two's Complement
def twocomp(num):       
    temp=abs(int(num)+1)
    temp_bin="{0:b}".format(int(temp))
    temp_bin_complement=flipped(temp_bin)
    return temp_bin_complement
#Flipping the bits of a no
def flipped(num):
    number=""
    for i in num:
        if i=="0":
            number+="1"
        else:
            number+="0"
    return number
#Function for checking either both no's are +ve or
#Both are neagative or one negative and one +ve
def checker(num1,num2):
    global check
    if(num1<0 and num2>0 or num1>0 and num2<0):
        check=True
        return
    else:
        check=False
        return
#Function for driving the No and finding 
#the no is either +ve or -ve 
def convert(num):
    if(int(num)<0):
        num_bin=twocomp(num)
        #print(num_bin)
        for i in range(max_bit-len(num_bin)):
            num_bin="1"+num_bin
        return list(num_bin)
    else:
        num_bin="{0:b}".format(int(num))
        for i in range(max_bit-len(num_bin)):
            num_bin="0"+num_bin
        return list(num_bin)
#Calling of main driver function
main()
