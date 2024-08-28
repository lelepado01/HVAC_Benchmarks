
from utils.prov_getters import get_metric, get_metrics, get_param, get_avg_metric

import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd


PATH = "/Users/gabrielepadovani/Desktop/Università/PhD/HVAC/data/"
EPOCHS = [10, 5, 3]
TYPES = ["HVAC", "PFS"]

sns.set(style="darkgrid")
# set figsize
plt.figure(figsize=(10, 5))
df_items = []
for TYPE in TYPES:
    for EPOCH in EPOCHS:
        df = {
            "type": TYPE, 
            "epoch": EPOCH
        }


        DIRNAME = PATH + TYPE + "_3B_64N_" + str(EPOCH) + "E"
        FILENAME = DIRNAME + "/provgraph.json"
        data = json.loads(open(FILENAME).read())

        train_step_time = get_avg_metric(data, "train_step_time_Context.TRAINING")
        epoch_time = get_avg_metric(data, "epoch_time_Context.TRAINING")
        training_time = get_param(data, "training_time")

        df["train_step_time"] = train_step_time
        df["epoch_time"] = epoch_time
        df["training_time"] = training_time

        df_items.append(df)

df = pd.DataFrame(df_items)

# sns.barplot(x="type", y="train_step_time", hue="epoch", data=df, color="b")
# sns.barplot(x="type", y="epoch_time", hue="epoch", data=df, color="r")
sns.barplot(x="type", y="training_time", hue="epoch", data=df, color="g")
plt.legend(title="Epochs")
plt.xlabel("Type")
plt.ylabel("Time (s)")
plt.savefig("training_time_comparison.pdf")
plt.show()
