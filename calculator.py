import math
import statistics

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def display_menu():
    print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}✨ ADVANCED CALCULATOR ✨{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    
    print(f"\n{Colors.GREEN}📌 BASIC OPERATIONS{Colors.END}")
    print(f"{Colors.YELLOW}1. Continuous Calculator (chain operations){Colors.END}")
    print("2. Single Operation      3. Square Root (√)")
    
    print(f"\n{Colors.GREEN}📌 TRIGONOMETRIC{Colors.END}")
    print("4. Sin                   5. Cos                   6. Tan")
    print("7. ArcSin                8. ArcCos                9. ArcTan")
    print("10. Sinh                 11. Cosh                 12. Tanh")
    
    print(f"\n{Colors.GREEN}📌 LOGARITHMIC & EXPONENTIAL{Colors.END}")
    print("13. Natural Log (ln)     14. Log Base 10          15. Log Base n")
    print("16. e^x                  17. n^x")
    
    print(f"\n{Colors.GREEN}📌 ADVANCED MATH{Colors.END}")
    print("18. Factorial (!)        19. GCD                  20. LCM")
    print("21. Permutation (nPr)    22. Combination (nCr)")
    print("23. Absolute Value       24. Round Number")
    
    print(f"\n{Colors.GREEN}📌 GEOMETRY{Colors.END}")
    print("25. Circle Area          26. Circle Circumference")
    print("27. Rectangle Area       28. Triangle Area")
    print("29. Sphere Volume        30. Cylinder Volume")
    
    print(f"\n{Colors.GREEN}📌 STATISTICS{Colors.END}")
    print("31. Mean                 32. Median               33. Mode")
    print("34. Standard Deviation   35. Variance")
    
    print(f"\n{Colors.GREEN}📌 CONVERSIONS{Colors.END}")
    print("36. Degrees to Radians   37. Radians to Degrees")
    print("38. Celsius to Fahrenheit 39. Fahrenheit to Celsius")
    print("40. Binary to Decimal    41. Decimal to Binary")
    print("42. Hex to Decimal       43. Decimal to Hex")
    
    print(f"\n{Colors.GREEN}📌 OTHER{Colors.END}")
    print("44. Expression Evaluator 45. Memory Store/Recall")
    print(f"{Colors.RED}0. Exit{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")

def get_number(prompt="Enter number: "):
    while True:
        try:
            return float(input(f"{Colors.CYAN}{prompt}{Colors.END}"))
        except ValueError:
            print(f"{Colors.RED}Invalid input! Please enter a valid number.{Colors.END}")

def get_numbers_list(prompt="Enter numbers separated by commas: "):
    while True:
        try:
            nums = input(f"{Colors.CYAN}{prompt}{Colors.END}").split(',')
            return [float(n.strip()) for n in nums]
        except ValueError:
            print(f"{Colors.RED}Invalid input! Please enter valid numbers.{Colors.END}")

def display_result(result, label="RESULT"):
    """Display result in a prominent colored box"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{label}: {Colors.HEADER}{result}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")

def continuous_calculator():
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🔢 CONTINUOUS CALCULATOR{Colors.END}")
    print(f"{Colors.GREEN}Perform multiple operations in sequence!{Colors.END}")
    print(f"{Colors.CYAN}Operations: + - * / ** // % √{Colors.END}")
    print(f"{Colors.YELLOW}Type 'done' to finish, 'clear' to start over{Colors.END}\n")
    
    result = get_number("Enter starting number: ")
    print(f"{Colors.BOLD}{Colors.GREEN}Current result: {result}{Colors.END}")
    
    while True:
        operation = input(f"\n{Colors.CYAN}Enter operation (or 'done'/'clear'): {Colors.END}").strip().lower()
        
        if operation == 'done':
            display_result(result, "FINAL RESULT")
            break
        
        if operation == 'clear':
            result = get_number("Enter new starting number: ")
            print(f"{Colors.BOLD}{Colors.GREEN}Current result: {result}{Colors.END}")
            continue
        
        if operation == '√':
            if result < 0:
                print(f"{Colors.RED}Error: Cannot take square root of negative number{Colors.END}")
                continue
            result = math.sqrt(result)
            print(f"{Colors.BOLD}{Colors.GREEN}√ → {result}{Colors.END}")
            continue
        
        if operation in ['+', '-', '*', '/', '//', '%', '**']:
            num = get_number("Enter number: ")
            
            try:
                if operation == '+':
                    result = result + num
                elif operation == '-':
                    result = result - num
                elif operation == '*':
                    result = result * num
                elif operation == '/':
                    if num == 0:
                        print(f"{Colors.RED}Error: Division by zero!{Colors.END}")
                        continue
                    result = result / num
                elif operation == '//':
                    if num == 0:
                        print(f"{Colors.RED}Error: Division by zero!{Colors.END}")
                        continue
                    result = result // num
                elif operation == '%':
                    if num == 0:
                        print(f"{Colors.RED}Error: Division by zero!{Colors.END}")
                        continue
                    result = result % num
                elif operation == '**':
                    result = result ** num
                
                print(f"{Colors.BOLD}{Colors.GREEN}→ {result}{Colors.END}")
            
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid operation!{Colors.END}")

def basic_operations():
    a = get_number("Enter first number: ")
    op = input(f"{Colors.CYAN}Enter operation (+, -, *, /, //, %, **): {Colors.END}")
    b = get_number("Enter second number: ")
    
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        '//': lambda x, y: x // y if y != 0 else "Error: Division by zero",
        '%': lambda x, y: x % y if y != 0 else "Error: Division by zero",
        '**': lambda x, y: x ** y
    }
    
    result = operations.get(op, lambda x, y: "Invalid operation")(a, b)
    display_result(result)

def trigonometric(func_name):
    angle = get_number(f"Enter angle in degrees for {func_name}: ")
    radians = math.radians(angle)
    
    functions = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'sinh': math.sinh,
        'cosh': math.cosh,
        'tanh': math.tanh
    }
    
    if func_name in functions:
        result = functions[func_name](radians)
        display_result(result, f"{func_name}({angle}°)")

def inverse_trig(func_name):
    value = get_number(f"Enter value for {func_name}: ")
    
    functions = {
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan
    }
    
    try:
        result_deg = math.degrees(functions[func_name](value))
        display_result(f"{result_deg}°", f"{func_name}({value})")
    except ValueError:
        print(f"{Colors.RED}Error: Value out of range for this function{Colors.END}")

def logarithmic():
    choice = input("1. ln  2. log10  3. log_n: ")
    
    if choice == '1':
        x = get_number("Enter number: ")
        display_result(math.log(x), f"ln({x})")
    elif choice == '2':
        x = get_number("Enter number: ")
        display_result(math.log10(x), f"log10({x})")
    elif choice == '3':
        x = get_number("Enter number: ")
        base = get_number("Enter base: ")
        display_result(math.log(x, base), f"log_{base}({x})")

def factorial_calc():
    n = int(get_number("Enter non-negative integer: "))
    if n < 0:
        print(f"{Colors.RED}Factorial not defined for negative numbers{Colors.END}")
    else:
        display_result(math.factorial(n), f"{n}!")

def gcd_calc():
    a = int(get_number("Enter first integer: "))
    b = int(get_number("Enter second integer: "))
    display_result(math.gcd(a, b), f"GCD({a}, {b})")

def lcm_calc():
    a = int(get_number("Enter first integer: "))
    b = int(get_number("Enter second integer: "))
    lcm = abs(a * b) // math.gcd(a, b) if a and b else 0
    display_result(lcm, f"LCM({a}, {b})")

def permutation():
    n = int(get_number("Enter n: "))
    r = int(get_number("Enter r: "))
    result = math.factorial(n) // math.factorial(n - r) if n >= r >= 0 else "Invalid"
    display_result(result, f"P({n}, {r})")

def combination():
    n = int(get_number("Enter n: "))
    r = int(get_number("Enter r: "))
    result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r)) if n >= r >= 0 else "Invalid"
    display_result(result, f"C({n}, {r})")

def circle_calculations():
    r = get_number("Enter radius: ")
    choice = input(f"{Colors.CYAN}1. Area  2. Circumference: {Colors.END}")
    if choice == '1':
        display_result(math.pi * r ** 2, "Circle Area")
    else:
        display_result(2 * math.pi * r, "Circle Circumference")

def rectangle_area():
    length = get_number("Enter length: ")
    width = get_number("Enter width: ")
    display_result(length * width, "Rectangle Area")

def triangle_area():
    base = get_number("Enter base: ")
    height = get_number("Enter height: ")
    display_result(0.5 * base * height, "Triangle Area")

def sphere_volume():
    r = get_number("Enter radius: ")
    display_result((4/3) * math.pi * r ** 3, "Sphere Volume")

def cylinder_volume():
    r = get_number("Enter radius: ")
    h = get_number("Enter height: ")
    display_result(math.pi * r ** 2 * h, "Cylinder Volume")

def statistics_calc(func_name):
    numbers = get_numbers_list()
    
    functions = {
        'mean': statistics.mean,
        'median': statistics.median,
        'mode': statistics.mode,
        'stdev': statistics.stdev,
        'variance': statistics.variance
    }
    
    try:
        result = functions[func_name](numbers)
        display_result(result, func_name.capitalize())
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def conversions(conv_type):
    if conv_type == 'deg_to_rad':
        deg = get_number("Enter degrees: ")
        display_result(f"{math.radians(deg)} radians", f"{deg}°")
    elif conv_type == 'rad_to_deg':
        rad = get_number("Enter radians: ")
        display_result(f"{math.degrees(rad)}°", f"{rad} rad")
    elif conv_type == 'c_to_f':
        c = get_number("Enter Celsius: ")
        display_result(f"{(c * 9/5) + 32}°F", f"{c}°C")
    elif conv_type == 'f_to_c':
        f = get_number("Enter Fahrenheit: ")
        display_result(f"{(f - 32) * 5/9}°C", f"{f}°F")
    elif conv_type == 'bin_to_dec':
        b = input(f"{Colors.CYAN}Enter binary: {Colors.END}")
        display_result(f"{int(b, 2)} (decimal)", f"{b} (binary)")
    elif conv_type == 'dec_to_bin':
        d = int(get_number("Enter decimal: "))
        display_result(f"{bin(d)[2:]} (binary)", f"{d} (decimal)")
    elif conv_type == 'hex_to_dec':
        h = input(f"{Colors.CYAN}Enter hex: {Colors.END}")
        display_result(f"{int(h, 16)} (decimal)", f"{h} (hex)")
    elif conv_type == 'dec_to_hex':
        d = int(get_number("Enter decimal: "))
        display_result(f"{hex(d)[2:].upper()} (hex)", f"{d} (decimal)")

def expression_evaluator():
    expr = input(f"{Colors.CYAN}Enter expression (e.g., 2+3*4): {Colors.END}")
    try:
        result = eval(expr)
        display_result(result, f"{expr}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def main():
    memory = 0
    print(f"{Colors.BOLD}{Colors.HEADER}🎉 Welcome to Advanced Calculator! 🎉{Colors.END}\n")
    
    while True:
        display_menu()
        choice = input(f"\n{Colors.BOLD}{Colors.YELLOW}Enter choice: {Colors.END}")
        
        if choice == '0':
            print(f"{Colors.BOLD}{Colors.HEADER}Thank you for using Advanced Calculator! 👋{Colors.END}")
            break
        
        try:
            if choice == '1':
                continuous_calculator()
            elif choice == '2':
                basic_operations()
            elif choice == '3':
                n = get_number()
                display_result(math.sqrt(n), f"√{n}")
            elif choice == '4':
                trigonometric('sin')
            elif choice == '5':
                trigonometric('cos')
            elif choice == '6':
                trigonometric('tan')
            elif choice == '7':
                inverse_trig('asin')
            elif choice == '8':
                inverse_trig('acos')
            elif choice == '9':
                inverse_trig('atan')
            elif choice == '10':
                trigonometric('sinh')
            elif choice == '11':
                trigonometric('cosh')
            elif choice == '12':
                trigonometric('tanh')
            elif choice == '13':
                x = get_number()
                display_result(math.log(x), f"ln({x})")
            elif choice == '14':
                x = get_number()
                display_result(math.log10(x), f"log10({x})")
            elif choice == '15':
                logarithmic()
            elif choice == '16':
                x = get_number("Enter x for e^x: ")
                display_result(math.exp(x), f"e^{x}")
            elif choice == '17':
                n = get_number("Enter base: ")
                x = get_number("Enter exponent: ")
                display_result(n ** x, f"{n}^{x}")
            elif choice == '18':
                factorial_calc()
            elif choice == '19':
                gcd_calc()
            elif choice == '20':
                lcm_calc()
            elif choice == '21':
                permutation()
            elif choice == '22':
                combination()
            elif choice == '23':
                n = get_number()
                display_result(abs(n), f"|{n}|")
            elif choice == '24':
                n = get_number()
                decimals = int(get_number("Decimal places: "))
                display_result(round(n, decimals), f"Round({n}, {decimals})")
            elif choice == '25' or choice == '26':
                circle_calculations()
            elif choice == '27':
                rectangle_area()
            elif choice == '28':
                triangle_area()
            elif choice == '29':
                sphere_volume()
            elif choice == '30':
                cylinder_volume()
            elif choice == '31':
                statistics_calc('mean')
            elif choice == '32':
                statistics_calc('median')
            elif choice == '33':
                statistics_calc('mode')
            elif choice == '34':
                statistics_calc('stdev')
            elif choice == '35':
                statistics_calc('variance')
            elif choice == '36':
                conversions('deg_to_rad')
            elif choice == '37':
                conversions('rad_to_deg')
            elif choice == '38':
                conversions('c_to_f')
            elif choice == '39':
                conversions('f_to_c')
            elif choice == '40':
                conversions('bin_to_dec')
            elif choice == '41':
                conversions('dec_to_bin')
            elif choice == '42':
                conversions('hex_to_dec')
            elif choice == '43':
                conversions('dec_to_hex')
            elif choice == '44':
                expression_evaluator()
            elif choice == '45':
                action = input(f"{Colors.CYAN}1. Store  2. Recall  3. Clear: {Colors.END}")
                if action == '1':
                    memory = get_number("Enter value to store: ")
                    print(f"{Colors.GREEN}Stored: {memory}{Colors.END}")
                elif action == '2':
                    print(f"{Colors.YELLOW}Memory: {memory}{Colors.END}")
                elif action == '3':
                    memory = 0
                    print(f"{Colors.GREEN}Memory cleared{Colors.END}")
            else:
                print(f"{Colors.RED}Invalid choice!{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    main()
