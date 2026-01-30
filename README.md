A Basic Rule-Based Chatbot
#A rule-based chatbot built with Python

#Features:
- Respond to greetings('hello', 'hi').
- Tells the current "Time" and "Date".
- says farewell ('bye', 'goodbye').
- Provides a default responses for unknown inputs.
- Explains what is it ('who are you', 'what are you').

  ##How it works:
  - User input is converted to lowercase for easier matching.
  - The chatbot checks for the keywords(hello, time, date etc.).
  - Based on the keyword, it returns a predefined response.
  - If no keyword matches, it returns a default fallback message.
 
  ##Concept used:
  - Python function [chatbot(user_input)].
  - String Manipulation [user_input.lower().strip()].
  - Conditional Statements (if-elif-else).
  - Keyword matching.
  - Datetime Module.
  - Return statements.
