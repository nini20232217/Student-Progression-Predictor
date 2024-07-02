# Student Progression Predictor

This Python program allows students to predict their progression outcome at the end of each academic year. The program prompts for the number of credits at pass, defer, and fail, then displays the appropriate progression outcome for an individual student.

## Features

- Predict progression outcomes: progress, trailing, module retriever, or exclude
- Input validation for correct data types and ranges
- Loop to allow multiple predictions
- Histogram representation of outcomes using `graphics.py`
- Save and load progression data from a text file

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nini20232217/Student-Progression-Predictor.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Student-Progression-Predictor
    ```

## Usage

1. Run the program:
    ```bash
    python Student-Progression_Predictor.py
    ```
2. Follow the prompts to enter the credits at pass, defer, and fail.
3. Enter 'y' to continue or 'q' to quit and view results.

## Example

```text
Enter your credits at pass: 120
Enter your credits at defer: 0
Enter your credits at fail: 0
Progress
Enter 'y' for yes or 'q' to quit and view results: y
Enter your credits at pass: 100
Enter your credits at defer: 0
Enter your credits at fail: 20
Progress (module trailer)
Enter 'y' for yes or 'q' to quit and view results: q

