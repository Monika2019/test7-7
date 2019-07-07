# -*- coding: UTF-8 -*-

# author by : （学员ID)
import random

for i in range(1,11):
    password = random.randint(0,9999)
    print ('password is : %04d'%(password))

nums = ('0''1''2''3''4''5''6''7''8''9')
password = []
for i in range(1,5):
    password.append(random.choice(nums))
    print('debug - password list changing : %s '%(password))
print('debug - list of password = %s '%(password))


print('password is : ',end='')
for item in password:
    print('%s'%(item),end='')

print('\n\n---------')
char1 = ['0''1''2''3''4''5''6''7''8''9']
char2 = ['a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''s''t''u''v''w''x''y''z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
charAll = char1 + char2 + char3 +char4
print('debug - All usable chars : %s' % (charAll))
pwdlen=8
password = []
for i in range(1,pwdlen):
    password.append(random.choice(charAll))
    print('debug - password list changing : %s'%(password))
print('debug - list of password = %s' %(password))

print('password is : ',end='')
for item in password:
    print('%s'%(item),end='')
