"""
a=int(input('a='))
b=int(input('b='))
print('%d + %d =%d' % (a,b,a+b))
print('%d - %d =%d' % (a,b,a-b))
print('%d * %d =%d' % (a,b,a*b))
print('%d / %d =%d' % (a,b,a/b))
print('%d // %d =%d' % (a,b,a//b))
print('%d %% %d =%d' % (a,b,a%b))
print('%d ** %d =%d' % (a,b,a**b))
"""
a=int(input('a='))
b=int(input('b='))
a+=b
a *= a+2
print (a)