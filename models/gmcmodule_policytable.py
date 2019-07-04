from odoo import models, fields



class GMCModulePolicyTable(models.Model):
	_name = 'gmcmodule.policytable'
	name = fields.Char('Title', required=True)	
	age = fields.Float('A', required=False)
	weight = fields.Char('B', required=True)
