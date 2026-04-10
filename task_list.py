lst = []

def add_task():
    print("enter youre task: ")
    task = str(input())
    lst.append(task)

def remove_task():
    print("enter num of task: ")
    num = int(input())
    del lst[num-1]

def show_list():
    for i in range(len(lst)):
        print(i+1, ". ", lst[i])
     

def main():
    exit = True
    while exit:
        print("what you want to do(add, remove, list, exit): ")
        task = str(input())
        if task == "add":
            add_task()
        elif task == "remove":
            remove_task()
        elif task == "list":
            show_list()
        elif task == "exit":
            exit = False

    


main()