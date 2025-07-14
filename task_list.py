import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QLineEdit, QMessageBox, QHBoxLayout,
    QListWidgetItem
)
from PyQt5.QtGui import QFont, QBrush, QColor

file_name = "tasks.txt"

def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file_content:
            for line in file_content:
                task, task_status = line.strip().split("|")
                list_item = create_list_widget_item(
                    task,
                    task_status == "1"
                )
                task_list.addItem(list_item)

def create_list_widget_item(text, completed=False):
    list_item = QListWidgetItem(text)
    font = QFont()
    font.setStrikeOut(completed)
    list_item.setFont(font)
    if completed:
        list_item.setForeground(QBrush(QColor("gray")))
    return list_item

def add_task():
    text = task_input.text().strip()
    if text:
        list_item = create_list_widget_item(text)
        task_list.addItem(list_item)
        task_input.clear()
        save_tasks()
    else:
        QMessageBox.warning(window, "Warning", "Please enter a task.")

def save_tasks():
    with open(file_name, "w", encoding="utf-8") as file_text:
        for index in range(task_list.count()):
            list_item = task_list.item(index)
            text = list_item.text()
            task_completed = "1" if list_item.font().strikeOut() else "0"
            file_text.write(f"{text}|{task_completed}\n")

def delete_task():
    list_item = task_list.currentItem()
    if list_item:
        index = task_list.row(list_item)
        task_list.takeItem(index)
        save_tasks()
    else:
        QMessageBox.warning(window, "Warning", "Please select a task.")

def complete_task():
    list_item = task_list.currentItem()
    if list_item:
        font = list_item.font()
        completed = not font.strikeOut()
        font.setStrikeOut(completed)
        list_item.setFont(font)
        list_item.setForeground(
            QBrush(QColor("gray") if completed else QColor("black"))
        )
        save_tasks()
    else:
        QMessageBox.warning(window, "Warning", "Please select a task.")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Task List")
window.setGeometry(100, 100, 400, 500)

main_layout = QVBoxLayout()

task_input = QLineEdit()
task_input.setPlaceholderText("Enter a new task...")
main_layout.addWidget(task_input)

buttons_layout = QHBoxLayout()

btn_add = QPushButton("Add")
btn_add.clicked.connect(add_task)
buttons_layout.addWidget(btn_add)

btn_delete = QPushButton("Delete")
btn_delete.clicked.connect(delete_task)
buttons_layout.addWidget(btn_delete)

btn_complete = QPushButton("Complete Task")
btn_complete.clicked.connect(complete_task)
buttons_layout.addWidget(btn_complete)

main_layout.addLayout(buttons_layout)

task_list = QListWidget()
main_layout.addWidget(task_list)

window.setLayout(main_layout)

load_tasks()

window.show()
sys.exit(app.exec_())
