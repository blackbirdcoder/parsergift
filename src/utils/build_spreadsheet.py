from data import headings, heading_style, column_width, spreadsheet_name # noqa
import xlsxwriter
from .create_output_folder import create_output_folder


@create_output_folder  # Wrapper for creating a folder where the result will be output
def build_spreadsheet(data: list):
    """Build an Excel spreadsheet with data from an online store.
    :param data: Object with goods, they will be written to the spreadsheet.
    """
    workbook = xlsxwriter.Workbook(spreadsheet_name)
    worksheet = workbook.add_worksheet()
    style = workbook.add_format(heading_style)
    row = 2

    def create_head():
        """Creates a spreadsheet header"""
        for current_item in headings:
            worksheet.write(current_item[0], current_item[1], style)
        for current_item in column_width:
            worksheet.set_column(current_item[0], current_item[1])

    create_head()

    def create_body():
        """Creates the body of the spreadsheet by filling with data"""
        nonlocal row
        for current_value in data:
            worksheet.write(f'A{row}', current_value.get('category'))
            worksheet.write(f'B{row}', current_value.get('vendor_code'))
            worksheet.write(f'C{row}', current_value.get('desc'))
            worksheet.write_url(f'D{row}', current_value.get('link_image'), string='Ссылка на изображение')
            worksheet.write(f'E{row}', current_value.get('price'))
            worksheet.write(f'F{row}', current_value.get('currency'))
            row += 1

    create_body()
    workbook.close()

