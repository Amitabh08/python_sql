# CALCULATE THE FREQUENCY DISTRIBUTION 
seq = [2,2,9,1,2,2,1,4,2,2,3,1]

dict={}

i = 0

count = 0

while i < len(seq):

    if(seq[i] in dict):

        count += 1

        dict.update({seq[i]:count})

    else:

        dict[seq[i]] = 1

        count = 1

    i+=1

print(dict)
