import json
from collections import OrderedDict
import os

data_path = os.path.dirname(os.path.realpath(__file__))
data_name = "/data.txt"
save_name = "/data.json"

file_data = OrderedDict()

"Open data"
with open(data_path + data_name, "r") as f:
  data = f.readlines()

for d in data:
  print("STEP", data.index(d))
  file_data["sentence"] = d.split("\t")[0]
  file_data["target"] = d.split("\t")[1].replace("\n", "")
  with open(data_path+save_name, "a", encoding="utf-8") as f:
    json.dump(file_data, f, ensure_ascii=False, indent="\t")
