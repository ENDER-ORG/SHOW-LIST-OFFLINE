from listdisplayer import tablecr
from boxcr import *
import time
def delp(x):
  l=1
  calling = ["#$ᴡᴀᴛᴄʜɪɴɢ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#",
              "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#", "#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#", "#$ᴅʀᴏᴘᴘᴇᴅ$#"]
  
  while(l>0):
       cav=1
       ko=1
       p=0
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
          K=1
          while(K>0):
           no=input('ARE YOU SURE YOU WANT TO DELETE THIS ENTRY?-Y/N|')
           print()
           no=no.upper()
           if(no=='Y'):
             del(x[lavana[0][1]])
             time.sleep(0.23)
             print('DELETED!!!!')      
             K=0
             l=0
           elif(no=='N'):
            
             K=0
             
             
           else:
             
             print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
             print()
             print()
             
         else:
           while True:
            zetsubo=input('Enter the serial number of the Entry you want to delete :')
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
                                no=input('ARE YOU SURE YOU WANT TO DELETE THIS ENTRY?-Y/N|')
                                print()
                                no=no.upper()
                                if(no=='Y'):
                                    del(x[lavana[zetsubo-1][1]])
                                    K=0
                                    l=0
                                    time.sleep(0.23)
                                    print('DELETED!!!!')
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
         
         

                  





