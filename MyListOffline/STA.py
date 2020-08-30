from listdisplayer import table
#THIS IS USED TO SORT BOTH BY TYPE AND STATUS AND SCORE
def storeinfo(cc):
  c = []
  w=[]
  p=[]
  d=[]
  fl=[]
  chi=[]
  t = []
  ov = []
  m = []
  on = []
  ff = []
  qo = []
  ge=len(cc)
  x=cc
  i=0
  while(i<ge):
      if(x[i][3]=="Completed"):
          c.append(x[i])
      if(x[i][3]=="Plan to Watch"):
          p.append(x[i])
      if(x[i][3]=="Watching"):
          w.append(x[i])
      if(x[i][3]=="Dropped"):
          d.append(x[i])
      i+=1
  i = 0
  while(i < len(c)):
      if(c[i][1] == "TV"):
          t.append(c[i])
      if(c[i][1] == "Movie"):
          m.append(c[i])
      if(c[i][1] == "OVA"):
          ov.append(c[i])
      if(c[i][1] == "ONA"):
          on.append(c[i])
      if c[i][1] == 'Special':
          ff.append(c[i])
      i += 1  
  i=0
  while (i<len(p)):
      if p[i][1]=='Unknown':
          p[i][1]='Special'
      i+=1
  
  fl.append(["#$ᴡᴀᴛᴄʜɪɴɢ$#"])
  fl.append(w)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#"])
  fl.append(t)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#"])
  fl.append(m)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#"])
  fl.append(ov)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#"])
  fl.append(on)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#"])
  fl.append(ff)
  fl.append(["#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#"])
  fl.append(p)
  fl.append(["#$ᴅʀᴏᴘᴘᴇᴅ$#"])
  fl.append(d)

  for i in fl:
      for m in i:
          chi.append(m)
  return chi
def stat(cc,lockdown=0,jab=True):
  c = []
  w=[]
  p=[]
  d=[]
  fl=[]
  chi=[]
  t = []
  ov = []
  m = []
  on = []
  ff = []
  qo = []
  ge=len(cc)
  x=cc
  i=0
  while(i<ge):
      if(x[i][3]=="Completed"):
          c.append(x[i])
      if(x[i][3]=="Plan to Watch"):
          p.append(x[i])
      if(x[i][3]=="Watching"):
          w.append(x[i])
      if(x[i][3]=="Dropped"):
          d.append(x[i])
      i+=1
  i = 0
  while(i < len(c)):
      if(c[i][1] == "TV"):
          t.append(c[i])
      if(c[i][1] == "Movie"):
          m.append(c[i])
      if(c[i][1] == "OVA"):
          ov.append(c[i])
      if(c[i][1] == "ONA"):
          on.append(c[i])
      if c[i][1] == 'Special':
          ff.append(c[i])
      i += 1  
  i=0
  if lockdown==1:
     w=sorted(w,reverse=jab)
     t=sorted(t,reverse=jab)
     m=sorted(m,reverse=jab)
     ov=sorted(ov,reverse=jab)
     on=sorted(on,reverse=jab)
     ff=sorted(ff,reverse=jab)
     p=sorted(p,reverse=jab)
     d=sorted(d,reverse=jab)
  if lockdown==3:
      w.sort(key=lambda datesor:datesor[5],reverse=jab)
      t.sort(key=lambda datesor:datesor[5],reverse=jab)
      m.sort(key=lambda datesor:datesor[5],reverse=jab)
      ov.sort(key=lambda datesor:datesor[5],reverse=jab)
      on.sort(key=lambda datesor:datesor[5],reverse=jab)
      ff.sort(key=lambda datesor:datesor[5],reverse=jab)
      p.sort(key=lambda datesor:datesor[5],reverse=jab)
      d.sort(key=lambda datesor:datesor[5],reverse=jab)
  if lockdown==2:
      w.sort(key=lambda datesor:datesor[4],reverse=jab)
      t.sort(key=lambda datesor:datesor[4],reverse=jab)
      m.sort(key=lambda datesor:datesor[4],reverse=jab)
      ov.sort(key=lambda datesor:datesor[4],reverse=jab)
      on.sort(key=lambda datesor:datesor[4],reverse=jab)
      ff.sort(key=lambda datesor:datesor[4],reverse=jab)
      p.sort(key=lambda datesor:datesor[4],reverse=jab)
      d.sort(key=lambda datesor:datesor[4],reverse=jab)
  if lockdown==4:
      w.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      t.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      m.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      ov.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      on.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      ff.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      p.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
      d.sort(key=lambda datesore:int(datesore[2]),reverse=jab)
             
      
  fl.append(["#$ᴡᴀᴛᴄʜɪɴɢ$#"])
  fl.append(w)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴠ$#"])
  fl.append(t)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴍᴏᴠɪᴇ$#"])
  fl.append(m)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏᴠᴀ$#"])
  fl.append(ov)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏɴᴀ$#"])
  fl.append(on)
  fl.append(["#$ᴄᴏᴍᴘʟᴇᴛᴇᴅ ꜱᴘᴇᴄɪᴀʟ$#"])
  fl.append(ff)
  fl.append(["#$ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ$#"])
  fl.append(p)
  fl.append(["#$ᴅʀᴏᴘᴘᴇᴅ$#"])
  fl.append(d)

  for i in fl:
      for m in i:
          chi.append(m)
  return chi
