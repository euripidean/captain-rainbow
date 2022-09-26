#initialize checklist
checklist = list()

#User Input Function
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#Create function
def create(item):
    checklist.append(item)

#Read function
def read(index):
    # return checklist[index]
    print(checklist[index])

#Update function
def update(index,item):
    checklist[index] = item

#Delete function
def destroy(index):
    checklist.pop(index)

#List function
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = '√'+ checklist[index]

def remove_check(index):
    checklist[index] = checklist[index].strip('√')

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        while item_index > len(checklist):
            item_index = int(user_input("Please enter a correct item number:"))
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    #Update chosen Item    
    elif function_code == "U":
        item_index = int(user_input("Index Number? > "))
        while item_index > len(checklist):
            item_index = int(user_input("Please enter a correct item number:"))
        item_update = (user_input("What would you like to update your item to?  > "))
        update(item_index,item_update)
        print(f"Item updated! It is now {checklist[item_index]}")

    #Check Item Off
    elif function_code == "X":
        item_index = int(user_input("Index Number? > "))
        while item_index > len(checklist):
            item_index = int(user_input("Please enter a correct item number:"))
        mark_completed(item_index)
        print(f"Check added to {checklist[item_index]}")

    #Remove Check
    elif function_code == "Z":
        item_index = int(user_input("Index Number? > "))
        while item_index > len(checklist):
            item_index = int(user_input("Please enter a correct item number:"))
        remove_check(item_index)
        print(f"Check removed from {checklist[item_index]}")


    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    else:
    # Catch all
        print("Unknown Option")
    return True



#Test function
def test():
    create("purple socks")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    mark_completed(0)
    print(checklist[0])

    select("C")
    select("R")
    select("P")
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

#Loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update an item on the list, X to check an item out, Z to remove a previous check, and press Q to exit :  ").upper()
    running = select(selection)

# test()
