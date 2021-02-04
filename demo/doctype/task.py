import frappe
def execute():
    a=frappe.new_doc("Task")
    a.subject='axy'
    a.save()
    print(a.name)
    # #bench execute demo.doctype.task.execute
    # print('***************')