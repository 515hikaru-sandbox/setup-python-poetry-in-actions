from main import fizz

def test_fizz3():
    n = 3
    result = fizz(n)
    expected = 'fizz'
    assert result == expected

def test_fizz5():
    n = 5
    result = fizz(n)
    expected = '5'
    assert result == expected

