import xml.etree.ElementTree as ET
def malsyncup(xmlfile,existinglist):
      try:
         tree = ET.parse(xmlfile)

         root = tree.getroot()
         
         for anim in root.findall('anime'):
        
             k = [anim.find('series_title').text, anim.find('series_type').text, anim.find('my_score').text, anim.find(
                 'my_status').text, anim.find('my_start_date').text, anim.find('my_finish_date').text]
             if k not in existinglist:
                 existinglist.append([anim.find('series_title').text, anim.find('series_type').text, anim.find('my_score').text, anim.find('my_status').text, anim.find('my_start_date').text,anim.find('my_finish_date').text])
        
                
        
         return None                 
      except Exception as js: 
          if str(type(js)) == "<class 'xml.etree.ElementTree.ParseError'>":
                     print("THERE IS AN ERROR IN THE SYNTAX!!!!!!!!!!\n\nNote :Try downloading the xml file again from mal..")
          else:
                 print("UNEXPECTED ERROR :",str(js).upper())
          print("\n")
          return "Err"
