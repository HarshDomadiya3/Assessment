def select_role():
    print("WELCOME TO FRUIT MARKET")
    print("1) Manager")
    print("2) Customer")
    
    role_choice=int(input("Select your Role (1 or 2):"))
    fruit_stock={}
    if role_choice == 1:
        def fruit_market_manager():
            while True:
                print("\nFruit Market Manager")
                print("1) Add Fruit Stock")
                print("2) View Fruit Stock")
                print("3) Update Fruit Stock")
        
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    def add_fruit_stock():
                        fruit_name = input("Enter fruit Name: ")
                        qty = float(input("Enter qty (in kg): "))
                        price = float(input("Enter price (for kg): "))
                        if fruit_name in fruit_stock:
                            fruit_stock[fruit_name]['qty'] += qty
                            fruit_stock[fruit_name]['price'] = price
                        else:
                            fruit_stock[fruit_name] = {'qty': qty, 'price': price}
                        print(f"{fruit_name}added/updated in the stock.")
                    add_fruit_stock()
                elif choice == 2:
                    def view_fruit_stock():
                        print("\nCurrent Fruit Stock:")
                        print(fruit_stock) 
                        print()
                    view_fruit_stock()
                elif choice == 3:
                    def update_fruit_stock():
                        fruit_name = input("Enter the fruit name to update: ")
                        if fruit_name in fruit_stock:
                            qty = float(input(f"Enter the new qty (current: {fruit_stock[fruit_name]['qty']} kg): "))
                            price = float(input(f"Enter the new price (current: {fruit_stock[fruit_name]['price']} per kg): "))
                            fruit_stock[fruit_name]['qty'] = qty
                            fruit_stock[fruit_name]['price'] = price
                            print(f"{fruit_name} has been updated in the stock.")
                        else:
                            print(f"{fruit_name} does not exist in the stock.")
                    update_fruit_stock()
                else:
                    print("Invalid choice. Please try again.")
                more_operations = input("Do you want to perform more operations (press y for yes and n for no): ").lower()
                if more_operations != "y":
                        break
        fruit_market_manager()
    else:
        print("...")
select_role()                    


