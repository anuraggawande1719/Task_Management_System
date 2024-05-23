from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task
#Create a task
task1=create_task("Complete Your Assignment","Finish TASK MANAGEMENT SYSTEM")

#Display The Task
print("Task 1:",task1)

#Edit The Task
edit_task(task1,new_title="Updated Assignment",new_description="Review and Submit to Rashmi Mam")

#Display The Update tsak
print("Updated Task 1:",task1)

#Categorize The Task
categorize_task(task1,"Zappcode Academy")

#Display the Categorized task
print("Categorized Task 1:",task1)