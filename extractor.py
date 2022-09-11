import os,json
from tqdm import tqdm


logs_path=""
while not logs_path:
    logs_path=input("PATH TO LOGS: ")
    if not os.path.exists(logs_path):
        logs_path=False
        print("\tERROR: path doesn't exists! enter an existsing path.")
    elif os.path.isfile(logs_path):
        logs_path=False
        print("\tERROR: path must be a fodler, not a file.")
          

user_agents={}
for file in tqdm(os.listdir(logs_path)):
    if not ".error" in file and file.endswith(".log"):
        with open(os.path.join(logs_path, file), errors="ignore") as f:
            for log in f:
                ua=log.strip().strip("\"").rsplit("\"", 1)[-1]

                if ua not in user_agents: user_agents[ua]=1
                else: user_agents[ua]+=1

if user_agents:
    with open(f"user_agents.json", "w") as f:
        json.dump(user_agents,f)
        
    with open(f"user_agents_sorted.json", "w") as f:
        json.dump(dict(sorted(user_agents.items(), key=lambda item: item[1])),f)