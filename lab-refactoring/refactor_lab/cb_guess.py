def codebreaker_guess(lst_color):
    print('\nThe game color options are: red, yellow, blue, green, pink and purple.\n')

    user_code_choice = input("Enter four colors separated by a SINGLE SPACE: \n").upper()
    user_choice = user_code_choice.split()

    while any(item not in lst_color for item in user_choice) == True or len(user_choice) != 4:
        user_code_choice = input("Try again: Enter four colors from the list separated by a SINGLE SPACE: \n").upper()
        user_choice = user_code_choice.split()

    return user_choice