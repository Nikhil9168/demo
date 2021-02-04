# Copyright (c) 2013, Homzhub and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	return[
	    { 
             "label":'Purchase Invoice',
			 "fieldname":'purchase_invoice',
			 "fieldtype":'Link',
			 "options":'Purchase Invoice',
		},
		{
			"label":'Posting Date',
			"fieldname":'posting_date',
			"fieldtype":'Date',
		},
		{
			"label":'Supplier Name',
			"fieldname":'supplier_name',
			"fieldtype":'Data',
		},
		{
			"label":'Total Quantity',
			"fieldname":'total_qty',
			"fieldtype":'Data',
		},
		{
			"label":'Item',
			"fieldname":'item',
			"fieldtype":'Data',
		},
		]

#def get_data(filters):
	data=[]
	fltr={}
	# {'name': 'ACC-PINV-2020-00002'}

	if filters.get('name'):
		fltr.update({'name':filters.get('name')})
	# if filters.get('posting_date'):	
	# 	fltr.update({'posting_date':filters.get('posting_date')})

		
	for d in frappe.get_all('Purchase Invoice',fltr,['posting_date','name','due_date','total_qty','supplier_name']):
		row={ 
			'posting_date':d.get('posting_date'),
			'purchase_invoice':d.get('name'),
			'total_qty':d.get('total_qty'),
			'supplier_name':d.get('supplier_name')
		}
		fltr2={'parent':d.name}
		if filters.get('item'):
			fltr2.update({'item_code':filters.get('item')})

		for c in frappe.get_all('Purchase Invoice Item',fltr2,['item_code']):
	
			row.update({'item':c.get('item_code')})
			data.append(row)			
	return data	

#def get_data(filters):
	conditions=''
	print(filters)
	if filters.get('item'):
		conditions+="Where pii.item_code='{0}'".format(filters.get('item'))
	if filters.get('name'):
		if not filters.get('item'):
			conditions+="Where pi.name='{0}'".format(filters.get('name'))
		else:
			conditions+=" AND pi.name='{0}'".format(filters.get('name'))
	if filters.get('posting_date'):
		if not filters.get('item'):
			conditions+="Where pi.posting_date='{0}'".format(filters.get('posting_date'))
		elif not filters.get('item'):
			conditions+=" AND pi.posting_date='{0}'".format(filters.get('posting_date'))
		else:
			conditions+=" AND pi.posting_date='{0}'".format(filters.get('posting_date'))			

     #print(conditions)

	query=frappe.db.sql("""select 
									pi.name as 'purchase_invoice',
									pi.posting_date,
									pi.supplier_name,
									pi.total_qty,
									pii.item_code as 'item'

							from 
									`tabPurchase Invoice` pi 
							Left Join `tabPurchase Invoice Item` pii
							ON  pi.name=pii.parent {0}""".format(conditions)
						,as_dict=1)
	
	return query

def get_data(filters):
	conditions=''
	print(filters)

	for i,d in enumerate(filters):
		if i==0:
			conditions+='Where '
			if d =='item':
				conditions+=" pii.item_code='{0}'".format(filters.get(d))
			elif d=='name':
				conditions+=" pi.name='{0}'".format(filters.get(d))
			elif d=='posting_date':
				conditions+=" pi.posting_date='{0}'".format(filters.get(d))
			elif d=='supplier_name':
				conditions+=" pi.supplier_name='{0}'".format(filters.get(d))
			elif d=='from_date':
				conditions+=" pi.from_date='{0}'".format(filters.get(d))
			else:
				conditions+=" pi.to_date='{0}'".format(filters.get(d))

		else:
			if d =='item':
				conditions+=" AND pii.item_code='{0}'".format(filters.get(d))
			elif d=='name':
				conditions+=" AND pi.name='{0}'".format(filters.get(d))
			elif d=='posting_date':
				conditions+=" AND pi.posting_date='{0}'".format(filters.get(d))	
			elif d=='supplier_name':
				conditions+=" AND pi.supplier_name='{0}'".format(filters.get(d))
			elif d=="from_date":
				conditions+=" AND pi.fram_date='{0}'".format(filters.get(d))
			else:
				conditions+=" AND pi.to_date='{0}'".format(filters.get(d))			
            
	query=frappe.db.sql("""select 
									pi.name as 'purchase_invoice',
									pi.posting_date,
									pi.supplier_name,
									pi.total_qty,
									pii.item_code as 'item'

							from 
									`tabPurchase Invoice` pi 
							Left Join `tabPurchase Invoice Item` pii
							ON  pi.name=pii.parent {0}""".format(conditions)
						,as_dict=1)
	
	return query

	




