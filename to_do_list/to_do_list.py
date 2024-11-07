from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QComboBox, QTableWidgetItem
from PySide6.QtCore import Slot
from task_editor import TaskEditor

class ToDoList(QMainWindow):
    """
    ToDoList Class (QMainWindow). Provides users a 
    way to manage their to-do tasks.
    """
    def __init__(self):
        """
        Initializes a ToDo List window in which 
        users can add and edit to-do tasks.
        """
        super().__init__()
        self.__initialize_widgets()
        
        
        self.add_button.clicked.connect(self.on_add_task)
        self.task_table.cellClicked.connect(self.on_edit_task)

    def __initialize_widgets(self):
        """
        Initializes the QWindow and all widgets.
        """
        self.setWindowTitle("To-Do List")

        # Input field for task description
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Task")

        # Combo box for task status
        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])

        # Buttons for adding tasks
        self.add_button = QPushButton("Add Task", self)

        # Table to display tasks
        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task", "Status"])

        # Label to display status messages
        self.status_label = QLabel(self)

        # Layout configuration
        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.status_combo)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_table)
        layout.addWidget(self.status_label)

        # Set up the main container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def on_add_task(self):
        """
        Slot for adding a task when the Add Task button is clicked.
        Validates input fields and adds a new task to the table.
        """
        task = self.task_input.text().strip()
        status = self.status_combo.currentText().strip()

        if task:
            row_position = self.task_table.rowCount()
            self.task_table.insertRow(row_position)
            self.task_table.setItem(row_position, 0, QTableWidgetItem(task))
            self.task_table.setItem(row_position, 1, QTableWidgetItem(status))
            self.status_label.setText(f"Added task: {task}")
            self.task_input.clear()
        else:
            self.status_label.setText("Please enter a task and select its status.")

    @Slot(int, int)
    def on_edit_task(self, row, column):
        """
        Slot for editing a task when a row is clicked in the task table.
        Opens the TaskEditor dialog to update the task's status.
        """
        current_status = self.task_table.item(row, 1).text()
        task_editor = TaskEditor(row, current_status)
        
        # Connect the task_updated signal from TaskEditor to the update_task_status slot
        task_editor.task_updated.connect(self.update_task_status)
        
        # Open the TaskEditor dialog
        task_editor.exec()

    @Slot(int, str)
    def update_task_status(self, row, new_status):
        """
        Slot to update the task status in the table.
        """
        self.task_table.setItem(row, 1, QTableWidgetItem(new_status))
        self.status_label.setText(f"Task status updated to: {new_status}")
