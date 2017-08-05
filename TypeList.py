lint = [2,3,1,7,4,12]

lmix = ['magical unicorns',19,'hello',98.98,'world']

lstr = ['magical','unicorns']

def typelist(x):
    sum=0
    words= ''
    for i in (x):

        if isinstance(i,str) or isinstance(i,float):
            listtype="mixed"
            if isinstance(i,float):
                sum+=i
                out=str(sum)
            else:
                words+=i+" "

        elif isinstance(i,int):
            listtype="interger"
            sum+=i
            out=str(sum)

        elif isinstance(i,str):
            listtype="string"
            words+=i+" "

    print "The list you entered is of "+listtype+" type."

    if listtype=="interger":
        print "Sum:",out

    elif listtype=="string":
        print "String: ",words

    else:
        print "Sum: ",out
        print "String: ",words



typelist(lmix)
