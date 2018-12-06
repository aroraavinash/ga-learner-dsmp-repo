# --------------
# Given string
topper = 'andrew ng'


# Code starts here
name_first_last=topper.split()
first_name=name_first_last[0]
last_name=name_first_last[1]

full_name=last_name+" "+first_name
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


# --------------
# Code starts here
courses={'Math': 65,'English':70,'History':80,'French':70,'Science':60}
#print(courses.values())
total =0
for key in courses.keys():
  total+=courses[key]
print (total)

percentage = (total/500)*100
print(percentage)


# Code ends here


# --------------
# Code starts here

mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
max_score=0
for key in mathematics.keys():
  if mathematics.get(key) > max_score:
    max_score = mathematics.get(key)
    topper = key  

#topper=max(mathematics)
print(topper)



# Code ends here  


# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print(new_class)





# Code ends here


