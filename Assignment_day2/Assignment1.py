# FREQUENCY DISTRIBUTION
def f_distribution(seq):
 dict={}
 i = 0

 while i < len(seq):
    if(seq[i] in dict):
       
        dict.update({seq[i]:dict[seq[i]]+1})
    else:
        
        dict[seq[i]] = 1
      
    i+=1
 print(dict)

seq = [2,2,9,1,2,2,1,4,2,2,3,1]

f_distribution(seq)







