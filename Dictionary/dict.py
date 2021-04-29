import json

def get_meaning(ins):
    if ins in data:
        ans = data[ins]
        print("\n")
        for f, v in enumerate(ans, start=1):
            print("{} : {}".format(f,v))
        print("\n")
    else:
        print("enter a valid word for search.")

file = open("/home/dhrumil/Documents/Github/Py-Games/Dictionary/all_data.json")
data = json.load(file)
print("input exit to terminate search")
while 1:
    ins = str(input("Enter the word you want to search : ")).lower()
    if ins == 'exit':
        break
    get_meaning(ins)