def main():
    # Get the name of a file.
    filename = input('enter a filename: ')

    try:
        # open the file
        infile = open(filename, 'r')

        # Read the file's contents
        contents = infile.read()

        print(contents)

        infile.close()

    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

main()
