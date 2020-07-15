from solutions import Graph
from mockdata import users

# problem 1
userGraph = Graph(False)
for user in users:
  userGraph.add_vertex(user)
for user, friends in users.items():
  for friend in friends:
    userGraph.add_edge(user, friend)

print(userGraph.min_connection("Dave", "Sean"))


# problem 2
min_connections = 0
for user1 in users:
  for user2 in users:
    if user1 == user2:
      continue
    min_connections += len(userGraph.min_connection(user1, user2)) - 1
print(min_connections)

# problem 3
print(userGraph.mutuals("Dave", "Collin"))