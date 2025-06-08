import random

# A small list of words to guess from
word_list = ["apple", "tiger", "house", "music", "river"]


word = random.choice(word_list)
word_letters = list(word)  
guessed_letters = []       
attempts = 6               

print("🎮 Welcome to Hangman!")
print("Try to guess the word, one letter at a time.")
print("_ " * len(word))  # Initial blank display


while attempts > 0:
    guess = input("\nEnter a letter: ").lower()


    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetical letter.")
        continue

    
    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue
      
    guessed_letters.append(guess)

  
    if guess in word_letters:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess. You have {attempts} attempts left.")

    
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Current word:", " ".join(display_word))

    
    if "_" not in display_word:
        print(f"\n🎉 Congrats! You guessed the word: {word}")
        break


else:
    print(f"\n😞 Game over. The correct word was: {word}")
