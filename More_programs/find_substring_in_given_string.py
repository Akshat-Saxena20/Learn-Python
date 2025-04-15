s="The idea of innovation is central to the idea of progress. Every great invention starts with an idea, and the strength of that idea determines its impact. The idea of collaboration often enhances the development of a single idea, transforming it into something extraordinary. Ultimately, the idea that sparks change is the one that resonates with people the most."

subString="idea"
found=False
pos=-1
lenght=len(s)

while True:
    pos=s.find(subString,pos+1,lenght)
    if pos == -1:
        break
    print("Found the sub string at position: ",pos)
    found=True
if found == False:
    print("Sub string does not found")    