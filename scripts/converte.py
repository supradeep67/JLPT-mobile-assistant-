import json
import csv
 # making a script that take user file path ( csv )  and desire file name and convert into a json file
your_cvs = input ( " please input your csv dile path : ")
print ( " please make sure that you have written '.json' at the end of the your file name eg, filename.json ")
your_json_file_name = input(" please  enter the  tergeted json file name  ")


csv_file = your_cvs 
json_file =  your_json_file_name

data = []


with open (csv_file , encoding= 'utf-8') as m :
    read = csv.DictReader(m)

    for  row in read:
        data.append(row) 

        with open ( json_file, 'w', encoding= 'utf-8') as  r :
            json.dump(data, r , ensure_ascii=False , indent=4)

print ( " file convertion is sucessfull go and check it out ! " ,{ json_file})

