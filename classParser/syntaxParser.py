# coding: utf-8


def getWeeks(s) -> list:
    s = s[0:len(s)-1]
    s = s.split(",")
    ret_lst = []
    for i in s:
        if i=='':
            continue

        v = i.split('-')
        if len(v)==1:
            ret_lst.append(int(v[0]))
        elif len(v)==2:
            for j in range(int(v[0]), int(v[1])+1):
                ret_lst.append(j)

    return ret_lst


def parse_attribute(attr_str):
    c_first = attr_str[0]
    c_last = attr_str[len(attr_str)-1]

    # week parsing
    if c_last=="周":
        return "weeks", getWeeks(attr_str)
    # classroom parsing
    elif c_first.isalpha():
        return "classroom", attr_str
    # ignore other attributes
    else:
        return None, None


def parse(lex_list) -> list:
    
    if lex_list==None or len(lex_list)==0:
        return []

    out = []
    eachClass = {}
    status = 0
    for item in lex_list:
        if status==0:
            if item[0]=="class":
                eachClass["name"] = item[1]
                status = 1
            else:
                raise SyntaxParseError("invalid syntax: attribute of no class")
        elif status==1:
            if item[0]=="attr":
                k, v = parse_attribute(item[1])
                eachClass[k] = v
            elif item[0]=="class":
                out.append(eachClass)
                eachClass = {"name": item[1]}
            else:
                raise SyntaxParseError("invalid syntax: (" + str(item[0]) + ", " + str(item[1]) + ") not supported.")
        
    out.append(eachClass)
    return out

parse('')