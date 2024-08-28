from utils.prov_getters import get_metric, get_metrics, get_param, get_avg_metric

import matplotlib.pyplot as plt
import seaborn as sns
import json

PATH = "/Users/gabrielepadovani/Desktop/Università/PhD/HVAC/data/"
EPOCHS = [10, 5, 3]
TYPES = ["HVAC", "PFS"]

TYPE = "HVAC"
EPOCH = 10

DIRNAME = PATH + TYPE + "_3B_64N_" + str(EPOCH) + "E"
FILENAME = DIRNAME + "/provgraph.json"
data = json.loads(open(FILENAME).read())

train_step_time = get_avg_metric(data, "train_step_time_Context.TRAINING")
epoch_time = get_avg_metric(data, "epoch_time_Context.TRAINING")
training_time = get_param(data, "training_time")

print("Training time: ", training_time)
print("Train step time: ", train_step_time)
print("Epoch time: ", epoch_time)

import pandas as pd

# adjust times to see overhead
# train_step_time = train_step_time * EPOCH * 10 # train_steps_in_epoch
# epoch_time = epoch_time * EPOCH

sns.set(style="darkgrid")
plt.figure(figsize=(10, 5))
sns.barplot(x=0, y=0, data=pd.DataFrame([train_step_time]), color="b", label="Train step time")
sns.barplot(x=1, y=0, data=pd.DataFrame([epoch_time]), color="r", label="Epoch time")
sns.barplot(x=2, y=0, data=pd.DataFrame([training_time]), color="g", label="Training time")
plt.ylabel("Time (s)")
plt.xlabel("")
plt.xticks(range(3), ["Train step time", "Epoch time", "Training time"])
plt.show()




