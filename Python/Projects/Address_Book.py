# Billy's Address Book
contacts = {"test_contact": ["test_contact", # The test contact list.
							 "1234567",
							 "test@internet.com",
							 "123 elm st."]}



def menu():# Screen title and menu, use the numbers to choose.
	print "Address Book."
	print "Choose a number for what you want to do."
	print "1. Add Contact "
	print "2. View Contacts"
	print "3. Update Contact"
	print "4. Delete Contact"
	print "5. Quit Address Book"

def add_contact():# prompt the user for contact information.
	print "Add Contact"
	new_contact_name = raw_input("Enter name ")
	new_contact_phone = raw_input("Enter phone number ")
	new_contact_email = raw_input("Enter email address ")
	new_contact_street_address = raw_input("Enter street address ")
	contacts[new_contact_name] = [new_contact_name,
								  new_contact_phone,
								  new_contact_email,
								  new_contact_street_address]

def update():
	#print "update called"# For tesing I created a print function to make sure its working.
	update_contact_name = raw_input("Who do you want to update? ")
	print contacts[update_contact_name]
	update_element = raw_input("What would you like to update? phone? email? street address? name? ")
	# make a menu for update choices.

	print update_element
	
	if update_element == "phone": 
		new_phone_number = raw_input("Whats the new phone number? ")
		contacts[update_contact_name][1] = new_phone_number
		print contacts[update_contact_name]
	
	if update_element == "email":
		new_email = raw_input("Whats the new email? ")
		contacts[update_contact_name][2] = new_email
		print contacts[update_contact_name]
	
	if update_element == "street address":
		new_contact_street_address = raw_input("Whats the new address? ")
		contacts[update_contact_name][3] = new_contact_street_address
		print contacts[update_contact_name]

	if update_element == "name":
		new_name = raw_input("Whats the new name? ")
		contacts[update_contact_name][0] = new_name
		print contacts[update_contact_name]
	

def delete():
	#print "delete called"# this is a test print again to see if its working.
	delete_contact = raw_input("Who would you like to delete? ")
	#print delete_contact# Used this print statement to make sure this function worked.
	del contacts[delete_contact]


def view(): # Simple but, it works.
	print contacts 

menu_option = 0 # Menu function.
while int(menu_option) < 5: # The program quits without int. With int it loops back to the menu as intended.
	menu()
	menu_option = raw_input(">")
	if menu_option == "1":
		add_contact()
		view()
	if menu_option == "2":
		view()
	if menu_option == "3":
		update()
	if menu_option == "4":
		delete()
	if menu_option == "5":
		print "Smell ya later!"
		break 






# Working on this set of commands to write and pull the contact info from a txt file.

# contacts_file = open("/home/student/Learn/Projects/contacts.txt", "w")
#
# for key in contacts:
# 	contact_info = []
# 	contact_info.append(key)
# 	for value in contacts[key]:
# 		contact_info.append(value)
#
# 	string_dump = """
# 			  contact: %s
# 			  name: %s
# 			  phone: %s
# 			  email: %s
# 			  address: %s
# 			  """ % contact_info
#
# 	contacts_file.write(string_dump)
#
# contacts_file.close()
#
# def show_contact():
