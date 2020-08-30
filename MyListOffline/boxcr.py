def linecrr(mo="_",rep=1,spa=2,cdis="",center=0,lineremov=0,specialfeature=0,lineaftersentence=0,adjuster=0,middlepart=12,ychar="┆"):
    if cdis!="":
        k=(rep*2)+1
    else:
        k=rep 
    middlepart=str(middlepart)   
    ja=cdis
    if cdis!="":
        for hoho in range(k):
            if hoho<(k//2) or (hoho>(k//2) and lineremov==0):
                if specialfeature==0:
                     print(mo*98)
                else:
              
                    
                    if hoho==(k-1):
                        print(f"{'╹'+(mo*96)+'╹'}")
                    else:
                       print(f"{'╷'+(mo*96)+'╷'}")
                
                    
            elif(hoho==(k//2)):
              if specialfeature==0:
                if center==0:
                     print(ja)
                else:
                    
                    print(" "*41+ja)
              else:
                  if middlepart.isalpha() is True and middlepart.lower()=='max':
                            middlepart=55
                  else:
                    if middlepart.isalpha() is False and int(middlepart)>55:
                        middlepart=12
                          
                  cdis=cdis.split("\n")
                  middlepart=int(middlepart)
                  for ik in cdis:
                      ik=ik.split('\\{1}')
                      if len(ik)==2:
                          if adjuster>0:
                              fornow=adjuster
                          else:
                              fornow=41  
                          if middlepart>53:
                              middlepart=53
                          if len(ik[0])>middlepart:
                              ik=list(ik[0])
                              for start in range(0, len(ik), middlepart):
                                     print(f'{ychar+" " +(" "*fornow)+"".join(ik[start:start+middlepart]) +(((96-(middlepart+(fornow+2)))*" ")+(middlepart-len("".join(ik[start:start+middlepart])))*" ")+" "+ychar}')
                              

                          else:
                             print(f'{ychar+" "+(" "*fornow)+ik[0]+(((96-(len(ik[0])+(fornow+2)))*" ")+" "+ychar)}')
                              

                         
                      elif len(ik)==1:
                          if len(ik[0])>96:
                              ik=list(ik[0])
                              for start in range(0, len(ik), 94):
                                     print(f'{ychar+" " + "".join(ik[start:start+94]) +(94-len("".join(ik[start:start+94])))*" "+" "+ychar}')
                          else:
                              print(f'{ychar+" "+ik[0]+((94-len(ik[0]))*" ")+" "+ychar}')
                      if lineaftersentence>0:
                         for lisass in range(lineaftersentence):
                              print(f"{ychar+(96*' ')+ychar}")
                          
                              
                    
    else:           
        for hoho in range(k):
            print(mo*98)
    
    if spa==0:
        pass
    elif spa==1:
        print()
    
    elif spa==2:
        print()
        print()

    elif(spa>=3):
          print()
          print()
          print()
          
