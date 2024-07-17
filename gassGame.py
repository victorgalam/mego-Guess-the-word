import random
WORD_FILE = "words.txt"

def read_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words


def choose_word(words):
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def main():

    words = read_words(WORD_FILE)

    print("ברוכים הבאים למשחק ניחושי המילים!")


    player1 = input("שחקן 1, אנא בחר מספר מילה לנחש: ")
    player2 = input("שחקן 2, אנא בחר מספר מילה לנחש: ")


    word_to_guess = words[int(player1) % len(words)]

    print("\nמילה נבחרה! שחקן 2, עכשיו תתחילו לנחש.")

    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        print("\nניסיון מספר", 6 - attempts_left + 1)
        print("מילה עד כה:", display_word(word_to_guess, guessed_letters))

        guess = input("נחש אות או מילה: ").strip().lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("כבר ניחשת את האות הזו בעבר.")
            elif guess in word_to_guess:
                print("נכון! האות מופיעה במילה.")
                guessed_letters.append(guess)
            else:
                print("האות לא נמצאה במילה.")
                attempts_left -= 1
        else:
            if guess == word_to_guess:
                print("כל הכבוד! ניחשת את המילה הנכונה -", word_to_guess)
                break
            else:
                print("ניחשת שגוי. נסה שוב.")
                attempts_left -= 1

    if attempts_left == 0:
        print("נגמרו הניסיונות. המילה הייתה:", word_to_guess)


if __name__ == "__main__":
    main()
