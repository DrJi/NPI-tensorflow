from tasks.copy import *

g = Copy()
E_out = g.generate_executions(4)

for E in g.E_out:
    print E
