# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---When you clicked to start a new game it would not let me. 
The game hinted for me to go lower when I entered in 15 despite the answer being 35. 
I picked 99 and the hint prompted me to go higher so I picked 100 and it prompted me to go lower.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used chatgpt. I accepted the AI suggestion of installing streamlit properly as i was confused on why my code was not updating in the website. ChatGPT suggested my streamlit was not working
I rejected one of the tests that was suggested as I felt it was unncessary 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I was able to decide if a bug was really fixed by doing a test or trying the game myself a few times to ensure it was working correctly. 
I ran the pytest cases test_hint_too_high and test_hint_too_low, which check that the hints displayed by the game match the secret number. For example, if the secret is 50 and the guess is 60, the outcome should be "Too High" and the hint message should include "LOWER"
Yes, AI helped me structure the tests by suggesting how to unpack the tuple returned from check_guess and how to assert not just the outcome, but also that6 the hint message contained the correct instruction (“HIGHER” or “LOWER”)
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- The code was sometimes converting the secret number to a string on alternating attempts
I decided to always keep the secret numeric, set attempts at 0 instead of 1 and fully reset state on a new game.
I would explain it to a friend by saying streamlit reruns the entire python script from top to bottom whenever you interact wit the app. st.session_state was important as its basically the memory for the app that stores values like the secret number. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

## I want to continue using targeted testing and small iterative fixes. 

Next time I would ask more focused step by step questions and be much more detailed and specific so its more effective and efficient. prompt enginerring is important

this project showed me that AI- generated code can be a powerful assistant but it requires careful review and testing....
