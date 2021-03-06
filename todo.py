# Final Project

import sys

def task_input():
    """Function to input new task attributes"""
    name = input("Task name: ")
    due_date = input("Due date: ")
    priority = input("Priority: ")
    return name, due_date, priority

class Task:
    """Representation of task attributes"""

    def __init__(self, created, completed, name, unique_id, priority, due_date, optional, age, match_term):
        self.created = created
        self.completed = completed
        self.name = name
        self.unique_id = unique_id
        self.priority = priority
        self.due_date = due_date
        self.optional = optional
        self.age = age
        self.match_term = match_term
    
class Tasks:
    """Task list"""
    def __init__(self):
        self.tasks_list = []

    def add(self):
        """Prompts to add task"""
        new_task = Task(name, due_date, priority)
        self._tasks_list.append(new_task)
        Print("Added a new task", len(self.tasklist), new_task.name)

    def list_task(self):
        """Displays a list of the uncompleted tasks sorted by the due date"""
        self.unique_id = unique_id
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name
    
    def list_task_search(self):
        """Search for tasks that match a term"""
        self.match_term = match_term
        self.unique_id = unique_id
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name        
        
    def done(self):
        """Complestes a task"""
        self.unique_id = unique_id

    def delete(self):
        """Deletes a task by passing the delete command and the unique identifier"""
        self.unique_id = unique_id

    def report(self):
        """Lists all tasks, including both completed and incomplete tasks"""
        self.unique_id = unique_id               
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name
        self.created = created
        self.completed = completed

# Driver code
if __name__ == "__main__":

    # Create variables to hold fraction values and convert to mixed fractions, decimals
    name, due_date, priority = task_input()
    new_task = Task(name, due_date, priority)
    

    add()    