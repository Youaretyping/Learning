# __author__ = 'Billy'

class ProjectApp(object):
    def show_contacts_menu(self):
        print "\n  Contacts Menu\n"
        print "  1. Add\n  2. View Contacts\n  3. Update\n  4. Delete\n  5. Back to main menu\n"

        command = ""
        while command != "5":
            command = raw_input("  Enter the command number: ").strip().lower()

            if command == "1":
                print "This is where we add a contact..."

    def show_inbox_menu(self):
        print "\n  Inbox Menu\n"
        print "  1. Add Project\n  2. List Projects\n  3. Back to Main Menu\n"

        command = ""
        while command != "3":
            command = raw_input("  Enter the project command number: ").strip().lower()

    def show_calendar_menu(self):
        print "\n Calendar Menu\n"
        print "1. List for the Day\n2. View Week\n3. View Month\n4. View Year\n5. Back to Main Menu"

        command = ""
        while command != "5":
            command = raw_input("  Enter the command number:").strip().lower()

    def command_loop(self):
        # Current command the user entered
        command = ""

        # Main command loop - ask for the command and execute it. Quit if user enters '4'
        while True:

            print "\nMain Menu\n"
            print "1. Contact Book\n2. Inbox\n3. Calendar\n4. Quit\n"

            command = raw_input("\nEnter the command number: ").strip().lower()
            if not command:
                continue

            elif command == "4":
                break

            elif command == "1":
                self.show_contacts_menu()

            elif command == "2":
                self.show_inbox_menu()

            elif command == "3":
                self.show_calendar_menu()

            else:
                print "Unknown command:", command

        print "Goodbye"


app = ProjectApp()
app.command_loop()