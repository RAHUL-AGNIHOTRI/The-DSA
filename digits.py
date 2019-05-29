import re

str='12345'

print('Matches,Special Case of ^ - ',re.findall('^\d',str))

print('Matches, NO digit with CAPITAL - D',len(re.findall('\D',str)))

print('Matches, ONLY digit with small - d',len(re.findall('\d',str)))

print('Matches, of "1" - ',re.findall('\d{5}',str)