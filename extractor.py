import os,json
from tqdm import tqdm

user_agents={}

logs_path=""
while not logs_path:
    logs_path=input("PATH TO LOGS: ")
    if not os.path.exits(logs_path):
        logs_path=False
        print("\tERROR: path doesn't exists! enter an existsing path.")
    elif os.path.isfile(logs_path):
        logs_path=False
        print("\tERROR: path must be a fodler, not a file.")

for file in tqdm(os.listdir(logs_path)):
    if not ".error" in file and file.endswith(".log"):
        with open(os.path.join(logs_path, file), errors="ignore") as f:
            file_content=f.read()
            
            logs=file_content.split("\n")
            
            for log in logs:
                ua=log.strip("\"").rsplit("\"", 1)[-1]
                if ua in user_agents: user_agents[ua]+=1
                else: user_agents[ua]=1

with open("user-agents.json", "w") as f:
    json.dump(
        dict(sorted(user_agents.items(), key=lambda item: item[1])),
        f
    )
                
        