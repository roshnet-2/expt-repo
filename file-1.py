def sayHello(name):
	print('Hello, {}'.format(name))

def main():
	myname = input('Your name: ')
	sayHello(myname)

if __name__ == '__main__':
	main()