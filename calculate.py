from random import randint,choice
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def exam():
    cmds = {'+':add,'-':sub}
    a = [randint(1,100) for i in range(2)]
    a.sort(reverse=True)
    b = choice('+-')
    result = cmds[b](*a)
    promat = '%s %s %s = ' % (a[0],b,a[1])
    counter = 0
    while counter < 3:
        try:
          c = int(input(promat))
        except ValueError:
            print('you is  null')
            exit()
        except (KeyboardInterrupt,EOFError):
            print('see you')
            exit()
        if c == result:
            print('you is very good')
            break
        else:
            print('you is worng')
            counter +=1
    else:
        print('%s %s' %(promat,result))
def fun1():
    while 1:
        exam()
        try:
          d = input('go on?/yn:').strip()[0]
        except IndexError:
           print('value is null')
           exit()
        except (KeyboardInterrupt,EOFError):
            print('see you')
            exit()
        if d == 'n':
            break
if __name__ == '__main__':
    fun1()