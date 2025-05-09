import csv
def get_class(average):
    if average >= 70:
        return "1"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3"
    else:
        return "F"

inputFile = input("Enter the student file name:")
outputFile = inputFile + "_out.csv"

with open(inputFile, 'r') as infile, open(outputFile, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if not row or not row[0].isdigit():
            continue
        
        student_id = row[0]
        grades = [int(g) for g in row[1:] if g.strip() != '']

        average = sum(grades) / len(grades)
        classification = get_classification(average)

        writer.writerow([student_id, f"{average:.2f}", classification])