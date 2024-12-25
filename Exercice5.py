import math

def sin_maclaurin(x: float, iterations: int = 10) -> float:
    """
    Calculate sine of x using Maclaurin series.

    Detailed description:
        Uses the formula: sin(x) = sum((-1)^n * x^(2n+1)/(2n+1)!)
        where n goes from 0 to infinity. We approximate using finite iterations.
    """
    if iterations < 1:
        raise ValueError("Iterations must be positive")
    
    result = 0
    for n in range(iterations):
        result += ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

def sh_maclaurin(x: float, iterations: int = 10) -> float:
    """
    Calculate hyperbolic sine of x using Maclaurin series.

    Detailed description:
        Uses the formula: sh(x) = sum(x^(2n+1)/(2n+1)!)
        where n goes from 0 to infinity. We approximate using finite iterations.
    """
    if iterations < 1:
        raise ValueError("Iterations must be positive")
    
    result = 0
    for n in range(iterations):
        result += x ** (2 * n + 1) / math.factorial(2 * n + 1)
    return result


def main():
    ITERATIONS = 10  # Fixed number of iterations
    
    while True:
        print("\nMaclaurin Series Calculator")
        print("1. sin(x)")
        print("2. sh(x)")
        print("3. Exit")
        
        try:
            choice = int(input("Choose function (1-3): "))
            if choice == 4:
                break
                
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please select 1-3.")
                continue
                
            x = float(input("Enter x value: "))
            
            if choice == 1:
                result = sin_maclaurin(x, ITERATIONS)
                print(f"sin({x}) â‰ˆ {result}")
                print(f"Built-in sin({x}) = {math.sin(x)}") 
                
            elif choice == 2:
                result = sh_maclaurin(x, ITERATIONS)
                print(f"sh({x}) â‰ˆ {result}")
                print(f"Built-in sinh({x}) = {math.sinh(x)}")  
                
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()