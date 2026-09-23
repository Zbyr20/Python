#global scope
x = 'global x'

def function():
    # local scope
    x = 'local x'
    print(x)

function()
print(x)

#######################################

name = 'Aslan'
def changName( ):
    global name
    print(name)

changName()
print(name)

#######################################

name = 'global string'
def greeting():
    # name='Zübeyir'

    def hello():
        # name = 'aslan'
        print('Hello'+ name)
    hello()
greeting()

#######################################
#####GLOBAL OLARAK TANIMLAMA ##########
x = 50
def test():
    global x
    print(f'x {x}')

    x = 100
    print(f'Changed x to  {x}')
test()
print(x)