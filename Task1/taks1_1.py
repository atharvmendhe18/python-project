jumbled_superheroes = ['DocToR_STRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

indices = []
decoded_names = []

for i in list(enumerate(jumbled_superheroes)):
    indices.append(i[0])
    decoded_names.append(i[1].replace('_',' ').lower())
length = lambda in_name: len(in_name)
name_lengths = list(map(length,decoded_names)) 
indices.sort(key=lambda x: name_lengths[x])

print('Phase 5 kickoff list:')

for i in list(enumerate(indices,1)):
    print(f"{i[0]}: {decoded_names[i[1]].title()}")