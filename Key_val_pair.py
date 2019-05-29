import re

Nameage='''
Rahul is 20,Aditya is 30,
Joy is 40 and Usha is 50.'''


ages=re.findall('\d{1,3}',Nameage) #return a list,'ages' is a list
names=re.findall('[A-Z][a-z]*',Nameage)

Name_age_dic=dict(zip(names,ages))

print(Name_age_dic)
print(names)