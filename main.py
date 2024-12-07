student_data = {'id1':
  {'name':['sara'],
   'class': ['V'],
   'subject_integration': ['maths']
  },
  'id2':
  {'name':['david'],
   'class': ['V'],
   'subject_integration': ['sceince']
  },
  'id3':
  {'name':['zara'],
   'class': ['V'],
   'subject_integration': ['english']
  }
  }
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        print(result)
test_dict = {'codingal'  : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding : 1'}
print("the oringinal dictionary :" + str(test_dict))
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("frequency of K is :" + str(res))
SPCMcountry_code = {'India' : '0091'}
print("country code for India -")
print("country_code.get('India), 'Not found")
