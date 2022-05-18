
import getopt, sys ,argparse

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


parser = argparse.ArgumentParser()

parser.add_argument('--arr', type=int, nargs='+',help="ENter array with --arr")
args = parser.parse_args()
x=int(input("Enter the number to find "))


		
#(try:
   
    #arguments, values = getopt.getopt(argumentList, options, long_options)
     

    # checking each argument
    #for currentArgument, currentValue in arguments:
 
   #     if currentArgument in ("-h", "--Help"):
    #        print ("Displaying Help")
             
  #      elif currentArgument in ("-m", "--My_file"):
  #          print ("Displaying file_name:", sys.argv[0])
             
#        elif currentArgument in ("-o", "--Output"):
 #           print (("Enabling special output mode (% s)") % (currentValue))
             
#except getopt.error as err:
#    print (str(err))
		

#arr=sys.argv[0].split(',')


result = binary_search(args.arr, 0, len(args.arr)-1, x)

if result != 0:
		print("Number is present at", str(result+1),"th place of the array")
else:
		print("Number is not present in array")
