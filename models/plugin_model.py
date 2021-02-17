from odoo import models, fields, api
from odoo.exceptions import ValidationError


class plugin_model(models.Model):
    _name = 'videoclub_app.empleados_model'
    _inherit = 'videoclub_app.empleados_model'
    _description = 'plugin'


    edad = fields.Integer(string="Edad", required=True)

    @api.constrains("edad")
    def _checkEdad(self):
        if self.edad<18:
            raise ValidationError ("Tiene que ser mayor de 18!")