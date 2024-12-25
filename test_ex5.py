from Exercice5 import sin_maclaurin, sh_maclaurin, arctg_maclaurin

def test_maclaurin():
    """
    Test Maclaurin series implementations without using external libraries.
    """
    print("Testing Maclaurin Series Approximations\n")

    # Test sin(x)
    x = 1.5708  # Approximation of pi/2
    sin_result = sin_maclaurin(x, 10)
    print(f"sin({x}) \u2248 {sin_result} (Expected: ~1.0)")

    # Test sh(x)
    x = 1
    sh_result = sh_maclaurin(x, 10)
    print(f"sh({x}) \u2248 {sh_result} (Expected: ~1.1752)")

    # Test arctg(x)
    x = 0.5
    arctg_result = arctg_maclaurin(x, 10)
    print(f"arctg({x}) \u2248 {arctg_result} (Expected: ~0.4636)")

def test_error_handling():
    """
    Test error handling for Maclaurin series functions.
    """
    print("\nTesting Error Handling\n")

    # Test invalid iterations
    try:
        sin_maclaurin(1, -1)
    except ValueError as e:
        print(f"Passed: {e}")

    try:
        sh_maclaurin(1, 0)
    except ValueError as e:
        print(f"Passed: {e}")

    # Test out-of-range input for arctg
    try:
        arctg_maclaurin(1.5, 10)
    except ValueError as e:
        print(f"Passed: {e}")

    # Test valid input
    try:
        result = arctg_maclaurin(0.5, 10)
        print(f"arctg(0.5) \u2248 {result} (No error)")
    except ValueError as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_maclaurin()
    test_error_handling()
