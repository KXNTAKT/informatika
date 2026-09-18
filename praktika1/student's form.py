name=input('Ваше имя:')
age_str=input('Ваш возраст:')
subjects_str=input('Любимые предметы(через запятую):')

nm=str(name)
age=int(age_str)
subjects=list(subjects_str)

student = {'name':nm, 'age':age, 'subjects':subjects}

print('='*30)
print('АНКЕТА СТУДЕНТА')
print('='*30)
