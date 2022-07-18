2(a)

# Python Program to Print Floyd's Triangle
rows = int(input("Please Enter the total Number of Rows : "))
number = 1

print("Floyd's Triangle")
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print(number, end = ' ')
    number = number + 1
  print()

  
2(b)
 
no_heaps = int(input("Enter no of pubble heaps"))
heaps = no_heaps
if(no_heaps % 2 == 0):
  while(no_heaps > 0):
    print(heaps)
    heaps = heaps + 2
    no_heaps = no_heaps - 1
else:
  while(no_heaps > 0):
    print(heaps)
    heaps = heaps + 2
    no_heaps = no_heaps - 1
 n = int(input("enter no of rows :"))
   
4(a)
 for i in range(0, n):
   for j in range(0, i+1):
      print("* ",end="")
   print() 

4(b)
    def monotonic_direction(a):
    n = len(a)
    if all(a[i]<=a[i+1] for i in range(n-1)) :
            return "Increasing"
    if  all(a[i]>=a[i+1] for i in range(n-1)) :
            return "Decreasing"
a = [2,3,4,5,6]
x = monotonic_direction(a)
if x :
   print("Given sequence of numbers is monotonically",monotonic_direction(a))
else :
	print("It is not monotonic")


6(a)

str = input("Input a string")
digits = 0
upper = 0
lower = 0
for char in str:
  if char.isdigit():
    digits = digits + 1
  elif char.isupper():
    upper = upper + 1
  elif char.islower():
    lower = lower + 1
  else:
    pass
print("Digits : ",digits)
print("Lower case letters : ", lower)
print("Upper case letters : ",upper)

6(b)

from array import *
a=array('i',[1,4,2,6,8,3,10])     
ele=int(input("Enter search element"))
flag=0
for i in range(len(a)):
        if(a[i] == ele):
            flag=i+1
            break
        else:
             pass
if(flag == 0):
    print("Not found")
else:
    print('Element found in',flag,'position')
