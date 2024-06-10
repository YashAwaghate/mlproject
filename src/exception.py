import sys
import logging

def error_msg_detail(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error Occured in script : [{0}] , Line: :[{1}] Error Message [{2}]".format(
    filename, exc_tb.tb_lineno,str(error))

    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_message = error_msg_detail(error_msg, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
    