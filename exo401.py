w= 'X-Dspam-Confidence:0.8475 '
colpos=w.find(':')
print(colpos)
afcol=w.find(' ',colpos )
print(afcol)
string1= w[ colpos+1 : afcol]
print(string1)
float1=float(string1)
print(float1)
print('i am adding 1 in float to check', float1 + 1.11)
