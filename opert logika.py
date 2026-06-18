#not
a = False
c = not a
print ('data a=',a)#otput false
print('data c=',c)#output true

#or jika salah satu true dipastikan nilai true
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)#output false

a= True
b = False
c = a or b
print(a,'OR',b,'=',c)#output true

#and jika dua nilai true hasil true,tpi jika ada false 
#maka hasilnya false

a = False
b = False
c = a and b
print(a,'and',b,'=',c)#output false

a = True
b = False
c = a and b
print(a,'and',b,'=',c)#output false

a = True
b = True
c = a and b
print(a,'and',b,'=',c)#output true

#XOR AKAN TRUE JIKA SALAH SATU TRUE tapi sisanya akan false
a = False
b = False
c = a^b
print(a,'XOR',b,c)#output false

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)#output false

a= False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)#output true


#operator bitwise
a=6
b=3


c= a & b
print('nilai:',a,)
print ('nilai:',b,)
print ('nilai bitwise AND:',c,)
 
 
#opertor or
a=6
b=3


c= a|b
print('nilai:',a,)
print('nilai:',b,)
print('nilai bitwise OR:',c,)
