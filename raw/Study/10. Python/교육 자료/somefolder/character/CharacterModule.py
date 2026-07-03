def namePrint(name, age):
    message = '\'{}\'님의 나이는 {}세입니다.'.format(name, age)
    print(message)
# end def

def sayHello(message, n = 10):
    for idx in range(n):
        print(message)
    print()
# end def