lett = raw_input()
ovl = 'aeiouAEIOU'
con = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
if lett in ovl:
    print 'Vowel'
elif lett in con:
    print 'Consonant'
else:
    print 'invalid'
