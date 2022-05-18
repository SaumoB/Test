
def binary_search(arr, low, high, x):
	if high >= low:

		mid = (high + low) 

		
		if arr[mid] == x:
			return mid

	
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		
		return 0
arr=[]

n=int(input("Enter the number of elements "))

if(n>100):print("Good luck!")

for i in range(0, n):

    num = int(input("Enter number "))
  
    arr.append(num) 
      
x=int(input("Enter the number to find "))

result = binary_search(arr, 0, len(arr)-1, x)

if result != 0:
	print("Number is present at", str(result+1),"th place of the array")
else:
	print("Number is not present in array")
