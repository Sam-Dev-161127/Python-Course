# LOOPING THROUGH A LIST USING WHILE LOOP

# A list with mixed elements (names and numbers as strings)
my_list = ["Sameer", "Abinash", "Chirkut", "1611", "278", "70707", "Thala"]

# Initialize index
i = 0

# Loop through the list
while i < len(my_list):  # Keep looping until i reaches the length of the list

    # Check if the element is numeric
    if my_list[i].isdigit():
        # Convert numeric string to integer and print
        print(int(my_list[i]))
    else:
        # Print the element as is (it's a name)
        print(my_list[i])
    
    # Increment index to move to the next element
    i += 1

'''
Output:
Sameer
Abinash
Chirkut
1611
278
70707
Thala
'''

# Explanation:
# 1. We start with i = 0, which points to the first element of the list.
# 2. The loop checks if i < len(my_list). Since the list has 7 elements, the loop will run while i is less than 7.
# 3. Inside the loop, we check if the current element (my_list[i]) is a digit using the isdigit() method. If it is, we convert it to an integer and print it. Otherwise, we print the element as a name.
# 4. After processing the current element, we increment i by 1 to move to the next element in the list.
# 5. This process continues until i reaches 7, at which point the loop condition (i < len(my_list)) becomes False and the loop stops.
# 6. The output shows the names as they are and the numeric strings converted to integers.

# Notes:
# - The while loop continues to execute as long as the condition (i < len(my_list)) is True. Once i becomes equal to the length of the list, the condition becomes False and the loop stops.
# - The isdigit() method checks if the string consists only of digits, which helps us determine if we should convert it to an integer or print it as a name.
# - Always remember to increment the index (i += 1) to avoid creating an infinite loop. If you forget to increment i, the condition will always be True and the loop will run forever.
# - This method of looping through a list using a while loop is less common than using a for loop, but it can be useful in certain situations where you need more control over the index or when you want to modify the list while iterating.