from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QComboBox
from PySide6.QtCore import Signal, Slot

class TaskEditor(QDialog):
    """
    TaskEditor Class (QDialog). Allows the user to update the 
    status of a to-do list item.
    """
    # Custom signal to notify the main window about the updated task status
    task_updated = Signal(int, str)

    def __init__(self, row: int, status: str):
        """
        Initializes the TaskEditor dialog with the specified row and status.
        """
        super().__init__()
        self.row = row  # Store the row number of the task being edited
        self.initialize_widgets()         
        self.status_combo.setCurrentText(status)

         # Connect Save button to on_save_status slot
        self.save_button.clicked.connect(self.on_save_status)


    def initialize_widgets(self, status: str):
        """
        Initializes the dialog window and its widgets.
        """
        self.setWindowTitle("Edit Task Status")

        # Dropdown to select the new status
        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])
        self.status_combo.setCurrentText(status)  # Set initial status

        # Save button to confirm the status change
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.on_save_status)  # Connect button to slot

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.status_combo)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.setFixedWidth(150)

    @Slot()
    def on_save_status(self):
        """
        Slot to handle saving the updated status.
        Emits the task_updated signal with the new status and row,
        then closes the dialog.
        """
        new_status = self.status_combo.currentText()
        self.task_updated.emit(self.row, new_status)  # Emit the signal with row and new status
        self.accept()  # Close the dialog
