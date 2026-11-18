# Mood Guesser

A small Python program that guesses whether a sentence is Happy or Sad.

## Level 3: Testing
Accuracy on the 5 practice sentences: 100 %

1. Which sentence went wrong (or was closest to going wrong), and why?
   None went wrong. The closest was "Today was a great day". My word lists do not contain "great" or "today", so the program found no clue word and the tie rule (Happy) gave the right answer by luck.
2. One change that would make my program better:
   Add more clue words, or let the program learn the words from examples instead of me choosing them.

## Learning questions
1. Total score of "good party today" and its mood: good (+2) + party (+1) + today (0, never seen) = +3, so Happy.
2. Total score of "bad exam day" and its mood: bad (-2) + exam (0) + day (-1) = -3, so Sad.
3. Why did "exam" get a score of 0, and is that good or bad?
   It appeared once in a Happy sentence and once in a Sad sentence, so +1 and -1 cancel out. This is mostly good, because "exam" does not tell us the mood by itself. But with so little data it may just be luck.
4. Why is "not good" labelled Happy by this method, and how could it be fixed?
   The method scores each word alone: "not" is unseen (0) and "good" is +2, so the total is +2. It ignores that "not" reverses the meaning. A fix: when "not" comes before a word, flip that word's score, or learn two-word pairs like "not good".

## AI declaration
I used an AI tool: yes / no,
If yes, what I asked it: I asked it how to use Github, how to create a repository, how to create a readme, Since I've never learnt python it helped me with learning basic codes ,how use basic code language and logic for this kind of code
questions.I used ChatGPT as a learning assistant to understand how to use GitHub, create repositories, and write README files. Since I had no prior experience with Python, it helped me learn basic Python syntax, coding concepts, functions, 
loops, and programming logic. I also used it to understand code, identify errors, debug problems, and learn how to correct them step by step.

## Reflection
What was hardest, and what I learned that I did not know before:
The hardest part was understanding Python syntax, programming logic, and fixing errors in my code because I was new to programming. I learned how to use functions, loops, variables, and conditions. I also learned how to create a GitHub
repository, write a README file, and use GitHub to manage my project. This experience helped me improve my problem-solving skills and gain confidence in coding.
