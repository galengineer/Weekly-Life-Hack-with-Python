# Weekly Life Hack using Python
# 1 - Simple Calculator
# galengineer.com
# April 2019

def addition(nX, nY):
	sum = nX + nY
	print("Sum of {0} and {1} is {2}".format(nX, nY, sum))


def main():
	while True:
		print("Enter nX value: ")
		nX = int(input( ))
		print("Enter nY value: ")
		nY = int(input( ))

		addition(nX, nY)

main()