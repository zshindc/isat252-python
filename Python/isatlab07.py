if __name__=="__main__":
    #variable to hold file data
    file=None

    #requesting filename from user till user enter valid name
    while file==None:
        filename=input("Enter the name of the file: ")

        #opening respective files
        if (filename.lower()=="labph.txt"):
            file=open("LabpH.txt", 'r')
        elif(filename.lower()=="turbidity.txt"):
            file=open("Turbidity.txt", 'r')
        else:
            print("Invalid file")

        i=0
        columnName=None
        count=0
        sum=0

        for line in file:
            try:
                if(i==0):
                    columnName=line.replace('\n','').replace('\r','')
                    i+=1
                else:
                    value=float(line.replace('\n',''))
                    sum+=value
                    count+=1
                except ValueError:
                    print("Invalid input found = "+line)

        avg=sum/count

        print("Average reading for "+columnName+" = "+str(round(avg,2)))
