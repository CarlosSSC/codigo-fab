#hOLA
def avarage(calific, mat):

    prom = sum(calific) / mat
    return prom

def validation(calific):

    cont = 0
    new_calific = []
    for cali in calific:
        if cali < 0 or cali > 10:
            new_calific = new_calific + [float(input(f"{cali} not is a a valid calification. Please enter a valid calification: "))]
    else:
        new_calific = new_calific + [calific[cont]]
        cont = cont + 1
    return new_calific

if __name__ == '__main__':
    while True:
        try:
            mat = int(input("Enter the number of the assignments: "))
            break
        except:
            print("Please enter a valid number as an integer, not a float or a string")

    while True:
        try:
            calific = list(map(str, input("Write the califications separated by space: ").rstrip().split()))

            if mat == len(calific):
                list_of_floats = [float(item) for item in calific]
                print(avarage(validation(list_of_floats), mat))
                break
            else:
                print("The number of the assignments is not equal to the number of the califications, please input again")
                print("Remember the number of the assignments is:", mat, "and separated by space")
        except ValueError:
            print("Invalid input, input again all the califications")
