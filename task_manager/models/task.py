from odoo import models, fields, api


class Task(models.Model):
    _name = 'task'
    _description = 'Task'

    name = fields.Char(string="Title", required=True, help="Title of the task")
    deadline = fields.Date(string="Deadline", required=True, help="Deadline of the task")
    status = fields.Selection([
        ('new', 'New'), ('completed', 'Completed')], string="Task Status", default="new")
    description = fields.Text(string="Description", help="Description of the task")
    remaining_days = fields.Integer(compute='_compute_remaining_days', string='Days Until Deadline',
                                    store=True)

    @api.depends('deadline')
    def _compute_remaining_days(self):
        for task in self:
            if task.deadline:
                deadline = fields.Datetime.from_string(task.deadline)
                today = fields.Datetime.from_string(fields.Datetime.now())
                delta = (deadline - today).days
                task.remaining_days = delta if delta > 0 else 0
            else:
                task.remaining_days = 0
