def search_by_amount(transaction,target_amount):
    for transaction in transaction:
      if transaction["amount"] == target_amount:
        return transaction
    return "transaction not found."

def sort(transaction):
  n = len(transaction)
  for i in range(n):
    for j in range(0, n-1):
      if transaction[j]["amount"] > transaction[j+1]["amount"]:
        transaction[j], transaction[j+1] = transaction[j+1], transaction[j]
  return transaction

def add_data(transaction):
  date = input("enter date: ")
  amount = int(input("enter amount: "))
  description = input("enter description: ")
  transaction.append({"date":date,"amount":amount,"description":description})
  return transaction

def delete_data(transaction):
  date = input("enter date: ")
  amount = int(input("enter amount: "))
  description = input("enter description: ")
  transaction.remove({"date":date,"amount":amount,"description":description})
  return transaction

def sum_amount(transaction):
  sum = 0
  year = input("enter year: ")
  for transaction in transaction:
    if transaction['date'][5:] == year:
      sum += transaction['amount']
  return sum
