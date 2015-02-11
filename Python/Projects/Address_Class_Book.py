# Billy's Address Book now with some Class.

class Contact:
	def __init__(self, name, email, phone, address):
		self.name = name
		self.email = email
		self.phone = phone
		self.address = address

	def __str__(self):
		return "Name: " + self.name + '\n' + "Email: " + self.email + '\n' + "Phone: " + self.phone + '\n' + "Address: " + self.address + '\n'

test_contact = Contact("bob", "bob@bob.com", "555-555-5555", "1234 SE bob ST") # Test info
contacts = {"test_contact": test_contact}

joey = Contact("joey", "joey@internet.com", "8675309", "123 Elm St") # Test info
contacts[joey.name] = joey


def menu():# Screen title and menu, use the numbers to choose.
	print "Address Book."
	print "Choose a number for what you want to do."
	print "1. Add Contact "
	print "2. View Contacts"
	print "3. Update Contact"
	print "4. Delete Contact"
	print "5. Quit Address Book"

def add_contact(contacts):
	print "Add Contact"
	new_contact_name = raw_input("Enter name ")
	new_contact_phone = raw_input("Enter phone number ")
	new_contact_email = raw_input("Enter email address ")
	new_contact_street_address = raw_input("Enter street address ")
	contacts[new_contact_name] = Contact(new_contact_name, new_contact_phone, 
		new_contact_email, new_contact_street_address)

def update(contacts):
	#print "update called"# For tesing I created a print function to make sure its working.
	update_contact_name = raw_input("Who do you want to update? ")
	print contacts[update_contact_name]
	update_element = raw_input("What would you like to update? phone? email? street address? name? ")
	
# TO DO make a new menu for update choices.

	print update_element
	
	if update_element == "phone": 
		new_phone_number = raw_input("Whats the new phone number? ")
		contacts[update_contact_name].phone = new_phone_number
		print contacts[update_contact_name]
	
	if update_element == "email":
		new_email = raw_input("Whats the new email? ")
		contacts[update_contact_name].email = new_email
		print contacts[update_contact_name]
	
	if update_element == "street address":
		new_contact_street_address = raw_input("Whats the new address? ")
		contacts[update_contact_name].address = new_contact_street_address
		print contacts[update_contact_name]

	if update_element == "name":
		new_name = raw_input("Whats the new name? ")
		contacts[update_contact_name].name = new_name
		print contacts[update_contact_name]
	

def delete(contacts):
	#print "delete called"# this is a test print again to see if its working.
	delete_contact = raw_input("Who would you like to delete? ")
	#print delete_contact# Used this print statement to make sure this function worked.
	del contacts[delete_contact]


def view(contacts): # Simple but, it works.
	for key in contacts:
		print contacts[key]

menu_option = 0 # Menu function.
while int(menu_option) < 5:
	menu()
	menu_option = raw_input(">") 
	if menu_option == "1":
		add_contact(contacts)
		view(contacts)
	elif menu_option == "2":
		view(contacts)
	elif menu_option == "3":
		update(contacts)
	elif menu_option == "4":
		delete(contacts)
	elif menu_option == "5":
		print "Smell ya later!"
		break 
	else:
		print "Not a valid option."
