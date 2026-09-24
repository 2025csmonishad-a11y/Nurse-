import staff
import technician_ui
import technician

while(1):
      def enter():
          student={}
          name=input("name:")
          password=(input("password:"))
          if name and password not in student.values():
                 student["name"]=name
                 student["password"]=password
          return student
      def tech():
           tech={}
           name=input("name:")
           password=(input("password:"))
           phone=(input("enter phone no:"))
           techcat=input("1.equiment maintainer\n2.maintanance\n3.IT\nenter one:")
           if name and password not in tech.values():
                  tech["name"]=name
                  tech["password"]=password
                  tech["techcat"]=techcat
                  tech["phone_no"]=phone
           return tech
      def staf():
           tech={}
           name=input("name:")
           password=(input("password:"))
           phoneno=(input("enter phone no:"))
           dept=input("")
           if name and password not in tech.values():
                  tech["name"]=name
                  tech["password"]=password
                  tech["dept"]=dept
                  tech["phone_no"]=phoneno
           return tech

      print("1.signup\n2.signin")
      choice=int(input("enter choice:"))
      print("\r")
      if choice==1:
            print("1.staff\n2.technician")
            choice2=int(input("enter :"))
            print("\r")
            if choice2==1:
                  a=staf()
                  staff.add(a)
            elif choice2==2:
                  print(choice)
                  b=tech()
                  technician.add(b)
                  technician_ui.display(b["techcat"])
      elif choice==2:
            print("1.staff\n2.technician")
            choice3=int(input("enter:"))
            print("\r")
            if choice3==1:
                c=enter()
                d=staff.staff_get(c["name"],c["password"])
                if d==[]:
                    print("invalid name or password")
                else:
                    print("signed")
            elif choice3==2:
                tech=enter()
                tech1=technician.technician_get(tech["name"],tech["password"])
                if tech1==[]:
                    print("invalid name or password")
                else:
                    print("signed")
                    print(tech1)
                    technician_ui.display(tech1[0]["techcat"])
