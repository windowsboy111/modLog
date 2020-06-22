from datetime import datetime
import exceptions
class Logger:
    def __init__(self,**kwargs):
        self.logs = dict()
        self.lvls = []
        self.settings = {"defaultLvl": self.info}
        if kwargs is not None:
            for key,value in kwargs.items():
                self.settings[key] = value or self.settings[key]
        setattr(self,'log',self.settings["defaultLvl"])
    def lvl(self=None,fn=None,*,name=''):
        """usage: 
        @logger.lvl
        def wow(message):
            print("wow " + message)
        you can pass the following arguments: name (str) -- @logger.lvl(name='wow')
        """
        if fn==None:
            raise exceptions.invArgs(f"Expected function. (This is a decorator!)",[self.critical,self.info],f'the argument func=={fn},this is unintended.')
        name = name or fn.__name__
        setattr(self,name,fn)
        self.lvls.append(fn)
    def warn(self,msg:str):
        self.logs[datetime.now().time()] = {'level':'warn','msg':msg}
    def info(self,msg:str):
        self.logs[datetime.now().time()] = {'level':'info','msg':msg}
    def exception(self,msg:str):
        self.logs[datetime.now().time()] = {'level':'exception','msg':msg}
    def critical(self,msg:str):
        self.logs[datetime.now().time()] = {'level':'critical','msg':msg}
    def debug(self,msg:str):
        self.logs[datetime.now().time()] = {'level':'debug','msg':msg}
    def get(self,args=None,kwargs=None):
        return self.logs
    def set_default_lvl(self, name):
        return getattr(self,name,None)