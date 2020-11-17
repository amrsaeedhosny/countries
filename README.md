# Countries

![GitHub](https://img.shields.io/github/license/amrsaeedhosny/countries)

This is the countries data stored in different file formats. The data has been constructed and organized with the help of [GeoNames](https://www.geonames.org) public data.

## Country Data

* English Name.
* Arabic Name.
* [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) Alpha-2 Code.
* [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) Alpha-3 Code.
* Phone Code.

## Availabe File Formats

* CSV:

English Name|Arabic Name|Alpha-2 Code|Alpha-3 Code|Phone Code
:-----:|:-----:|:-----:|:-----:|:-----:
Egypt|مصر|EG|EGY|20

* JSON:
```json
{
 "english_name": "Egypt",
 "arabic_name": "مصر",
 "alpha2_code": "EG",
 "alpha3_code": "EGY",
 "phone_code": "20"
}
```

* SQL:
```sql
INSERT INTO COUNTRY (ENGLISH_NAME, ARABIC_NAME, ALPHA2_CODE, ALPHA3_CODE, PHONE_CODE) VALUES('Egypt', 'مصر', 'EG', 'EGY', '20');
```

## Custom File Format

You can use the following python script to read countries data from **countries.csv** file, then you can rewrite them back to another file with a new format.
```python
import csv

my_file = open("my_file.txt", "w")

with open('countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_reader.next()
    for row in csv_reader:
        for column in row:
            my_file.write(column + ",")
        my_file.write("\n")

my_file.close()
```
