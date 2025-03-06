# Free Python eBooks and Learning Resources

## 📚 Free eBooks

### 1. Think Python 2e
- **Author**: Allen B. Downey
- **Download**: [Green Tea Press](https://greenteapress.com/wp/think-python-2e/)
- **Topics**:
  - Python fundamentals
  - Object-oriented programming
  - Data structures
  - Recursion
  - Debugging

### 2. A Byte of Python
- **Author**: Swaroop C H
- **Read Online**: [Python Tutorial](https://python.swaroopch.com/)
- **Topics**:
  - Python basics
  - Object-oriented programming
  - Input/Output
  - Exception handling
  - Modules

### 3. Python Data Science Handbook
- **Author**: Jake VanderPlas
- **Read Online**: [GitHub Repository](https://jakevdp.github.io/PythonDataScienceHandbook/)
- **Topics**:
  - NumPy
  - pandas
  - Matplotlib
  - Scikit-learn
  - IPython

### 4. Python for Everybody
- **Author**: Charles Severance
- **Website**: [py4e.com](https://www.py4e.com/book)
- **Topics**:
  - Basic Python
  - Data structures
  - Web scraping
  - Databases
  - Data visualization

## 🎓 Interactive Learning Platforms

### 1. Codecademy Python Track
- Free interactive Python course
- Hands-on coding exercises
- Immediate feedback
- [Start Learning](https://www.codecademy.com/learn/learn-python)

### 2. Google's Python Class
- Free course from Google
- Video lectures
- Exercises and solutions
- [Access Course](https://developers.google.com/edu/python)

### 3. Microsoft's Python for Beginners
- 44 video lessons
- Practical examples
- Source code included
- [Watch Series](https://channel9.msdn.com/Series/Intro-to-Python-Development)

## 📺 YouTube Channels

1. **Corey Schafer**
   - In-depth Python tutorials
   - Best practices
   - Real-world applications

2. **Sentdex**
   - Python programming
   - Machine learning
   - Data analysis

3. **Real Python**
   - Python tutorials
   - Tips and tricks
   - Best practices

## 🛠️ Practice Resources

### 1. Project Ideas
- Calculator
- To-do list
- Weather app
- File organizer
- Web scraper
- Chat application
- Blog system
- API integration

### 2. Coding Challenges
- [CodingBat Python](https://codingbat.com/python)
- [Python Challenge](http://www.pythonchallenge.com/)
- [Exercism Python Track](https://exercism.io/tracks/python)

### 3. Example Projects
```python
# Simple Calculator
def calculator():
    """Basic calculator implementation."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")

# To-Do List
class TodoList:
    """Simple to-do list implementation."""
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added task: {task}")
    
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"Marked task {index} as done")
        else:
            print("Invalid task index")
    
    def show_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")
```

## 📝 Additional Resources

### 1. Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)

### 2. Community
- [Python Discord](https://discord.gg/python)
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Stack Overflow - Python](https://stackoverflow.com/questions/tagged/python)

### 3. Tools
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Jupyter Notebooks](https://jupyter.org/)