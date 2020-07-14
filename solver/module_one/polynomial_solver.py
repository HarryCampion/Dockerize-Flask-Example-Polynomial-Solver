# given array of coordinates and degree, class will solve polynomial for zero.

import numpy as np
from .models.polynomial import Polynomial


class PolynomialSolver(Polynomial):
    
    def fit_polynomial(self):
        """
        Fits x and y coordinates to a polynomial of deg
        coords are a list of tuples
        """
        coefficients = np.polyfit(self.x, self.y, deg=self.deg)
        return list(coefficients)

    def get_roots(self, coefficients):
        """
        solves polynomial numerically for 0.
        e.g.
        p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
        where p is the coefficients and n is the deg of polynomial
        """
        roots = np.roots(coefficients)
        return [np.real(x) for x in roots ]

    def solve_polynomial(self):
        """
        Solves polynomial from coordinates
        Returns information on the function.
        """
        coefficients = self.fit_polynomial()
        roots = self.get_roots(coefficients)
        return {
            "x": list(self.x),
            "y": list(self.y),
            "deg": self.deg,
            "coefficients": list(coefficients),
            "roots": list(roots)
        }
