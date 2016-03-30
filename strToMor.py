import RPi.GPIO as GPIO
import time

pin = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def charToMor(letter):
    print(letter),
    if letter.lower() == "a":
        a()
#    elif letter.lower() == " ":
#       space()
    elif letter.lower() == "b":
        b()
    elif letter.lower() == "c":
        c()
    elif letter.lower() == "d":
        d()
    elif letter.lower() == "e":
        e()
    elif letter.lower() == "f":
        f()
    elif letter.lower() == "g":
        g()
    elif letter.lower() == "h":
        h()
    elif letter.lower() == "i":
        i()
    elif letter.lower() == "j":
        j()
    elif letter.lower() == "k":
        k()
    elif letter.lower() == "l":
        l()
    elif letter.lower() == "m":
        m()
    elif letter.lower() == "n":
        n()
    elif letter.lower() == "o":
        o()
    elif letter.lower() == "p":
        p()
    elif letter.lower() == "q":
        q()
    elif letter.lower() == "r":
        r()
    elif letter.lower() == "s":
        s()
    elif letter.lower() == "t":
        t()
    elif letter.lower() == "u":
        u()
    elif letter.lower() == "v":
        v()
    elif letter.lower() == "w":
        w()
    elif letter.lower() == "x":
        x()
    elif letter.lower() == "y":
        y()
    elif letter.lower() == "z":
        z()
    
def a():
    dot()
    dash()
    
def b():
    dash()
    dot()
    dot()
    dot()
    
def c():
    dash()
    dot()
    dash()
    dot()
    
def d():
    dash()
    dot()
    dot()
    
def e():
    dot()
    
def f():
    dot()
    dot()
    dash()
    dot()
    
def g():
    dash()
    dash()
    dot()
    
def h():
    dot()
    dot()
    dot()
    dot()
    
def i():
    dot()
    dot()
    
def j():
    dot()
    dash()
    dash()
    dash()
    
def k():
    dash()
    dot()
    dash()
    
def l():
    dot()
    dash()
    dot()
    dot()
    
def m():
    dash()
    dash()
    
def n():
    dash()
    dot()
    
def o():
    dash()
    dash()
    dash()
    
def p():
    dot()
    dash()
    dash()
    dot()
    
def q():
    dash()
    dash()
    dot()
    dash()
    
def r():
    dot()
    dash()
    dot()
    
def s():
    dot()
    dot()
    dot()
    
def t():
    dash()
    
def u():
    dot()
    dot()
    dash()
    
def v():
    dot()
    dot()
    dot()
    dash()
    
def w():
    dot()
    dash()
    dash()
    
def x():
    dash()
    dot()
    dot()
    dash()
    
def y():
    dash()
    dot()
    dash()
    dash()
    
def z():
    dash()
    dash()
    dot()
    dot()

def space():
    print ""
    time.sleep(1)

def dot():
    print("."),
    GPIO.output(pin, True)
    time.sleep(0.4)
    GPIO.output(pin, False)
    time.sleep(0.2)
    
def dash():
    print("-"),
    GPIO.output(pin, True)
    time.sleep(0.7)
    GPIO.output(pin, False)
    time.sleep(0.2)

try:

    string = raw_input("Input a string to convert to Morse code: ")

    for letter in string:
        charToMor(letter)
        print ""
        time.sleep(0.4)

except Exception,e:
    print "Error!"
    print str(e)
finally:
    GPIO.cleanup()
