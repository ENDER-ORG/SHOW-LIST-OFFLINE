from listdisplayer import tablecr
from boxcr import *
import time

            
def scorech(x):               
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
          while kop>0:
            to=input("ARE YOU SURE YOU WANT TO CHANGE THE SCORE-Y/N:").strip()
            to=to.upper()
            print()
            if(to=='Y'):
             while True:
                 
                    try:
                                       ok=input('SCORE(0-10) :').strip()
                                       if ok.lower() in ['#end',"#exit"]:
                                            kop=0
                                            print('\n')
                                            break
                                       else:
                                        ok=int(ok)
                                        Ye=ok
                      
                                        ok= str(ok).zfill(2)
                      
                                        print('\n')                    
                                        if(Ye>10 or Ye<0):
                                            print("ENTER THE SCORE WITHIN THE LIMIT(0-10)")
                                            print('\n')
                                        else:
                                            x[lavana[0][1]][2]=ok
                                            kop=0
                                            l=0
                                            time.sleep(0.23)
                                            print('SCORE CHANGED!!!!')
                                            break
                          

                    except:
                                          print('\n')
                                          print("ENTER A NUMBER")
                                          print('\n')

            elif(to=='N'):
               kop=0
            
            else:
               print('PLEASE CHOOSE FROM THE OPTIONS ONLY')
               print()
               print()
            
             
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
                          K=1
                          while(K>0):
                                no=input('ARE YOU SURE YOU WANT TO CHANGE THE SCORE?-Y/N|')
                                print()
                                no=no.upper()
                                if(no=='Y'):
                                    while True:
                                      try:
                                       ok=input('SCORE(0-10) :').strip()
                                       if ok.lower() in ['#end',"#exit"]:
                                            K=0
                                            print('\n')
                                            break
                                       else:
                                        ok=int(ok)
                                        Ye=ok
                      
                                        ok= str(ok).zfill(2)
                      
                                        print('\n')                    
                                        if(Ye>10 or Ye<0):
                                            print("ENTER THE SCORE WITHIN THE LIMIT(0-10)")
                                            print('\n')
                                        else:
                                            x[lavana[zetsubo-1][1]][2]=ok
                                            K=0
                                            l=0
                                            time.sleep(0.23)
                                            print('SCORE CHANGED!!!!')
                                            break

                                      except:
                                          print('\n')
                                          print("ENTER A NUMBER")
                                          print('\n')
                        

                                    
                                elif(no=='N'):
                                    K=0
             
             
                                else:
                                  print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
                                  print()
                                  print()
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
         
def namechang(x):               
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
          while kop>0:
            to=input("ARE YOU SURE YOU WANT TO CHANGE THE NAME-Y/N:").strip()
            to=to.upper()
            print()
            if(to=='Y'):
             while True:

                                       ok=input('NEW TITLE :').strip()
                                       if ok.lower() in ['#end',"#exit"]:
                                            kop=0
                                            print('\n')
                                            break
                                       else:
                                        
                                        print('\n')                    
                                        if(ok==''):
                                            print("TITLE CANNOT BE EMPTY")
                                            print('\n')
                                        else:
                                            x[lavana[0][1]][0]=ok
                                            kop=0
                                            l=0
                                            time.sleep(0.23)
                                            print('NAME CHANGED!!!!')
                                            break
                        

            elif(to=='N'):
               kop=0
            
            else:
               print('PLEASE CHOOSE FROM THE OPTIONS ONLY')
               print()
               print()
            
             
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
                          K=1
                          while(K>0):
                                no=input('ARE YOU SURE YOU WANT TO CHANGE THE NAME?-Y/N|')
                                print()
                                no=no.upper()
                                if(no=='Y'):
                                    while True:
                                       ok=input('NEW TITLE :').strip()
                                       if ok.lower() in ['#end',"#exit"]:
                                            kop=0
                                            break
                                       else:
                                        
                                        print('\n')                    
                                        if(ok==''):
                                            print("TITLE CANNOT BE EMPTY")
                                            print('\n')
                                        else:
                                            x[lavana[zetsubo-1][1]][0]=ok
                                            K=0
                                            l=0
                                            time.sleep(0.23)
                                            print('NAME CHANGED!!!!')
                                            break
                        

                                    
                                elif(no=='N'):
                                    K=0
             
             
                                else:
                                  print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
                                  print()
                                  print()
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