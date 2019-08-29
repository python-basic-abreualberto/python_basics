def ask_user_difficulty_level(dict):
    difficulty_level = input("Choose the difficult level (easy, medium or hard) for the game: \n").lower()

    if difficulty_level not in dict.keys():
        print("\n FATAL ERROR: Your response must be 'easy', 'medium' or 'hard'. \n")
        sys.exit()

    else:
        return dict[difficulty_level]