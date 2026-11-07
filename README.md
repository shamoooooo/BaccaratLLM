# BaccaratLLM
Baccarat Simulator with OpenAI API integration
This project is a Python-based baccarat simulator that integrates a Large-Language Model through the OpenAI API to analyze historical game results and generate predictions for subsequent hands.

The project simulates baccarat outcomes, manages a players bankroll, and records results in a text file. Before each new hand, the program retrieves previously recorded results and sends them to a LLM for predictive analysis. 

The project was developed to practice Python fundamentals, file handling, and integrating external APIs into an interactive application.

How It Works:
-The user launches the program and enters an initial virtual bankroll.

-The user selects a wager amount and chooses Player or Banker.

-The program reads historical outcomes stored in Bacarrat_Results.txt.

-The historical data is submitted to the OpenAI API for analysis.

-The LLM generates a prediction, which is displayed before the simulated hand.

-Randomized Player and Banker scores determine the actual result.

-The application updates the player's bankroll and records the outcome for future analysis.
