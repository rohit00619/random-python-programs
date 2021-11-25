punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#pw=open('positive_words.txt')
#pw1=pw.readlines()
#pw2=pw1[35:]
#print(pw2)
#pwl=[]
#for x in pw1:
#    if x not in pwl:
#        pwl=x.append(pwl)
#print(pwl)
def strip_punctuation(a):
    for x in punctuation_chars:
        x=x.replace(a,"")
    return(a)

def poscount(a):
    ss=strip_punctuation(a)
    sl=ss.lower()
    ssl=sl.split()
    x1=0
    for x in x1:
        if x in nwl:
            x1=x1+1
        return(x1)


def negcount(a):
    ss=strip_punctuation(a)
    sl=ss.lower()
    ssl=sl.split()
    x1=0
    for x in x1:
        if x in pwl:
            x1=x1+1
        return(-x1)

pwl=[]
with open('positive_words.txt', 'r') as f:
    pwl = [line.split() for line in f]
pwl1=pwl[35:]
print(pwl1)


nwl=[]
with open('negative_words.txt', 'r') as f:
    nwl = [line.split() for line in f]
nwl1=nwl[35:]
print(nwl1)


td=[]
with open('project_twitter_data.csv', 'r') as f:
    for line in f:
        td=line.split()
td1=td[1:]
rt=td1[1]
tw=td1[0]
#rc=td1[2]
rc=[]
#for rc in td1:
 #   rc = td1.split(',')
  #  rc = td1[2]
print(rc)
print(td1)
#print(rt)
#print(tw)
#print(rc)



#td=open('project_twitter_data.csv')
#td1=td.readlines()
#print(td1)

#def positivecounter():





#def negativecounter():
