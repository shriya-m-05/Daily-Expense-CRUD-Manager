from expense import Expense

def main():

    file_path_expense = "expense.csv"
    #Get user input
    expense = user_input()

    #Expense to a file
    expense_file(expense, file_path_expense)

    #Summarize expense
    summarize_expense(file_path_expense)

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
            category_choice = category_expense[choice]
            if choice == 0 :
                for j, sub_category_name in enumerate(sub_category_need):
                    print(f"{j+1}.{sub_category_name}")

                range_subcategory = f"[1 - {len(sub_category_need)}]"
                sub_choice = int(input("Enter category number from {range_subcategory} - "))-1
                sub_category_choice = sub_category_need[sub_choice]

            else :
                for j, sub_category_name in enumerate(sub_category_want):
                    print(f"{j+1}.{sub_category_name}")

                range_subcategory = f"[1 - {len(sub_category_want)}]"
                sub_choice = int(input("Enter category number from {range_subcategory} - "))-1
                sub_category_choice = sub_category_want[sub_choice]
   

            new_expense = Expense(name=name_expense, category = category_choice,sub_category=sub_category_choice,amount = amount_expense)
            return new_expense

        else:
            print("Invalid. Enter again.")
            
        

def expense_file(expense : Expense ,file_path_expense):
    print("Saving User Expense : {expense} to {file_path_expense}")

    with open (file_path_expense, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.sub_category}\n")

def summarize_expense(file_path_expense):
    print("Summary of Expense")
    with open(file_path_expense, "r") as f:
        lines = f.readlines()

        for line in lines:
            print(line)
    
    

if __name__ == "__main__":
    main() #to ensure that the this method runs only in this file
    main()