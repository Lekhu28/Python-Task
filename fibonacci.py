n = int(input("Enter No of terms: "))
t1 = 0
t2 = 1
count = 0
if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(t1)

else:
   print("Fibonacci sequence:")
   while count < n:
       print(t1)
       t = t1 + t2

       t1 = t2
       t2 = t
       count += 1
