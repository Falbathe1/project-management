import frappe
from frappe.model.document import Document

class Expenses(Document):
    def before_save(self):
        """Calculate total expenses before saving the document."""
        self.total_expenses = sum(
            item.amount for item in self.get("expenses_items", []) if item.amount
        )
