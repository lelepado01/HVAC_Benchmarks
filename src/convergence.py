
from utils.prov_getters import get_metric, get_metrics

import matplotlib.pyplot as plt
import seaborn as sns
import json

PATH = "/Users/gabrielepadovani/Desktop/Università/PhD/HVAC/data/"
EPOCHS = [10, 5, 3]
TYPES = ["HVAC", "PFS"]

sns.set(style="darkgrid")
# set figsize
plt.figure(figsize=(10, 5))
for TYPE in TYPES:
    for EPOCH in EPOCHS:

        DIRNAME = PATH + TYPE + "_3B_64N_" + str(EPOCH) + "E"
        FILENAME = DIRNAME + "/provgraph.json"
        data = json.loads(open(FILENAME).read())

        loss = get_metric(data, "loss_Context.TRAINING")
        sns.lineplot(x=range(len(loss)), y=loss["value"], label=TYPE + " " + str(EPOCH) + " epochs")

plt.title("Training Loss")
plt.xlabel("Training steps")
plt.show()
