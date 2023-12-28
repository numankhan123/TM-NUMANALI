from odoo import api, fields, models
from datetime import date, datetime
import pdb


class TaskReport(models.AbstractModel):
    _name = 'report.task_manager.report_task'
    _description = 'Task Report'

    @api.model
    def _get_report_values(self, docsid, data=None, paper=None):

        tasks = self.env['task'].sudo().search([])

        report = self.env['ir.actions.report']._get_report_from_name('task_manager.report_task')

        docargs = {
            'doc_ids': [],
            'doc_model': report.model,
            # 'data': data['form'],
            'tasks': tasks or False

        }
        return docargs
