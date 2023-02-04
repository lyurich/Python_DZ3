import re

word = input('Введие слово: ').upper()
dictionary = {'[AEIOULNSTR]': '1',
              '[DG]': '2',
              '[BCMP]': '3',
              '[FHVWY]': '4',
              'K': '5',
              '[JX]': '8',
              '[QZ]': '9',
              '[А, В, Е, И, Н, О, Р, С, Т]': '1',
              '[Д, К, Л, М, П, У]': '2',
              '[Б, Г, Ё, Ь, Я]': '3',
              '[Й, Ы]': '4',
              '[Ж, З, Х, Ц, Ч]': '5',
              '[Ш, Э, Ю]': '8',
              '[Ф, Щ, Ъ]': '9'}


for k in dictionary:
    word = re.sub(k, dictionary[k], word)
print(sum(map(int, word)))


