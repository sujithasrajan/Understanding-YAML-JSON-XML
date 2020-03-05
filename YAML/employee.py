import yaml

skills1 = ['python','C/C++','Pascal']
skills2 = ['Java','RESTful API','TestNG']
skills3 = ['Maven','Git']
skills4 = ['Project Management','Scrum']

emp_details = [{"name":{"first":"Joe", "last":"Apple"},"ID": 5674882, "Age": 26, "Position": "Programmer", "Skills": skills1},
               {"name":{"first":"Alex", "last":"Pear"},"ID": 8635820, "Age": 34, "Position": "Tester", "Skills": skills2},
               {"name":{"first":"Jenny", "last":"Orange"},"ID": 7800356, "Age": 31, "Position": "AQ Eng", "Skills": skills3},
               {"name":{"first":"Peter", "last":"Nuts"},"ID": 7849080, "Age": 47, "Position": "Manager", "Skills": skills4}]
            

root = {"company":{"name":"KingSoft.Inc","employee":emp_details}} 

yaml_str = yaml.dump(root)

fh = open("LAB1_Q1.txt","w")
yaml.dump(root, fh)
