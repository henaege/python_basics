# Exer
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
print(phonebook_dict["Elizabeth"])
phonebook_dict["Kareem"] = "938-489-1234"
del (phonebook_dict["Alice"])
phonebook_dict["Bob"] = "968-345-2345"for i in phonebook_dict:
print (i + ":" + phonebook_dict[i])Exer 2
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
 {
   'name': 'Jasmine',
   'email': 'jasmine@yahoo.com',
   'interests': ['photography', 'tennis']
 },
 {
   'name': 'Jan',
   'email': 'jan@hotmail.com',
   'interests': ['movies', 'tv']
 }
]
}

ramit["email"]
ramit["interests"][0]
ramit["friends"][0]["email"]
ramit["friends"][1]["interests"][1]exer3


def letter_histogram(word):
 count = {}
 count_num = 1
 for letter in word:
     if letter in count.keys():
        count[letter] += 1
    else:
        count[letter] = count_num
    print(count)

def letter_histogram2(paragraph):
    paragraph_in_words = paragraph.lower().split(" ")
    count = {}
    count_num = 1
    for letter in paragraph_in_words:
        if letter in count.keys():
            count[letter] += 1
        else:
            count[letter] = count_num
    print(count)




def max_letter(dict_max):
    max_key = ""
    new_dict = {}
    if len(dict_max.keys()) < 3:
        print ("You need at least three different letters in your word.")
    while len(new_dict.keys()) <= 2:
        max_num = 0
        for i in dict_max:
            if dict_max[i] > max_num:
                max_num = dict_max[i]
                max_key = i
        del (dict_max[max_key])
        new_dict[max_key] = max_num
    print(new_dict)


dict_max1 = {'to': 2, 'be': 2, 'or': 1, 'not': 1}
max_letter(dict_max1)

def find_home(list_input):
    final_dict = {}
    copy_list = list_input[:]
    for i in range(len(list_input)):
        if isinstance(list_input[i], bool):
            list_input[i] = str(list_input[i])
        count = 0
        for j in copy_list:
            if isinstance(j, bool):
                j = str(j)
            if list_input[i] == j:
                count += 1
        if count in final_dict.keys() and list_input[i] not in final_dict[count]:
            final_dict[count].append(list_input[i])
        else:
            final_dict[count] = [list_input[i]]
    print (final_dict)

list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
find_home(list1)
