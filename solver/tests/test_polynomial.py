from ..module_one.models.polynomial import Polynomial

def test_polynomial():

    """
    Given x, y and degree a polynomial is created
    """
    x = (1, 2, 3, 4)
    y=(1, 3, 4, 5)
    deg="3"
    p1 = Polynomial(x, y, deg)
    assert p1.x == list(x)
    assert p1.y == list(y)
    assert p1.deg == int(deg)

    assert isinstance(p1, Polynomial)