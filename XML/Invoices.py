from lxml import etree as et

root = et.Element('invoice')

#CHILD0
child = et.SubElement(root,'InvoiceNo')
child.text = '56889456'

#CHILD1
child1 = et.SubElement(root,'billing') 

child1_1 = et.SubElement(child1,'name')
child1_1.text = 'Smart Computer Depot'

child1_2 = et.SubElement(child1,'phno')
child1_2.text = '765-555-1234'

child1_3 = et.SubElement(child1,'addr', units='street addr')
child1_3.text = '57 Stream Lane'

child1_4 = et.SubElement(child1,'addr', units='city')
child1_4.text = 'Bell Gardens'

child1_5 = et.SubElement(child1,'addr', units='state')
child1_5.text = 'CA'

child1_6 = et.SubElement(child1,'addr', units='zip')
child1_6.text = '90201'



#CHILD2
child2 = et.SubElement(root,'billed')

child2_1 = et.SubElement(child2,'name')
child2_1.text = 'Awesome software Inc'

child2_2 = et.SubElement(child2,'phno')
child2_2.text = '568-163-0798'

child2_3 = et.SubElement(child2,'addr', units='street addr')
child2_3.text = '68 Main Street'


child2_4 = et.SubElement(child2,'addr', units='city')
child2_4.text = 'Crystal Lake'

child2_5 = et.SubElement(child2,'addr', units='state')
child2_5.text = 'IL'

child2_6 = et.SubElement(child2,'addr', units='zip')
child2_6.text = '60014'

#CHILD3

child3 = et.SubElement(root,'items')

#child3-1

child3_1 = et.SubElement(child3,'item')

child3_1_1 = et.SubElement(child3_1,'name')
child3_1_1.text = 'Laptop'

child3_1_2 = et.SubElement(child3_1,'StockNo')
child3_1_2.text = '35463'

child3_1_3 = et.SubElement(child3_1,'UnitCost')
child3_1_3.text = '12000.00'

child3_1_4 = et.SubElement(child3_1,'Quantity')
child3_1_4.text = '2'

child3_1_5 = et.SubElement(child3_1,'Amount', units='USD')
child3_1_5.text = '2400.00'

child3_1_6 = et.SubElement(child3_1,'Amount', units='EUR')
child3_1_6.text = '2192.68'


#child3-2

child3_2 = et.SubElement(child3,'item')

child3_2_1 = et.SubElement(child3_2,'name')
child3_2_1.text = 'Monitor'

child3_2_2 = et.SubElement(child3_2,'StockNo')
child3_2_2.text = '12573'

child3_2_3 = et.SubElement(child3_2,'UnitCost')
child3_2_3.text = '150.00'

child3_2_4 = et.SubElement(child3_2,'Quantity')
child3_2_4.text = '5'

child3_2_5 = et.SubElement(child3_2,'Amount', units='USD')
child3_2_5.text = '750.00'

child3_2_6 = et.SubElement(child3_2,'Amount', units='EUR')
child3_2_6.text = '685.21'

#child3-3

child3_3 = et.SubElement(child3,'item')

child3_3_1 = et.SubElement(child3_3,'name')
child3_3_1.text = 'Mouse'

child3_3_2 = et.SubElement(child3_3,'StockNo')
child3_3_2.text = '68005'

child3_3_3 = et.SubElement(child3_3,'UnitCost')
child3_3_3.text = '30.00'

child3_3_4 = et.SubElement(child3_3,'Quantity')
child3_3_4.text = '5'

child3_3_5 = et.SubElement(child3_3,'Amount', units='USD')
child3_3_5.text = '150.00'

child3_3_6 = et.SubElement(child3_3,'Amount', units='EUR')
child3_3_6.text = '137.04'

child4 = et.SubElement(root, 'TotalBilled', units='USD')
child4.text = '3300.40'

child5 = et.SubElement(root, 'TotalBilled', units='EUR')
child4.text = '3014.94'

xml_str = et.tostring(root, xml_declaration=True, pretty_print=True).decode('utf-8')
                                                                            
print(xml_str)

