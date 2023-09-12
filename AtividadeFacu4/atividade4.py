salary = float(input("DIGITE SEU SALARIO: "))

if salary <= 400.00:
    print("Novo Salario: {:.2f}".format(salary * 0.15 + salary))
    print("Reajuste ganho: {:.2f}".format(salary * 0.15))
    print("Percentual: 15%")
elif salary >= 400.01 and salary <= 800.00:
    print("Novo Salario: {:.2f}".format(salary * 0.12 + salary))
    print("Reajuste ganho: {:.2f}".format(salary * 0.12))
    print("Percentual: 12%")
elif salary >= 800.01 and salary <= 1200.00:
    print("Novo Salario: {:.2f}".format(salary * 0.10 + salary))
    print("Reajuste ganho: {:.2f}".format(salary * 0.10))
    print("Percentual: 10%")
elif salary >= 1200.01 and salary <= 2000.00:
    print("Novo Salario: {:.2f}".format(salary * 0.07 + salary))
    print("Reajuste ganho: {:.2f}".format(salary * 0.07))
    print("Percentual: 7%")
elif salary >= 2000.01:
    print("Novo Salario: {:.2f}".format(salary * 0.04 + salary))
    print("Reajuste ganho: {:.2f}".format(salary * 0.04))
    print("Percentual: 4%")