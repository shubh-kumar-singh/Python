#  Name -> Shubh Kumar Singh
#  Branch -> CSE core 
#  Section -> "O"
#  PS No. -> 94
#  Project Title -> Shopping Cart System 


products = {
    "Pen":10,
    "Notebook":50,
    "Bag": 500
}

cart={}

def view_all_product():
    for i in products:
        print(f"{i} : Rs.{products[i]}")

def add():
    view_all_product()
    product = input("Enter Product Name:- ")
    if product in products:
        if product not in cart:
            cart[product]=0
        quantity = int(input("Enter Quantity:- "))
        if quantity<1:
            print("Minimum 1 quantity is allowed")
            return
        
        cart[product] += quantity
        
    else:
        print("Invalid Product!!!")
    

def remove():
    if len(cart)==0:
        print("Cart is empty!!!")
        return
    
    view_all_product()
    product = input("Enter product name to remove: ")
    
    if product in cart:
        del cart[product]
        print(f"{product} removed from cart. ")
    else:
        print("Product not found in cart")
    
   
def view_cart():
    subtotal = 0
    if not cart:
        print("Your cart is empty.")
        return
    for product, quantity in cart.items():
        price = products[product]
        total = price * quantity
        subtotal+=total
        print(f"{product} x {quantity} = Rs.{total}")

    print("-------------------------------------")
    print(f"Cart Subtotal: Rs.{subtotal}")
    
def checkout():
    if not cart:
        print("\nYour cart is empty. Add products first.")
        return

    subtotal = 0
    for product, quantity in cart.items():
        price = products[product]
        total = price * quantity
        subtotal += total
        
    discount = 0

    if subtotal > 500:
        discount = subtotal * 0.10

    amount = subtotal - discount
    gst = amount * 0.18

    grand_total = amount + gst

    print("\n========== FINAL BILL ==========")

    for product, quantity in cart.items():
        price = products[product]
        total = price * quantity
        subtotal+=total

        print(f"{product} x{quantity} = Rs.{total}")

    print("--------------------------------")
    print(f"Subtotal       : Rs.{subtotal:.2f}")
    print(f"Discount (10%) : Rs.{discount:.2f}")
    print(f"GST (18%)      : Rs.{gst:.2f}")
    print("--------------------------------")
    print(f"Grand Total    : Rs.{grand_total:.2f}")
    print("================================")

    print("Thank you for shopping!")

    cart.clear()



while True:
    print("\n========== SHOPPING CART SYSTEM ==========")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    print("==========================================")
    
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        view_all_product()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("Thank you for using Shopping Cart System!")
        break
    else:
        print("Invalid choice. Please select between 1 and 6.")    
