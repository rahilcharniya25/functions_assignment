
list = []


def adding_item_to_list():
    item = str(input("enter the name of item to add in the list : "))
    list.append(item)
    print(f" {item} has been added to your list ")
    
    
def deleting_item_from_the_list():
    item = str(input("enter the name of item to remove from the list  : "))
    for item in list:
        list.remove(item)
        print(f" {item} has been removed to your list ")
    else: 
        print(f"item doesnt exist in the list ")
    
def show_item_in_list():
    for item in list:
        print(f"* { item}")
    

while True:
    print(" press 1 to add item to the list ")
    print(" press 2 to remove item to the list ")
    print(" press 3 to view item in the list ")
    print(" press 4 to exit ")

    choice = input("enter the option :")
    if choice=="1":
        adding_item_to_list()
    elif choice=="2":
        deleting_item_from_the_list()
    elif choice=="3":
        show_item_in_list()
    elif choice=="4":
        break
    else:
        print("please enter the correct choice again. thank you ")
