import datetime
dyb=['#exit','#end']
from boxcr import *
from listdisplayer import *
import time
def spac():
    print()
    print()
    print()


def spac2():
    print()
    print()


def spac3():
    print()
    
    

def datteaa(a=1,b="",Z=0):
    libra = ['0','1','2','3','4','5','6','7','8','9']
    lib = [5,8]
    while True:
      
      if a==1:
          datu = input("ENTER THE DATE STARTED[DATE FORMAT- 'YYYY-MM-DD'] :")
      else:
         datu = input("ENTER THE DATE ENDED[DATE FORMAT- 'YYYY-MM-DD'] :")
      spac()
      datu = datu.strip()
      if datu.lower() in dyb:
          return ''
          
      if(len(datu) ==10):

          hey = 0
          k = 1
        
          for i in datu:
              if i =='-' and k in lib:
                  pass

              elif i in libra:
                  pass

              else:
                  hey = 1
                  print("ENTER NUMBERS AND CORRECT FORMAT ONLY!!!!!!!!")
                  spac()
                  break
              k += 1
          if hey ==0:
              try:
                 dattte = datetime.date(int(datu[0:4]),int(datu[5:7]),int(datu[8:10]))

                 if dattte >datetime.date.today():
                     print(
                         "THIS DATE DOESN'T EXIST YET! |PLEASE ENTER A VALID DATE!!!")
                     spac()

                 elif dattte <datetime.date(1900,12,31):
                     print("PLEASE ENTER A VALID DATE!!!!!")
                     spac()

                 elif a==0 and Z!=1 and b>dattte:
                     print("THE DATE ENDED CAN'T BE GREATER THAN THE DATE STARTED......PLEASE ENTER AGAIN")
                     spac2()
                 else:
                     
                     return dattte

                    
              except Exception as er:
                   if str(er) =="month must be in 1..12":
                                   print("ERROR:MONTH MUST BE BETWEEN 1-12|[IT CAN'T BE-", datu[5:7],"]|!!!!")
                                   spac()

                   elif str(er) =="day is out of range for month":
                                  print("ERROR:THE DAY IS OUT OF RANGE FOR MONTH!!!!!")
                                  spac()
                   else:
                       print("UNEXPECTED ERROR :",er)
                       spac2()
              except KeyboardInterrupt:

                   print("UNEXPECTED ERROR")
                   spac()
                   continue


      else:
          print("CORRECT FORMAT ONLY!!!!!!!!")
          spac()
          
def inputt():
 while(True):
        if True: 
         spac3()
         o=input('DATE STARTED \nTODAY-Y/N :').strip()
         if o.lower() in dyb:
              return ''
         spac3()
         o= o.upper()
          
     
          
         if o=='Y':
            p= datetime.date.today()
            ppp=p
            p=str(p)
            j=0
            break
         elif(o=='NTODAY'):
             p= '0000-00-00'
             ppp=p
             j=1
             break
         elif(o=="N"):
             j=0
             spac3()
             while True:
              
              try:
                p=datteaa()
                if p=='':
                    return ''
                ppp=p
                break
              except Exception as uee:
                  spac3()
                  print("UNEXPECTED ERROR:",uee)
                  spac2()
                  break
             break
        
         else:
              
               spac3()
               linecrr("=",1,2,'ENTER A DATE OR NTODAY!!!!')
               linecrr('-')
               spac2()
               continue
        else:
            p='0000-00-00'
            break       
     
 if True:
        spac2()
        while(True):

          n=input('DATE ENDED \nTODAY-Y/N :').strip()
          
          if n.lower() in dyb:
              return ''

          n= n.upper()
      
      
          
          if n=="Y":
              q= datetime.date.today()
              q=str(q)
              spac2()
              break
          
          elif n=='NTODAY':
              q='0000-00-00'
              spac2()
              break
          elif(n=="N"):
            spac3()
            while True:
              try:
               if j==1:
                
                q=datteaa(0,ppp,1)
               else:
                   q=datteaa(0,ppp)
               if q=='':
                   return ''
               break
              except Exception as uee:
                  spac3()
                  print("UNEXPECTED ERROR:", uee)
                  spac2()
                  break
            break              
                  
          else:
              spac3()
              linecrr("=",1,2,'ENTER A DATE OR NTODAY!!!!')
              linecrr('-')
              spac2()
        return [p,q]                     
def datre():
   
       kp=1
       u=0 
       while(kp>0):
        
        to=input("ARE YOU SURE YOU WANT TO CHANGE THE DATE-Y/N:").strip().lower()
        if to in dyb:
            return ''
        to=to.upper()
        print()  
        if to=='Y':               
           poka=inputt()
           if len(poka)==0:
               return ''
           elif len(poka)==2:
               return poka
           else:
               return ''
        elif(to=='N'):
            return ''
        else:
            print("PLEASE CHOOSE FROM THE OPTIONS ONLY")
            print()
            print()
      

def datechang(x):
  l=1
  calling = ["#$ᴡᴀᴛᴄʜɪɴɢ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#",
              "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#", "#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#", "#$ᴅʀᴏᴘᴘᴇᴅ$#"]
  
  while(l>0):
       p=0
       cav=1
       ko=1
       lavana=[]
       opq=input("SEARCH BAR|COM:").strip()
       print()
       if opq.lower()=='#end' or opq.lower()=='#exit':
             break
       for i in x:
         if i not in calling:
              if opq.lower() in i[0].lower():
                   lavana.append([i[0],x.index(i)])
                   p=1
                   j=i
       if(p==1):
         tablecr([['TITLE',85]],list(map(lambda js: [js[0]],lavana)),0,1,1,1,0,'POSSIBLE MATCHES')
         if len(lavana)==1:
          kop=1
          kams=datre()
          if len(kams)==0:
              print('\n')
          elif len(kams)==2:
              x[lavana[0][1]][4]=str(kams[0])
              x[lavana[0][1]][5]=str(kams[1])
              l=0
              time.sleep(0.26)
              print('DATE CHANGED!!!!')
          else:
             print('\n') 
             
         else:
           while True:
            zetsubo=input('Enter the serial number of the Entry you want to edit :').strip()
            print()
            if zetsubo.isnumeric()==True:
                      zetsubo=int(zetsubo)
                      if zetsubo>len(lavana) or zetsubo==0:
                            print()
                            print('The entry number is out of range!!!')
                            print('\n')
                      else:
                         
                                 kop=1
                                 kams=datre()
                                 if len(kams)==0:
                                           print('\n')
                                           pass
                                 elif len(kams)==2:
                                  x[lavana[zetsubo-1][1]][4]=str(kams[0])
                                  x[lavana[zetsubo-1][1]][5]=str(kams[1])
                                  l=0
                                  time.sleep(0.26)
                                  print('DATE CHANGED!!!!')
                                 else:
                                     print('\n') 
                                 break
            else:
                  if zetsubo.lower()=='#exit' or zetsubo.lower()=='#end':
                        break
                  else:
                        print('Please enter a number only!!!')
                        print('\n')                   
            
       if p!=1 and cav!=0 and ko!=0:
         print(f'NO SUCH ENTRY WITH THE NAME {opq} FOUND')
         print()
         print()