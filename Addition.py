import argparse,math

parser=argparse.ArgumentParser()
parser.add_argument('--arr', type=list, nargs='+',help="Enter array with --arr")
parser.add_argument('--opt',type=int)
try:
	args=parser.parse_args()

except :
  print("Invalid input")
  exit()
	

global a,o
a=args.arr
o=args.opt
def add():
 res=sum(a)
 print("Sum=",str(res))
 exit()

def multiply():
    r = 1
    for x in a:
         r = r * a
    print(r)
def sort():
	a.sort()
	print(a)
	exit()

	


def default():
  	print("Wrong Choice")

switcher={
		1:add,
		2:sort,
		3:multiply
	}
def switch(y):
  	return switcher.get(y,default)()
switch(o)

