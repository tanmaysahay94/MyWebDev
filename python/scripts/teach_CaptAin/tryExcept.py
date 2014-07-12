def mult(a, b):
    try:
        print a * b
    except TypeError:
        print 'input only numbers plz'

mult(1, 2)
mult('a', 'b')
