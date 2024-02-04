def parse_input(user_input):
    cmd, *args= user_input.split()
    cmd=cmd.strip().lower()
    return cmd, *args
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    name, phone= args
    contacts[name]=phone
    return "this name is in your contacts.\nchanges is done\n"
def show_all(contacts):
    return contacts
def main():
    contacts={}
    print("Hello. \nI'm glad to see you")
    while True:
        try:
            user_input =input("Enter a command: ")
            command, *args = parse_input(user_input)
        
            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command== "hello":
                print("How can I help you?")
            elif command=="add":
                print(add_contact(args, contacts))
            elif command=="change":
                print(change_contact(args, contacts))
            elif command == "show":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print("there are something wrong",f" \n{e}", "\n Plese, try again.")

if __name__=="__main__":
    main()