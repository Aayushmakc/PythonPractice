try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except ValueError as v:
    print("heyyyy")
    print(v)
# You can uncomment the below line if you want to handle other exceptions
# except Exception as e:
#     print(e)

print("Thank you!!!")
