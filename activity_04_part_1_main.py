""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
from contact_list.contact_list import ContactList
from PySide6.QtWidgets import QApplication
import sys

# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactList()
    window.show()
    sys.exit(app.exec())