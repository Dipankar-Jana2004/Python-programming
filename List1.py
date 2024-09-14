# Question 1: Create a list named fruits containing the following elements: "apple", "banana", "orange", "grape", "mango".
# Question 2: Access and print the third element of the fruits list.
# Question 3: Add the element "kiwi" to the end of the fruits list.
# Question 4: Remove the first element from the fruits list.
# Question 5: Find and print the index of the element "grape" in the fruits list.

def fruit_container():
    fruit_names=["apple","banana","orange","grape","mango"]
    print(fruit_names[2])    
    fruit_names.append("kiwi")
    print(fruit_names)
    fruit_names.remove("apple")
    print(fruit_names)
    if 'grape' in fruit_names:
        print("grape is founded in fruit list.")
        index_of_grape=fruit_names.index("grape")
        print("The grape is founded at index no:",index_of_grape)
    else:
        print("grape is founded in fruit list.")
fruit_container()