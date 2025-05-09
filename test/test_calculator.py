from app.calculator import add, subtract

def test_add():
    assert add(3, 4) == 7

def test_substract():
    assert subtract(10, 2) == 8

    
