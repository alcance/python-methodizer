from pyfiglet import Figlet

# ascii title config
f = Figlet(font='slant')
print(f.renderText('python methodizer'))

name = input("What is your name? ")
print(f"Hello, {name}!")

# remove(): remove the first occurrence of a *specified* value
def remove_element(my_list):
    while True:
        try:
            element = int(input("--> what element do you want to remove? "))
            print(f"removing {element}...")
            if element in my_list:
                my_list.remove(element)
                print(f"--> good job! The element has been removed.")
                print(f"--> this is the new list: {my_list}")
                break
            else:
                print("--> target is not in list. Try again!")
        except ValueError:
            print("--> please enter a valid number.")

# adds an element to the end of the list
def append_element(my_list):
	while True:
		try:
			element =int(input("--> what element do you want to append? "))
			if element in  my_list:
				print("--> element already exists. try another one!.")
			else:
				print(f"removing {element}")
				my_list.append(element)
				print(f"--> good job! The element has been appended.")
				print(f"--> this is the new list: {my_list}")
				break
		except ValueError:
			print("--> please enter a valid number.")


my_list = [1, 2, 3, 4, 5, 6]
print(f"This is the list {my_list}")

action_end = True
while action_end:
    action = input("--> What do you want to do with the list? ")

    options = {
        "remove": remove_element,
		"append": append_element
    }

    selected_function = options.get(action)
    if selected_function:
        selected_function(my_list)
    else:
        print("--> Invalid option. Try again.")

    keep_going = input("Do you want to keep operating? (y/n) ").lower()
    while keep_going not in ['y', 'n']:
        keep_going = input("Not a proper input. Type 'y' or 'n': ").lower()

    if keep_going == 'n':
        action_end = False

print(f"This is the new list: {my_list}")
