# coding: utf-8


def space_sub(c):
    if c==' ':
        return '_'
    return c

def space_remove(c):
    if c==' ':
        return ''
    return c


def parse(raw_str) -> list:
    if raw_str=="" or raw_str==None:
        return []
    
    out = []
    value = ""
    status = 0
    for c in raw_str:
        if status==0:
            # read attribute
            if c=='[':
                status = 1
            # ignore prefix-blanks
            elif c=='\n' or c==' ':
                pass
            # read classname
            else:
                value = value + space_sub(c)
                status = 2
        elif status==1:
            # attribute end
            if c==']':
                out.append(("attr", value))
                value = ""
                status = 0
            # continue reading attribute
            else:
                value = value + c
        elif status==2:
            # classname end, immediately following attribute
            if c=='[':
                out.append(("class", value))
                value = ""
                status = 1
            # classname end, following newline character
            elif c=='\n':
                out.append(("class", value))
                value = ""
                status = 0
            # continue reading classname
            else:
                value = value + space_sub(c)
    return out
