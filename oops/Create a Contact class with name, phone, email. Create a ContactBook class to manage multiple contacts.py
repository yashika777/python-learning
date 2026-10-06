class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
c1=Contact('Rajesh',367283758,'xx@gmail.com')
c2=Contact('Sutesh',327488429,'egw@gmail.com')
c3=Contact('Gajni',8578433548,'frf@gmail.com')
contacts=[c1,c2,c3]
class ContactBook:
    def __init__(self,contact):
        self.contact=contact
    def add(self):
        name=input('Enter your name:')
        phone=input("Enter your mobile number:")
        email=input('Enter you mail id:')
        c4=Contact(name,phone,email)
        self.contact.append(c4)
        return self.contact
    def remove(self):
        phone=int(input("Enter your mobile number:"))
        for c in self.contact:
            if c.phone==phone:
                self.contact.remove(c)
        return self.contact
    def edit(self):
        ent=input("do you want to change something yes/no:")
        if ent=='yes':
            wh=int(input('Which contact you want to change:'))
            if wh>=0 and wh<len(self.contact):
                c=self.contact[wh]
                ch=input('Enter what you want to edit name/phone/email:')
                if ch=='name':
                        c.name=input('enter changes')
                elif ch=='phone':
                        c.phone=int(input('Enter new number:'))
                elif ch=='email':
                        c.email=input('Enter new email')
                else:
                        return 'No such attribute'
            else:
                return 'no such contact'
        else:
            return"user don't want to edit"
cb1=ContactBook(contacts)
print(cb1.add())
print(cb1.remove())
print(cb1.edit())
