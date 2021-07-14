text = ('Hola, estamos haciendo un ejercicio de conteo de palabras, para ello tendrás que limpiar dichas palabras.'
' Hola, ya que queremos contar palabras el contenido de estos textos será repetitivo en cuanto a palabras se refiera')
print(text)

def clearText(text):
    stringText = str(text)
    return stringText.lower().replace(',', '').replace('.', '')

def countWords(text):
    set = {}
    eachWord = text.split()
    for word in eachWord:
        if clearText(word) in set:
            set[clearText(word)] += 1
        else:
            set[clearText(word)] = 1
    print(set)

countWords(text)


