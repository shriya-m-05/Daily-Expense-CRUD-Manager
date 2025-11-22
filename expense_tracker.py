def main():

    #Get user input
    user_input()

    #Expense to a file
    expense_file()

    #Summarize expense
    summarize_expense()
    
    pass

def user_input():
    name_expense = input("Enter name of expense - ")
    amount_expense = float(input("Enter amount of expense - "))

    category_expense = ['Needs', 'Wants']
    sub_category_need = ['Food','Home','Learn']
    sub_category_want = ['Enetrtainment','Shopping','Others']

    print("Enter category based on number given : ")
   
    while True:
        for i, category_name in enumerate(category_expense):
            print(f"{i+1}. {category_name} ")
        
        range_category = f"[1 - {len(category_expense)}]"
        try:
            choice = int(input("Enter category number from {range_category} - "))-1

        except Exception:
            pass

        if choice in range(len(category_expense)):
            if choice == 0 :
                for j, sub_category_name in enumerate(sub_category_need):
                    print(f"{j+1}.{sub_category_name}")

            else :
                for j, sub_category_name in enumerate(sub_category_want):
                    print(f"{j+1}.{sub_category_name}")

            break

        else:
            print("Invalid. Enter again.")
            
        

def expense_file():
    pass

def summarize_expense():
    pass

if __name__ == "__main__": #to ensure that the this method runs only in this file
    main()