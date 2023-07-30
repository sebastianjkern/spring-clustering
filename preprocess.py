def read_file():
    entries = []
    with open("data/weighted_network.txt", "r") as file:
        for line in file.readlines():
            m1, m2, weight = line.replace("\n", "").split(" ")

            entries.append([int(m1), int(m2), int(weight)])

    return entries
