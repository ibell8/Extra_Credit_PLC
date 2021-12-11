import sys
import re
import os




IDENT = 1
INTEGER = 90
STRING = 91
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

types = {
    'int': ['int', 35],
    'float': ['floating-point', 36],
    'string' : ['string', 99],
    'void' :['void', 66],
    'boolean' : ['boolean', 66]
}
#This is our table where we will track the types and values for our variables
st = {}
#This is where we will go for our method declaration
def method():
    print("<Enter method>")
    if(nextToken != keyWords.get('method')[1]):
        error()
    else:
        lex()
        if(nextAct not in types):
            error()
        else:
            lex()
            if(nextToken !=IDENT):
                error()
            else:
                lex()
                if(nextToken != Left_parenthesis):
                    error()
                else:
                    lex()
                    if(nextToken != Right_parenthesis):
                        error()
                        lex()
                        block()
                


#This is where we will go to define a class
def Class():
    print("<Enter class>")
    if(nextToken != keyWords.get('public')[1] and nextToken != keyWords.get('private')[1]):
        error()
    else:
        lex()
        if nextToken != keyWords.get('class')[1]:
            error()
        else:
            lex()
            if(nextAct not in types):
                error()
            else:
                lex()
                if(nextToken != IDENT):
                    error()
                else:
                    lex()
                    block()
                    print('exit class')

#This is our recursive subprogram which is based on the following eBNF:: <selection_statement>  if ‘(‘ <boolexpr> ‘)’ <statement> [ else <statement> ]
def ifStatement():
    print("<Enter if statement>")
    if(nextToken != keyWords.get('if')[1]):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            boolExpr()
            if(nextToken != Right_parenthesis):
                error()
            else:
                lex()
                block()
                if(nextToken == keyWords.get('else')[1]):
                    lex()
                    block()
                    print("<Exit if statement>")

#This is our recursive subprogram which is based on the following eBNF: <while_loop>  while ‘(‘ [<expression>] ‘)’ <statement>
def while_loop():
    print("<Enter while loop>")
    if(nextToken != keyWords.get('while')[1]):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            expr()
            if(nextToken != Right_parenthesis):
                error()
            else:
                lex()
                block()
                print("<Exit while loop>")

def do_while_loop():
    print("<Enter do_while loop>")
    if(nextToken != keyWords.get('do')[1]):
        error()
    else:
        lex()
        block()
        lex()
        if(nextToken != keyWords.get('while')[1]):
            error()
        else:
            lex()
            if(nextToken != Left_parenthesis):
                error()
            else:
                lex()
                expr()
                if(nextToken!= Right_parenthesis):
                    error()
                    print("<Exit do_while loop>")

#This is the recursive decent subprogram which is based on the eBNF: <block> -> '{' { <statement> } '}'
def block():
    print("<Enter block>")
    if (nextToken != Left_bracket):
        error()
    else:
        lex()
        while(nextToken != Right_bracket):
            #lex()
            statement()
            '''if(nextToken != special_sym.get(';')[1]):
                error()
            else:'''
            lex()
            print("<Exit block>")
#block statement for our switch statement            
def caseblocks():
    while(nextToken != keyWords.get('case')[1] and nextToken != keyWords.get('default')[1]):
        #lex()
        statement()
        if(nextToken != Semicolon):
            error()
        else:
            lex()
#This is our recursive subprogram which is based on the following eBNF: <for_loop> --> for ‘(‘ [<expression>] ’;’ [<expression>] ‘;’ [<expression>] ‘)’ <statement> 
def for_loop():
    print("Enter for>")
    if(nextToken != keyWords.get('for')[1]):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            expr()
            if(nextToken != Semicolon):
                error()
            else:
                lex()
                statement()
                if(nextToken != Semicolon):
                    error()
                else:
                    lex()
                    expr()
                    if(nextToken != Right_parenthesis):
                        error()
                    else:
                        lex()  
                        block()
                        print("<Exit for>")

#Python for each
def foreach_loop():
    print("<Enter Foreach>")
    if(nextToken != keyWords.get('foreach')[1]):
        error()
    else:
        lex()
        if(nextToken!=Left_parenthesis):
            error()
        else:
            lex()
            if(nextToken != IDENT and nextToken != keyWords.get('int')[1]):
                error()
            else:
                lex()
                if(nextToken != IDENT):
                    error()
                else:
                    lex()
                    if(nextToken!= special_sym.get(':')[1]):
                        error()
                    else:
                        lex()
                        if(nextToken!=IDENT):
                            error()
                        else:
                            lex()
                            if(nextToken != Right_parenthesis):
                                error()
                            else:
                                lex()
                                block()
                                print("<Exit foreach>")

#We can either just have "return ;", by itself or we can have "return identifier ;"
def returnStatement():
    print("<Enter return>")
    if(nextToken != keyWords.get('return')[1]):
        error()
    else:
        lex()
        if(nextToken == special_sym.get(';')[1]):
            lex()
            return
        if(nextToken != IDENT and nextToken != INTEGER and nextToken != FLOATING_POINT):
            error()
        else:
            expr()
        if(nextToken != special_sym.get(';')[1]):
            error()
        else:
            lex()
            print("<Exit return>")
#This is where are program should really start and end
def program():
    print("<Enter program>")
    if(nextToken != keyWords.get('VOID')[1]):
        error()
    else:
        print("Next token is: " + str(53) + " next lexeme is: VOID" )
        lex()
        if(nextToken != keyWords.get('MAIN')[1]):
            error()
        else:
            lex()
            if(nextToken != Left_parenthesis):
                error()
            else:
                lex()
                if(nextToken != Right_parenthesis):
                    error()
                else:
                    lex()
                    block()
                    print("<Exit program>")
            
#Because of the special syntax for the switch statement, I gave special instructions to make sure syntax is correct
def cases():
    lex()
    if(nextToken != IDENT and nextToken != INTEGER):
        error()
    else:
        lex()
        if(nextToken != special_sym.get(':')[1]): 
            error()
        else:
            lex()
            caseblocks()
#This will check the syntax of our switch statement 
def switchStatement():
    if(nextToken != keyWords.get('switch')[1]):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            expr()
            if(nextToken != Right_parenthesis):
                error()
            else:
                lex()
                if(nextToken!=Left_bracket):
                    error()
                else:
                    lex()
                    while(nextToken == keyWords.get('case')[1]):
                        cases()
                        '''if(nextToken != IDENT and nextToken != Integer):
                            error()
                        else:
                            lex()
                            if(nextToken != special_sym.get(':')[1]):
                                error() '''

                    if(nextToken != keyWords.get('default')[1]):
                        error()
                    else:
                        lex()
                        if(nextToken != special_sym.get(':')[1]):
                            error()
                        else:
                            lex()
                            statement()
                            if(nextToken != special_sym.get(';')[1]):
                                error()
                            else:
                                lex()
                                if(nextToken != Right_bracket):
                                    error()

def assignment():
    print("enter assignment>")
    
    if(nextToken != IDENT or nextAct not in st):
        semantical_error()

    else:
        currVar = nextAct
        lex()
        if(nextToken != Equal_sign):
            error()
        else:
            lex()
            assignedVal = expr()
            '''
            if(type(assignedVal)!=st.get(currVar)[0]):
                semantical_error()
            '''
            if(type(assignedVal)==int):
                if(st.get(currVar)[0]!='int'):
                    semantical_error()
            if(type(assignedVal)==str):
                if(st.get(currVar)[0]!='string'):
                    semantical_error()

            
            st.get(currVar)[1] = assignedVal
            
            
            if(nextToken != special_sym.get(';')[1]):
                error()
            else:
                print("<Exit assignment>")
#Here is where we'll go to initialize a variable
def initialize():
    print('<Enter initialize>')
    
    if(nextToken != 'int' and nextToken !='float' and nextToken !='string' and nextToken !='real'):
        varName = peakAct()
        varType = nextAct
        st[varName] = [varType, None]
    
    lex()
    if(nextToken != IDENT):
        error()
    else:
        lex()
        if(nextToken != special_sym.get(';')[1]):
            error()
        else:
            print("<Exit initialize")
    

#From this statement function we are able to enter into the proper statement according to our code
def statement():
    print("<Enter statement>")
    # The following will be similar to a switch statement
    if(nextToken == keyWords.get('switch')[1]):
        switchStatement()
    elif(nextToken == keyWords.get('foreach')[1]):
        foreach_loop()
    elif (nextToken == keyWords.get('for')[1]):
        for_loop()
    elif(nextToken == keyWords.get('while')[1]):
        while_loop()
    elif(nextToken == keyWords.get('do')[1]):
        do_while_loop()
    elif(nextToken ==keyWords.get('if')[1]):
        ifStatement()
    elif(nextToken == IDENT):
        assignment()
    elif (nextToken == keyWords.get('return')[1]):
        returnStatement()
    elif(nextToken == Left_bracket):
        block()
    elif(nextToken == types.get('int')[1] or nextToken == types.get('string')[1] or nextToken == types.get('float')[1]):
        initialize()
    elif(nextToken == keyWords.get('public')[1] or nextToken ==keyWords.get('private')[1]):
        Class()
    elif(nextToken == keyWords.get('method')[1]):
        method()
    else:
        error()
    print("<Exit statement>")
#Call to get the next lexeme/token code
def lex():
    global i, nextToken, arr, nextLexem, nextAct
    i = i + 1
    
    if(i < len(arr) and i < len(array)):
        nextToken = arr[i]
        nextLexem = array[i]
        nextAct = actArray[i]
        print("Next token is: " + str(nextToken) + " next item is: " +nextLexem)

def peak():
    global i, nextToken, arr
    i=i+1
    if(i < len(arr) and i < len(array)):
        peakVal = array[i]
    else:
        error()
    i = i-1 
    return peakVal

def peakAct():
    global i, nextAct, arr
    i=i+1
    if(i < len(arr) and i < len(array)):
        peakValue = actArray[i]
    else:
        error()
    i = i-1 
    return peakValue

def peak2():
    global i, nextToken, arr
    i=i+2
    if(i < len(arr) and i < len(array)):
        peakVal = array[i]
    else:
        error()
    i=i-2
    return peakVal

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
        actArray.append(fileInput)

def boolExpr():
    print('Enter boolexpr')
    expr()
    while(nextToken == special_sym.get('<')[1] or nextToken == special_sym.get('>')[1]):
        lex()
        expr()
    print('Exit boolexpr')

# <expr> -> <term> {(+|-) <term>}
def expr():
    print("enter expression")
    if(nextToken==STRING):
        s = nextAct
        lex()
        return s[1:len(s)-1]
    result = 0
    print("Enter <expr>")
    # Parse the first term */
    result += term()
    ''' As long as the next token is + or -, get
     the next token and parse the next term '''
    while(nextToken == Plus_sign or nextToken == minus_sign):
        if(nextToken==Plus_sign):
            lex()
            result += term()
        else:
            lex()
            result -=term()
   
    return result
    print("Exit <expr>")

# <term> -> <factor> {(* | /) <factor>}
def term():
    Tresult = 0
    print("Enter <term>")
    # Parse the first factor */
    Tresult += factor()
    
    # As long as the next token is * or /, get the next token and parse the next factor
    while (nextToken == Multiplication_symbol or nextToken == Division_symbol):
        if(nextToken == Multiplication_symbol):
            lex()
            Tresult *= factor()
        else:
            lex()
            c = factor()
            
            if(c==0):
                
                semantical_error()
            Tresult /= c
    return Tresult
    print("Exit <term>")

# <factor> -> id | int_constant | ( <expr> )
def factor():
    print("Enter <factor>")
    # Determine which RHS
    #if (nextToken == IDENT or nextToken == INTEGER or nextToken == FLOATING_POINT):
        # Get the next token
        #lex()
    if(nextToken == IDENT):
        cuu = nextAct
        lex()
        print("Exit <factor>")
        return st.get(cuu)[1]
    elif(nextToken == INTEGER):
        Fresult = int(nextAct)
        lex()
        print("Exit <factor>")
        
        return Fresult
    elif(nextToken == FLOATING_POINT):
        Fresult = float(nextLexem)
        lex()
        print("Exit <factor>")
        return Fresult

        # If the RHS is ( <expr> ), call lex to pass over the left parenthesis, call expr, and check for the right parenthesis
    else:
        if (nextToken == Left_parenthesis):
            lex()
            Fresult = expr()  # left par
            if (nextToken == Right_parenthesis):
                lex()
            else:
                error()
        # It was not an id, an integer literal, or a left parenthesis '''
        else:
            error()
    print("Exit <factor>")

#This is where we shut the program down if we run into an error
def exiter():
    sys.exit()

#Where we go if we run into a Syntactical error
def error():
    print("Syntactical error!!!")
    exiter()

#Where we go if we run into a lexical error
def lexical_error():
    print("Lexical error!!!")
    exiter()

def semantical_error():
    print("There was a semantical error")
    exiter()

#This is where I convery the string version of the lexemes to its integer values to make it easier to process
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
            print(array[i])
            return None
    
    return newArray

#where the lex analyzer begins
def mainLexAnalzer():
    global lexArray, actArray
    lexArray = []
    actArray = []

    print("\nUnedited program file")
    #Here is where we open the program file
    word = open(os.path.join(sys.path[0], "/Users/ibell8/Documents/PLC_Programming/Final/test.txt"), "r")

    print(word.read())
    word.close()
    print("\nJave File tokenized:")
    print()
    #Here is also where we open and process the program file
    with open(os.path.join(sys.path[0], "/Users/ibell8/Documents/PLC_Programming/Final/test.txt"), "r") as fileInput:
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

#Where the syntactical analysis begins
def mainSynAnalyzer(array):
    # arr = [26, 11, 21, 11, 27]
    # arr = [26, 11, 21, 12, 27, 24, 11, -1]
    global i, nextToken, arr
    arr = array
    i = 0
    nextToken = arr[0]
    
    program()
    # expr = (leftPar, ident, add, ident, rightPar)


if __name__ =='__main__': 
    
    array = mainLexAnalzer()
    print(array)
    tokenarray = convertor(array)
    
    tokenarray.append(-1)
    mainSynAnalyzer(tokenarray)
    print()
    print("Ran successfully, Syntax and Semantics are correct")
    
    