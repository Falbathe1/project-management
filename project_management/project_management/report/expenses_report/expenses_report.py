# Copyright (c) 2025, pm and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def get_data():
    return frappe.db.sql("""
        SELECT parent AS parent, amount AS amount
        FROM `tabExpenses Items`
        ORDER BY parent ASC
    """, as_dict=True)



def get_columns():
    return [
        {
            "label": _("Parent Name"),
            "fieldname": "parent",
            "fieldtype": "data",
            "options": "Expenses", 
            "width": 250
        },
        {
            "label": _("Expense Amount"),
            "fieldname": "amount",
            "fieldtype": "float",
            "width": 150
        }
    ]

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data
