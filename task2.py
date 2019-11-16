""" ###################################################################################################"""  

""" ###################################################################################################"""  
def bind_method(value, instance):
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value

def make_instance(cls):
        attributes = {}
        def get_value(name):
            if name in attributes:
                return attributes[name]
            else:
                value = cls['get'](name)
            return bind_method(value, instance)
        def set_value(name, value):
            attributes[name] = value
        instance = {'get': get_value, 'set': set_value}
        return instance

def init_instance(cls, *args):
        instance = make_instance(cls)
        init = cls['get']('__init__')
        if init:
            init(instance, *args)
        return instance

def make_class(attributes, base_class=None):
        def get_value(name):
            if name in attributes:
                return attributes[name]
            elif base_class is not None:
                return base_class['get'](name)
        def set_value(name, value):
            attributes[name] = value
        def new(*args):
            return init_instance(cls, *args)
        cls = {'get': get_value, 'set': set_value, 'new': new}
        return cls
""" ###################################################################################################"""   

""" ###################################################################################################"""  
def make_Data_class():
    def __init__(self,year,month,day):
        self['set']('year',year)
        self['set']('month',month)
        self['set']('day',day)
              
    def get_year(self):
        return self['get']('year')
    
    def get_month(self):
        return self['get']('month')   
    
    def get_day(self):
        return self['get']('day')         
                 
    return make_class({'__init__': __init__,'get_year':get_year,'get_month':get_month,'get_day':get_day}) 

def make_time_class():
    def __init__(self,hour,minute):
        self['set']('hour',hour)
        self['set']('minute',minute)
              
    def __str__(self):
        H = self['get']('hour')
        M = self['get']('minute')
        tmp='0'
        if M<10:
            tmp=tmp+str(M)
            return "{}:{}".format(H, tmp)
        else: return  "{}:{}".format(H, M)     
    return make_class({'__init__': __init__,'__str__':__str__}) 

def make_calentry_class():
    def __init__(self,year,month,day):
        tasks=[]
        self['set']('Tdate',Data['new'](year,month,day))
        self['set']('tasks',tasks)
              
    def addTask(self,task,start,end):
        self['get']('tasks').append('({},{}): {}'.format(start['get']('__str__')(),end['get']('__str__')(),task))
         
    def tasks(self):
        return self['get']('tasks')
             
    return make_class({'__init__': __init__,'addTask':addTask,'tasks':tasks})
""" ###################################################################################################"""  
# Data = make_Data_class()
# today = Data['new'](2017,1,20)
# print(today['get']('year'))
# calendarEntry = make_calentry_class()
# todo = calendarEntry['new'](2017,1,20)
# Time = make_time_class()
# t = Time['new'](16,9)
# print(t['get']('__str__')())
# todo['get']('addTask')("PPL lecture",t,Time['new'](13,0))
# todo['get']('addTask')("PPL HomeWork #4",Time['new'](14,0),Time['new'](16,0))
# print(todo['get']('tasks'))
