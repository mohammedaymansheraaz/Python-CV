
my_dict = {}
print("Enter keys and values (type 'done' to finish):")
while True:
    key = input("Key: ")
    if key == 'done': 
        break
    my_dict[key] = input("Value: ")

while True:
    print(f"\nDict: {my_dict} | Length: {len(my_dict)}")
    print("\n1.get  2.keys  3.values  4.items  5.update  6.pop")
    print("7.popitem  8.clear  9.copy  10.fromkeys  11.setdefault  0.exit")
    
    choice = input("\nChoice: ")
    
    if choice == '1':
        key = input("Key: ")
        print(f"Result: {my_dict.get(key, 'Not found')}")
    
    elif choice == '2':
        print(f"Keys: {list(my_dict.keys())}")
    
    elif choice == '3':
        print(f"Values: {list(my_dict.values())}")
    
    elif choice == '4':
        print("Items:")
        for k, v in my_dict.items():
            print(f"  {k}: {v}")
    
    elif choice == '5':
        new_key = input("New key: ")
        new_val = input("New value: ")
        my_dict.update({new_key: new_val})
        print("Updated!")
    
    elif choice == '6':
        key = input("Key to pop: ")
        result = my_dict.pop(key, "Not found")
        print(f"Popped: {result}")
    
    elif choice == '7':
        if my_dict:
            print(f"Popped: {my_dict.popitem()}")
        else:
            print("Dict is empty!")
    
    elif choice == '8':
        my_dict.clear()
        print("Cleared!")
    
    elif choice == '9':
        copy_dict = my_dict.copy()
        print(f"Copy: {copy_dict}")
    
    elif choice == '10':
        keys = input("Keys (comma-separated): ").split(',')
        val = input("Default value: ")
        new_dict = dict.fromkeys(keys, val)
        print(f"Created: {new_dict}")
        if input("Replace current dict? (y/n): ") == 'y':
            my_dict = new_dict
    
    elif choice == '11':
        key = input("Key: ")
        default = input("Default: ")
        result = my_dict.setdefault(key, default)
        print(f"Result: {result}")
    
    elif choice == '0':
        print(f"Final dict: {my_dict} | Length: {len(my_dict)}")
        break
    
    else:
        print("Invalid choice!")
