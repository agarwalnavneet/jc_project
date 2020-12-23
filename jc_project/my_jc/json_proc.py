
# Class: JsonProcessor
# Description: Class Library to parse json formatted string and build a token list. Can be extended for full parsing
# Public Methods: buildTokenList

class JsonProcessor():
    JSON_QUOTE = '"'
    JSON_WS = [' ', '\t']
    JSON_TOKEN = ['{', '}', ',', ':']
    MAX_STRING_LEN = 20
    MAX_NUMBER_LEN = 10
    
    def __init__(self, s):
        self.str = s
        self.token_list = []
    
    # Returns the next token
    def getNextToken(self):
        if len(self.token_list):
                v = self.token_list.pop(0)
                return(v)
        else:
            return(None)

    # Check if the token value is of specific type before popping off the list.
    # t: str or int or float
    def isValue(self, t):
        if len(self.token_list):
            if self.token_list[0] in self.JSON_TOKEN:
                return(False)
            return(isinstance(self.token_list[0], t))
        else:
            return(False)

    # Method: buildTokenList
    # Input: None
    # Output: None
    #
    # Builds a list of JSON tokens and stores them in the token list. This function can be extended to include
    # other types. Current support is for string, integer and float
    def buildTokenList(self):
        
        # sub-function name: getSring
        # input: token string (str)
        # return: string token, offset value
        #
        # This sub-function checks for a string (identified by double quotes). If found, returns the string and
        # an offset value after the string token. If not found, returns None and an offset value of 0. The calling
        # function can use the offset value to continue processing other tokens
        def getString(str):
            res = ''

            if str[0] == '"':
                str = str[1:]
            else:
                return (None, 0)

            # Peel off the string and clean it by removing leading and trailing whitespaces
            for c in str:
                if c == '"':
                    return(res.strip(), len(res) + 2)
                else:
                    res += c
                    if len(res) > self.MAX_STRING_LEN:
                        raise Exception(f'token error: string length limit ({self.MAX_STRING_LEN}) exceeded')

            raise Exception('token error: missing terminating string quote')
        
        # sub-function name: getNumber
        # input: token string (str)
        # return: integer or float, offset value
        #
        # This sub-function checks for an integer/float number. If found, returns the value and an offset value after the token.
        # If not found, returns None and an offset value of 0. The calling function can use the offset value
        # to continue processing other tokens
        def getNumber(str):
            res = ''
            num_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

            for c in str:
                if c in num_set:
                    res += c
                    if len(res) > self.MAX_NUMBER_LEN:
                        raise Exception(f'token error: number length limit ({self.MAX_NUMBER_LEN}) exceeded')
                else:
                    break

            # If all good then convert to int or float.
            if len(res):
                if '.' in res:
                    return(float(res), len(res))
                else:
                    return(int(res), len(res))

            # Nothing found. Let others handle it
            return(None, 0)
        
        # Other sub-functions can go here for other types (Bool, arrays etc) for extending the functionality
        
        # buildTokenList function starts from here...
        while len(self.str):
            
            # check for a string token. If found, store, skip and move on
            res, ofs = getString(self.str)
            if ofs:
                self.str = self.str[ofs:]
                if len(res):
                    self.token_list.append(res)
                continue

            # String not found. Look for numbers. Store value if found. Skip further processing.
            res, ofs = getNumber(self.str)
            if res != None:
                self.token_list.append(res)
                self.str = self.str[ofs:]
                continue
            
            # Neither string or number. Ignore and jump over white spaces if any.
            if self.str[0] in self.JSON_WS:
                self.str = self.str[1:]
            elif self.str[0] in self.JSON_TOKEN:
                # No whitespaces. For string to be valid, the next char has to be token
                self.token_list.append(self.str[0])
                self.str = self.str[1:]
            else:
                # Nothing valid matches. Flag exception
                raise Exception(f'token error: invalid "{self.str[0]}"')
            
        #print(self.token_list)
        
