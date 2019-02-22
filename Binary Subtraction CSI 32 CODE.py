#Ganesh Jainarain
#Feb 21, 2019
#CSI 32
#Binary Subtraction 


def converter():
    binary1 = input("Enter your first binary number here: ")
    binary2 = input("Enter your second binary number here: ")
    num1 = decimalF(binary1)
    num2 = decimalF(binary2)
    result = num1 - num2
    final_result = binaryG(result)
    print(final_result)
#various prints etc    
def decimalF(binary):
    counter = len(binary)-1
    plist = []
    for i in binary:
        if i == "1":
            plist.append(counter)
            counter -= 1
        else:
            counter -= 1
    decimal = 0
    for j in plist:
        decimal = decimal + 2**j
    return decimal
#sets counter to the length of binary-1
#creates new empty list
#for every postion in binary if the position is a 1 it appends it to the list
#otherwise it doesnt add 0 because it doesnt add any value but
#you still have to -1 from the counter, because you want to keep iterating through
#next i initialized decimal to 0
#for every postion in plist i raised 2 to j to get the numerical value ex 5



def binaryG(result):
    binary_list = []
    while result != 0:
        binary_list.append(result % 2)
        result = result // 2
    return binary_list
#takes result as a parameter
#initalizes binary_list as the empty list
#enters while loop
#takes result % 2 to convert from numerical to base 2 binary keeps doing this until 0
#appends either 1 or 0 in the list
#sets result // 2 as new result until result = 0





#Basically the idea behind this was that since you have to keep borrowing
#to subtract a binary from a binary(this is difficult)
#I thought that we can first convert these two binary's into their numerical
#value then say 11001 = 25 and 10100 = 20 so I first did 25-20=5 then
#calculated the binary number for that digit 
        
    
converter()

    
    
