from JSSP.solver import Solver
from JSSP.data import SpreadsheetData

# initialize data
data = SpreadsheetData('data/given_data/sequenceDependencyMatrix.csv',
                       'data/given_data/machineRunSpeed.csv',
                       'data/given_data/jobTasks.csv')

# run parallel Tabu Search
solver = Solver(data)
solution = solver.tabu_search_iter(iterations=500,
                                   num_processes=4,
                                   tabu_list_size=20,
                                   neighborhood_size=250)

# create Schedule
solution.create_schedule_xlsx_file('output/Schedule.xlsx') 