import pdb
import time
from odoo import api, fields, models, _, tools
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import logging
import pdb

_logger = logging.getLogger(__name__)


class TaskWiz(models.TransientModel):
    _name = 'task.wiz'
    _description = 'Task Report Wizard'

    def print_report(self):
        self.ensure_one()
        [data] = self.read()
        datas = {
            'form': data
        }
        return self.env.ref('task_manager.action_report_task').with_context(
            landscape=False).report_action(self, data=datas, config=False)
