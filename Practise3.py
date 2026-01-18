class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True


tasks = []



def add_task():
    title = input("Task title: ")
    tasks.append(Task(title))


def list_tasks():
    for i, task in enumerate(tasks):
        if task.completed:
            status = "✓"
        else:
            status = "✗"
        print(f"{i+1} - {task.title} [{status}]")


def complete_task():
    index = int(input("Task index: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index].complete()


def delete_task():
    index = int(input("Task index: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]


def save_task():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task.title}|{task.completed}\n")


def load_task():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                title, completed = line.strip().split("|") #satırı temizle ve ayır
                task = Task(title)
                task.completed = completed == "True" #dosyada true yazıyorsa görev tamamlanmış gelir
                tasks.append(task) #false yazıyorsa tamamlanmamış gelir
    except FileNotFoundError:
        pass


load_task()


while True:
    print("\n1- Add Task\n2- List Tasks\n3- Complete Task\n4- Delete Task\n5- Save Task\n6- Exit")
    choice = input("Choice: ")


    if choice =="1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_task()
    elif choice == "6":
        break