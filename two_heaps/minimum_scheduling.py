# Given a set of n number of tasks, implement a task scheduler method, tasks(),
# to run in O(n logn) time that finds the minimum number of machines required 
# to complete these n tasks.

from heapq import heappush, heappop

def tasks(tasks_list):
    num_machines = 0
    tasks_heap = []
    machines_heap = []

    for task in tasks_list:
        heappush(tasks_heap, task)

    while tasks_heap:
        current_task_start, current_task_end = heappop(tasks_heap)
        if machines_heap and machines_heap[0] <= current_task_start:
            heappop(machines_heap)
        else:
            num_machines += 1
        
        heappush(machines_heap, current_task_end)
    
    return num_machines

tests = [[[1,1],[5,5],[8,8],[4,4],[6,6],[10,10],[7,7]], [[1,7],[1,7],[1,7],[1,7],[1,7],[1,7]]]

for test in tests:
    print(f"input : {test}, output: {tasks(test)}")