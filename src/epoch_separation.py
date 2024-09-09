from utils.prov_getters import get_metric, get_avg_metric, get_metrics

import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd

PATH = "/Users/gabrielepadovani/Desktop/Università/PhD/HVAC/data/"
EPOCH = 3
TYPES = "HVAC"

sns.set(style="darkgrid")
plt.figure(figsize=(10, 5))
metrics = []

DIRNAME = PATH + TYPES + "_3B_2N_" + str(EPOCH) + "E"
FILENAME = DIRNAME + "/provgraph.json"
data = json.loads(open(FILENAME).read())
#print(get_metrics(data))

metric = get_metric(data, "train_step_time_Context.TRAINING")
for E in range(0, EPOCH):
    metric_e = metric[metric["epoch"] == E]
    avg_m = metric_e["value"].mean()
    metrics.append(avg_m)

metrics = pd.DataFrame(metrics)

plt.plot(metrics.index, metrics, color='b', label='10 epochs')
plt.ylabel("Training step time")
plt.xlabel("Epoch")
plt.savefig(f"training_step_time_{EPOCH}.pdf")