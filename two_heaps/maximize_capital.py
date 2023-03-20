# You need to develop a program for making automatic investment decisions for 
# a busy investor. The investor has some start-up capital, c, to invest and 
# a portfolio of projects in which they would like to invest in. The investor 
# wants to maximize their cumulative capital as a result of this investment. 
# To help them with their decision, they have information on the capital 
# requirement for each project and the profit it’s expected to yield. For 
# example, if project A has a capital requirement of 3, and the investor’s 
# current capital is 1, then the investor can’t invest in this project. On the
# other hand, if the capital requirement of a project B is 1, then the investor 
# can invest in this project. Now, supposing that the project yields a profit of 
# 2, the investor’s capital at the end of the project will be 1+2=3. The investor 
# can now choose to invest in project A as well since their current capital has 
# increased. As a basic risk-mitigation measure, the investor would like to set a 
# limit on the number of projects, k, they invest in. For example, if the value of 
# k is 2, then we need to identify the two projects that the investor can afford 
# to invest in, given their capital requirements, and that yield the maximum profits.
# Further, these are one-time investment opportunities, that is, the investor 
# can only invest once in a given project.


from heapq import *

def maximum_capital(c, k, capitals, profits):
    min_heap_capitals = []
    max_heap_profits = []
    for i, capital in enumerate(capitals):
        heappush(min_heap_capitals, (capital, i))
    for i in range(k):
        while min_heap_capitals and min_heap_capitals[0][0] <= c:
            top = heappop(min_heap_capitals)
            heappush(max_heap_profits, -profits[top[1]])
        if not max_heap_profits:
            break
        top_profit = heappop(max_heap_profits)
        c -= top_profit
        
    return c


tests = [(1 , 3 , [0, 1, 1, 2, 2] , [1, 3, 4, 6, 8]), (2 , 2 , [1, 2, 3, 4] , [1, 3, 5, 7]), (
2 , 3 , [1, 3, 4, 5, 6] , [1, 2, 3, 4, 5]), (1 , 3 , [0, 1, 2] , [1, 2, 3])]

for test in tests:
    print(f"input : {test}, output: {maximum_capital(test[0], test[1], test[2], test[3])}")