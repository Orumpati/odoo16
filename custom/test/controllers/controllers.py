""" from odoo import http
import odoo


class OdooAcademy(odoo.http.controllers):

    @http.route('/sai',auth='public')
    def index(self):
        return "hello world"


         """