class dic:
    def __init__(self,c):
        self.c = c
    
    def keys(self):
        if type(self.c) == dict:
            return self.c.keys()
        
    def values(self):
        if type(self.c) == dict:
            return self.c.values()
        
    def err(self):
        if type(self.c) != dict:
            raise Exception(self.c,'It is not a dictionary')
        else:
            return 'It is a dictionary'
            
    def key_value(self):
        self.c = eval(input())
        print(self.c.keys())
        print(self.c.values())        
        
    def insertion(self,kv):
        self.c[k] = v