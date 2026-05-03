# AI Transparency Document — Student Grade Predictor

**Project:** Student Grade Predictor  
**Author:** Aparajith Suresh  
**Version:** 1.0  
**Date:** 2026  

---

## 1. What This Model Does

This project uses a Random Forest Regression model to predict a student's upcoming test grade based on a combination of academic, lifestyle, and personal inputs. The model takes in factors such as previous test score, sleep, hydration, diet, sports activity, revision hours, number of subjects, year of study, and tuition hours, and outputs a predicted grade out of 100.

The goal is to help students reflect on how their habits and lifestyle choices may be influencing their academic performance.

---

## 2. How It Was Built

### Model Type
Random Forest Regressor (via scikit-learn)

### Training Data
The model was trained on a synthetically generated dataset of 300 student profiles. The dataset was designed to reflect realistic relationships between lifestyle factors and academic performance, based on general educational research. It covers students in Years 10 through 13.

### Key Design Decisions
- Categorical variables (diet, sports, year of study) were converted to numerical values to allow the model to process them
- A Random Forest was chosen over a single Decision Tree to reduce overfitting and improve accuracy
- The dataset was split 75/25 into training and validation sets using `train_test_split`
- `random_state=1` was used throughout to ensure reproducibility

### Model Performance
- **Mean Absolute Error (MAE): 4.15 marks**
- This means the model's predictions are within 4.15 marks of the actual grade on average, on a scale of 0–100

---

## 3. Limitations

- **Synthetic data:** The training data was computationally generated, not collected from real students. Real-world student data would produce a more nuanced and accurate model.
- **Limited features:** Many factors that influence academic performance — such as mental health, quality of teaching, socioeconomic background, and learning difficulties — are not captured in this model.
- **Simplified categories:** Diet and sports are simplified into three categories each, which may not reflect the full range of student experiences.
- **Year range:** The model covers Years 10–13 only and may not generalise well outside this range.
- **No professional validation:** This model has not been reviewed by educational psychologists or academic researchers and should not be used as a substitute for professional academic guidance.

---

## 4. Potential Biases

- The synthetic dataset was built with assumptions about how each factor affects grades. These assumptions reflect general trends but may not apply equally to all students.
- The model does not account for differences between school systems, grading standards, or subject difficulty.
- Students with learning differences, disabilities, or exceptional circumstances may not be well represented in the data.

---

## 5. Ethical Considerations

- **Not a professional tool:** This model is built for educational and portfolio purposes only. It should not be used to judge, rank, or make decisions about students.
- **Data privacy:** If this model is adapted to use real student data, strict data protection and consent processes must be followed.
- **Fairness:** Predictions reflect population-level patterns and should never be used to label or limit an individual student's potential.
- **Transparency:** The full dataset, model code, and this document are publicly available on GitHub to ensure complete openness about how the model works.

---

## 6. Intended Use

✅ Personal reflection on how lifestyle habits may affect academic performance  
✅ Educational demonstration of machine learning applied to student data  
✅ Portfolio project showcasing Python and ML skills  

❌ Official academic assessment or grading  
❌ Student selection, ranking, or comparison  
❌ Medical, psychological, or professional educational advice  

---

## 7. How to Use Responsibly

- Treat the output as a rough estimate for personal reflection, not a definitive prediction
- Use the model to identify areas for improvement (e.g. sleep, revision hours) rather than to predict failure or success
- Never use this tool to compare students or make judgements about academic ability
- If adapting with real student data, ensure full ethical approval and informed consent

---

## 8. Future Improvements

- Collect anonymised real student data with appropriate consent to replace the synthetic dataset
- Add more nuanced features such as study quality, mental wellbeing, and subject-specific revision
- Build a simple interactive interface where students can input their own stats easily
- Expand to cover more year groups and subject types
- Validate the model with educational researchers

---

*This document was produced in line with AI transparency best practices as taught by Anthropic Academy's AI Fluency programme.*
