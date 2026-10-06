class Shopping_cart:
    def __init__(self,items):
        self.ite=items
    def add_items(self):
        it=input('Enter items:')
        quantity=int(input('Enter quantity:'))
        if it in self.ite:
            self.ite[it]['quantity']+=quantity
        else:
            pri=int(input('Enter price:'))
            self.ite[it]={'price':pri,'quantity':quantity}
        return self.ite
    def remove_items(self):
        remove=input('Enter item to be removed :')
        if remove in self.ite:
                del self.ite[remove]
        return self.ite
    def Total_price(self):
        price=0
        for key,value in self.ite.items():
            price+=value['price']*value['quantity']
        return price
    def discount(self):
        total=self.Total_price()
        if total>500:
            discount=self.price*0.1
            return discount
        else:
            return'No discount'
              
sc1=Shopping_cart({'Pen':{'price':20,'quantity':2},'Pencil':{'price':10,'quantity':1},'Copy':{'price':100,'quantity':4}})
print(sc1.discount())