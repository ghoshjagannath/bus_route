
## Below mentioned list are demo route of 3 nos for here 
## we could implement for more nos of route for better route reference 


lis1=['a','b','d','e']
lis2=['b','g','c','h','i']
lis3=['x','y','c','m','l']





## Here we will use 3 nos of route for operations
def route_between(a:"origin",b:"destination",c:"intersection"):
    ##We are in need of 3 type of route for this operation 
    ## 1st one is where origin is situated
    ##2nd one is where destination is situated 
    
    ## 3rd one is used for assumption that it would connect with destination and 
    ## origin in between 
    #
    
    ## we can use loop for iteration of many types of route for future 
    ## like  for route in routes:
        ## def route_between(origin,destination ,route):
                ## rest of the operation remain same 
    
    
    #To bring out origine and intesection list common place this variable is taken            
    ori_intersec=None
    #bring out intersection between intersection list and destination list
    des_intersec=None
   
    
    ## We will need only in lower case as it is case sensitive for searching 
    ## origin.lower(), destination.lower() is used here 
    origin=input('Type your origin ->').lower()
    destination=input('Type your destination name ->').lower()
    
    
    
    def route():
        ##Searching is there is any commnon ground between origin and insection 
        ## and destination and intersection list 
        
        ## intersect place is different that is why 3 routes are here 
        if (set(a).intersection(set(c)))!=None and (set(b).intersection(set(c)))!=None:
            des_intersec=set(b).intersection(set(c))
            ori_intersec=set(a).intersection(set(c))
            path=a[a.index(origin):a.index(list(ori_intersec)[0])+1]
            if len(path)==0:
                #In case if path is returing no list then we need to reverse because 
                ## destination or origin place may be before of intersection 
                ## that is why it is returning zero list 
                
                ## example:-
                ##list=[1,2,3,4,5]
                ##lis2=[23,3,22]
                
                a.reverse()
                print(a[a.index(origin):a.index(list(ori_intersec)[0])+1])
            else:
                print(path)
                
            
            path2=c[c.index(list(ori_intersec)[0]):c.index(list(des_intersec)[0])+1]
            
            if len(path2)==0:
                c.reverse()
                print(c[c.index(list(ori_intersec)[0]):c.index(list(des_intersec)[0])+1])
            else:
                print(c[c.index(list(ori_intersec)[0]):c.index(list(des_intersec)[0])+1])
                
                

            path3=b[(b.index(list(des_intersec)[0])):(b.index(destination))+1]
            
            if len(path3)==0:
                b.reverse()
                print(b[(b.index(list(des_intersec)[0])):(b.index(destination))+1])
            
            else:
                print(b[(b.index(list(des_intersec)[0])):(b.index(destination))+1])

        else:
            print('Nothing will happend')
        
        
        
    try:
        type(origin[0])==str
        type(destination[0]==str)
        route()
    except IndexError():
        print('Please type all value')
        
    


if __name__=="__main__":
    route_between(lis1,lis3,lis2)