# solution-1
def decimal_to_binary1(num):   # recursive approach
	if num>0:
		decimal_to_binary(num//2)
	print(num%2,end="")

# solution-2
def decimal_to_binary2(num):   # iterative approach
	mylist = []
	while num>0:
		mylist.append(num%2)
		num = num // 2
	mylist.reverse()
	# we cannot directly convert an interger list to single string, first we need to convert integer list to string list
	print(''.join(map(str,mylist)))
# taking inputs
def main():
	intvalue = int(input())
	decimal_to_binary1(intvalue)


if __name__ == "__main__":
	main()