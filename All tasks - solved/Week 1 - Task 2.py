from typing import List, Dict, Tuple

# first func
def calculate_statistics(data: list[float]) -> dict[str, float]:
    """this function  is to calculate mean and median of the data"""
    n = len(data)
    mean = sum(data) / n

    sorted_data = sorted(data)
    mid = n // 2
    median = sorted_data[mid]

    return {'mean': mean , 'median': median}




#second func
def normalize_data(data: List[float], method: str = "minmax") -> List[float]:
    """this function  is to normalizing-scale the data"""
    min_val = min(data)
    max_val = max(data)

    if method == "minmax":
        return [(x - min_val) / (max_val - min_val) for x in data]
    return data




#third func

def remove_outliers(data: List[float], threshold: float) -> List[float]:
    """this function  is to remove outliers the data"""
    return [x for x in data if abs(x) <= threshold]




# forth func
def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
    """this function is to train, test and split the data"""
    split_index = int(len(data) * ratio)
    return data[:split_index], data[split_index:]



# fifth func
def encode_labels(labels: List[str]) -> Dict[str, int]:
    """this function is to encode labels"""
    unique_labels = list(set(labels))
    return {label: i for i, label in enumerate(unique_labels)}




# --- Small Tests for Each Function ---

print("--- Running Tests ---")

# 1. Test Statistics
data_sample = [10.0, 20.0, 30.0, 40.0, 50.0]
print(f"Stats: {calculate_statistics(data_sample)}")

# 2. Test Normalization
print(f"Normalized (0-1): {normalize_data(data_sample)}")

# 3. Test Outliers (Let's add 100 as an outlier and set threshold to 60)
data_with_outlier = [10.0, 20.0, 100.0, -5.0]
print(f"Filtered (Threshold 50): {remove_outliers(data_with_outlier, 50.0)}")

# 4. Test Train/Test Split
train, test = train_test_split(data_sample, ratio=0.7)
print(f"Train set: {train} | Test set: {test}")

# 5. Test Label Encoding
categories = ["cat", "dog", "cat", "bird"]
print(f"Labels: {encode_labels(categories)}")