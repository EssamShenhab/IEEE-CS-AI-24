while True:
    num = input("Enter a numeric value: ")
    try:
        numeric_value = float(num)
        break
    except ValueError:
        print("Error: Only numeric values allowed")
print(f"You entered: {numeric_value}")
