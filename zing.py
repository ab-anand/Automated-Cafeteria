s = "coke", "iry"
t = {"Coke": 1}


def sp(s):
    s = [x.lower() for x in s]
    # s = list(map(str, s.split()))
    print(s)


sp(t)
