students = int(input('What Are The Number Of Sudents? '))
names= list()
for name in range(1, students+1):
    name =input(f"Enter The {name} Of The Students")
    names.append(name)
print(names)
