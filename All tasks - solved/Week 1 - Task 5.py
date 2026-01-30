import json
from pathlib import Path

config_path = Path("config.json")
results_path = Path("results.json")


# create new json file
default_config = {
        "learning_rate": 0.001,
        "epochs": 50,
        "batch_size": 32
    }

with open(config_path, "w") as f:
    json.dump(default_config, f, indent=4)
print(f" Created a new {config_path}")




#1) Load config.json from disk
with open(config_path, "r") as f:
    config = json.load(f)


#2) Print config values
for key, value in config.items():
    print(f"{key}: {value}")


#3) Simulate training results (dict)
results = {
        "status": "success",
        "final_accuracy": 0.95,
        "loss": 0.05,
        "trained_epochs": config.get("epochs", 0)
    }



# 4) Save results to JSON safely
with open(results_path, "w") as f:
    json.dump(results, f, indent=4)
print(f"\n Results saved successfully to {results_path}")