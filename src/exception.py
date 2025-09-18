import sys
import logging
from src.logger import logging
def error_message_detail(error, error_detail: sys): # type: ignore
    """
    Formats a detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # type: ignore
    line_number = exc_tb.tb_lineno # type: ignore
    error_message = f"Error occurred in script [{file_name}] at line [{line_number}] with message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    A custom exception class that provides detailed error information.
    """
    def __init__(self, error_message, error_detail: sys): # type: ignore
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
