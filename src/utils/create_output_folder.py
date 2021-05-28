import os
import os.path
import shutil
from data import RESULT_FOLDER, spreadsheet_name  # noqa
from functools import wraps


def create_output_folder(func):
    """There is a decorator, it is used to create the final folder
     and place the file in it.
    :param func: function on which the add-in will be performed
    :return: wrapper
    """
    @wraps(func)
    def wrapper(data):
        """Performs folder creation, file move and file deletion.
        :param data: goods from the online store
        """
        if os.path.isdir(RESULT_FOLDER):
            func(data)
        else:
            os.mkdir(RESULT_FOLDER)
            func(data)

        if os.path.exists(spreadsheet_name):
            operation_result = shutil.copy(spreadsheet_name, RESULT_FOLDER)
            os.remove(spreadsheet_name)
            print(f'All is ready! The result is located here "{operation_result}"')
    return wrapper
