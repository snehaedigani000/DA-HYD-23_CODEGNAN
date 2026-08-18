#Task:Create a dictionary with your personal details,similar to your
#Codegnan Profile
details = {
    'ID': 'CGH4017',
    'name': 'Edigani.Sneha',
    'Gender': 'Female',
    'Age': 22,
    'Batch': 'DA-HYD-023',
    'place': 'HYDERABAD'
}

print(details)
print(len(details))

print(details.keys())
print(details['ID'], details['name'])

# Skills
details['Skills'] = []
details['Skills'].append('Python')
details['Skills'].extend(['MySQL', 'Pandas', 'Data Analytics'])
print(details)

# Percentage
details['Percentage'] = []
details['Percentage'].append(72)
details['Percentage'].extend([97, 67])
print(details)

# Education
details['Education'] = []
details['Education'].append('B.Tech')
details['Education'].extend(['12th', '10th'])
print(details)

# Accessing data
print(details['Skills'][2])
print(details['Education'][1])

# get()
print(details.get('name'))
print(details.get('College'))

# setdefault()
details.setdefault('College')
print(details)

# update()
details.update({'College': 'MLRITM', 'Branch': 'CSE'})
print(details)
