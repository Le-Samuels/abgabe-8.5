import json

# Loading the JSON File in a dictionary

def get_person_data():
    file = open('data/person_db.json')
    person_data = json.load(file)
    return person_data 

def get_person_name(person_data):
   
    names = []
    for person in person_data:
        names.append(person["lastname"] + ", " +  person["firstname"])
    return names


#Bilder von den Personen



def find_person_data_by_name():
    suchstring  = get_person_name(person_data)

    # Teilt einen String in und speichert die Ergebnisse in einer Liste
    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    person_data = get_person_data()

    # Nun können wir vergleichen bis wir einen Treffer finden
    for eintrag in person_data:
        if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
            print(eintrag)

    

if __name__ == '__main__':
    print(get_person_data)
    print(get_person_name(person_data))