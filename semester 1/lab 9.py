import csv

with open("salaries.csv") as csvfile:
    rows = list(csv.reader(csvfile))[1:]

    # `rows` is now a list of lists containing the rows of the CSV

    # For example

    # rows[0] is the first row of the file
    # rows[0][0] is the first value in the first row

    # Compute and display the following items as detailed in the readme

    # 1. The total number of salaries in the file (remember not to include the header row)
    totalsal = 0

    for row in rows:
        totalsal += 1

    print(f"there are {totalsal} total sallaries")
              
    # 2. The average (mean) salary for entry-level positions
    elmean = 0 
    totalmean = 0

    for row in rows:
        if row[1] == "EN":
            elmean +=1
            totalmean += int(row[4])
        averagemean = totalmean / elmean

    print(f"The average salary for entry-level posititions is ${averagemean}")
    

    # 3. The average (mean) salary for entry-level positions with a Data Scientist Title
    eldatamean = 0 
    totaldatamean = 0

    for row in rows:
        if row[1] == "EN" and row[3] == "Data Scientist":
            eldatamean +=1
            totaldatamean += int(row[4])
        averagemean = totaldatamean / eldatamean

    print(f"The average salary for entry-level Data Scientist posititions is ${averagemean}")
    

    # 4. The highest salary for a fully remote, entry-level position
    fullremotesal = 0 

    for row in rows:
        if row[1] == "EN" and row[6] == "100":
            if int(fullremotesal) < int(row[4]):
                fullremotesal = row[4]

    print(f"The highest salary for entry-level fully remote posititions is ${fullremotesal}")
    

    # 5. The average (mean) salary for all mid-level positions
    mlmean = 0 
    totalmlmean = 0

    for row in rows:
        if row[1] == "MI":
            mlmean += 1
            totalmlmean += int(row[4])
            averagemlmean = totalmlmean / mlmean

    print(f"The average salary for all mid-level posititions is ${averagemlmean}")
    

    # 6. A descriptive statistic of your choice calculated from this dataset
    # Average salary of all mid-level software enginieers 
    softengamean = 0 
    totalsoftamean = 0

    for row in rows:
        if row[1] == "MI" and row[3] == "Software Enginieer":
            softengamean +=1
            totalsoftamean += int(row[4])
            averagemean = totalsoftamean / softengamean

    print(f"The average salary for a mid-level Software Enginieer is ${averagemean}")
    