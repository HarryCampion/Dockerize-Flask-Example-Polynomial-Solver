from ..module_one.polynomial_solver import PolynomialSolver
from ..module_one.models.polynomial import Polynomial
import random
import numpy as np

class TestPolynomialSolver():

    x = []
    y = []
     
    for i in range(15):
        x.append(random.randint(0, 30))
        y.append(random.randint(0, 30))


    p1 = PolynomialSolver(x=x, y=y, deg=2)
    p2 = PolynomialSolver(x=x, y=y, deg=3)

    c1 = p1.fit_polynomial()
    c2 = p2.fit_polynomial()

    roots = p1.get_roots(c1)

    def test_polynomial_solver(self):

        assert isinstance(self.p1, Polynomial)
        assert isinstance(self.p2, Polynomial)
    
    def test_fit_polynomial(self):
        
        assert type(self.c1) == list
        assert type(self.c2) == list
        assert len(self.c1) == 3
        assert len(self.c2) == 4
        assert all(isinstance(x, np.float64) for x in self.c1)

    def test_get_roots(self):

        assert type(self.roots) == list
        assert all(isinstance(x, np.float64) for x in self.roots)

    def test_solve_polynomial(self):

        results = self.p1.solve_polynomial()
        
        assert isinstance(results, dict)
        assert all(k in results for k in ("x", "y", "deg", "coefficients", "roots"))
