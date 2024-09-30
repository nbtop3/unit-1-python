task = {}




while True:
    print("/n0ptions: ")
    print("1. add tasks? ")
    print("2. remove task? ")
    print("3. view tasks? ")
    print("4.exit ")

    choice = input("choose options 1-4: ")

    if choice == "1":
        a = input("enter task:")
        task.append(a)
        print(f"task'{task}' added: ")

    elif choice == "2":
        task_number = int(input("enter task choice to remove: "))
        if 0 <= task_number < len(task):
            removed_task = task.
        
