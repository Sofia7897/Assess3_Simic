"""
Upper and Lower
"""


# Provide your solution here

def count_upper_lower(words: str):
    words = words.strip(" ")
    upper = 0
    lower = 0

    for i in words:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    print(f"Number of Upper case characters: {upper} \nNumber of Lower case characters: {lower}")


"""
Check 33
"""


# Provide your solution here

def has_33(numbers: [int]) -> bool:
    a = len(numbers) - 1
    while a != 0:
        if numbers[a] == 3 and numbers[a - 1] == 3:
            return True
        a -= 1
    return False








if __name__ == '__main__':
    while True:
        text = input("If you'd like to stop the counting of upper and lower, write \"done\". \nPlease write me a Text: ")
        if text == "done":
            break
        count_upper_lower(text)

    list1 = [1, 3, 3]
    list2 = [1, 3, 1, 3]
    list3 = [3, 1, 3]

    bool1 = has_33(list1)
    bool2 = has_33(list2)
    bool3 = has_33(list3)

    print(f"has_33({list1}) -> {bool1}")
    print(f"has_33({list2}) -> {bool2}")
    print(f"has_33({list3}) -> {bool3}")

    """
    Since I was done earlier, I tried to do it with the users input. 
    """
    my_list = []

    while True:
        number = input("Please write a number. Write \"done\" when you are done: ")
        if number == "done":
            break
        else:
            my_list.append(int(number))

    my_bool = has_33(my_list)
    print(f"has_33({my_list}) -> {my_bool}")

