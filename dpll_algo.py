
"""
clause -> list of tuples (a,b,c)
    -ve symbol means negation
    example (1,2,-3) means x U y U not z
    
symbol -> list of symbols used [a,b,c,d...]
model  -> allocation of variables....
        True / False / -1
"""


def check_all_true(clause , symbol , model):

    value = dict()
    for a,b in model:
        value[a] = b

    for cl in clause:

        valid = False
        for v in cl:
            if v in value:
                if value[v] == True:
                    valid = True
            else:
                return False
        if valid == False:
            return False

    return True

def check_any_false(clause , symbol , model):

    value = dict()
    for a,b in model:
        value[a] = b

    for cl in clause:

        valid = True
        for v in cl:
            if v in value:
                if value[v] == True:
                    valid = False
            else:
                valid = False
                break
            
        if valid == True:
            return True
        
    return False


def find_pure_symbols(clause , symbol , model):


    symb = []
    vals = []

    for x in symbol:

        pos = 0
        neg = 0

        for cl in clause:
            if x in cl:
                pos += 1
            if -x in cl:
                neg += 1
        if pos == 0 and neg > 0:
            symb.append(x)
            vals.append(False)
        if neg == 0 and pos > 0:
            symb.append(x)
            vals.append(True)

    return (symb , vals)

def find_unit_symbols(clause , symbol , model):

    symb = []
    vals = []

    value = dict()
    for a,b in model:
        value[a] = b

    for x in symbol:
        for cl in clause:
            for v in cl:
                if v in value:
                    if value[v] == True:
                        break
                elif abs(v) == x:
                    continue
                else:
                    break
            else:
                if x in cl:
                    symb.append(x)
                    vals.append(True)
                    break
                if -x in cl:
                    symb.append(x)
                    vals.append(False)
                    break
        else:
            continue
        
    return (symb , vals)
            

def dpll(clause , symbol , model):

    symbol = list(symbol)

    if check_all_true(clause , symbol , model):
        print("valid : ", model)
        return True
    if check_any_false(clause , symbol , model):
        return False

    p,val = find_pure_symbols(clause , symbol , model)

    if p != []:

        print("pure symbols: " , p)

        # allocate the symbols
        for i in range(len(p)):
            x , v = p[i] , val[i]
            model.append((x,v))
            model.append((-x,not v))
            symbol.remove(x)

        return dpll(clause , symbol , model)

    
    p,val = find_unit_symbols(clause , symbol , model)

    if p != []:
        
        print("unit symbols: " , p , val)
        # allocate the symbols
        for i in range(len(p)):
            x , v = p[i] , val[i]
            model.append((x,v))
            model.append((-x,not v))
            symbol.remove(x)

        return dpll(clause , symbol , model)


    first_var = symbol[0]
    rest_var = symbol[1:]

    return dpll(clauses , rest_var , model + [[first_var,True] , [-first_var,False]]) or dpll(clauses , rest_var ,model + [[first_var,False], [-first_var,True]])
    

clauses =[[1,2,3] , [1,2,-3] , [1,-2,3] , [1,-2,-3] , [-1,2,-3] , [-1,-2,3] , [-1,-2,-3] ]
symbol = [1,2,3,4,5]
model = []

ans = dpll(clauses , symbol , model)
print(ans)
if ans == True:
    print("Yes The given expression is satisfiable by dpll algorithm")
else:
    print("No, it is not satisfiable ... ")

