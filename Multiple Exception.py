try:
    num1 = int(input("enter the first num : "))
    num2 = int(input("Enter the second number : "))
    result = num1/num2
    print("result is : " , result)

except ZeroDivisionError :
    print("Division by zero is error !")
except ValueError :
    print("Please enter whole number value : ")
except:
    print("Wrong input")
else :
    print("No exception")
finally:
    print("Tihs will execute no matter what !")