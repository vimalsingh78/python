"""Example demonstrating a REST API server using FastAPI."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(title="Sample API Server")

# Data Models
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()

# In-memory database
tasks_db = []
task_counter = 1

# API Routes
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Task Management API"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks(skip: int = 0, limit: int = 10):
    """Get all tasks with pagination."""
    return tasks_db[skip : skip + limit]

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Get a specific task by ID."""
    task = next((task for task in tasks_db if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """Create a new task."""
    global task_counter
    task.id = task_counter
    task_counter += 1
    tasks_db.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    """Update a task by ID."""
    task_idx = next((idx for idx, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updated_task.id = task_id
    tasks_db[task_idx] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by ID."""
    task_idx = next((idx for idx, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db.pop(task_idx)
    return {"message": "Task deleted successfully"}

# Add some sample tasks
sample_tasks = [
    Task(title="Learn FastAPI", description="Study FastAPI framework", completed=True),
    Task(title="Build API", description="Create a REST API server", completed=False),
    Task(title="Write Tests", description="Add unit tests for the API", completed=False)
]

for task in sample_tasks:
    task.id = task_counter
    task_counter += 1
    tasks_db.append(task)

def main():
    """Run the API server."""
    print("Starting API server...")
    print("Once running, visit:")
    print("- API documentation: http://localhost:8000/docs")
    print("- Alternative documentation: http://localhost:8000/redoc")
    
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()