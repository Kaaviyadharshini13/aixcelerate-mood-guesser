#AIXcelerate Task 1 - Mood Guesser (Happy or Sad)

train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]


# ---------- Level 1: Count the moods ----------
def count_moods(data):
    happy_count = 0
    sad_count = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy_count = happy_count + 1
        elif mood == "Sad":
            sad_count = sad_count + 1
    return happy_count, sad_count


print("Level 1:", count_moods(train_data))
print()

#---------- Level 2: Guess the mood ----------
# Each list has exactly 5 words (my roll number's last digit is 5)
happy_words = ["won", "surprise", "excited", "favourite", "tasty"]
sad_words = ["upset", "lost", "failed", "missed", "lonely"]


def clean_words(sentence):
    # make small letters and remove punctuation, then split into words
    sentence = sentence.lower()
    clean = ""
    for ch in sentence:
        if ch.isalpha() or ch == " ":
            clean = clean + ch
    return clean.split()


def guess_mood(sentence):
    happy_score = 0
    sad_score = 0
    for word in clean_words(sentence):
        if word in happy_words:
            happy_score = happy_score + 1
        if word in sad_words:
            sad_score = sad_score + 1

    if happy_score > sad_score:
        return "Happy"
    elif sad_score > happy_score:
        return "Sad"
    else:
        # Tie (or no clue word found): I choose Happy because train_data
        # has more Happy sentences (8) than Sad (7), so Happy is the safer guess.
        return "Happy"


print("Level 2: guess_mood examples")
print("I lost my phone on the bus ->", guess_mood("I lost my phone on the bus"))
print("We won the match! ->", guess_mood("We won the match!"))
print()



# ---------- Level 3: Test the program ----------
def test_program(data):
    correct = 0
    for sentence, real_mood in data:
        answer = guess_mood(sentence)
        print(sentence, "->", answer, "(real:", real_mood + ")")
        if answer == real_mood:
            correct = correct + 1
    return correct / len(data) * 100


print("Level 3: testing guess_mood")
accuracy = test_program(practice_data)
print("Accuracy:", accuracy, "%")
print()


# ---------- Bonus: learn the scores from examples ----------
def learn_scores(data):
    scores = {}
    for sentence, mood in data:
        # set() so a word is counted once per sentence
        for word in set(clean_words(sentence)):
            if word not in scores:
                scores[word] = 0
            if mood == "Happy":
                scores[word] = scores[word] + 1
            else:
                scores[word] = scores[word] - 1
    return scores


learned_scores = learn_scores(train_data)


def guess_mood_learned(sentence):
    total = 0
    for word in clean_words(sentence):
        if word in learned_scores:
            total = total + learned_scores[word]
    # unseen words score 0; positive total = Happy, otherwise Sad
    if total > 0:
        return "Happy"
    else:
        return "Sad"


def test_learned(data):
    correct = 0
    for sentence, real_mood in data:
        answer = guess_mood_learned(sentence)
        print(sentence, "->", answer, "(real:", real_mood + ")")
        if answer == real_mood:
            correct = correct + 1
    return correct / len(data) * 100


print("Bonus: testing guess_mood_learned")
learned_accuracy = test_learned(practice_data)
print("Accuracy:", learned_accuracy, "%")








