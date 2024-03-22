str1 = input("Enter elements for the set (separated by spaces or commas): ")
list1 = str1.replace(",", " ").split()
set1 = set(list1)

str2 = input("Enter elements for the set (separated by spaces or commas): ")
list2 = str2.replace(",", " ").split()
set2 = set(list2)

commom_elements = set1 & set2
print(commom_elements)
