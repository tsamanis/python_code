#! /usr/bin/env python
# https://www.techbeamers.com/python-dictionary/


dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("The student who left:", dict.get('Student Name'))
dict['Student Name'] = 'Larry'
print("The student who replaced: [Update]", dict.get('Student Name'))
dict['Student Name'] = 'Jarry'
print("The student who joined: [Addition]", dict.get('Student Name'))
