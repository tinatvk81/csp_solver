from CSP.Problem import Problem
from CSP.Variable import Variable
from King.Constraint1 import Constraint1
from King.Constraint2 import Constraint2
from King.Constraint3 import Constraint3
from King.Constraint4 import Constraint4
from King.Constraint5 import Constraint5
from King.Constraint6 import Constraint6
from King.Constraint7 import Constraint7
from King.Constraint8 import Constraint8
from King.Constraint9 import Constraint9
from King.Constraint10 import Constraint10
from King.Constraint11 import Constraint11


class KingProblem(Problem):
    def __init__(self):
        super().__init__([], [], "King Problem")

        x1 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'x1')
        x2 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'x2')
        x3 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'x3')
        x4 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'x4')
        x5 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'x5')
        y1 = Variable[str](['acid', 'poison', 'healing', 'invisible', 'transform'], 'y1')
        y2 = Variable[str](['acid', 'poison', 'healing', 'invisible', 'transform'], 'y2')
        y3 = Variable[str](['acid', 'poison', 'healing', 'invisible', 'transform'], 'y3')
        y4 = Variable[str](['acid', 'poison', 'healing', 'invisible', 'transform'], 'y4')
        y5 = Variable[str](['acid', 'poison', 'healing', 'invisible', 'transform'], 'y5')

        c1 = Constraint1([x1, x2, x3, x4, x5])
        c2 = Constraint1([y1, y2, y3, y4, y5])
        c3 = Constraint2([y1])
        c4 = Constraint3([x1])
        c5 = Constraint4([y2])
        c6 = Constraint5([x2])
        c7 = Constraint6([x3])
        c8 = Constraint7([y3])
        c9 = Constraint8([y4])
        c10 = Constraint9([x4])
        c11 = Constraint10([y5])
        c12 = Constraint11([x5])

        self.constraints = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
        self.variables = [x1, x2, x3, x4, x5, y1, y2, y3, y4, y5]
