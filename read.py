from debater import Debater
def read(file):
    try:
        f = open(file)
    except:
        print("There is no input file! Create a file called '" + file + "' and add space seperated values that can then be parsed by the program")
        exit(1)
    #encode to debater object
    lines = f.read().split('\n')
    values = [l.split() for l in lines]
    debaters = [Debater(v[0],v[1],v[2]," ".join(v[3:])) for v in values]
    return debaters