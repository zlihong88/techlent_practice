from app.src.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1,1) == 2
    assert cal.add(1,2) == 3

def test_subtract():
    assert cal.subtract(3,1) == 2
    assert cal.subtract(2,1) == 1

def test_devide():
    assert cal.devide(6,2) == 3
    assert cal.devide(4,2) == 2