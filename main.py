import re, time
def check_par(filelist,start=1,stop="end", raiser=0):
    if stop=="end":
        joined="\n".join(filelist[start-1:])
    else:joined="\n".join(filelist[start-1:stop])
    countl=0
    countr=0
    for char in joined:
        if char=="(":countl+=1
        elif char==")":countr+=1
    #print ("(:{} ):{}".format(countl, countr))
    if countl==countr: return True
    elif raiser==1:raise SyntaxError("Number of '('({}) and ')'({}) are not equal.".format(countl, countr))
    else: return False
    
def synth_lines(filelist):
    filelist=" ".join(filelist)
    pattern1=r"([()])([\t ])+(.)"
    filelist=re.sub(pattern1,r"\1\3", filelist)      
    pattern2=r"([()])([\t ])+(.)"
    filelist=re.sub(pattern2,r"\1\3", filelist)      
    pattern3=r"([^()])([\t ])+([^()])"
    filelist=re.sub(pattern3,r"\1 \3", filelist)
    pattern4=r"(.)([\t ])+([()])"
    filelist=re.sub(pattern4,r"\1\3", filelist)
    newlist=[]
    while list(filelist)!=[]:
        print("\nasdf",[filelist],"\n")
        countl=countr=0
        for ind in range(len(filelist)):
            if ind==len(filelist)-1:
                newlist.append(filelist)
                filelist=[]
                break
            if (countl==0 and filelist[ind]=="(" and ind!=0):
                pattern=r"([ \t])*(.)+([\t ])"
                x=re.match(pattern, filelist[:ind]).group()
                print("x=",x)
                if filelist[ind] in " (":
                    newlist.append(filelist[0:ind])
                    filelist=filelist[ind:]
                    break
            if filelist[ind]=="(":countl+=1
            elif filelist[ind]==")":countr+=1
            if countr==countl!=0:
                newlist.append(filelist[0:ind+1])
                filelist=filelist[ind+1:]
                break
    return newlist

def nest(line):
    if line[0]!="(":
    	    return line
    newline=[]
    while line!="()":
        #print(newline, line)
        
        for x in range(1, len(line)):
            #print("x=",x,"line[x]=",line[x])
            if line[x]==" ":
                #print("if 1")
                newline.append(line[1:x])
                line="("+line[x+1:]
                break
            if line[x]=="(":
                if(x!=1):
                    newline.append(line[1:x])
                    line="("+line[x:]
                    #print("if 2")
                    break
                lcnt=1
                rcnt=0
                for y in range(2, len(line)):
                    if line[y]=="(":
                        lcnt+=1
                    if line[y]==")":
                        rcnt+=1
                    #print("if 2 loop", y, line, line[y], lcnt, rcnt)
                    if lcnt==rcnt:
                        newline.append(nest(line[x:y+1]))
                        line="("+line[y+1:]
                        break
                break
            if line[x]==")":
                newline.append(line[1:x])
                return newline
    return newline

def interpret(lst):
    pass
    if "(" in lst[1:]:
        pass
    else:   
        return "x" 
        
    

def openandsplit(path):
    program_file=open(path, "r")
    program=program_file.readlines()
    program_file.close()
    for i in range(len(program)):
        if program[i][-1]=="\n": program[i]=program[i][:-1]
    return program
s_exp={"+":"add"}
inputfile="program"
program=openandsplit("{}.txt".format(inputfile))
check_par(program, 1, "end", 1)
print(program)
program=synth_lines(program)
print(program, "\n")
for line in program:
    print(nest(line))
    #test
