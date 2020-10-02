from listdisplayer import *
from STA import *
from delet import *
from sa import *
from DV import *
from malsync import *
import time
import pathlib
import os
from boxcr import *
import getpass_ak
from scorechange import *

#_---------------------------------------------VARIABLES-----------------------------------------------------
h=0
restartit=0
calling = ["#$ᴡᴀᴛᴄʜɪɴɢ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#",
              "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#", "#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#", "#$ᴅʀᴏᴘᴘᴇᴅ$#"]
dyb=['#end','#exit']
dab=0
#-------------------------------------------------------FUNCTIONS------------------------------------------

#controls the way the program quits or ends
def endin(a=0):
    if a==0:
        spac2()
        print("QUITTING TO MAIN MENU......")
        time.sleep(0.89)
        spac2()
    
    else:
      global h  
      
      if a==2:
           h = '#END'
           return "aka"
        
      
      elif a==3:
          global restartit
          restartit=1
          spac2()
          print("RESTARTING THE PROGRAM....")
          time.sleep(1.2)
          spac2()
      else:
        spac2()
        h = '#END'
        print("QUITTING THE PROGRAM....")
        time.sleep(1.72)
        spac2()
#manages display of details
def displa():
       print("SAVING DETAILS....")
       time.sleep(0.22)
       spac2()
       print("SAVED DETAILS....")
       time.sleep(0.17)
       endin()
#checks if the file for sync entered exists or not          
def filexistcheck(fil):
    try: 
     file = pathlib.Path(fil)
     if file.exists ():
        return "true"
     else:
         return "false"
    except OSError:
        return 'false'
    except Exception as exce:
        print("UNKNOWN ERROR :",exce)
        spac2()

# is responsible for the major part of the interface
def linecr(mo,rep=1,spa=2,dis=0,cdis="",gap=0,lineremov=0):

    
    namingsa=['NEW ENTRY',"LIST","MODIFY","SEARCH","MAL SYNC","DEFAULT RESET","SIGN IN","HELP INFO","MYSQL CONNECTION"]
    k=rep+dis
    if cdis=="":
        ja=namingsa[(dis-1)]
    else:
        ja=cdis
    if dis!=0 or cdis=="":
        for hoho in range(k):
            if hoho==0 or (hoho==(k-1) and lineremov==0):
                 print(mo*98)
            elif(hoho==dis and cdis==""):
                 print(" "*47+ja)
            elif(cdis!="" and hoho==dis):
                if gap==0:
                     print(ja)
                else:
                    print(" "*47+ja)
    else:           
        for hoho in range(k):
            print(mo*98)
    
    if spa==0:
        pass
    elif spa==1:
        spac3()
    
    elif spa==2:
        spac2()
    elif(spa>=3):
          spac()
# controls the way dates are entered
def datte(a=1,b="",Z=0):
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
                  print("ENTER NUMBERS AND CORRECT FORMAT ONLY!!")
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
                     print("PLEASE ENTER A VALID DATE!!")
                     spac()

                 elif a==0 and Z!=1 and b>dattte:
                     print("THE DATE ENDED CAN'T BE GREATER THAN THE DATE STARTED......PLEASE ENTER AGAIN")
                     spac2()
                 else:
                     
                     return dattte

                    
              except Exception as er:
                   if str(er) =="month must be in 1..12":
                                   print("ERROR:MONTH MUST BE BETWEEN 1-12|[IT CAN'T BE-", datu[5:7],"]|!!")
                                   spac()

                   elif str(er) =="day is out of range for month":
                                  print("ERROR:THE DAY IS OUT OF RANGE FOR MONTH!!")
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
#checks if the feature can be used or not
def checker(lis):
    if len(lis)==0:
        spac2()
        print("THIS FEATURE CAN ONLY BE ACCESSED WHEN THERE IS AN ENTRY IN THE LIST!!!!!!!!!!!")
        spac2()
        return 0
    else:
        return 1
def defaultrese():
    rop = open("INFO LIST", "w+")
    rop.write('')
    rop.close()
#creates the info file and also reads the file
def reader(a=0,b=0,c=[]):
  while(True):
    try:
      
      if b!=0:
          rop = open("INFO LIST", "w+")

          for i in c:
              rop.write(i+"\n")
          return "done"
      rara = []
      
      rop = open("INFO LIST", "r")


      for kami in rop:
         kami = kami.strip()
         rara.append(kami)

      rop.close()
      if a==1 and rara==[]:
          spac2()
          
          return "unexpected error 2"
      else:
         return rara

    except Exception as exce:
      if "[Errno 2] No such file or directory: 'INFO LIST'"==str(exce) and a==0:
                          hope = open("INFO LIST", "w")
                          hope.write("")
                          hope.close()   
      elif "[Errno 2] No such file or directory: 'INFO LIST'" == str(exce) and a != 0:
                          hope = open("INFO LIST", "w")
                          hope.write("")
                          hope.close()
                          return "unexpectedly ending"                
        
      else:
         spac2() 
         print("UNEXPECTED ERROR :",exce)
         spac2()
         break
# creates and reads the list file
def filecreatorwriter(a=0,liss=[]):
 while True: 
  try:
   statustypesep = ["#$ᴡᴀᴛᴄʜɪɴɢ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#",
                    "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#", "#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#", "#$ᴅʀᴏᴘᴘᴇᴅ$#"]
   locls=0
   while locls<8:
     try:
       liss.remove(statustypesep[locls])
       locls+=1
     except Exception as lisremoer:
         if "list.remove(x): x not in list"==str(lisremoer):
             break
         else:
             print()
             exit(f"UNEXPECTED ERROR : {lisremoer}")
   if a==1:
       if(len(liss) == 0):
                baka = open("LIST.txt", "bw")
                baka.write(b"")
                baka.close()
        
       else:
            oof=open("LIST.txt","bw")
            liss=storeinfo(sorted(liss))
            spac2()
            liindex=0
            while liindex<len(liss):
               i=liss[liindex]
               while(i not in statustypesep and liindex<len(liss)):
                   coun=0
                   while coun<6:
                      
                      inf=i[coun]
                      oof.write(inf.encode('UTF-8','strict')+"\n".encode('UTF-8'))
                      coun+=1
                   liindex += 1
                   if liindex<len(liss):
                        i=liss[liindex]
                   
    
               else:
                 if i in statustypesep:
                   oof.write(i.encode('UTF-8', 'strict')+"\n".encode('UTF-8'))
                   liindex+=1
            oof.close()
       break
   else:
       raw = open("LIST.txt", "rb")
       listinfo=raw.readlines()
       raw.close()
       if(len(listinfo)==0):
                  nam=[]
       else:             
           t=0
           q=[]
           m=[]
           for i in listinfo:
                 valu =i.decode('UTF-8').strip()
                 if valu not in statustypesep:
                      m.append(valu)
                      t+=1
                      if(t==6):
                          q.append(m)
                          t=0
                          m=[]
                 else:
                     q.append(valu)
                      
           
           
           nam=q 
       return nam 

  except Exception as exce:
      if "[Errno 2] No such file or directory: 'LIST.txt'"==str(exce):
                          hope = open("LIST.txt", "bw")
                          hope.close() 
      else: 
          print("UNEXPECTED ERROR :",exce)  
          spac2()  
          break
# checks if the password is correct or not
def passcheck():
  h=0
  try:
   while(True):
   
    k=reader(1)
    if k=="unexpectedly ending":
        return "unexpectedly ending"
    
    elif k=="unexpected error 2":
        return "unexpected error 2"
    if k[1]=='#0':
        return 'y'   
    porch=(getpass_ak.getpass('Password: '))
    
    spac2()
    
    
    if porch==k[1]:
        return "y"
       
    elif porch=="#exit" or porch=="#EXIT":
        break  
    
    else:
        k=reader(1)
        if k=="unexpectedly ending":
                   return "unexpectedly ending"
    
        elif k=="unexpected error 2":
                  return "unexpected error 2"
        print("INCORRECT PASSWORD!!ENTER AGAIN")
        spac2()
        
        h+=1
        if h>3:
            print("YOU HAVE ENTERED THE WRONG PASSWORD TOO MANY TIMES!!TRY AGAIN LATER")
            spac2()
            return "q"
        
  except Exception as ekk:
      print(ekk)

linecr("=",2,2,2,"SERIES LIST",1)



linecrr('─',1,2,"COMMANDS-\n ● #end    ● TENTRY   \n ● #exit   ● START (use this to start the program) \n ●NTODAY (use this while adding dates.This will set '0000-00-00' as the date..)",0,0,1,1)


import datetime
# the main program 
def com():

  
  R = 2
  nam = filecreatorwriter()
  while(R>0):
    global hapa
    filecreatorwriter(1,nam)
    nam=filecreatorwriter()    
    linecr("―", 2, 0, 8, "MENU", 1, 1)
    spac3()
    mo=input("1 : MAKE A NEW ENTRY                                  2 : VIEW MY LIST\n\n3 : VIEW A PARTICULAR RECORD                          4 : EDIT MY LIST \n\n5 : MALSYNC                                           6 : DEFAULT RESET \n\nCOMM :")

    x=mo.upper()
    if(x=='3'):
      spac2()
      while(True):
       p=0
       lavana=[]
       opq=input("SEARCH BAR|COM:").strip()
       print()
       if opq.lower()=='#end' or opq.lower()=='#exit':
             break
       for i in nam:
         if i not in calling:
              if opq.lower() in i[0].lower():
                   if len(i[2])==2:
                       kapapa=i[2]
                   else:
                       kapapa='0'+i[2]
                   lavana.append([i[0],i[1],kapapa,i[4],i[5]])
                   p=1
       if p==0:
           linecrr("=",1,2,'NO SUCH RECORD FOUND!!!',1) 
           spac2()
       else:
           tablecr([['TITLE',84],['type',7],['score|{special}|',7],['Datestartded|{special}|',14],['Date ended|{special}|',14]],lavana,0,1,1,1,0,'POSSIBLE MATCHES')
           spac3()
           input('_')
           break
    elif(x=="1"):
     dab=0
     kok=1
     spac2()
     linecr("=",2,2,1)
     while(kok>0):
      t=input("TITLE:").strip()
      if t.lower() in dyb:
          dab=1
          spac2()
          break
      
      if t=="":
          spac3()
          print("TITLE CANNOT BE EMPTY")
          spac2()
      else:
       MOe=len(t)
       kok=0
       if(len(t)>49):
          t=t[:-(MOe-49)]
       
       spac2()
       if dab==1:
             break
       linecr("-",2,0,3,"TYPE",1)
       while True:
           
           oks=input("1 :TV\n2 :MOVIE\n3 :OVA\n4 :ONA\nCHOOSE :").strip()
           if oks.lower() in dyb:
               dab=1
               break
           if oks=='1':
               typ='TV'
           elif oks=='2':
               typ='Movie'
           elif oks=='3':
               typ='OVA'
           elif oks=='4':
               typ='ONA'
           else:
               spac2()
               linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!')
               linecrr('-')
               spac2()
               continue
           break
       re = 1
       spac2()
       if dab==1:
             break
       linecr("-",2,0,3,"STATUS",1)
       while re>0:   
          
          u=input("1 : PLAN TO WATCH\n2 : COMPLETED\n3 : DROPPED\n4 : WATCHING\nCHOOSE :").strip()
          if u.lower() in dyb:
              dab=1
              spac2()
              break
      
      
          if u=='1':
             aa='Plan to Watch'
             re-=1
             spac2()

          elif u=='2':
             aa='Completed'
             re-=1
             spac2()
          elif u=='3':
             aa='Dropped'
             re-=1
             spac2()
          elif u=='4':
             aa='Watching'
             re=0
             spac2()
          else:
               spac2()
               linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!')
               linecrr('-')
               spac2()
       if dab==1:
             break    
     
     while(True and dab!=1):
     
      try:
       if u!='1':
        k=input('SCORE(0-10) :').strip()
        if k.lower() in dyb:
            dab=1
            spac2()
            break
        k=int(k)
        YO=k
        k= str(k).zfill(2)
        spac2()
        
        if(YO>10 or YO<0):
            spac3()
            linecrr("=",1,2,'ENTER THE SCORE WITHIN THE LIMIT(0-10)')
            linecrr('-')
            spac2()
            
        else:
           break
       else:
           k='0'
           break
      except:
         spac3()
         linecrr("=",1,2,'ENTER A NUMBER ONLY!!!')
         linecrr('-')
         spac3()
    

     while(dab!=1 and True):
        if u!='1': 
         spac3()
         o=input('DATE STARTED \nTODAY-Y/N :').strip()
         if o.lower() in dyb:
             dab=1
             spac2()
             break
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
                p=datte()
                if p=='':
                    dab=1
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
        else:
            p='0000-00-00'
            break       
     
     if dab!=1 and u!='1':
        spac2()
        while(True):

          n=input('DATE ENDED \nTODAY-Y/N :').strip()
          
          if n.lower() in dyb:
              dab=1
              spac2()
              break

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
                
                q=datte(0,ppp,1)
               else:
                   q=datte(0,ppp)
               if q=='':
                   dab=1
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
                            
     else:
         q="0000-00-00"  
     if dab!=1:      
        displa()
        kick=[t,typ,k,aa,str(p),str(q)] 
        nam.append(kick)
      
    
    elif(x=="2"):
          spac2()
          linecr("=",2,2,2)
        
          if nam==[]:
                print("OOPS!LOOKS LIKE YOUR LIST IS EMPTY")
                spac2()
          else:
            
            if(len(nam)<10):
                table(nam)
            else:
                spac2()
                while True:				
                  spac2()
                  print("SORT BY: \n\n● 1 NAME \n\n● 2 DATE STARTED  \n\n● 3 DATE ENDED \n\n● 4 SCORE \n"+("-"*96),
                        "\n\n●[ENTER '#end' or '#exit' TO EXIT TO MAIN MENU]\n●[ADD 'D' TO THE END OF THE OPTION FOR DESCENDING SORT LIKE '1D']", "\n\n"+("-"*96))
                  Op=input("CHOOSE :").upper().strip()
                  spac2()
                  
                  namcop=nam
                  if Op=='2':
                       namcop=stat(namcop,2,False)
                       table(namcop)
                       spac2()     
                       
                  elif Op=='2D':
                        namcop=stat(namcop,2,True)
                        table(namcop)
                        spac2()
                  elif Op=='3':
                        namcop=stat(namcop,3,False)
                        table(namcop)
                        spac2()
                  elif Op=='3D':
                        namcop=stat(namcop,3,True)
                        table(namcop)
                        spac2()
                  elif Op=='1D':
                        table(stat(namcop,1))
                        spac2()
                  elif(Op=='1'):
                        table(namcop)
                        spac2()
                    
                              
                  elif Op=='4':
                              table(stat(namcop,4,False))
                              spac2()
                  elif Op=='4D':
                              table(stat(namcop,4,True))
                              spac2()                        
                  
                  elif Op=='#EXIT':
                              spac2()
                              
                              
                  elif Op=='#END':
                              spac2()
                  else:
                      linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!')
                      linecrr('-')
                      spac2()
                      continue  
                  if Op.lower() not in dyb:
                     pclpl=input('_')
                  break                
                              
    elif(x=="4"):

        ak=1
        jojo=checker(nam)
        if jojo==1:
          spac2()
          linecr("=",2,2,3)
          while(ak>0):
             spac2()
             nope=input(f"● 1 DELETE RECORD(S)                                ● 2 ALTER THE SCORE \n\n● 3 CHANGE THE DATE                                 ● 4 CHANGE THE STATUS \n\n● 5 CHANGE THE NAME                                 ● 6 CHANGE THE TYPE\n\n                      ● 7 DELETE THE WHOLE LIST \n\nCOM :").strip()
             print()
             if nope.lower() in dyb:
                 break
             if(nope=='1'):
                  
                  delp(nam)
                  ak=0
                  spac2()
                
             elif(nope=='7'):
              mlp=len(nam)
              lop=0
              ak=0
              spac2()
              leafa=passcheck()
              if leafa=='unexpectedly ending' or leafa=="unexpected error 2":
                    print("CONNECTION TO FILE LOST.......")
                    time.sleep(1)
                    endin(1)
                    
                    hapa=1
                    R=0
              if(leafa=='y'):
                 kpop=1
                 while(kpop>0):
                    lope=input("ARE YOU SURE YOU WANT TO DELETE THE LIST-Y/N|CHOOSE:").strip()
                    lope=lope.upper()
                    if(lope=='Y'):
                      while(mlp>0):
                         del(nam[lop])
                         mlp=len(nam)
                      spac3()
                      print('LIST DELETED!!')
                      spac2()
                      kpop=0
                    elif(lope=='N'):
                      kpop=0
                      spac2()
                    else:
                      spac3()
                      print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
                      spac3()
              
               
             elif(nope=='2'):
               scorech(nam)
               ak=0
               spac3()
                
             elif(nope=='4'):
                 spac2()
                 status(nam)
                 ak=0
                 spac2()
             elif(nope=='3'):
                 spac2()
                 datechang(nam)
                 ak=0
                 spac2()
             elif nope=='5':
                 namechang(nam)
                 ak=0
                 spac3()
             elif nope=='6':
                 typechang(nam)
                 ak=0
                 spac3()
             else:
                 
                 linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!')
                 linecrr('-')
           
    elif x=="5":
        linecr("=",2,2,5)
        while True: 
         malxmlfile=input("ENTER THE XML FILE NAME (WITH EXTENSION) :").strip()
         spac2()
         if malxmlfile=="#EXIT" or malxmlfile=="#exit":
              break
         elif malxmlfile=="#END" or malxmlfile=="#end":
             break
         result=filexistcheck(malxmlfile)
         if result=="true" and malxmlfile!='':
             print('SYNCING UP....')
             time.sleep(0.52)
             spac2()
             endresult=malsyncup(malxmlfile,nam)
             if endresult is None:
                  print("MAL SYNC COMPLETE!!")
                  R=0
                  filecreatorwriter(1, nam)
                  endin(3)
                  break
             
              
             
         else:
             print("THE FILE DOES NOT EXIST!!PLEASE TRY AGAIN    \n\nNote :make sure the mal xml file name is correct and is in the same directory as this program i.e", os.path.dirname(__file__))
             spac2()
         
         
    elif(x=="#END"):
            R-=2
            spac2()
            filecreatorwriter(1,nam)

            
                
 
    elif(x=="TENTRY"):
           spac3()
           
           print("TOTAL NUMBER OF ENTERIES=",len(nam)-8)
           spac3()
    elif(x=='#EXIT'):
        R=0
        spac2()

        filecreatorwriter(1, nam)
    
    elif x=='6':
        linecr('=',2,2,6)
        leafa=passcheck()
        if leafa=='unexpectedly ending' or leafa=="unexpected error 2":
                    print("CONNECTION TO FILE LOST.......")
                    time.sleep(1)
                    endin(1)
                    hapa=1
                    R=0
        if(leafa=='y'):
            spac2()
            
            while True:
                   
                   pkasd=input('ARE YOU SURE YOU WANT TO RESET THE USER SETTING ?|Y/N| :').strip().upper()   
                   if pkasd=='Y':
                       defaultrese()
                       endin(3)
                       R=0
                       hapa=1
                   elif pkasd=='N':
                       pass
                   else:
                       spac3()
                       print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
                       spac3()
                       continue
                   break
        spac3()
                       
    else:
        spac2()
        linecrr("=",1,2,'SORRY YOU HAVE TO CHOOSE FROM THE GIVEN OPTIONS')
        continue


while True:
    
    spac3()
    h=input("COMMAND:").upper()
    hapa=0
    if(h=='START'):
      while True: 
        spac2()
        klpq=reader()
        if klpq==[]:
           jak=""
           linecr("―",2,2,7)
           while True:
               off=input("WRITE A USERNAME :").upper().strip()
               
               if off=="#END":
                   jak=endin(2)
                   break
               spac2()
               if off=="":
                   print("EMPTY FIELD!!PLEASE ENTER AGAIN") 
                   spac2() 
                   continue
               
               hef=input("press any key to continue").upper()
               if hef!="#again":
                       spac2()
                       break
               
           if off!="#END": 
             while True:   
                 ypl=input("DO YOU WANT TO CREATE A PASSWORD-Y/N :").upper().strip()
                 if ypl=="#END":
                       break
                 if(ypl=='Y'):
                     while True:
                            spac2()
                            yop=input("ENTER THE NEW PASSWORD :").strip()
                            spac2()
                            
                            if yop=="#END" or yop=="#end":
                                    jak=endin(2)
                                    break
                            if yop=="":
                                print("EMPTY FIELD!!PLEASE ENTER AGAIN")
                                spac2()
                            opp=0
                            for uuh in yop:
                                if uuh=="#":
                                   print("YOU CAN'T USE # IN PASSWORD")
                                   opp=1
                            if opp==1:
                                continue
                            hef=input("press any key to continue").upper()
                            if hef!="#again":
                                    reader(0,1,[off,yop])
                                    break
                            
                            spac2()
                            
                            
                     
                     break  
                 elif(ypl=='N'):
                       yop=" "
                       reader(0,1,[off,'#0'])
                       break
                 else:
                   spac3()
                   print("PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!!!!!")
                   spac2()
           
           if jak!="aka":
                    spac2()
                    allship=0
                    z='STARTING'
                    for trialss in range(15):
                         
                      
                      if allship==0:
                        z="STARTING.    "
                      elif allship==1:
                        z='STARTING..   '
                      elif allship==2:
                          z='STARTING... '
                      elif allship==3:
                          z='STARTING....'

                      allship+=1

                      if allship==5:
                          allship=0
                      else:
                        print(f'{z}\r',end='')
                        time.sleep(0.23)                  
                    print('                \r')
                    linecr('-')
                    com()
        
       
        else:
                linecr("―",2,2,7)
                cpp=reader()
                print("USER :",cpp[0])
                ho=passcheck()
                if ho=='y':
                    spac2()
                    allship=0
                    z='STARTING'
                    for trialss in range(15):
                         
                      
                      if allship==0:
                        z="STARTING.    "
                      elif allship==1:
                        z='STARTING..   '
                      elif allship==2:
                          z='STARTING... '
                      elif allship==3:
                          z='STARTING....'

                      allship+=1

                      if allship==5:
                          allship=0
                      else:
                        print(f'{z}\r',end='')
                        time.sleep(0.23)                  
                    print('                \r')
                    linecr('-')
                    com()
                elif ho=='unexpectedly ending' or ho=="unexpected error 2":
                    spac2()
                    print("CONNECTION TO FILE LOST.......")
                    time.sleep(1)
                    endin(1)
                    hapa=1
                
        if restartit==1:
           restartit = 0
           continue
        else:
           break         

    if(h=="#END"):
       if hapa==1:
         print('COME AGAIN')
         break
       else:
         endin(1)
         print('COME AGAIN')
         break
