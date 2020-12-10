class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        i = 0
        inserted = False
        for (prt, _, _) in self.heap : 
            if prt > priority : 
                self.heap.insert(i, entry)
                inserted = True
                break
            i = i + 1

        if not inserted : 
            self.heap.append(entry)

        self.count += 1

    def pop(self):
        (_, _, item) = self.heap.pop(0)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                # heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
    
class PriorityQueueWithFunction(PriorityQueue):
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )



# elements_with_costs = [
#     ('a', 10),
#     ('b', 103),
#     ('c', 0.10),
#     ('d', 110),
#     ('e', 30),
# ]

# Frontier = PriorityQueue()
# for e in elements_with_costs:
#     Frontier.push(*e)

# while not Frontier.isEmpty():
#     e = Frontier.pop()
#     print(e)




# print("------------------test 2-----------------------")

# elements_without_cost = ['c' , 'd' , 'b', 'x' , 'a']

# # Frontier = PriorityQueue()
# Frontier1 = PriorityQueueWithFunction(ord)
# for e in elements_without_cost:
#     Frontier1.push(e)

# while not Frontier1.isEmpty():
#     e = Frontier1.pop()
#     print(e)
    
