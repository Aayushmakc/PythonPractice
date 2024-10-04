
def main():
  try:
    a=int(input("Enter a number:"))
    print(a)
    return #return means function is returned the code below it doesnt work!!!!!!!! here if we use finally the code the function works even if we use return

  except Exception as e:
    print(e)
    return

  finally: # The use of finally is in function
    print("I am inside the finally")

main()