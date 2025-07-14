# Task List App (PyQt5)

A simple desktop application built with **Python** and **PyQt5** for managing your personal task list.

---

## 📦 Features

- ✅ Add new tasks
- ❌ Delete selected tasks
- 🕘 Mark tasks as completed (with strikethrough)
- 💾 Automatically saves tasks to a local text file
- 📂 Loads saved tasks on startup

---

## 🖥️ GUI Preview

![screenshot](https://github.com/Kyara0797/TaskList/blob/main/images/Reference_Project_Task_List.png)


---

## 🚀 Getting Started

### 1. **Clone the repository**

```markdown
git clone https://github.com/Kyara0797/TaskList.git
cd TaskList
```
### 2. **Create a virtual environment** (recommended)
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows

### 3. **Install dependencies**
pip install -r requirements.txt

### 4. **Run the application**
python task_list.py

📁 **File Structure**
bash
Copy
Edit
TaskList/
├── env/                # (ignored) virtual environment
├── task_list.py        # main Python file
├── tareas.txt          # local task storage
├── requirements.txt    # dependencies
├── .gitignore
└── README

###🧑‍💻 **Technologies Used**
Python 3.x
PyQt5
