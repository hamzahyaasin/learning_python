def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        return "Division by zero is not allowed"