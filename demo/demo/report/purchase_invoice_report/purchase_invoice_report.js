// Copyright (c) 2016, fairsh and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase_invoice_report"] = {
	"filters": [
			
			{
				'label':'Item Code',
				'fieldname':'item',
				'fieldtype':'Link',
				'options':'Item'
			},
			{
				'label':'Purchase Invoice',
				'fieldname':'name',
				'fieldtype':'Link',
				'options':'Purchase Invoice'
			},
			{
				'label':'Posting Date',
				'fieldname':'posting_date',
				'fieldtype':'Date',
				//'options':'Purchase Invoice'
			},
			{
				'label':'Supplier Name',
				'fieldname':'supplier_name',
				'fieldtype':'Data',
				//'options':'Purchase Invoice'
			},
			{
				'label':'From Date',
				'fieldname':'from_date',
				'fieldtype':'Date',
				//'options':'Purchase Invoice'
			},
			{
				'label':'To Date',
				'fieldname':'to_date',
				'fieldtype':'Date',
				//'options':'Purchase Invoice'
			},
			
	]
};
