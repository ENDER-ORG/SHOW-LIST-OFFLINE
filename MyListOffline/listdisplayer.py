
def table(x):
   calling = ["#$ᴡᴀᴛᴄʜɪɴɢ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#",
              "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#", "#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#", "#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#", "#$ᴅʀᴏᴘᴘᴇᴅ$#"]


   dss=0
   t=len(x)
   print("", "_"*154)
  
   pl=0   
   for KI in x:
    dss+=1
    if KI in calling:
              subst=KI.replace("$","")
              substat=subst.replace("#","")
              print(' '+"-"*154+"", "\n", substat)
              pl=0
              if dss==len(x):
                  print(' '+"-"*154+"")
                  print(f"|   NONE {' '*146}|")
                  print("╹"+"─"*154+"╹")
              elif x[dss] in calling:
                  print(f"|   NONE {' '*146}|")
              

    else:
      pl += 1
      if pl>=100000:
          count="ERR"
      elif pl<10:
          count="0"+str(pl)
      else:
          count=pl
      if len(KI[0])>83:
          name=KI[0][0:83]
      else:
          name=KI[0]
      if len(KI[2])<2:
          score="0"+KI[2]
      else:
          score=KI[2]
      
      print("|   ",count," "*(5-len(str(count))),"|",name," "*(84-len(name))+"|"," ",KI[1]," "*(7-len(KI[1])),"|","  ",score," ","|"," ",KI[4]," ","|"," ",KI[5]," |") 
      
      if KI==x[-1]:
          print("╹"+"─"*154+"╹")
    
  

#   ]
def tablecr(tablecolumninfo,records,disphead=1,ifcenter=0,showtotalentries=0,ifsrno=0,ifsplit=0,tdisplay='T.ENTRIES',emptytobedisplayedas='─'):
  tcl,re,etd=tablecolumninfo,records,emptytobedisplayedas
  lengt=len(tcl)
  myinfo=[]
  checker=[]
  myinfo2=[]
  checker2=[]
  if ifsrno==0:
     head=""
     calculee=0
  else:
    head='|___Sr_NO___|'
    calculee=1
    
    lengt+=1
  calcul=0
  copy=calculee
  head2=head
  if ifsplit==0:
    for inf in tcl:
      
      inf[0]=inf[0].split('|{special}|')
      lgtcname=len(inf[0][0])
      mentionedlgt=inf[1]
      
      sk=0
      if lgtcname>mentionedlgt:
          mentionedlgt=lgtcname
          diff2=0
          diff1=0
      else:
          diff=mentionedlgt-lgtcname
          
          if ifcenter==0:          
              diff2=diff
              if diff==0:
                  diff2=0
        
          else:        
             if diff%2!=0:
                    
                    diff+=1
                    
             diff1,diff2=(diff//2),(diff//2)
         
      if lgtcname==0 and mentionedlgt==0: 
              pass
      else:        
        if calculee==0:
           if ifcenter==0:
                 head+=f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                 checker.append(len(f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
           else:
               disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               head+=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               checker.append(len(f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
        else:
          if ifcenter==0: 
             head+=f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
             checker.append(len(f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
          else:
               disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               head+=f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               checker.append(len(f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
        
        if len(inf[0])==2 and ifcenter!=0:
            myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),disvar.index(inf[0][0][1])-2])              
        else:
          if ifcenter==0:
            myinfo.append([mentionedlgt,0])
          else:
             
              myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),0])
        calcul+=1
        calculee+=1
    if len(head) > 167:
     
      print(f"The Column length is exceeding the current limit i.e 167 characters.\nYour length is {len(head)}||It should be at most 167 characters\nTry reducing {len(head)-167} character(s)")
  
    else:     
            if showtotalentries!=0:
                  a=len(re)
                  dig=len(str(a))
                  print("", ("_"*(len(tdisplay)+3)), "_"*13)
                  print(f'{"|__"+tdisplay+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}')
                
            if disphead==1:
              print("", "_"*(len(head)-2))
              print(head)
            else:
                print()
            dio11=0
            for reco in re:
                dio11+=1
                if ifsrno!=0:
                   
                   if dio11>=100000:
                        count="ERR"
                   elif dio11<10:
                     count="0"+str(dio11)
                   else:
                     count=str(dio11)
                   
                   strire=''
                   
                   strire+=f'{"|    "+count+" "*(7-len(str(count)))+"|"}'
                   dioo=1
                   
                else:
                    strire=''
                    dioo=0
                dio=0
                for recor in reco:
                    recor=str(recor)
                    if recor=='':
                        recor=etd
                    elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo[dio][0]:
                            recor='Err'
                    elif len(recor)>myinfo[dio][0]:
                        recor=recor[0:(myinfo[dio][0])]
                   
                    if dioo==0:
                        strire+=f"{'| '+(' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"
                          
                    else:
                        strire+=f"{(' '+' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"
                        
                    dio+=1
                    dioo+=1
                    
                   
                print(strire)
            print("╹"+"─"*(len(head)-2)+"╹")       
