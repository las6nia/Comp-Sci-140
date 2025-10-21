'''

                                #fix and study @ home
num = float(input("Enter num: "))
count = 0
total = 0
while num!=0:
    count+=1
    total+=num
    num =float(input("enter num: "))
print(f"the average of the nums are {total/count:.2f}")

#count from 1 to 20 (odd numbers)
count =1
space = ""

while count <=20:
    count+=2
    print(count,end=" ")




#50, 47, backwards. in one line

count2 = 50

while count2 > 0:
    count-=3
    print(count, end=" ")




    #print (all divisible numbers by 2 and 3)
count3 = 100
while count3 > 0:
    count3-=1
    if (count3 % 2==0 and count3 % 3 == 0):
        print(count3,end=" ")
    

                                        #printing range as list,
                                        #start from starting value, end -1
    
nums = range(10,1,-1) #last number skips every other value, 1,3,5.
print(list(nums))

#for loop

#question, start from -100, print all values up to 0, skipping every 3 values
for i in range (-100,0,3):
    print(i, end=" ")

# Write a code to print all the unicode characters for the even numbers ranging from 100 to 120 inclusive
num = ord('a') 

for num in range (100,121,2):
            print(f"{num} - {chr(num)}")

#for loop, axis by value
for c in "Apple":
        print(c, end=" ")

#axis by index for loop
#index will start from 0 -  Apple, 0,1,2,3,4
word = "Apple"
for c in range(5):
        print(word[c], end=" ")
        #when you need to use index, use this function
    '''   
#task - print unicode +5, will print 65 but will print 70, space +=5.
sentence = "A quick brown fox"
for c in range(17):
    result = int((ord(sentence[2])+5))
print(chr(result)) #for my visual understanding
print(result)

print(ord(sentence))





    




