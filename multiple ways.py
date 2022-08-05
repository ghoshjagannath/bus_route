
from main import *


list1=['AIRPORT','ULTADANGA','SCIENCE CITY','PARK CIRCUS','RABINDRA SADAN','ESPLANADE']
list2=['Alam Bazar','Baranagar Bazar','SCIENCE CITY','Bibir Bazar','Cossipur','Bagbazar']
list3=['HOWRAH STN','HOWRAH BRIDGE EAST','B.B.D. BAG','ELGIN','Bagbazar','HAZRA',
      'RASHBEHARI AVE','TOLLYGUNJ','GARIA']


routes=[list1,list2,list3]


from itertools import combinations

total_combination=list(combinations(routes, 2))




# print(routes)


def finder():
      sou=input('Type your source name ')
      des=input('Type your destination name ')
      data=True
      while data:
            for route in total_combination:
                  lis1,lis2=route
                  print(lis1)
                  data=False
                  # data=decider(sou, des, lis1, lis2)
                  # print(data)
                  # if type(data)!=None:
                  #       print(data)
                  #       data=True

                  # else:
                  #       pass

finder()