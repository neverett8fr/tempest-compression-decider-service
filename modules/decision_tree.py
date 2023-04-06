import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def get_comp_ext(ext):
    ext_dict = {
        0: "", "": 0,
        1: ".gzip", ".gzip": 1,
        2: ".rle", ".rle": 2,
        3: ".lzw", ".lzw": 3
    }
    return ext_dict[ext]


def get_type_ext(ext):
    ext_dict = {
        0: "", "": 0,
        1: ".txt", ".txt": 1,
        2: ".png", ".png": 2,
        3: ".jpg", ".jpg": 3
    }
    return ext_dict[ext]


def get_best_method(type, size):
    # Load data
    data = pd.read_csv("files/results.csv")

    # Select relevant features
    X = data[["file_type", "original_file_size",
              "compression_method"]]  # feature - in
    y = data["compression_ratio"]  # target - out

    # Split data into training and testing sets
    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    best_method = 0
    highest_ratio = -10000
    for compression_method in range(1, 4, 1):
        x = pd.DataFrame(
            [[type, size, compression_method]],
            columns=X.columns
        )
        y = model.predict(x)
        if y[0] > highest_ratio:
            best_method = compression_method
            highest_ratio = y[0]

        print(
            f"Compression Method: {compression_method}, File Type: {type}, Predicted Ratio: {y[0]}")

        print("  file type, best predicted method", type, best_method)
    if highest_ratio <= 0:
        return 0  # if < 0, no point compressing
    return best_method
