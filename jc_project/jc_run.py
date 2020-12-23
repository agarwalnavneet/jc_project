from my_jc import ActionProcessor

if __name__=='__main__':
    s = ActionProcessor()
    
    res = s.addAction('{" action":"run", "time":10}')
    if res:
        print(s.getErrorMsg())
    res = s.addAction('{" action":"jump", "time":100}')
    if res:
        print(s.getErrorMsg())
    res = s.addAction('{"action ":"run", "time":20}')
    if res:
        print(s.getErrorMsg())
              
    print(s.getStats())
    
    del s
