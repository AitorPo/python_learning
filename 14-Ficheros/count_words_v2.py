text = ('Hola, estamos haciendo un ejercicio de conteo de palabras, para ello tendrás que limpiar dichas palabras.'
        ' Hola, ya que queremos contar palabras el contenido de estos textos será repetitivo en cuanto a palabras se refiera')

def clearText(text):
    stringText = str(text)
    return stringText.lower().replace(',', '').replace('.', '')

def countWords(text):
    listOfWords = clearText(text).split()

    eachWord = []
    for word in listOfWords:
        eachWord.append(listOfWords.count(word))

    print(str(list(zip(listOfWords, eachWord))))    

countWords(text)
