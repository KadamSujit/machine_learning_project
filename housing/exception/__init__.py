import os
import sys

#creating our own custom exception class
class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):      #sys module has all the info of err. (info about err in which file which line), #error_message: Exception, here error_message is an object for Exception class, like Exception e
        super().__init__(error_message)     #passing error_message info to Exception class
        
        self.error_message = HousingException.get_detailed_error_method(error_message=error_message,error_detail=error_detail)
    

    #creating a static method to get detailed error message #static method can be called without creating object
    @staticmethod
    def get_detailed_error_method(error_message:Exception, error_detail:sys)->str:  #return type of this function is str. It is done by using->str
        """
        error_message: Exception object
        error_details: object of sys module
        """
        
        _, _ , exec_tb = error_detail.exc_info()        #exc_info() returns 3 values (type, value, traceback). As we only need 3rd value, first two variables are just _, _ and third is exec_tb for traceback(traceback has location of err)

        #capturing error in file and at line number
        file_name = exec_tb.tb_frame.f_code.co_filename     #gives file name having error
        line_number = exec_tb.tb_frame.f_lineno             #gives line number havine error

        error_message = f"Error occured in script:[{file_name}] at line number:[{line_number}] error message: [{error_message}]"

        return error_message

    def __str__(self):
        return self.error_message
        #It is a Dunder method -->google it.
        #whenever we try to print the object of any class, the information that is displayed py print function can be defined by this __str__() method.
        #for e.g, if here I print HousingException class object, then it will give us whatever info it has in error_message.

    def __repr__(self) ->str:
        return HousingException.__name__.str()
        #It is a Dunder method
        #__repr__ is object representation, it defines what info object should give without print statement.
    
