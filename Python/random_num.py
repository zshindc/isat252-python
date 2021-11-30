# Program that writes a series of random
# numbers to a random_num.txt and displays total of random numbers
# Progammer: Zachary Shin
# Language: Python  3.7.x
# random_num.py

# import the random module
import random

# define function of random number file writer (part 1)
def random_num():

    # open random_num.txt file for writing and assign variable
    random_numbers = open('random_num.txt', 'w')

    # input - get the number of generated random numbers 
    gen_nums = int(input('How many random numbers should be written to the file: '))

    # for loop generates random numbers based on input given
    for count in range (gen_nums):
        number = random.randint(1,500)

        # numbers converted to a string and written to random_num.txt file
        random_numbers.write(str(number)+ '\n')


    # close the file
    random_numbers.close()

    
# define main function or random number file reader (part 2)
def main():
    
    # call random_num function
    random_num()
    
    # open random_num.txt file for reading and assign variable
    random_numbers = open('random_num.txt', 'r')
    
    # initialize variables and constants
    gen_numbers = 0
    total = 0
    
    # display random numbers
    print("Here are the generated numbers:")
    for randoms in random_numbers.readlines():
        print(randoms)
        total = total+int(randoms)
        gen_numbers +=1
        
    # display total (sum) of random numbers
    print("Total of generated numbers: "+str(total))
    
    # displays number of random numbers told by input
    print("Number of the random numbers read from file: "+str(gen_numbers))
    
# call the main function
main()
