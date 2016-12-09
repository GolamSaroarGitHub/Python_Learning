from string import Template

def Main():
    cart=[]
    cart.append(dict(item="Coke",qty=2,price=8))
    cart.append(dict(item="Cake",qty=4,price=20))
    cart.append(dict(item="Fish",qty=8,price=48))

    t=Template("$qty x $item = $price")
    total=0
    print("Cart:")

    for data in cart:
        print(t.substitute(data))
        total+=data["price"]

    print("Total Price : "+str(total))

if __name__=='__main__':
    Main()