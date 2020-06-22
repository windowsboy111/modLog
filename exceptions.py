class invArgs(Exception):
    """The argument passed is invalid"""
    def __init__(self,message,possible=None,reason=""):
        super.__init__(super(str,message))
        self.message = message
        self.possible = possible
        self.reason = reason
    def get_message(self):
        return self.message
    def get_reason(self):
        return self.reason
    def get_possible(self):
        return self.possible
    def __str__(self):
        return self.message
    def __repr__(self):
        return {'error':'invArgs','message':self.message,'possible':self.possible,'reason':self.reason}