# bus route is mainly have 2 function . 
# according to time and input this function will output  route for this 
#according to time  route will be delevered 
# #find route for that 
# lis1=['AIRPORT','ULTADANGA','SCIENCE CITY','PARK CIRCUS','RABINDRA SADAN','ESPLANADE']
# lis2=['Alam Bazar','Baranagar Bazar','SCIENCE CITY','Bibir Bazar','Cossipur','Bagbazar']

# intersect_lis=[x for x in lis1 if x in lis2]

# print(intersect_lis)





lis1=['a','b','d','e']
lis2=['b','g','c','h','i']
lis3=['x','y','c','m','l']

#this function will decide in which function it will go for whether it is simple_route or 
# diff_route for further process .
def decider(sou:str,des:str,lis1,lis2):
    if sou in lis1 and des in lis1:
        simple_route(sou, des, lis1, lis2)
    elif sou in lis2 and des in lis2:
        simple_route(sou,des, lis1, lis2)
    elif sou in lis1 and des in lis2:
        diff_route(sou, des, lis1, lis2)
    elif sou in lis2 and des in lis1:
        diff_route(sou, des, lis1, lis2)
    else:
        print('Print right name for bus ')



#this function is used when source and des are in same  bus route
def simple_route(sou,des,lis1,lis2):
    if sou in lis1 and des in lis1:
        print (lis1[lis1.index(sou):lis1.index(des)+1])
    elif sou in lis2 and des in lis2:
        print(lis2[lis2.index(sou):lis2.index(des)+1])   
    else:
        print('something else')
            

        
            
#this function is used when source and des are not in the same bus route        
def diff_route(sou,des,lis1,lis2):
    intersect_lis=[]
    intersect_lis=[x for x in lis1 if x in lis2]
    try:
        if sou in lis1: 
            return((lis1[lis1.index(sou):lis1.index(intersect_lis[0])+1])+(lis2[lis2.index(intersect_lis[0])+1:lis2.index(des)+1]))
        elif sou in lis2:
            return((lis1[lis1.index(des):lis1.index(intersect_lis[0])])+(lis2[lis2.index(intersect_lis[0]):lis2.index(sou)+1]))
    except ValueError:
        return None
    
    
    
    
if __name__=="__main__":
    decider('b','m',lis2,lis3)



