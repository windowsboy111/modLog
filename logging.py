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
    def lvl(self,*func):
        oldlvl = self.lvls
        self.lvls.append(list(func))
        for lvl in self.lvls:
            if len(lvl) > 9:
                raise exceptions.invalidName(f'lvl name \"{lvl}\" has more than 9 characters',['warn','info','critical','exception','debug'], 'level names cannot be longer than 9 characters to prevent code injection')
            continue
            exec(f'self.{lvl} = lvl',globals=globals(),locals=locals())
        return oldlvl
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
    def log(self,args,kwargs):
        return self.settings['defaultLvl'](args,kwargs)
    def get(self,args,kwargs):
        return self.logs