vi = 2
vf = 2.3
vc = 'a'
vs = "aaa"
vb = True
print("vInt: ", vi)
print("vFloat: ", vf)
print("vChar: ", vc)
print("vString: ", vs)
print("vBoolean: ", vb)

#cast: conversion de tipo de datos
print('vi: ' + str(vi)) #str convierte en string el valor entero de vi
vc = '2' #Una variable puede cambiar de valor durante la ejecucion
print('vc:' + vc )
vci = int(vc)
print('type vc: ', type(vc))
print('type vci: ', type(vci))
#Python asignacion dinamica de tipos
vci = True
print('type vci:', type(vci))

#maneras de hacer print
print("vi:", vi, "vf:", vf,"vb:", vb)
print(f"vi: {vi}, vf {vf}, vb {vb}")

#Expresiones
a=2
b=3
c= a + b
print("c: ", c)
c = 2 * a
#updated