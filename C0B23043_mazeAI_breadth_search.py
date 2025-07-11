import pprint
import copy
path1 = "maze1.txt"
path2 = "maze2.txt"
path3 = "maze-astar-test.txt"
maze=[]
data=[]
values=[]
def generate_maze(path):
    MAZE="maze"
    with open(path, mode="r",encoding="utf-8")as r:
        for input_line in r.readlines():
            row = input_line.replace(",","").replace("W","1").rstrip().split(" ")
            if "#"in row:
                MAZE="data"
            if "$" in row:
                MAZE="value"
            if MAZE=="maze":
                maze.append(row)
            elif MAZE=="data":
                data.append(row)
            elif MAZE=="value":
                values.append(row)
        visit_maze=copy.deepcopy(maze)
        del data[0]
        del values[0]
        # print(maze)
        # print(data)r
        maze[int(data[0][0])][int(data[0][1])]="S"
        visit_maze[int(data[0][0])][int(data[0][1])]="1"
        maze[int(data[1][0])][int(data[1][1])]="G"
        now_pos=[int(data[0][0]),int(data[0][1])]
        goal=[int(data[1][0]),int(data[1][1])]
        move_cost=dict()
        for row in values:
            key=row[0]+row[1]+row[2]+row[3]
            move_cost[key]=int(row[4])
        # print(move_cost)
        return visit_maze,maze,now_pos,goal,move_cost
    
def show_maze(maze,now_pos):
    print("Maze:")
    temp=""
    if maze[now_pos[0]][now_pos[1]]!="1":
        temp=maze[now_pos[0]][now_pos[1]]
        maze[now_pos[0]][now_pos[1]]="A"
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(f"  {maze[i][j]}",end="")
        print("")
    if temp!="":
        maze[now_pos[0]][now_pos[1]]=temp


class RuleAI:
    def manhattan_calc(target,goal):
        return abs(target[0]-goal[0])+abs(target[1]-goal[1])
    
    def get_next_move(maze,visit_maze,now_pos,goal):
        moves=[[-1,0],[1,0],[0,-1],[0,1]]
        best_distance=10000
        best_move=[0,0]
        for move in moves:
            target=[x+y for (x,y) in zip(now_pos,move)]
            if target[0] >= 0 and target[0] < len(maze) and target[1] >= 0 and target[1] < len(maze[0]):
                if visit_maze[target[0]][target[1]]=="0":
                    distance=RuleAI.manhattan_calc(target,goal)
                    if distance<best_distance:
                        best_distance=distance
                        best_move=move
        # print(best_move)
        best_target=[x+y for (x,y) in zip(now_pos,best_move)]
        print(f"Next AI Move: {best_target[1]} {best_target[0]}")
        visit_maze[best_target[0]][best_target[1]]="1"
        now_pos=best_target
        return now_pos
    
class Node:
    def __init__(self, position, parent=None, cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost

    def breadth_first_search(visit_maze,data):
        print("Starting Breadth First Search...")
        already=False
        # visit_maze=copy.deepcopy(maze)
        # maze[int(data[0][0])][int(data[0][1])]="S"
        # visit_maze[int(data[0][0])][int(data[0][1])]="1"
        # maze[int(data[1][0])][int(data[1][1])]="G"
        Node.position=[int(data[0][0]),int(data[0][1])]
        goal=[int(data[1][0]),int(data[1][1])]
        start_node=Node([int(data[0][0]),int(data[0][1])])
        goal_node=Node([int(data[1][0]),int(data[1][1])])
        queue=[]#nodelist
        queue.append(start_node)
        moves=[[-1,0],[1,0],[0,-1],[0,1]]
        while True:
            current_node=queue.pop(0)
            # print("Now:")
            # print(current_node.position)
            # print("-"*10)
            # show_maze(visit_maze,current_node.position)
            visit_maze[current_node.position[0]][current_node.position[1]]="1"
            if current_node.position==goal_node.position:
                route=[]
                node=current_node
                while node:
                    route.append(node.position)
                    node=node.parent
                route.reverse()
                # print("-"*10)
                # print(route)
                # print(current_node.position)
                print("Breadth First Search success!!")
                return route, current_node.position 
            for move in moves:
                next_pos=[current_node.position[0]+move[0],current_node.position[1]+move[1]]
                if next_pos[0] >= 0 and next_pos[0] < len(maze) and next_pos[1] >= 0 and next_pos[1] < len(maze[0]):
                    if visit_maze[next_pos[0]][next_pos[1]]=="0":
                        # print(next_pos,current_node.depth)
                        # for node in queue:
                        #     if node.position==next_pos:
                        #         already=True
                        #         break
                        # if not already:
                        next_node = Node(next_pos,current_node,current_node.depth+1)
                        queue.append(next_node)
        
    def dijkstra(visit_maze,data,move_cost):
        print("Starting Dijkstra...")
        already=False
        # visit_maze=copy.deepcopy(maze)
        # maze[int(data[0][0])][int(data[0][1])]="S"
        # visit_maze[int(data[0][0])][int(data[0][1])]="1"
        # maze[int(data[1][0])][int(data[1][1])]="G"
        # Node.position=[int(data[0][0]),int(data[0][1])]
        goal=[int(data[1][0]),int(data[1][1])]
        start_node=Node([int(data[0][0]),int(data[0][1])])
        goal_node=Node([int(data[1][0]),int(data[1][1])])
        queue=[]#nodelist
        queue.append(start_node)
        moves=[[-1,0],[1,0],[0,-1],[0,1]]
        while queue:
            min_index = 0
            for i in range(1, len(queue)):
                if queue[i].cost < queue[min_index].cost:
                    min_index = i
            current_node = queue.pop(min_index)
            # print("finish sort")
            # print("Now:")
            # print(current_node.position)
            # print("-"*10)
            # show_maze(visit_maze,current_node.position)
            if visit_maze[current_node.position[0]][current_node.position[1]]=="2":
                continue
            visit_maze[current_node.position[0]][current_node.position[1]]="2"
            if current_node.position==goal_node.position:
                route=[]
                node=current_node
                while node:
                    route.append(node.position)
                    node=node.parent
                route.reverse()
                # print("-"*10)
                # print(route)
                # print(current_node.position)
                print("Dijkstra success!!")
                return route, current_node.cost, current_node.position 
            for move in moves:
                next_pos=[current_node.position[0]+move[0],current_node.position[1]+move[1]]
                # print("-"*10)
                # print(current_node.position)
                # print(next_pos)
                if next_pos[0] >= 0 and next_pos[0] < len(visit_maze) and next_pos[1] >= 0 and next_pos[1] < len(visit_maze[0]):
                    if visit_maze[next_pos[0]][next_pos[1]]=="0":
                        # print("-"*10)
                        # print(current_node.position)
                        # print(next_pos)
                        key=str(current_node.position[0])+str(current_node.position[1])+str(next_pos[0])+str(next_pos[1])
                        key2=str(next_pos[0])+str(next_pos[1])+str(current_node.position[0])+str(current_node.position[1])
                        # print(key)
                        try:
                            next_cos=move_cost[key]
                        except KeyError:
                            next_cos=move_cost[key2]
                        # print(f"cost={next_cos}")
                        # next_node = Node(next_pos,current_node,current_node.cost+next_cos)
                        update=False
                        for node in queue:
                            # print(f"now={node.position}")
                            # print(f"next={next_pos}")
                            if node.position == next_pos:
                                # print("#"*10)
                                if current_node.cost+next_cos<=node.cost or node.cost==0:
                                    # print("?"*10)
                                    node.cost=current_node.cost+next_cos
                                    node.parent=current_node
                                    # print(update)
                                # print(queue)
                                update=True
                                break
                        if not update:
                            next_node = Node(next_pos,current_node,current_node.cost+next_cos)
                            queue.append(next_node)


def check_goal(now_pos,goal):
    result="Miss"
    moves=[[-1,0],[1,0],[0,-1],[0,1]]
    for move in moves:
        target=[x+y for (x,y) in zip(now_pos,move)]
        if target[0] >= 0 and target[0] < len(maze) and target[1] >= 0 and target[1] < len(maze[0]):
            if visit_maze[target[0]][target[1]]=="0":
                result=""
    # print("-"*10)
    # print(now_pos)
    # print(goal)
    # print("-"*10)
    if now_pos==goal:
        result="Goal"
    return result

visit_maze,maze,now_pos,goal,move_cost=generate_maze(path3)
show_maze(maze,now_pos)
routes,cost,node_pos=Node.dijkstra(visit_maze,data,move_cost)
print(f"Path cost: {cost}")
print("Path to goal:")
for i in range(len(routes)-1):
    print(routes[i], end="")
    print("->", end="")
print(f"{routes[-1]}")
if now_pos in routes:
    idx = routes.index(now_pos)
    print(f"Next AI Move: {routes[idx]}, -> {routes[idx+1]}")