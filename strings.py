def compare (str_a, str_b):
    res='Ни одно условие не выполнено'
    if not isinstance(str_a, str) or not isinstance(str_b, str):
        res=0
    elif str_a==str_b:
        res=1
    else:
        if len(str_a)>len(str_b):
            res=2
        if str_b=='learn':
            res=3
    return res


res=compare(123,'sedw')
print (res)

res=compare('abcd', 'abcd')
print (res)

res=compare('abcde', 'abc')
print (res)

res=compare('avc', 'learn')
print (res)

res=compare('abc', 'abcde')
print (res)