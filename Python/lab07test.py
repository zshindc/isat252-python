# Program that displays average value of file data
# Programmer: Zachary Shin
# Language: Python 3.7.x
# lab07.py

def calculateAverage(filename):

    #Open input file
    inputFile = open(filename, 'r')
    count = 0
    sum = 0
    for line in filename:
        list = line.split(' ')
        sum = sum + int(list[1])
        count = count + 1
    print("The average of the first column of readings is ", sum/count)

inputFile.close()

def main():
    # Input name of file
    filename = input("Enter the filename you wish to open: ")

        if (filename.lower()=="labph.txt"):
            file=open("LabpH.txt", 'r')
            calculateAverage(filename)
        elif(filename.lower()=="turbidity.txt"):
            file=open("Turbidity.txt", 'r')
            calculateAverage(filename)
        else:
            print("Invalid file")
    

main()

for line in inputFile:

            # Convert line to a float
            amount = float(line)
            total += amount
            count += 1
            average = total / count
            
        # Close the file
        inputFile.close()

        print(format(amount, '.2f'))
        print(format(average, '.2f'))
