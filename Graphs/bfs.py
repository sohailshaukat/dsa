from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person == name:
            print("Found "+name)
            return True
        else:
            searched.add(person)
            search_queue += graph[person]
    return False
    

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(search('anuj'))