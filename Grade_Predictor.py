#importing pandas to handle data
import pandas as pd
#importing train test split function to split the data to train a model and to test it as well
from sklearn.model_selection import train_test_split
#importing the random forest regressor instead of decision tree regressor to decrease the mean absolute error in calculations
from sklearn.ensemble import RandomForestRegressor
#importing to calculate mean absolute error
from sklearn.metrics import mean_absolute_error

#reading the student csv file into a data frame
stud_data = pd.read_csv('student_data.csv')

# Converting text columns to numbers so the model can understand them
diet_map = {'good': 2, 'avg': 1, 'poor': 0}
sports_map = {'regular': 2, 'occasional': 1, 'none': 0}

stud_data['diet'] = stud_data['diet'].map(diet_map)
stud_data['sports'] = stud_data['sports'].map(sports_map)
stud_data['year_of_study'] = stud_data['year_of_study'].str.extract('(\d+)').astype(int)

#this is what we want to predict
y = stud_data['upcoming_test_grade']

#these are the values that will be used as clues to predict the final grade (y)
predictors = ['prev_test_score', 'sleep', 'hydration', 'diet', 'sports',
              'revision_hours_per_week', 'subjects_taken', 'year_of_study', 'tuition']

#storing the predictors of the student data to the value X
X = stud_data[predictors]

#testing and training using the split function
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

#finding patterns using the regressor
grade_model = RandomForestRegressor(random_state=1)

#fitting/training the model to show that x leads to y and asking the model to find patterns
grade_model.fit(train_X, train_y)

#predicting
predictions = grade_model.predict(val_X)

#finding the mean absolute error
mae = mean_absolute_error(val_y, predictions)
print(f"Mean Absolute Error: {mae:.2f} marks")

print("\n--- Predict Your Upcoming Test Result Grade ---")

my_stats = pd.DataFrame([{
    'prev_test_score': 80,
    'sleep': 8,
    'hydration': 3,
    'diet': 2,        # 2 = good, 1 = avg, 0 = poor
    'sports': 2,      # 2 = regular, 1 = occasional, 0 = none
    'revision_hours_per_week': 28,
    'subjects_taken': 4,
    'year_of_study': 12,
    'tuition': 0
}])

my_prediction = grade_model.predict(my_stats)
print(f"Predicted upcoming grade: {my_prediction[0]:.2f}")
