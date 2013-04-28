'''
Kody Alan Kantor
Weather Research

Creating a program to parse a data file and create a comma separated value file.

Mod History:
4-24-13: Original compilation.
    Converts one line of the file into an array.
4-25-13: Parsed the relevant information from the file.
    Created a text file of the relevant information.
    The file is comma-separated-values

notes: condense the loops. There shouldn't be 5 loops.

'''
file = open ('MunicipalTextData.txt', 'r')
fields = []
file.readline()
string = file.readline()
count = 0
i = 0
j = 0

while len(string) > 0:
    fields.append(string.split(" "))
    string = file.readline()
    count = count + 1

while i < len(fields):
    while j < len(fields[i]):
        if len(fields[i][j]) is 0:
            fields[i].remove(fields[i][j])
        else: j = j + 1
    i = i + 1
    j = 0




hold = ""
dataArray = []
data = []
i = 0
while i < len(fields):
    string = fields[i][2]
    hold = string[0:4] + "-" + string[4:6] + "-" + string[6:8]
    dataArray.append (hold)
    hold = string[8:10] + ":" + string [10:12]
    dataArray.append (hold)
    dataArray.append (fields[i][3])#wind direction (degrees)
    dataArray.append (fields[i][4])#wind speed (mph)
    dataArray.append (fields[i][7])#sky condition
    dataArray.append (fields[i][21])#temperature
    string = fields[i][28]
    hold = string[0:4]
    dataArray.append (hold)
    data.append      (dataArray)
    dataArray = []
    i = i + 1

destination = open ("WeatherData.txt", 'a')

i = 0
while i < len(data):
    commaList = ",".join(data[i])+"\n"
    print (destination.write(commaList))
    i = i + 1

file.close()

destination.close()



