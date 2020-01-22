#============================================================================================================================================================================================
Dicti = dict() #Create Dictionary
LettersRus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', "Ъ", "Ы", "Ь", 'Э', 'Ю', 'Я',
'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', "ъ", "ы", "ь", 'э', 'ю', 'я'] 
LettersEng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LettersEngMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Create massives with letters
#============================================================================================================================================================================================
for i in range(192, 256):
    Dicti[i] = LettersRus[i-192] #Combine number and letter in our dictionary
for i in range(65,91):
    Dicti[i] = LettersEng[i-65]
for  i in range(97,123):
    Dicti[i] = LettersEngMin[i-97]
phrase = input("Введите фразу:") #Input phrase

def get_key(Dicti, value):
    for k, v in Dicti.items(): #Get key from value
        if v == value:
            return k

for i in phrase: #Divine Phrase on letters and analize them
    if i == " ":
        print("32")
    elif i == ".":
        print("46")
    else:
        print(get_key(Dicti, i)) #Go to function get_key