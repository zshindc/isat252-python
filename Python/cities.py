def writing():
    # Create list of strings
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    outfile = open('cities.txt', 'w')

    for item in cities:
        outfile.write(item + '\n')

    outfile.close()

def main():
    writing()

    infile = open('cities.txt', 'r')

    cities = infile.readlines()

    infile.close()

    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

print(cities)

main()
