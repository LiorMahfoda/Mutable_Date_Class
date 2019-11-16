""" ###################################################################################################"""  

""" ###################################################################################################"""  
class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.day=day
        self.month=month
    def __repr__(self):
        return 'Date({},{},{})'.format(self.year,self.month,self.day)
    def __str__(self):
        monthN = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return "{}th of {} {}".format(self.day,monthN[self.month],self.year)
    
class ClaendarEntry(object):
    def __init__(self,year,month,day):
        self.Tdate=Date(year,month,day)
        self.tasks=[]
        
    def addTask(self,task,start,end):
        self.tasks.append('[{},{}]: {}'.format(start,end,task))
         
    def tasks(self):
        return self.tasks
            
    def __repr__(self):
        return ''.format(self.tasks)
    
    def __str__(self):
        def printt():
            print ('Todo list for {}:'.format(self.Tdate))
            for i in range(len(self.tasks)):
                print ('{}.   {}'.format(i+1,self.tasks[i]))
        
        return  str(printt())
        
class Time(object):
    def __init__(self,hour,minute):
        self.hour=hour
        self.minute=minute
        
    def __repr__(self):
        tmp='0'
        if self.minute<10:
            tmp=tmp+str(self.minute)
            return "{}:{}".format(self.hour, tmp)
        else: return  "{}:{}".format(self.hour, self.minute)
            
""" ###################################################################################################"""     
# today =Date(2017,1,20)
# print(today)
# todo= ClaendarEntry(2017,1,20)
# t=Time(10,0)
# str(t)
# todo.addTask("PPL lecture", t, Time(13,0))
# todo.addTask("PPL homework#4", Time(14,0), Time(16,0))
# print(todo.tasks)
# print(todo)
