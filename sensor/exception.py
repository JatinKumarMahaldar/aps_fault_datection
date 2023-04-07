import sys
import os

def error_message_detail(error ,error_detail: sys):
    _,_, error_tb = error_detail.exc.info
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occures python script name[{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno, str(error)
    )
    return error_message

class SensorException(Exception):
    def __init__(self,error_message,error_detail):
        self.error_message= error_message_detail(error=error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



        
