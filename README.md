# MAACLAURING SERIES CALCULATOR 

## Description

This project implements a **Maclaurin Series Calculator** in Python. The Maclaurin series is a representation of functions as a series expansion around zero. The calculator allows users to compute approximations for various mathematical functions using iterative calculations.

### TASK )))))))))

1. Создать публичный удаленный репозиторий и связать его с локальным
репозиторием. Для удаленного репозитория может быть использован
GitHub.com, GitLab.com, gitea.com и другие аналоги по выбору студента.
2. Согласно своему варианту задания реализовать две формулы из списка
элементарных функций из файла «Практическая работа №5. Ряды Маклорена».
Количество итераций для вычисления значения определяется программистом, то
есть «захардкожено» «константой» в коде.
3. Реализовать меню пользователя, где пользователь выбирает функцию,
вводит «x» и получает результат, который выводится на экран. При реализации
данной функции нужно учитывать граничные значения для «x».
4. Написать документацию (Docstrings) для всех вами написанных
функций и классов в коде.
5. Оформить для этого проекта README.md в корне проекта.
6. Залить эту версию проекта на репозиторий. После этого напарник
«форкает» проект себе, связывает его со своим локальным репозиторием,
например, через клонирование.
7. Напарник реализует оставшуюся, третью функцию, добавляет
возможность вызова ее в меню пользователя, добавляет комментарии к ней.
Количество итераций задается той же константой, что и у других функций.
8. Напарник заливает свои наработки на репозиторий и делает запрос на
слияние.
9. Принять запрос на слияние, обновить свой локальный репозиторий.
10. Запустить реализованную программу и проверить ее
работоспособность.
11. Предоставить отчет, программу и скрипты на проверку, ответить на
вопросы и выполнить дополнительные задания по усмотрению преподавателя.

sounds ALot but (get load of this guy) THIS IS SIMPLE I REQUIRE MORE !

## Features

- **sin(x)**: Calculate the sine of a value using its Maclaurin series expansion.
- **sh(x)**: Calculate the hyperbolic sine of a value using its Maclaurin series expansion.
- **arctg(x)**: Calculate the arctangent of a value using its Maclaurin series expansion (only for -1 ≤ x ≤ 1).

## How It Works

The Maclaurin series for the implemented functions is defined as follows:

### Sine Function:

sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n \cdot x^{2n+1}}{(2n+1)!}

### Hyperbolic Sine Function:

sh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}


### Arctangent Function:

arctg(x) = \sum_{n=0}^{\infty} \frac{(-1)^n \cdot x^{2n+1}}{2n+1}, \quad -1 \leq x \leq 1


## Usage

1. Clone this repository to your local machine:

   git clone (https://github.com/Mohamed-Amini2/BBPD5.git)
   cd BBPD5


2. Run the program:

   python Exercice5.py


3. Follow the menu to select a function and input a value for `x`. The calculator will display the approximated result and compare it to Python's built-in functions.

### Example Menu:
```
Maclaurin Series Calculator
1. sin(x)
2. sh(x)
3. arctg(x)
4. Exit
Choose function (1-4):
```

### Example Output:
```
sin(1.5708) ≈ 1.0000035425842861
Built-in sin(1.5708) = 1.0
```

## Requirements

- Python 3.6 or higher

## Implementation Details

### Functions Implemented

- **Factorial Calculation**: Computes the factorial of a number iteratively without using external libraries.
- **Power Calculation**: Computes the power of a number iteratively without using external libraries.
- **Maclaurin Series Functions**: 
  - `sin_maclaurin`
  - ![image](https://github.com/user-attachments/assets/dc6e2d3a-e99a-48fe-8673-2ecad1d29495)

  - `sh_maclaurin`
  - ![image](https://github.com/user-attachments/assets/d12d45fd-5385-46e4-847f-18e5e249256f)

  - `arctg_maclaurin`
  - ![image](https://github.com/user-attachments/assets/7b47bb56-7541-43ad-9ce4-9e8450e7201f)


Each function is implemented with detailed error handling and validations.

### Testing

The program includes a test suite to validate the correctness and robustness of the functions:
- Approximations of `sin(x)`, `sh(x)`, and `arctg(x)` are tested for accuracy.
- Error handling tests ensure appropriate exceptions are raised for invalid inputs (e.g., out-of-range values or non-positive iterations).

## Example Code Snippet

Here’s a snippet showing the implementation of `sin_maclaurin`:

```python
def sin_maclaurin(x: float, iterations: int = 10) -> float:
    if iterations < 1:
        raise ValueError("Iterations must be positive")

    result = 0
    for n in range(iterations):
        result += ((-1) ** n * power(x, 2 * n + 1)) / factorial(2 * n + 1)
    return result
```

## To-Do

- [x] Implement `sin(x)`
- [x] Implement `sh(x)`
- [x] Implement `arctg(x)`
- [ ] Add more functions from the Maclaurin series.
- [ ] Optimize performance for large inputs.

## Contribution Workflow

1. Fork the repository.
2. Create a feature branch:

   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:

   git commit -m "Add your message here"
   ```
4. Push to your branch:

   git push origin feature/your-feature-name
   
5. Submit a pull request for review.


*Happy Calculating!*

