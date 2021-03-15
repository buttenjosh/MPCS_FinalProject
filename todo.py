# Final Project

class Task:
    """Representation of task attributes"""

    def __init__(self, created, completed, name, unique_id, priority, due_date, optional):
        self.created = created
        self.completed = completed
        self.name = name
        self.unique_id = unique_id
        self.priority = priority
        self.due_date = due_date
        self.optional = optional
    
class Tasks:
    """Task list"""

    def __init__(self, created, completed, name, unique_id, priority, due_date, optional, age, match_term, tasks_lists):
        self.created = created
        self.completed = completed
        self.name = name
        self.unique_id = unique_id
        self.priority = priority
        self.due_date = due_date
        self.optional = optional
        self.age = age
        self.match_term = match_term
        self.tasks_lists = []

    def add_task(self, name, due_date, priority):
        """Prompts to add task"""
        self.name = name 
        self.due_date = due_date
        self.priority = priority
        
    def list_task(self, unique_id, age, due_date, priority, name):
        """Displays a list of the uncompleted tasks sorted by the due date"""
        self.unique_id = unique_id
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name
    
    def list_task_search(self, match_term, unique_id, age, due_date, priority, name):
        """Search for tasks that match a term"""
        self.match_term = match_term
        self.unique_id = unique_id
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name        
        
    def done(self, unique_id):
        """Complestes a task"""
        self.unique_id = unique_id

    def delete(self, unique_id):
        """Deletes a task by passing the delete command and the unique identifier"""
        self.unique_id = unique_id

    def report(self, unique_id, age, due_date, priority, name, created, completed):
        """Lists all tasks, including both completed and incomplete tasks"""
        self.unique_id = unique_id               
        self.age = age
        self.due_date = due_date
        self.priority = priority
        self.name = name
        self.created = created
        self.completed = completed
        
        


       