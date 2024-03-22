import Functions

numbers = Functions.get_numbers()
print(f"Min: {Functions.find_min(numbers)}")
print(f"Max: {Functions.find_max(numbers)}")
print(f"Mean: {Functions.find_mean(numbers)}")
print(f"Mode: {Functions.find_mode(numbers)}")
print(f"Median: {Functions.find_median(numbers)}")
print(f"Range: {Functions.find_range(numbers)}")
print(f"Variance: {Functions.find_variance(numbers)}")
print(f"Standard Deviation: {Functions.find_STD(numbers)}")
print(f"Quartiles: {Functions.find_Quariles(numbers)}")
print(f"Interquartile Range (IQR): {Functions.find_IQR(numbers)}")
