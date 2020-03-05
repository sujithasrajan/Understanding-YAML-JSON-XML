import yaml


#Creating the catalogue mentioned in the file as a list of similar elements represented as Key Value pairs.
catalogue_list = [{"Title": "Empire Birlesque", "Artist":"Bob Dylan", "Price": 10.90,"Year":1985},{"Title": "Hide your heart", "Artist":"Bonnie Tyler", "Price":9.90 ,"Year":1988},
                  {"Title": "Still got the blues", "Artist":"Gary Moore","Price":10.20 ,"Year":1990},{"Title": "Eros", "Artist":"Eros Ramazzotti", "Price":9.90 ,"Year":1997},
                  {"Title": "For the good times", "Artist":"Kenny Rogers", "Price":8.70 ,"Year":1995}]
#Represents the YAML object
root = {"company": {"header": {"Company_name":"CoolCDs Inc", "Address":{"street":"678 Main street", "city":"Frederick", "state":"MD", "zip_code":21703}}, "catalogue": catalogue_list}}

#Converting the YAML object to a string
yaml_str = yaml.dump(root)

print(yaml_str)

#Saving the YAML represntation in a file called HW1Q1.txt
fh = open("HW1Q1.txt","w")
yaml.dump(root, fh)

