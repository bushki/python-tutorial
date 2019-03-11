# iterate over list, tuple, set, dictionary, string

# for loop
people = ['John', 'Paul', 'Sara', 'Steve']

for person in people:
    print(f'Person: {person}')

# break out of loop
for person in people:
    if person == 'Sara':
        break
    print(f'Person: {person}')

print('*********')

# Continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Person: {person}')

print('*********')
# range
for i in range(len(people)):
    print(people[i])

for i in range(1, 11):  # does not include 11
    print(f'number: {i}')

# while loops
print('*********')
count = 0
while count <= 15:
    print(f'count: {count}')
    count += 1
