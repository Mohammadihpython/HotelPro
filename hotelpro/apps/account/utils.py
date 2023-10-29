import os
from sms_ir import SmsIr



class SmsTools:
    def __init__(self,api_key,line_number) -> None:
        self.api_key = api_key
        self.line_number = line_number
        self.sms_ir = SmsIr(api_key,line_number)

    def send(self,number,message):
        self.sms_ir.send_sms(number,message)





sms = SmsTools(api_key=os.environ.get("api_key"),line_number=os.environ.get("line_number"))