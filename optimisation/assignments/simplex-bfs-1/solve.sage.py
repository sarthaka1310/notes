
# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_10 = Integer(10); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4)#!/usr/bin/env python

# use the flow() function, query it for the LP. Or hack sage so you can
# query it for the LP. Not too hard.
# http://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.flow
import json
import pprint
p = MixedIntegerLinearProgram(maximization=True)
VAR = p.new_variable(real=True)

# vertices
x1 = p["x1"]
x2 = p["x2"]


# maximise flow out of source
p.set_objective(-_sage_const_1  * x1 + -_sage_const_1  * x2)
p.add_constraint(x1 + _sage_const_10  * x2 <= _sage_const_5 )
p.add_constraint(_sage_const_4  * x1 + x2 <= _sage_const_4 )
p.add_constraint(x1 >= _sage_const_0 )
p.add_constraint(x2 >= _sage_const_0 )
print(p.solve())
opt1, opt2 = tuple(p.get_values([x1, x2]))
print(opt1, opt2)

