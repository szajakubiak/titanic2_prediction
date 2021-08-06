import tensorflow as tf
import pandas as pd


model_filename = "ML_model_titanic2"
model = tf.keras.models.load_model(model_filename)


def prediction(input_data):
    '''
    Expects dictionary with the following keys and values:
    Age: int, SibSp: int, Parch: int, Fare: float, Sex: str, Embarked: str, Pclass: int.
    Returns float value.
    '''
    # Data normalization
    input_data["Is_male"] = int(input_data["Sex"] == "male")
    input_data["Pclass_norm"] = input_data["Pclass"] / 3
    input_data["Embarked_S"] = int(input_data["Embarked"] == "S")
    input_data["Embarked_C"] = int(input_data["Embarked"] == "C")
    input_data["Embarked_Q"] = int(input_data["Embarked"] == "Q")

    # Remove unnecessary items
    del input_data["Sex"]
    del input_data["Pclass"]
    del input_data["Embarked"]

    # Create DataFrame from dict
    model_input = pd.DataFrame(input_data, index = [0])
    # Reorder columns to match DataFrame used for model training
    model_input = model_input[["Age",
                             "SibSp",
                             "Parch",
                             "Fare",
                             "Is_male",
                             "Embarked_S",
                             "Embarked_C",
                             "Embarked_Q",
                             "Pclass_norm"]]

    return model.predict(model_input)[0, 0]


if __name__ == "__main__":
    print(prediction({"Age": 38,
                      "Pclass": 2,
                      "SibSp": 0,
                      "Parch": 1,
                      "Fare": 30.00,
                      "Sex": "male",
                      "Embarked": "S"}))