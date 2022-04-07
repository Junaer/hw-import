from application.salary import calculate_salary
from application.db.people import get_employees
print ('main start')

if __name__ == '__main__':
    calculate_salary()
    get_employees()