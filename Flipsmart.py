"""

Project 1: Electronic Commerce Application.

You need to create the foundations of an e-commerce engine for a B2C (business-to-consumer) retailer. You need to have a class for a customer called User, a class for items in inventory called Item, and a shopping cart class called Cart. Items go in Carts, and Users can have multiple Carts. Also, multiple items can go into Carts, including more than one of any single item.

"""
import sys

index = 0

class tags:

	UNDERLINE = '\033[4m'
	END = '\033[0m'
	BLUE = '\033[91m'

# User item selection
class Cart():

	def __init__(self ):
		global index
		self.cart_index = index
		self.purchase = []
		self.carts = [[]]

	def add_cart(self):
		global index
		print("Cart added")
		self.carts.append([])
		self.cart_index += 1
		
	def cart_count(self):
		
		return self.cart_index

	def add_item(self,item,qty,store_qty):
		
		self.carts[index].append([item[0],item[1],qty])
		store_qty = store_qty - qty

		#print(self.carts)
		return store_qty

	def remove_item(self,item):
		
		# flase flag to be used if the value is not present to tell the user
		flag = False

		# i is the index and j is the value
		for i,j in enumerate(self.carts[index]):
			# if the item name given by user matches the product present in the inventory then it deletes the value
			if( item[0] ==  j[0] ):
				self.carts[index].remove(j) 
				flag = True
			
		if( flag == False ):
			return 'The item does not exist in the inventory'
		
		#test case to see the product is successfully deleted	
		#print(self.product)

		# return the final product
		return self.carts[index]

	def update_quantity(self,item,qty,store_qty):
		
		# flase flag to be used if the value is not present to tell the user
		flag = False
		current_qty = 0
		if( qty > store_qty ):
			print("The quantity is greater than the store quantity")

		
		
		# i is the index and j is the value
		for i,j in enumerate(self.carts[index]):
			# if the item name given by user matches the product present in the inventory then it deletes the value
			if( item[0] ==  j[0] ):
				current_qty = j[2]
				

		if( qty < current_qty):
			# i is the index and j is the value
			for i,j in enumerate(self.carts[index]):
				# if the item name given by user matches the product present in the inventory then it deletes the value
				if( item[0] ==  j[0] ):
					new = current_qty - qty
					store_qty = store_qty - new
					j[2] = new
					return store_qty

		if( qty > current_qty):
			# i is the index and j is the value
			for i,j in enumerate(self.carts[index]):
				# if the item name given by user matches the product present in the inventory then it deletes the value
				if( item[0] ==  j[0] ):
					new = current_qty + qty
					store_qty = store_qty - new
					j[2] = new
					return store_qty
			
		if( flag == False ):
			return 'The item does not exist in the inventory'
		
		#test case to see the product is successfully deleted	
		#print(self.product)

		# return the final product
		return self.carts[index]


	def view_cart(self):
		
		#print("List of items in your cart currently : ",self.carts[index])
		return self.carts[index]


	def bill(self):
		
		final = 0
		total = 0
		print("List of items in your cart \n")
		print("Item No.		Item name 		Item Price 		Item QTY")
		for i,j in enumerate(self.carts[index]):
			print(i,*j,sep='\t 	  	')

		print("\n")

		for i,j in enumerate(self.carts[index]):
			final = float( j[1] * j[2] )
			total += float( j[1] * j[2] )
			print(i,final,sep='\t 	  		 ')

		print("-------------------------------------------------------")
		print("Final Price is :		",total)

		

# User Class - Working

class User(Cart):

	global index

	# init has 2 parameters 1. cust_name = customer name and 2. item which is the object of item which has all the inventory and item function

	def __init__(self, cust_name , item , cart = Cart()):
		self.carts = cart
		self.name = cust_name
		self.item = item
		self.count = 1
	
	def add_item(self, item, amount, cart_index=0):
		self.carts[index].add_item(item, qty,store_qty)

	def remove_item(self, item, amount, cart_index=0):
		self.carts[index].remove_item(item)

	def update_quantity(self, item, amount, cart_index=0):
		self.carts[index].update(item,qty,store_qty)
	
	
	def choice(self):
		print("\n")
			
		print(str.center("Welcome to FlipSmart",200))
		#working
		print(str.center("1.View list of items",200))
		#working
		print(str.center("2.View number of current shopping carts ",200))
		#working
		print(str.center("3.Do you wish to add a new shopping cart? ",200))
		#working
		print(str.center("4.View current shopping cart items",200))
		#working
		print(str.center("5.Change your cart? ",200))
		#working		
		print(str.center("6.Add item to shopping cart",200))
		#working
		print(str.center("7.Remove item from shopping cart",200))
		#working
		print(str.center("8.Update quantity from shopping cart",200))
		#working
		print(str.center("9.Check Out",200))
		#working
		print(str.center("0.Quit program",200))

		print(str.center("Make your choice",200))
		

		option = int(input())		
		
		# view items in FlipSmart
		if(option == 1):
			print(str.center("List of Current Items in FlipSmart \n",200))
			self.item.display()
		# view current number of shopping carts
		elif(option == 2):
			print(str.center("Your current number of shopping carts are : \n",200))
			self.carts.add_cart()
			self.count = self.carts.cart_count()
			print("Total number of carts being used (If 1 then its default cart ) : ",self.count)
			print("\n")
		#add a new cart
		elif(option == 3):
			print(str.center("Attemping to add a new cart : \n",200))
			self.carts.add_cart()		
			self.count = self.carts.cart_count()
			print("Total number of carts being used  : ",(self.count+1))
		# view items in shopping cart
		elif(option == 4):
			print(str.center("Your current items in shopping cart are : \n",200))
			global index

			print(str.center("Enter the shopping cart you wish to view: \n",200))
			x = int(input())
			index = x

			print(self.carts.view_cart())
		
		# change cart
		elif(option == 5):
			
			self.count = self.carts.cart_count()
			
			if(self.count == 0):
				print("You only have 1 cart. ")
				index = 0 

			else:
			
				print("Enter the cart number you wish from 0 to ", self.count)
				
				index = int(input())
				
			
		# add item to cart
		elif(option == 6):

			print(str.center("Adding Items to your cart \n",200))
			
			print("Enter the item name you wish to add ")
			buy = str(input())

			print("Enter the item quantity you wish to add ")
			qty = int(input())
		
			x,y = self.item.find_item(buy)
			store_qty = self.item.get_quantity(x)
			
			if( y == True ):
				a = self.carts.add_item(x,qty,store_qty)
				self.item.set_quantity(x,a)
			
			print(self.carts.view_cart())
			
		elif(option == 7):

			print(str.center("Removing Items from your cart \n",200))
			
			print("Enter the item name you wish to remove ")
			buy = str(input())
		
			x,y = self.item.find_item(buy)

			if( y == True ):
			
				self.carts.remove_item(x)
				self.item.set_quantity(x,100)
					

			print(self.carts.view_cart())

		elif(option == 8):

			print("Updating Items from your cart :" , index , sep ='\t	' )

			
			print("Enter the item name you wish to update ")
			buy = str(input())

			print("Enter the item quantity you wish to update ")
			qty = int(input())
		
			x,y = self.item.find_item(buy)

			if( y == True ):

				store_qty = int(self.item.get_quantity(buy))
				
				if( store_qty != 0 ):
					change = self.carts.update_quantity(x,qty,store_qty)
			
					self.item.set_quantity(x,change)
				else:
					print("The store does not have enough stock left to add more ")
					
			print(self.carts.view_cart())

			
		# check out
		elif(option == 9):
			print(str.center("Checking Out of FlipSmart \n",200))


			self.carts.bill()

		# exit program
		elif(option == 0):
			print(str.center("Exiting Program \n",200))
			return False 
			#sys.exit()
		else:
			print(str.center("Invalid choice Enter again \n\n",200))
			self.choice()	




	def __repr__(self):
		print("\n")
		txt = str.center('Welcome ' + self.name + ' to FlipSmart and enjoy your shopping',200)
		txt =  tags.BLUE + txt + tags.END
		return txt
		
		

# Items Class - Fully Functional
# Contains all the items in the store 
# This class has 4 Functions :
# add_inventory to add individual items into one list
# remove_inventory to remove a specific item from list
# find_item to find the specific item from inventory
# display to display all the items currently in a list

class Item(Cart):

	def __init__(self):

		#default variables publicly used within class 
		
		self.name = None
		self.price = None
		self.quantity = None
		self.product = list()
			
			
	def add_inventory(self,name,price,qty):
		
		# initialize the variables to its correct data type		
		self.name = str(name)
		self.price = float(price)
		self.quantity = int(qty)
		
		# if the item details are not blank append a list of 1 item to the main product list
		if( name is not None and price is not 0 and qty is not 0):
			self.product.append([self.name,self.price,self.quantity])	
		
		#test case to see all products appended	successfully	
		#print(self.product)
		
		# return the final product
		return self.product
		
	def remove_inventory(self,item):
		
		# flase flag to be used if the value is not present to tell the user
		flag = False

		# i is the index and j is the value
		for i,j in enumerate(self.product):
			# if the item name given by user matches the product present in the inventory then it deletes the value
			if( item in j[0] ):
				self.product.remove(j) 
				flag = True
			
		if( flag == False ):
			return 'The item does not exist in the inventory'
		
		#test case to see the product is successfully deleted	
		#print(self.product)

		# return the final product
		return self.product

	def find_item(self,name):
	
		# flase flag to be used if the value is not present to tell the user
		flag = False
		choices = []

		# loop through the inventory and return if found only for exact match not partial match
		for i in self.product:
			if(name == i[0]):
				flag = True
				return (i,flag)
			else:
				flag = False
			
			"""
			This gives the option to get all possible values if user enters wrong or partially correct name such 
			inventory = Papaya , Paan  and user enters Pa then it appends both values as it matches
			elif(name in i[0]):
				flag = True
				choices.append(i)
			"""	

		if( flag == False ):
			print("Item is not found \n")
			return ('Item is not found',flag)

		#return choices
	
	def display(self):


		print("List of items available in store: \n")
		print("Item No.		Item name 		Item Price 		Item QTY")
		for i,j in enumerate(self.product):
			print(i,*j,sep='\t 	  	')

		print("\n")

	def get_quantity(self,name):
			
		for i in self.product:
			if( name[0] in i[0] ):
				return i[2]

	def set_quantity(self,name,qty):
		
		for i in self.product:
			if( name[0] in i[0] ):
				i[2] = qty

		#self.display()

		
def main():
	
	i = Item()
	i.add_inventory('Apple',20,100)
	i.add_inventory('Mango',60,100)
	i.add_inventory('Banana',70,100)
	i.add_inventory('Berry',10,100)
	i.add_inventory('Coconut',30,100)
	i.add_inventory('Papaya',25,100)
	i.add_inventory('Papla',22,100)
	i.add_inventory('pop',50,100)

	#i.display()
	#print(i.findItem('Papaya'))
	
	abc = User('Ananth',i)
	
	print(abc.__repr__())

	x = True
	while( x != False ):
		x = abc.choice()
		
	
	#abc.add_cart()
	#abc.carts[1].add_item(mango,4)

	#abc.carts[1].remove_item('mango',4)

if __name__ == '__main__':
    main()









