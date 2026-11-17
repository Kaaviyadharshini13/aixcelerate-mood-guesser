#AIXcelerate - Mood Guesser Project

#Training dataset 
train_data = [
  ("I got full marks in the test today!", "Happy"),
  ("We won the college cricket match", "Happy"),
  ("My friends planned a surprise party for me", "Happy"),
  ("The food in the canteen was really tasty", "Happy"),
  ("I am so excited for the weekend trip", "Happy"),
  ("Our project got selected for the exibition", "Happy"),
  ("I finally learnt how to ride a bicycle", "Happy"),
  ("Mom made my favourite sweets today", "Happy"),
  ("I lost my phone on the bus", "Sad"),
  ("I failed in mathematics exam", "Sad"),
  ("My best friend is moving to another city", "Sad"),
  ("It rained and our picnic was cancelled", "Sad"),
  ("I missed the last bus and felt very upset", "Sad"),
  ("My laptop stopped working before the submission", "Sad"),
  ("I felt lonely during the long holidays", "Sad")
]

#Level 1: Count Happy and Sad sentences
def count_moods(data):
  happy = 0
  sad = 0

for sentence, mood in data:
  if mood == "Happy":
     happy += 1
  elif mood == "Sad":
     sad += 1

return happy, sad


#Display the counts
result = count_moods(train_data)
print("Happy sentences:", result[0])
print("Sad sentences:", result[1])
