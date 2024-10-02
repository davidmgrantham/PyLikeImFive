def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add_returns_correct_result():
    # Arrange
    a = 1
    b = 2

    # Act
    result = add(a, b)

    # Assert
    assert result == 3

def test_subtract_returns_correct_result():
    # Arrange
    a = 5
    b = 3

    # Act
    result = subtract(a, b)

    # Assert
    assert result == 2