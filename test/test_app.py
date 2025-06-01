from app.app import doble

def test_doble():
    assert doble(2) == 4
    assert doble(0) == 0
    assert doble(-3) == -6
