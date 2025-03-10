frappe.ui.form.on("Expenses", {
    refresh: function(frm) {
        calculate_total_expenses(frm);
    },
    expenses_items_add: function(frm, cdt, cdn) {
        calculate_total_expenses(frm);
    },
    expenses_items_remove: function(frm) {
        calculate_total_expenses(frm);
    }
});

function calculate_total_expenses(frm) {
    let total = 0;
    frm.doc.expenses_items.forEach(item => {
        total += item.amount || 0; // Ensure it doesn’t break if amount is undefined
    });

    // Set the total in the form field
    frm.set_value("total_expenses", total);
}
