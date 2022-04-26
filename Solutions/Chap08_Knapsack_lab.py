weights = [48, 27, 30, 36, 36,  42, 42, 36, 24, 30, 19] # Weights 
n = len(weights)
capacity = 80
# init solver
solver = pywraplp.Solver.CreateSolver('SCIP')
# adding vars
# Variables
# x[i, j] = 1 if item i is packed in bin j.
items = []
for i in range(n):
    items.append(solver.IntVar(0, 1, f'x_{i}'))

# adding constraints
solver.Add(sum(items[i]*weights[i]  for i in range(n)) <= capacity)

solver.Maximize(solver.Sum(items[i]*weights[i]  for i in range(n))) # solver.Sum can be replaced by sum. It is just about using a faster sum that solver offers.
status = solver.Solve()                
if status == pywraplp.Solver.OPTIMAL:
    selected_items = []
    total_weight = 0
    for i in range(n):
        if items[i].solution_value() == 1:
            selected_items.append(i)
            total_weight += weights[i]
    print("Selected items: ", selected_items)
    print("Selected weights: ", [weights[i] for i in selected_items])
    print("Total Weight: ", total_weight)