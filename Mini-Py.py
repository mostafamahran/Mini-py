
def Charapper(x,c):
    return [i for i,j in enumerate(x) if j==c]

def customizedsplit(strn,letter,opt):
    indlist=Charapper(strn,letter)
    split_values = []
    tmp  = ''  
    if opt ==1:
        return [strn[:indlist[0]],strn[indlist[0]+1:]]
    if opt ==2:             
        for words in inp:
            if words == letter:
                split_values.append(tmp)
                tmp = ''
            else:
                tmp += words
        if tmp:
            split_values.append(tmp)    
        print(split_values)
    else:
        print("Enter Correct Option")
        
