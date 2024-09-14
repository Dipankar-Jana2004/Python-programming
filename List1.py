# Question 1: Create a list named fruits containing the following elements: "apple", "banana", "orange", "grape", "mango".
# Question 2: Access and print the third element of the fruits list.
# Question 3: Add the element "kiwi" to the end of the fruits list.
# Question 4: Remove the first element from the fruits list.
# Question 5: Find and print the index of the element "grape" in the fruits list.

# def fruit_container():
#     fruit_names=["apple","banana","orange","grape","mango"]
#     print(fruit_names[2])    
#     fruit_names.append("kiwi")
#     print(fruit_names)
#     fruit_names.remove("apple")
#     print(fruit_names)
#     if 'grape' in fruit_names:
#         print("grape is founded in fruit list.")
#         index_of_grape=fruit_names.index("grape")
#         print("The grape is founded at index no:",index_of_grape)
#     else:
#         print("grape is founded in fruit list.")
# fruit_container()
# 2. List Slicing and Manipulation:
# Question 6: Create a new list called numbers containing the numbers from 1 to 10.
# Question 7: Create a new list called even_numbers containing only the even numbers from the numbers list.
# Question 8: Reverse the order of elements in the numbers list.
# Question 9: Create a new list called numbers_squared containing the squares of each number in the numbers list.
# Question 10: Create a new list called numbers_reversed containing the elements of the numbers list in reverse order, but using slicing.

def slicing_and_manipulation():
    def number_containing():
        numbers = list(range(1, 11))
        return numbers  

    def even_num(numbers):
        num = [num for num in numbers if num % 2 == 0]
        print("Even numbers:", num)
    
    def reverse_list(numbers):
        reversed_numbers = numbers[::-1]
        print("Reversed numbers:", reversed_numbers)

    def squared_containing(numbers):
        square_numbers=[num**2 for num in numbers]
        return square_numbers 

    def number_reversed(square_numbers):
        reversed_order=square_numbers[::-1]
        print("Reversed order is:",reversed_order)
    numbers=number_containing()
    print("numbers:",numbers)

    even_num(numbers)
    reverse_list(numbers)
    square_numbers=squared_containing(numbers)
    number_reversed(square_numbers)
slicing_and_manipulation()


