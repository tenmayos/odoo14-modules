from odoo import api, models, fields
# When inserting image import base64 && io


class PatientXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_id_patient_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        for obj in patients:
            report_name = obj.name
            print(patients)
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name)
            # Sets the size of the columns, in a range A:B
            sheet.set_column('A:B', 20)
            # Merges the cells specified cells
            # row1, col1, row2, col2, name, format
            center_format = workbook.add_format({'align': 'center'})
            sheet.merge_range(1, 1, 2, 1, 'yass', center_format)
            # format takes a dictionary with key:value pairs
            formats = workbook.add_format({'bold': True, 'align': 'center'})
            # rows, columns, string, format
            sheet.write(0, 0, obj.name, formats)
            sheet.write(0, 1, obj.age, formats)

