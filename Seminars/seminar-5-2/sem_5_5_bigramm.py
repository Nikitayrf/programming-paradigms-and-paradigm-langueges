text= "Machine learning is a subfield of artificial intelligence that focuses on the interaction between " \
     "computers and humans. Machine learning involves the use of algorithms and statistical models to enable " \
     "computers to perform tasks without explicit programming. In machine learning, data plays a crucial role." \
     " Data is used to train the algorithms and improve their performance over time. Machine learning has " \
     "applications in various fields, including natural language processing, image recognition, and autonomous vehicles."

# Разделяем текст на слова, приводим к нижнему регистру и получаем список слов
words = text.lower().split()

# Создаем словарь для хранения пар слов и их количества
word_pairs = {}

# Проходим по списку слов с шагом 2, чтобы образовать биграммы
for i in range(len(words) - 1):
    # Формируем биграмму из текущего слова и следующего слова
    word_pair = (words[i], words[i + 1])

    # Если биграмма уже есть в словаре, увеличиваем счетчик
    if word_pair in word_pairs:
        word_pairs[word_pair] += 1
    else:
    # Если биграммы нет в словаре, добавляем ее и устанавливаем счетчик в 1
        word_pairs[word_pair] = 1

# Проходим по словарю биграмм и их количества
for word_pair, count in word_pairs.items():
    # Если количество больше 2, выводим биграмму и количество
    if count > 2:
        print(f"Word pair: {word_pair}, Count: {count}")