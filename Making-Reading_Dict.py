

mydiction={"name":"Eric","age":"42","country of birth":"United States","favorite language":"Python"}

def dictionary_function(dictionary):

    for key,data in dictionary.iteritems():
        print "My",key,"is",data

dictionary_function(mydiction)
