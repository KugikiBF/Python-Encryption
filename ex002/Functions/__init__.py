def add_expense(amount,category,lists):
    lists.append({'amount':amount,'category':category})
    
def total_expense(lists):
    return(sum(map(lambda expense:expense['amount'], lists)))

def show_expenses(lists):
    for expense in lists:
        print(f"Amount: R${expense["amount"]}  Category: {expense["category"]}")   

def filter_category(category, lists):
    return (filter(lambda search: search['category']==category,lists))

def large(width=30):
    return print("-"*width)

def title(text):
    large()
    print(text.upper().center(30))
    large()

def main():
    from time import sleep
    expenses=[]
    while True:
        title('Expense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        large()
        while True:
            try:
                choice=int(input("Make your choice: "))
                break
            except:
                print("Error: Invalid Type.")
        if choice == 1:
            title("add expense")
            amount=float(input("Enter amount: "))
            category=input("Enter category:\033[34m \033[m").capitalize()
            add_expense(amount,category,expenses)
            sleep(0.3)
        elif choice == 2:
            title("All expenses")
            show_expenses(expenses)
            sleep(1)
        elif choice == 3:
            title("Total:")
            print(f"Total Expenses: {total_expense(expenses)}")
            sleep(1)
        elif choice == 4:
            title("category filter")
            category=input("Enter category to search: ").capitalize()
            print()
            print(f"{category} expenses find:")
            print()
            filtered_expenses=filter_category(category,expenses)
            show_expenses(filtered_expenses) 
            sleep(1.5)   
        elif choice == 5:
            title("Leaving...")
            sleep(0.6)
            break
        else:
            print("Error: Choice Out of range!")
            sleep(1.5)
