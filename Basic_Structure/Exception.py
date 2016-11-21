while True:
    try:
        number=int(input('Enter a number\n'))
        print(18/number)
        break
    except ValueError:
        print('You must enter a Valid number')
    except ZeroDivisionError:
        print('Avoid Zero')
    finally:
        print('Iteration Complete')
