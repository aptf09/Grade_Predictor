#  Student Grade Predictor

A machine learning model that predicts a student's upcoming test grade based on lifestyle, academic, and personal factors.

## Built With
- Python
- Scikit-learn (Random Forest Regressor)
- Pandas

## Model Performance
- Mean Absolute Error: 4.15 marks (on a 0-100 scale)

## Features Used
Previous test score, sleep hours, hydration, diet quality, sports activity, revision hours per week, number of subjects taken, year of study, and tuition hours per week

## How It Works
1. Load the student dataset
2. Convert categorical variables (diet, sports, year of study) to numerical values
3. Split data into training and validation sets
4. Train a Random Forest Regressor on the training data
5. Evaluate model accuracy using Mean Absolute Error
6. Predict your own upcoming grade by inputting your personal stats

## How To Run
```bash
pip install pandas scikit-learn
python grade_predictor.py
```

## Example Prediction
Input your own stats in the `my_stats` section at the bottom of the code:
- `diet`: 2 = good, 1 = avg, 0 = poor
- `sports`: 2 = regular, 1 = occasional, 0 = none
- `year_of_study`: enter as a number e.g. 12 for Year 12

## Author
Aparajith Suresh — [LinkedIn](https://www.linkedin.com/in/aparajith-suresh-6149442b2/) | [GitHub](https://github.com/)
