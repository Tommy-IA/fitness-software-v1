# Fitness Software V1.0

Fitness Software V1.0 is a beginner-focused Python tool designed to provide a simple and structured starting point for workout planning.
The software collects basic user information such as training goal, experience level, weekly availability, and muscle focus, then generates a recommended workout split along with general guidance on training volume, frequency, and exercise priority, all based from a deep science research on fitness approach.

## Project Goal

The goal of this project is to turn beginner fitness confusion into a clear and practical training direction.

Many gym beginners do not know:
- how often to train
- which split to follow
- how to organize training based on their goal
- how to prioritize a weak muscle group

This software was built to solve that problem with a simple logic-based recommendation system.

## Main Features

- User input system with validation
- Workout split recommendation based on weekly availability and muscle focus
- Goal-based training approach modifier
- Experience-based training recommendation
- Priority exercise suggestion based on selected muscle focus
- Final structured report output

## User Inputs

The software currently asks for:

- **Training Goal**
  - Hypertrophy
  - Fat Loss / Definition
  - Strength

- **Experience Level**
  - Beginner (0–1 year)
  - Intermediate (1–3 years)
  - Advanced (3+ years)

- **Weekly Availability**
  - 2 training days per week
  - 3 training days per week
  - 4 training days per week

- **Muscle Focus**
  - Chest
  - Back
  - Quads and Ham
  - Glutes
  - None

## Core Logic

The software uses decision rules to:

1. interpret the user profile
2. recommend a compatible workout split
3. adjust the plan based on the selected goal
4. provide a direction for training volume, frequency, and exercise emphasis

For example:
- **2 training days** → simpler split options
- **3–4 training days** → more balanced split structures
- **Fat loss / definition** → integration of LISS cardio suggestions
- **Muscle focus selected** → priority exercise emphasis

## Example Output

A user may receive:
- a recommended split
- a goal-specific training approach
- an experience-based recommendation
- a priority exercise direction for the selected weak point

## Technologies Used

- Python
- Dictionaries
- Functions
- Conditional logic
- Input validation
- Console formatting

## Current Version

This is **Version 1.0**, which focuses on workout structure and recommendation logic.

## Future Improvements 
### V2.0
- muscle-specific weekly volume guidance
- athlete name input
- training tips
- body weight and body measurements tracking

### V3.0
- manual workout logging (exercise, sets, reps, load)
- weekly set tally
- PR tracking
- baseline logging with dat, time, muscle group and notes
- local JSON-based history and progress comparison
- indexed training weeks for easier progress review

### V3.5
- screenshot parsing
- OCR / computer vision integraation
- semi-automated workout data extraction

## Author

**Tommaso Marras**
[GitHub](https://github.com/Tommy-IA) · [LinkedIn](https://www.linkedin.com/in/tommaso-marras-a681252ba)  


