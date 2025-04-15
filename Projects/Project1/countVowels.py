word=input("Enter the word: ")
vowels={'a','e','i','o','u'} #and {'A','E','I','O','U'}
result={}

for c in word:
    if c in vowels:
        result[c]=result.get(c,0)+1

for k,v in sorted(result.items()):
    print(k," is present",v," times")        