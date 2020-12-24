#!/usr/bin/env python3

from .json_proc import JsonProcessor

# Class: ActionProcessor
# Description: Class Library to implement the 'action' functionality to compute activity average
# Public Methods: addAction, getStats

class ActionProcessor():
    def __init__(self):
        self.key_dict = {}
        self.err_msg = None
        
    def __del__(self):
        self.key_dict.clear()

    # Method: getErrorMsg
    # Input: None
    # Output: Returns the exception message when addAction returns -1
    def getErrorMsg(self):
        return(self.err_msg)

    # Method: processAction
    # Input: JsonProcessor object
    # Output: returns token
    # Description: It returns the value token following the 'action' keyword. Raises exception if the value is not a string type or invalid syntax
    def processAction(self, p):
        
        # check and skip over the ':'
        v = p.getNextToken()
        if v == ':':
            if p.isValue(str):
                return(p.getNextToken())
            else:
                raise Exception('syntax error: action value should be non-empty string')
        else:
            raise Exception('syntax error: missing ":"')
    
    # Method: processTime
    # Input: JsonProcessor object
    # Output: returns token
    # Description: It returns the value token following the 'time' keyword. Raises exception if the value is not of int or float type or invalid syntax
    def processTime(self, p):
        
        # check and skip over ':'
        v = p.getNextToken()
        if v == ':':
            if p.isValue(int) or p.isValue(float):
                return(p.getNextToken())
            else:
                raise Exception('syntax error: time value should be number')
        else:
            raise Exception('syntax error: missing ":"')

    # Method: add2Collection
    # Input: key, value
    # Output: none
    # Description: This function takes the value pair of 'action' and 'time' keywords and updates the dictionary. Final average computation is
    # done when getStats is called. Special handling is done when time value is 0/0.0. Count value is not increased for 0/0.0.
    def add2Collection(self, k, v):
        # should not happen but worth checking before updating dictionary
        if k == None or v == None:
            raise Exception('syntax error: key or value missing')
        
        if self.key_dict.get(k) == None:
            self.key_dict[k] = (v, 1)
        else:
            (v1, n) = self.key_dict[k]
            if int(v1) > 0 and int(v) > 0:
                n += 1
            self.key_dict[k] = (v1 + v, n) 
    
    # Method: addAction
    # Input: json string
    # Output: 0 on success, -1 on error.
    # Description: This function processes the json formatted string to process 'action' and 'time' keywords. It leverages JsonProcessor to
    # do lexical analysis and build a token list. It does a syntax check and add/update the collection dictionary.
    def addAction(self, str):
        
        # syntax definition
        tokens = ['{', 'action', ',', 'time', '}']
        
        self.err_msg = None
        res = 0
        
        # setup json processor object
        p = JsonProcessor(str)
        
        # let the processor do lexical analysis and build a token list.
        try:
            p.buildTokenList()
        except Exception as e:
            self.err_msg = e
            return(-1)
        
        # So far so good. We now have a supposedly good token list. Lets match it against the
        # syntax defined above. If exception, return -1 and store exception message so it can be queried
        # as needed.
        k, v = None, None
        for t in tokens:
            token = p.getNextToken()
            if token == t:
                try:
                    if t == 'action':
                        # get value of 'action'
                        k = self.processAction(p)
                    if t == 'time':
                        # get value of 'time'
                        v = self.processTime(p)
                        
                        # All good. Add values to dictionary collection
                        self.add2Collection(k, v)
                        #print(self.key_dict)
                except Exception as e:
                    self.err_msg = e
                    res = -1
                    break
            else:
                if token == None:
                    token = ' '
                self.err_msg = 'syntax error: expecting "' + t + '" received "' + token + '"'
                res = -1
                break
            
        return(res)
                    
    # Method: getStats
    # Input: None
    # Output: json formatted array string.
    # Description: This function computes average of dictionary items and builds a json formatted array string.
    def getStats(self):
        
        # Check if there is anything to return
        if not len(self.key_dict):
            return('')
        
        res = ''
        for k,v in self.key_dict.items():
            # Check and do integer/float division to get the correct output format.
            # For ex, 10/2 should be displayed as 5 and not 5.0
            if v[0] % v[1]:
                v1 = v[0] / v[1]
            else:
                v1 = v[0] // v[1]
            
            # Round off to 2 decimal places for float values
            if isinstance(v1, float):
                v1 = round(v1, 2)
            
            # Build the output string
            if len(res):
                res += ',\n'
            res += '\t{"action":"' + k + '", "avg":' + str(v1) + '}'
        
        # complete by converting the string to a json array
        res = '[\n' + res + '\n]\n'
        
        # print(res)
        return(res)
    
# Useful when this file is run as standalone. Does a sample run    
if __name__ == '__main__':
    s = ActionProcessor()
    
    res = s.addAction('{" action ":"run", "time":10}')
    if res:
        print(s.getErrorMsg())
    res = s.addAction('{" action":"jump", "time":100}')
    if res:
        print(s.getErrorMsg())
    res = s.addAction('{"action ":"run", "time":}')
    if res:
        print(s.getErrorMsg())
              
    print(s.getStats())
    
    del s
    
    