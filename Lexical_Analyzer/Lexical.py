import sys
import re
import os

FLOAT = 36
IDENT = 1
INTEGER = 90
Left_parenthesis = 41
Right_parenthesis = 42
Plus_sign = 11
minus_sign = 12
Equal_sign = 17
Division_symbol = 14
Multiplication_symbol = 13
Left_bracket = 43
Right_bracket = 44
Semicolon = 77
FLOATING_POINT = 91

# This is a dictionary or hashmap containing our special symnols, and I map them to a string name and numerical token code
special_sym = {
    '+': ['Plus_sign', 11],
    '-': ['Minus_sign', 12],
    '(': ['Left_parenthesis', 41],
    ')': ['Right_parenthesis', 42],
    '{': ['Left_bracket', 43],
    '}': ['Right_bracket', 44],
    '*': ['Multiplication_symbol', 13],
    '/': ['Division_symbol', 14],
    '$': ['Dollar_sign', 19],
    '%': ['Percent_symbol', 15],
    '=': ['Equal_sign', 17],
    '<': ['Less_than', 21],
    '>': ['Greater_than', 22],
    '<=': ['Less_Than_Equal', 23],
    '>=': ['Greater_Than_Equal', 24],
    ';': ['semicolon', 77],
    ':' :['colon', 78]
    }
# This is a dictionary or hashmap containing our key words, and I map them to a string name and numerical token code
keyWords = {
        'foreach' : ['foreach-loop', 30],
        'for': ['for-loop', 31],
        'if': ['if-statement', 32],
        'while': ['while-loop', 33],
        'do': ['do-while', 34],
        #'int': ['int', 35],
        #'float': ['floating-point', 36],
        'switch': ['switch-statement', 37],
        'return': ['return-statement', 39],
        'else' : ['else-statement', 45],
        'case':['switch-case', 38],
        'default': ['default-case', 51],
        'in' : ['in', 52],
        'VOID' : ['VOID', 53],
        'MAIN' : ['MAIN', 54],
        'type' : ['type', 56],
        'public' : ['public-class', 62],
        'private' : ['private-class', 63],
        'class' : ['class', 64],
        'method' : ['method', 4],
        'void' : ['void', 5]
    }
#This is a dictionary for our variable types
types = {
    'int': ['int', 35],
    'float': ['floating-point', 36],
    'string' : ['string', 99],
    'void' :['void', 66],
    'boolean' : ['boolean', 66]
}
def lex():
    global i, nextToken, arr
    i = i + 1
    
    if(i < len(arr) and i < len(array)):
        nextToken = arr[i]
        nextLexem = array[i]
        print("Next token is: " + str(nextToken) + " next item is: " +nextLexem)

def convertor(array):
    newArray = []
    
    for i in range (0, len(array)):
        if(array[i]=='IDENT' ):
            newArray.append(1)
        elif(array[i]=='INTEGER'):
            newArray.append(90)
        elif(array[i]=='STRING'):
            newArray.append(91)
        elif(array[i]=='method'):
            newArray.append(4)
        elif(array[i]=='string'):
            newArray.append(99)
        elif(array[i]=='floating-point'):
            newArray.append(36)
        elif(array[i]=='int'):
            newArray.append(35)
        elif(array[i]=='FLOATING-POINT'):
            newArray.append(91)
        elif(array[i]=='Left_parenthesis'):
            newArray.append(41)
        elif(array[i]=='Right_parenthesis'):
            newArray.append(42)
        elif(array[i]=='Plus_sign'):
            newArray.append(11)
        elif(array[i]=='Minus_sign'):
            newArray.append(12)
        elif(array[i]=='Division_symbol'):
            newArray.append(14)
        elif(array[i]=='Multiplication_symbol'):
            newArray.append(13)
        elif(array[i]=='Equal_sign'):
            newArray.append(17)
        elif(array[i]=='percent_symbol'):
            newArray.append(15)
        elif(array[i]=='Left_bracket'):
            newArray.append(43)
        elif(array[i]=='Right_bracket'):
            newArray.append(44)
        elif(array[i]=='switch-statement'):
            newArray.append(37)
        elif(array[i]=='if-statement'):
            newArray.append(32)
        elif(array[i]=='while-loop'):
            newArray.append(33)
        elif(array[i]=='do-while'):
            newArray.append(34)
        elif(array[i]=='for-loop'):
            newArray.append(31)
        elif(array[i]=='foreach-loop'):
            newArray.append(30)
        elif(array[i]=='semicolon'):
            newArray.append(77)
        elif(array[i]=='colon'):
            newArray.append(78)
        elif(array[i]=='else-statement'):
            newArray.append(45)
        elif(array[i]=='switch-case'):
            newArray.append(38)
        elif(array[i]=='default-case'):
            newArray.append(51)
        elif(array[i]=='VOID'):
            newArray.append(53)
        elif(array[i]=='MAIN'):
            newArray.append(54)
        elif(array[i]=='return-statement'):
            newArray.append(39)
        elif(array[i]=='int'):
            newArray.append(35)
        elif(array[i]=='Less_than'):
            newArray.append(21)
        elif(array[i]=='Greater_than'):
            newArray.append(22)
        elif(array[i]=='Less_Than_Equal'):
            newArray.append(23)
        elif(array[i]=='Greater_Than_Equal'):
            newArray.append(24)
        elif(array[i]=='method'):
            newArray.append(4)
        elif(array[i]=='public-class'):
            newArray.append(62)
        elif(array[i]=='private-class'):
            newArray.append(63)
        elif(array[i]=='class'):
            newArray.append(64)
        elif(array[i]=='void'):
            newArray.append(5)
        else:
            print('error')
            
        return newArray[0]
    
    return newArray
'''This was taken from our lexical analyzer, This will classify the tokens, 
and give an array of the order of tokens'''
def tokenize(fileInput):
    global lexArray, actArray

    value = None

    identifier = re.fullmatch(r"[a-zA-Z][a-zA-Z]*", fileInput)
    stringLit = re.fullmatch(r"(\"|\')([a-zA-Z][a-zA-Z]*)(\"|\')",fileInput)
    classDer = re.fullmatch(r"[a-zA-Z][a-zA-Z]*[.][a-zA-Z][a-zA-Z]*", fileInput)
    special = re.fullmatch(r"[^a-zA-Z0-9]*", fileInput)
    integer = re.fullmatch('([1-9][0-9]*)|0', fileInput)
    floats = re.fullmatch('([+|-])?(\d+([.]\d*)?([e]([+|-])?\d+)?|[.]\d+([eE]([+|-])?\d+)?)', fileInput)
    octal = re.fullmatch('0[0-7]+', fileInput)
    

    if(identifier):
        if fileInput in keyWords:
            value = keyWords.get(fileInput)[0]
        elif(fileInput in types):
            value = types.get(fileInput)[0]
        else:
            value = 'IDENT'
    elif(classDer):
        value = 'IDENT'
    elif stringLit:
        value = 'STRING'
    elif special:
        if fileInput in special_sym:
            value = special_sym.get(fileInput)[0]
        else:
            #print error
            return "LEXICAL ERROR"
    elif integer:
        value = 'INTEGER'
    elif floats:
        value = 'FLOATING-POINT'
    elif octal:
        value = 'OCTAL'
    
    if value == None:
        
        return "ERROR"
    else:
        lexArray.append(value)
        print('Next token: ' + str(convertor([value])) + ', Next Lexeme: ' + fileInput)

#This is where we shut the program down if we run into an error
def exiter():
    sys.exit()


#Where we go if we run into a lexical error
def lexical_error():
    print("Lexical error!!!")
    exiter()

#where the lex analyzer begins
def mainLexAnalzer():
    global lexArray
    lexArray = []
    print("\nUnedited program file")
    print()
    #Here is where we open the program file
    word = open(os.path.join(sys.path[0], "test.txt"), "r")

    print(word.read())
    word.close()
    print("\nJave File tokenized:")
    print()
    #Here is also where we open and process the program file
    with open(os.path.join(sys.path[0], "test.txt"), "r") as fileInput:
        words = re.split(' |\n|\t',fileInput.read())
        for i in range (0, len(words)):
            if words[i]:
                    checker = tokenize(words[i]) 
                    if checker=='ERROR':
                        lexical_error()
                        break
                    else:
                        continue  
            else:
                continue     
    pass
    return lexArray

if __name__ =='__main__': 
    
    array = mainLexAnalzer()
    print()
    print("Ran successfully")
    
 