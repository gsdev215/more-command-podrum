import json,os

path: str = os.path.join(os.getcwd(), "plugins")

def json_open():
	file = f"{path}/zCommand/input.json"
	with open(file,"r") as f:
		n = json.load(f)
	return n
	
def json_dump(n:str=None):
	file = Path(f"plugins/zCommand/input.json")
	with open(file,"w") as f:
		json.dump(n,f)
