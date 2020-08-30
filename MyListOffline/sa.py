from listdisplayer import tablecr
from boxcr import *
import time

            
def status(x):               
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
            to=input("ARE YOU SURE YOU WANT TO CHANGE THE STATUS-Y/N:").strip()
            to=to.upper()
            print()
            geez=''
            if(to=='Y'):
             while True:
               
               er=input("1 : PLAN TO WATCH\n2 : COMPLETED\n3 : DROPPED\n4 : WATCHING\nCHOOSE :").strip()
               if er.lower()=='#exit' or er.lower()=='#end':
                      print('\n')
                      break
               print()
               if(er=='1'):
                  geez="Plan to Watch"
               elif(er=='2'):
                  geez="Completed"

               elif(er=='3'):
                  geez="Dropped"

               elif(er=='4'):
                  geez='Watching'
                  
               if geez!='':
                   x[lavana[0][1]][3]=geez
                   time.sleep(0.26)
                   l=0
                   kop=0
                   print('STATUS CHANGED!!!!')
                   break
               else:
                
                print('PLEASE CHOOSE FROM THE OPTIONS ONLY')
                print()
                print()
                

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
                                no=input('ARE YOU SURE YOU WANT TO CHANGE THE STATUS?-Y/N|').strip()
                                print()
                                no=no.upper()
                                if(no=='Y'):
                                    while True:
                                      er=input("1 : PLAN TO WATCH\n2 : COMPLETED\n3 : DROPPED\n4 : WATCHING\nCHOOSE :").strip()
                                      if er.lower() in ['#end','#exit']:
                                             K=0
                                             print('\n')
                                             break
                                      print()
                                      if(er=='1'):
                                         geez="Plan to Watch"
                                      elif(er=='2'):
                                          geez="Completed"
                                      elif(er=='3'):
                                        geez="Dropped"
                                      elif(er=='4'):
                                         geez='Watching'
                  
                                      if geez!='':
                                        x[lavana[zetsubo-1][1]][3]=geez
                                        K=0
                                        l=0
                                        time.sleep(0.23)
                                        print('STATUS CHANGED!!!!')
                                        break
                                      else:
                
                                        print('PLEASE CHOOSE FROM THE OPTIONS ONLY')
                                        print()
                                        print()
                                    
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
         
def typechang(x):               
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
            to=input("ARE YOU SURE YOU WANT TO CHANGE THE TYPE-Y/N:").strip()
            to=to.upper()
            print()
            geez=''
            if(to=='Y'):
             while True:
               
                 oks=input("1 :TV\n2 :MOVIE\n3 :OVA\n4 :ONA\nCHOOSE :").strip()
                 if oks.lower() in ['#end','#exit']:
                       kop=0
                       print('\n')
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
                    print('\n')
                    linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!')
                    linecrr('-')
                    print('\n')
                    continue
                 x[lavana[0][1]][1]=typ
                 kop=0
                 time.sleep(0.23)
                 print('\n')
                 print('TYPE CHANGED!!!!')
                 l=0
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
                                no=input('ARE YOU SURE YOU WANT TO CHANGE THE TYPE?-Y/N|').strip()
                                print()
                                no=no.upper()
                                if(no=='Y'):
                                    while True:
                   
                                       oks=input("1 :TV\n2 :MOVIE\n3 :OVA\n4 :ONA\nCHOOSE :").strip()
                                       if oks.lower() in ['#end','#exit']:
                                           print('\n')
                                           K=0
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
                                              print('\n')
                                              linecrr("=",1,2,'PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!')
                                              linecrr('-')
                                              print('\n')
                                              continue
                                       x[lavana[zetsubo-1][1]][1]=typ
                                       print(x[lavana[zetsubo-1][1]])
                                       K=0
                                       time.sleep(0.23)
                                       print('\n')
                                       print('TYPE CHANGED!!!!')
                                       l=0
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