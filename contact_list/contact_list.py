from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot

class ContactList(QMainWindow):
    """
    Contact List Class (QMainWindow). Provides users a 
    way to manage their contacts.
    """
    def __init__(self):
        """
        Initializes a Contact List window in which 
        users can add and remove contact data.
        """
        super().__init__()
        self.__initialize_widgets() 
        
        # Connect add_button to the on_add_contact slot
        self.add_button.clicked.connect(self.on_add_contact)
        
        # Connect remove_button to the on_remove_contact slot
        self.remove_button.clicked.connect(self.on_remove_contact)

    def __initialize_widgets(self):
        """
        Initializes the QWindow and all widgets.
        """
        self.setWindowTitle("Contact List")

        # Input fields for contact name and phone number
        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        # Buttons for adding and removing contacts
        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        # Table to display contacts
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        # Label to display status messages
        self.status_label = QLabel(self)

        # Layout configuration
        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        # Set up the main container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def on_add_contact(self):
        """
        Slot for adding a contact when the Add Contact button is clicked.
        Validates input fields and adds a new contact to the table.
        """
        # Extract text from input fields
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        # Check if both name and phone fields have data
        if name and phone:

            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)
            
            # Create QTableWidgetItem for name and phone
            name_item = QTableWidgetItem(name)
            phone_item = QTableWidgetItem(phone)
            
            # Add the items to the respective columns in the new row
            self.contact_table.setItem(row_position, 0, name_item)
            self.contact_table.setItem(row_position, 1, phone_item)
            
            # Update the status label with a success message
            self.status_label.setText(f"Added contact: {name}")
            
            # Clear input fields after adding the contact
            self.contact_name_input.clear()
            self.phone_input.clear()
        else:
            # Prompt the user to enter both fields if data is missing
            self.status_label.setText("Please enter a contact name and phone number.")

    @Slot()
    def on_remove_contact(self):
        """
        Slot for removing a contact when the Remove Contact button is clicked.
        Confirms deletion and removes the selected contact from the table.
        """
        selected_row = self.contact_table.currentRow()
        if selected_row >= 0:
            # Prompt the user to confirm removal
            reply = QMessageBox.question(self, "Confirm Removal", "Are you sure you want to remove this contact?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Remove the selected row
                self.contact_table.removeRow(selected_row)
                self.status_label.setText("Contact removed.")
            else:
                # User canceled the removal
                self.status_label.setText("Contact removal canceled.")
        else:
            # No row selected
            self.status_label.setText("Please select a row to be removed.")



