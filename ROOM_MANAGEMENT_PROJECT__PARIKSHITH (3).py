import pickle,os
##HOTEL MANAGEMENT PROJECT##

#PARIKSHITH.N  XII A1

def ins():#working
     
     f=open("data.dat","wb")
     print("."*267)
     l=[]
     e=[]
     while True:
          
          nam=input("enter the room donater's name, if no enter 'null' ")
          rno=int(input("enter room number"))
          eroom=[i[1] for i in e]
          if rno in eroom:
               print("ROOM NUMBER ALDREADY EXISTS")
               continue
               
          ava=input("enter if the room AVAILABLE or NOT AVAILABLE ")
          ni=int(input("enter how many nights you are going to stay in the room"))
          flo=int(input("enter which floor"))
          
          typ=input("""enter room type:
| NORMAL    [100$]    |
| PRO        [200$]    |  
| DELUXE    [250$]    |
| ULTRA     [500$]    |
""")
          ch=input("do you want to add more records, enter | y | or | n |")
          l=[nam,rno,ava,ni,flo,typ]
          e.append(l)
          print("."*267)
          if ch=='n':
               break
     
     pickle.dump(e,f)
     print("RECORDS ADDED SUCCESFULLY")
     print("."*267)
     f.close()

     
def dis():#working
     f=open("data.dat","rb")
     
     try:
          while True:
               
               e=pickle.load(f)
               x=sorted(e)
               for i in x:
                    print('*'*45)
                    print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                    print('ROOM NO.=============>   ||',i[1],'||')
                    print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                    print('NO.OF NIGHTS==========>   ||',i[3],'||')
                    print('FLOOR===============>   ||',i[4],'||')
                    print('ROOM TYPE===========>   ||',i[5],'||')
                    print('*'*45)
               
     
     except:
          f.close()
     tot=len(e)
     av=0
     nav=0
     for i in e:
          if i[2]=='available':
               av=av+1
          if i[2]=="not available":
               nav=nav+1
     print('.'*267)
     print("TOTAL ROOMS------------------>",tot)
     print("AVAILABLE ROOMS COUNT--------->",av)
     print("NOT AVAILABLE ROOMS COUNT----->",nav)
     print('.'*267)
def sea():
     
     f=open("data.dat","rb")
     try:
          
          l=pickle.load(f)
          
          gh=int(input("""enter what you want to search;
ROOM PROVIDER'S NAME....................................................1
ROOM NUMBER........................................................................2
BY AVAILABILITY..................................................................3
ROOM TYPE.............................................................................4
ROOMS WHICH HAS GOT NO PROVIDER(NULL)..............5
"""))
          print("."*267)
          print(" ")

          
          if gh==1:
               print("."*267)
               sf=input("what name you want search")
               print("."*267)
               for i in l:
                    if i[0]==sf:
                         print("."*267)
                         print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                         print('ROOM NO.=============>   ||',i[1],'||')
                         print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                         print('NO.OF NIGHTS==========>   ||',i[3],'||')
                         print('FLOOR===============>   ||',i[4],'||')
                         print('ROOM TYPE===========>   ||',i[5],'||')
                         print(" ")
                         print("."*267)
                    
                         
               
                         
                         

          if gh==2:
               print("."*267)
               sf=int(input("what room no. you want to search"))
               print("."*267)
               for i in l:
                    
                         
                    if i[1]==sf:
                         print("."*267)
                         print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                         print('ROOM NO.=============>   ||',i[1],'||')
                         print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                         print('NO.OF NIGHTS==========>   ||',i[3],'||')
                         print('FLOOR===============>   ||',i[4],'||')
                         print('ROOM TYPE===========>   ||',i[5],'||')
                         print(" ")
                         print("."*267)
                    
                                   
          if gh==3:
               print("."*267)
               print("AVILABLE ROOMS:")
               
               for i in l:
                         
                    if i[2]=="available":
                         
                         print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                         print('ROOM NO.=============>   ||',i[1],'||')
                         print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                         print('NO.OF NIGHTS==========>   ||',i[3],'||')
                         print('FLOOR===============>   ||',i[4],'||')
                         print('ROOM TYPE===========>   ||',i[5],'||')
                         print(" ")
               
                              
               print("."*267)                   
               print("NOT AVAILABLE ROOMS:")
               
               for i in l:
                    
                    if i[2]=="not available":
                         print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                         print('ROOM NO.=============>   ||',i[1],'||')
                         print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                         print('NO.OF NIGHTS==========>   ||',i[3],'||')
                         print('FLOOR===============>   ||',i[4],'||')
                         print('ROOM TYPE===========>   ||',i[5],'||')
                         print(" ")
                         
                         
               print("."*267)

          if gh==4:
               print("."*267)
               rtypes=int(input("""enter which room type you want to search
NORMAL...................1
PRO...........................2
DELUXE...................3
ULTRA.....................4
"""))
               
               print("."*267)
               if rtypes==1:
                    
                    print("."*267)
                    
                    for i in l:
                         if i[5] in 'normalNormalNORMAL':
                              print("NORMAL ROOMS:")
                              print(' ')
                              print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                              print('ROOM NO.=============>   ||',i[1],'||')
                              print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                              print('NO.OF NIGHTS==========>   ||',i[3],'||')
                              print('FLOOR===============>   ||',i[4],'||')
                              print('ROOM TYPE===========>   ||',i[5],'||')
                              print(" ")
                              
                              print("."*267)
                         else:
                              print('NO NORMAL ROOMS FOUND!')
               if rtypes==2:
                    print("."*267)
                    
                    for i in l:
                         if i[5] in 'proProPRO':
                              print("PRO ROOMS:")
                              print(' ')

                              print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                              print('ROOM NO.=============>   ||',i[1],'||')
                              print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                              print('NO.OF NIGHTS==========>   ||',i[3],'||')
                              print('FLOOR===============>   ||',i[4],'||')
                              print('ROOM TYPE===========>   ||',i[5],'||')
                              print(" ")
                              
                              print("."*267)
               if rtypes==3:
                    print("."*267)
                    
                    for i in l:
                         if i[5] in 'deluxeDeluxeDELUXE':
                              print("DELUXE ROOMS:")
                              print(' ')
                              print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                              print('ROOM NO.=============>   ||',i[1],'||')
                              print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                              print('NO.OF NIGHTS==========>   ||',i[3],'||')
                              print('FLOOR===============>   ||',i[4],'||')
                              print('ROOM TYPE===========>   ||',i[5],'||')
                              print(" ")
                              print("."*267)
               if rtypes==4:
                    print("."*267)
                    
                    for i in l:
                         if i[5] in 'ultraUltraULTRA':
                              print("ULTRA ROOMS:")
                              print(' ')
                              print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                              print('ROOM NO.=============>   ||',i[1],'||')
                              print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                              print('NO.OF NIGHTS==========>   ||',i[3],'||')
                              print('FLOOR===============>   ||',i[4],'||')
                              print('ROOM TYPE===========>   ||',i[5],'||')
                              print(" ")


                              print("."*267)
          if gh==5:
               print("ROOMS WITH NO PROVIDER")
               for i in l:
                    if i[0] in 'nullNull':
                         print('ROOM PROVIDER NAME===>   ||',i[0],'||')
                         print('ROOM NO.=============>   ||',i[1],'||')
                         print('ROOM AVAILABILITY=====>   ||',i[2],'||')
                         print('NO.OF NIGHTS==========>   ||',i[3],'||')
                         print('FLOOR===============>   ||',i[4],'||')
                         print('ROOM TYPE===========>   ||',i[5],'||')
                         print(" ")
                    
     except:
          f.close()
          print("."*267)

          #all working


def update():#working
     uch=int(input("""
ADD A RECORD......1
UPDATE.....................2
"""))
     if uch==1:
          
          try:
               f=open("data.dat","rb")
               e=pickle.load(f) 
               f.close()
          except:
               
               return
          print("."*267)
          l=[]
     
          while True:
               nam=input("enter the room holder's name, if no enter 'NULL' ")
               rno=int(input("enter room number"))
               ava=input("enter if the room AVAILABLE or NOT AVAILABLE ")
               ni=int(input("enter how nights you are going to stay in the room"))
               flo=int(input("enter which floor"))
               typ=input("""enter room type:
| NORMAL    [100$]    |
| PRO        [200$]    |  
| DELUXE    [250$]    |
| ULTRA     [500$]    |
""")
               ch=input("do you want to add more records, enter | y | or | n |")
               l=[nam,rno,ava,ni,flo,typ]
               e.append(l)
               if ch=='n':   
                    break
          
          print("RECORD ADDED SUCCESFULLY")
          print("."*267)
          f=open('data.dat','wb')
          pickle.dump(e,f)
          f.close()
     if uch==2:
          try:
               f=open("data.dat","rb")
               e=pickle.load(f)
               f.close()
          except:
               
               return
          rono=int(input("enter the room no. to be changed"))
          upda=int(input("""TO CHANGE:
ROOM PROVIDER NAME..................1
STAY NIGHTS....................................2
MAKE AVAILABILE..........................3
MAKE NOT AVAILABLE..................4
FLOOR..................................................5
ROOM TYPE........................................6
"""))
          if upda==1:
               
               y=input('enter new provider name')
               for i in e:
                    
                    if i[1]==rono:
                         
                         i[0]=y
          if upda==2:
               y=int(input('enter new no. of nights'))
               for i in e:
                    
                    if i[1]==rono:
                         i[3]=y
          if upda==3:
               z=[]
               for i in e:
                    z.append(i[1])
               if rono in z:
                    
                    for i in e:
                         
                         if i[1]==rono:
                              
                              i[2]="available"
               print("RECORD MARKED AVAILABLE")
          if upda==4:
               
               z=[]
               for i in e:
                    z.append(i[1])
               if rono in z:
                         
                    for i in e:
                         if i[1]==rono:
                              i[2]="not available"
               print("RECORD MARKED NOT AVAILABLE")
          if upda==5:
               
               y=int(input("enter new floor no."))
               for i in e:
                    if i[1]==rono:
                         i[4]=y
          if upda==6:
               y=input("enter new room type")
               for i in e:
                    if i[1]==rono:
                         i[5]=y
          
         
          f=open("data.dat","wb")
          pickle.dump(e,f)
          f.close()
          print('RECORD UPDATED SUCCESFULLY')
          
                               
                         
                                  
def delete():
     print("."*267)
     
     try:
          
          f=open("data.dat",'rb')
          e=pickle.load(f)
          f.close()
     except :
          
           
          return

     rono=int(input("ENTER ROOM NO.TO BE DELETED"))
     chy=int(input("are you sure you want to delete the record..............1"))
     print("."*267)
      
     if chy==1:
          ne=[]
          for i in e:
               if i[1]!=rono:
                    ne.append(i)
                
          fl=open("script.dat",'wb')
          pickle.dump(ne,fl)
          fl.close()
          os.remove("data.dat")
          os.rename("script.dat","data.dat")
          print("THE RECORD HAS BEEN DELETED")
          print("."*267)


def billc():
     try:
          f=open("data.dat","rb")
          e=pickle.load(f)
          f.close()
     except:
          return
     
     bills=int(input("""SHOW:
ALL CUSTMER'S BILLS.........1
ONE CUSTUMER'S BILL.........2
"""))
     if bills==1:
          for i in e:
               
               if i[5] in "normalNormalNORMAL":
                    
                    
                    q=i[3]*100
                    print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')
                    
               if i[5] in "proProPRO":
                    q=i[3]*200
                    print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')

               if i[5] in "deluxeDeluxeDELUXE":
                    q=i[3]*250
                    print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')
                    
               if i[5] in "ultraUltraULTRA":
                    q=i[3]*500
                    print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')
                    
     if bills==2:
          rono=int(input('enter the room no. you want to calculate the bill'))
          for i in e:
               if i[1]==rono:
               
                    
                    if i[5] in "normalNormalNORMAL":
                         
                         
                         q=i[3]*100
                         print(q,'$  is the bill amount for ',i[3],'night for room number',i[1],'[',i[5],']')

                                             
                    if i[5] in "proProPRO":
                         q=i[3]*200
                         print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')

                    if i[5] in "deluxeDeluxeDELUXE":
                         q=i[3]*250
                         print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')
                    
                    if i[5] in "ultraUltraULTRA":
                         q=i[3]*500
                         print(q,'$  is the bill amount for ',i[3],'nights for room number',i[1],'[',i[5],']')
                    
                   
     

                      
print("~"*133)               
print("                                        ||     WELCOME TO HOTEL GRANDE INN     ||                                                            ")
print("~"*133) 
while True:
     print("~"*133)
     defch=int(input("""ENTER WHAT FUNCTION YOU WANT TO DO:
|1|-------------------> || INSERT  ||

|2|-------------------> || DISPLAY ||

|3|-------------------> || SEARCH ||

|4|-------------------> || UPDATE ||

|5|-------------------> || DELETE ||

|6|-------------------> ||   BILL   ||

|7|-------------------> ||   EXIT   ||
  """))
     
     print("~"*133)

     if defch==1:
          ins()
     if defch==2:
          dis()
     if defch==3:
          sea()
     if defch==4:
          update()
     if defch==5:
          delete()
     if defch==6:
          billc()
     if defch==7:
          break
     


     
print(" "*55," || THANK YOU  ||", " "*59)
print("~"*133)


                                                              #-PROJECT BY PARIKSHITH.N   XII A1 CS



     
     
          
     

     
          
     
          
          
