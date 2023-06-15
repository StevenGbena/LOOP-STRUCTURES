user=input('enter the sentence')

vowels='a,e,i,o,u'

for i in user:
    if i in vowels:
        user=user.replace(i,'')

        print(user)
