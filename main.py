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