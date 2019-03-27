import texttable as tt


carlist = [
    ['DT-LT-87','Citroen','XM','1999-09-23',34500],
    ['GF-NX-07','Volkswagen','Polo',"1999-07-12",78000],
    ['GF-PD-34','Volkswagen','Polo',"1999-07-22",57500],
    ['KR-RT-65','Volkswagen','Golf',"1999-08-08",42000],
    ['PT-ER-45','Ford','Fiesta',"1999-03-02",25000],
    ['TT-PR-73','Citroen','XM','1999-03-02',1200],
    ['TT-RW-01','Volkswagen','Polo',"1999-11-14",4500]
]


tab = tt.Texttable()
header = ['Kenteken', 'Merk', 'Type', 'DatumAPK', 'Kilometerstand']
tab.header(header)

for c in carlist:
    tab.add_row(c)

draw = tab.draw()
print(draw)