import json
from pathlib import Path 


file_path=Path("lists.json")


if file_path.is_file():
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            data=json.load(file)
    except json.JSONDecodeError:
        lists={"tasks":[]}
        with open(file_path,"w",encoding="utf-8") as file:
            json.dump(lists,file,indent=2,ensure_ascii=False)
        with open(file_path,"r",encoding="utf-8") as file:
            data=json.load(file)
        
else:
    lists={"tasks":[]}
    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(lists,file,indent=2,ensure_ascii=False)
    with open(file_path,"r",encoding="utf-8") as file:
        data=json.load(file)


def save_tasks(data):
    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=2,ensure_ascii=False)

def add_tasks(data,task):
    data['tasks'].append(task)
    save_tasks(data)
    print("Task added successfully")
        
def view_tasks(data):
    if not data['tasks']:
        print('No Tasks to be done')
        return False
    else:
        for index, item in enumerate(data["tasks"],1):
            print(f'{index}. {item}')
        return True


def remove_tasks(data,number):
    if number>=1 and number <=len(data['tasks']):
        data['tasks'].pop(number-1)
        save_tasks(data)
        print('Task removed successfully !')
    else:
        print('Invalid task number. Please choose from the given above')

def check(s):
    if not s.strip():
        print('Cannot leave blank')
        return False
    else:
        return True 

while True:
    try:
        obj=int(input("Welcome to your Task Manager \n1.Add Task\n2.View Tasks\n3.Remove a Task\n4.Exit\n"))
        if obj==1:
            ent=input("Enter task : ")
            if check(ent):
                add_tasks(data,ent)
        elif obj==2:
            view_tasks(data)
        elif obj==3:
            if view_tasks(data):
                try:
                    num=int(input('Enter the tasks number you would like to remove : '))
                    remove_tasks(data,num)
                except ValueError:
                    print('Enter a number')

        elif obj==4:
            print('Exited program successfully !')
            break
        else:
            print("Invalid input please choose from the options given above")
    except ValueError:
        print('Please choose from the numbers provided above')
        continue
