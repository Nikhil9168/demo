# Copyright (c) 2013, fairsh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns=get_columns()
	data=get_data()
	return columns, data
def get_columns():
	return[
		{
			"label":'Purchase Invoice',
			"fieldname":'purchase_invoice',
			"fieldtype":'Link',
			"options":'Purchase Invoice',
		},
		{
			"label":'Supplier Name',
			"fieldname":'supplier_name',
			"fieldtype":'Data',

		},
		{
			"label":'Item',
			"fieldname":'item',
			"fieldtype":'Data',
		},
		{
			"label":'Posting Date',
			"fieldname":'posting_date',
			"fieldtype":'Date',
		},
		{
			"label":'Due Date',
			"fieldname":'due_date',
			"fieldtype":'Date',
		},
		{
			"label":'Taxes And Charges',
			"fieldname":'taxes_and_charges_added',
			"fieldtype":'Currency',
		},
		{
			"label":'Grand Total',
			"fieldname":'grand_total',
			"fieldtype":'Currency',
		},
		{
			"label":'Total Quantity',
			"fieldname":'total_qty',
			"fieldtype":'Data',
		},
	]

def get_data():
	print('$$$$$$$$$$$$$$$$$$')
	data=[]
	for d in frappe.get_all('Purchase Invoice',['posting_date','name','due_date','grand_total','taxes_and_charges_added']):
		row={
			'posting_date':d.get('posting_date'),
			'purchase_invoice':d.get('name'),
			'due_date':d.get('due_date'),
			'taxes_and_charges_added':d.get('taxes_and_charges_added'),
			'grand_total':d.get('grand_total')
		}
		for c in frappe.get_all('Purchase Invoice Item',{'parent':d.name},['item_code']):
			row.update({'item':c.get('item_code')})
		#data.append(row)
		for e in frappe.get_all('Purchase Invoice',['total_qty','supplier_name']):
			row.update({'total_qty':e.get('total_qty')})
			row.update({'supplier_name':e.get('supplier_name')})
		data.append(row)			
	return data		



