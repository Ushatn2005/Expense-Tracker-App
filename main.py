from feature import search_by_amount,sort,add_data,delete_data,sum_amount

transaction = [
    {"date":"28-8-2024","amount":2500,"description":"dress"},
    {"date":"29-8-2024","amount":500,"description":"fruits"},
    {"date":"30-8-2024","amount":1000,"description":"ear pods"},
    {"date":"30-8-2024","amount":250000,"description":"laptop"},
    {"date":"30-8-2024","amount":3000,"description":"groceries"}
]

flag = True
while flag:
  print("1.add data")
  print("2.sorting data")
  print("3.searching data")
  print("4.delete data")
  print("5.display data")
  print("6.sum amount")
  print("7.exit")
  choice = int(input("enter your choice: "))
  if choice == 1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    transaction = add_data(transaction)
    print("-"*50)
  elif choice == 2:
    print("-"*50)
    print("sorting data")
    print("-"*50)
    transaction = sort(transaction)
    print("-"*50)
  elif choice == 3:
    print("-"*50)
    print("searching data")
    print("-"*50)
    transaction = search_by_amount(transaction,1000)
    print("-"*50)
  elif choice == 4:
    print("-"*50)
    print("deleting data")
    print("-"*50)
    transaction = delete_data(transaction)
    print("-"*50)
  elif choice == 5:
    print("-"*50)
    print("displaying data")
    print("-"*50)
    print(transaction)
  elif choice == 6:
    print("-"*50)
    print("sum of amount of a given year")
    print(sum_amount(transaction))
    print("-"*50)
  elif choice == 7:
    print("-"*50)
    print("exiting program")
    print("-"*50)
    flag = False
  else:
    print("invalid choice")
    print("-"*50)

