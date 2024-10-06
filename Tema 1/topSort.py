#Topological Sort
from collections import deque

g = {
    "calcetines" : ["zapatos"],
    "pantalón" : ["zapatos","cinturón"],
    "camisa" : ["cinturón", "jersey"],
    "zapatos" : [],
    "cinturón" : [],
    "jersey" : []
}


def topSortVisit(data, k):
    data["state"][k] = "VISITED"
    data["time"] = data["time"] + 1
    data["d"][k] = data["time"]
    for adj in data["graph"][k] :
        if data["state"][adj] == "NOT VISITED":
            topSortVisit(data,adj)
    data["state"][k] = "FINISHED"
    data["time"] += 1
    data["f"][k] = data["time"]
    data["sol"].appendleft(k)


def topSort (g):
    data = {
        "graph" : g,
        "state" : dict(),
        "d" : dict(),
        "f" : dict(),
        "time" : 0,
        "sol" : deque()
    }

    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["d"][k] = 0
        data["f"][k] = 0

    for k in g .keys():
        if data["state"][k] == "NOT VISITED":
            print("Hola, te visito "+k)
            topSortVisit(data, k)

    print(data["sol"])

topSort(g)
