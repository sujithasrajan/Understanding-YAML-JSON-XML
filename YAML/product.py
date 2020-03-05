import yaml

fh = open("lab02_YAML_example.yaml","rt")

root = yaml.load(fh, Loader=yaml.FullLoader)

print("YAML OBJECT")
print(root)

print("Number of products")
print(len(root['product']))

print("Description and price of products")
for i in range(len(root['product'])):
    print(root['product'][i]['description'])
    print(root['product'][i]['price'])

print("SHIPTO Postal Code")
print(root['ship-to']['address']['postal'])

print("Sum of quantitie of all products")
sum = 0
for i in range(len(root['product'])):
    sum += root['product'][i]['quantity']
print(sum)
