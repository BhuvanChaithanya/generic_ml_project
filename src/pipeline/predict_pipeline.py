import sys
import pandas as pd 
from src.exception import CustomException

from src.utils import load_object




class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys) #type: ignore
class CustomData:
    def __init__(
            self,
            gender,
            race_ethnicity,
            parental_level_of_education,
            lunch,
            test_preparation_course,
            reading_score,
            writing_score
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity], # Changed key to match training
                "parental level of education": [self.parental_level_of_education], # Changed key
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course], # Changed key
                "reading score": [self.reading_score], # Changed key
                "writing score": [self.writing_score], # Changed key
            }

            df = pd.DataFrame(custom_data_input_dict)
            
            # --- THIS IS THE FIX ---
            # 💡 Impute missing values with the mode from your training data
            # Replace 'group C' with the actual mode you found in Step 1.
            df['race/ethnicity'].fillna('group C', inplace=True) 
            # Do the same for other categorical columns that might be None
            # df['parental level of education'].fillna('some college', inplace=True)

            return df

        except Exception as e:
            raise CustomException(e, sys) #type: ignore
