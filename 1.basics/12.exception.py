try:
    number = 5
    # devided = 0
    devided= "pizza"
    result = number / devided
except ZeroDivisionError as e:
    print(e)
    print("can't devide by zero")
except ValueError as e:
    print(e)
    print("enter number please")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("finished")