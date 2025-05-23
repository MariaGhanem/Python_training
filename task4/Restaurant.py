from MenuItem import MenuItem
from Order import Order
class  Restaurant:
    def __init__(self):
        self.menu_items = []
        self.orders = []
        
    def menu(self):
        print("\nWelcome to the Restaurant Management System!")
        print("Choose an option:")
        print("1. Add menu item")
        print("2. View menu")
        print("3. Create new order")
        print("4. List all orders")
        print("5. Exit")
        
    def run(self):
        while True:
            self.menu()
            choice= input("Enter your choice:\n")
            if choice == "1":
                name= input("Enter item name:\n")
                price= float(input("Enter item price:\n"))
                category= input("Enter item category:\n")
                item= MenuItem(name,price,category)
                self.menu_items.append(item)
                print("Menu item added successfully.")
            elif choice =="2":
                if self.menu_items:
                    i=1
                    for m in self.menu_items:
                        print(f"{i}. {m.name} (${m.price}) [{m.category}]")
                        i+=1
                else:
                    print('There is No Item to Display')
                    
            elif choice=="3":
                ord=input("Enter item numbers for the order separated by commas\n")
                order=Order()
                index=ord.split(",")
                for i in index: 
                    if int(i):
                        j = int(i)
                        order.add_item(self.menu_items[j-1])  
                    else:
                        print("please just enter a numbers")
                        break
                self.orders.append(order)
                print("Order created and added successfully.")
                
            elif choice== "4":
                i=1
                order_total =0
                print("Orders:\n")
                for o in self.orders:
                    print(f"Order {i}:")
                    for item in o.items:
                        print(f"- {item.name} (${item.price})")
                    order_total = o.total() 
                    print(f"Order Total: ${order_total}")
                    i += 1
                
                
            elif choice == "5":
                print("Thank you for using the Restaurant Management System!")
                break
            
            else:
                print("plese select a correct choice")
                
            
if __name__ == "__main__":
    restaurant=Restaurant()
    restaurant.run()