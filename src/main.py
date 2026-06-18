import processamento_de_dados as pdd
import os

words_list = {}
data_path = os.path.join('data', 'text')
savement_path = "data/processed/words_list.json"

for period in os.listdir(data_path):

    period_path = os.path.join(data_path, period)

    if os.path.isdir(data_path):

        words_list[period] = []
        for file in os.listdir(period_path):
            if file.endswith("txt"):

                file_path = os.path.join(period_path, file)
                words = pdd.load_words(file_path)
        
            frequency = {}
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1

            words_list[period].append(frequency)

pdd.list_write(savement_path, words_list)