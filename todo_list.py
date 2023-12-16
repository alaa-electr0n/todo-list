# print the message to the user to know what to choose 
    # 1- add task to the list 
    # 2- Remove a task 
    # 3- mark task as complited 
    # 4- Delete all Tasks
    # 5- View the List 
    # 6- exit the program
# get the user input
# do a loop of function to begin the program again  
# check if the user input within 1- 6 else raise an error 
#  if user choose 1 -->  --> print task is sucessfully added 
# if user choose 2--> ask what to remove    ---> delete the task if it exsists --> print task has been removed 
# if user choose 2--> ask what to remove   ---> show there is no task if the task is not exist---->  print there is no such task 
# if user choose 3 ---> ask what to mark    ---> do a Mark the input task ---> print task is completed , Hooray 
# if user choose 4 ----> delete all tasks    ---> print No tasks for today
# if user choose 5 ----> view all tasks   
# if user choose 6 -----> exit the programe ---> print ---> ok Have a taskless day  


# get what the user want to do
print ("Welcome to The TO DO LIST 📃")
def get_user_action ():

    while True:

        message ='''Please choose a number from 1 to 6
            1- add task to the list 
            2- Remove a certain task 
            3- mark a certain task as complited 
            4- Delete all Tasks
            5- View the List 
            6- exit the program 
            '''  
           
           #handeling the errors and validating that inputs are only between 1 and 6
        try :
            user_action= input(message)
            if user_action in ["1","2","3","4","5","6"]:
                return user_action
            else:     
                raise ValueError("Please Enter a Number from 1 to 6")
        except ValueError:
            print("Invalid Input! Please Enter a Number from 1 to 6")   

#create the list variable 
tasks =[]


#add tasks to the list 
def add_task():
    #ask the user what task want to add
    added_task = input("What Task You Want To Add? ")
    tasks.append(added_task)
    print(f"Task '{added_task.capitalize()}' has been added!...")


# choose one task to remove 
def remove_one_task():
    #check if the list has tasks or not
    if len(tasks) :
       
    # show the user the tasks he already has :
        view_tasks()

        removed_task =int(input("Enter the task number you want to remove! "))

        if 0< removed_task >= len(tasks):
            del tasks[removed_task-1]  #delete a task by its index 
            print (f"Task '{removed_task}' has been removed!...")
        else: # Invalid number
            print("Task is not in the list! ")

    else:
        print("The List is Empty")    
     

def  mark_one_task():
    
    # show the tasks for the user 
    view_tasks()
    # ask him what task number is done
    completed_task = int(input("What Task Number You Have Accomplished?"))
    # reprint the task that has completed with a line  
    tasks[completed_task-1]= f"{tasks[completed_task-1]} ✔"
    view_tasks()
    


# clear the list 
def remove_all_tasks():
    if len(tasks):
        tasks.clear()
        print("All your tasks are removed successfully! ")
    else:
        print("It's already empty!")    


def view_tasks():
    if len(tasks):
        for i, task in enumerate(tasks):
            print(f"{i+1}- {task}")
    else:
        print("Nothing To Show!...")

def exit_list():
    print("Okay , Have a Taskless Day!")


def using_list ():
    while True:
        user_input = get_user_action()
        if user_input == "1":
            add_task()
        elif user_input == "2":
            remove_one_task()
        elif user_input =="3":
            mark_one_task()
        elif user_input =="4" :
            remove_all_tasks()
        elif user_input =="5":
            view_tasks()
        elif user_input =="6":
            exit_list()
            break        

using_list()