from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_functions = time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_functions = time()

print(f"Работа функций: {end_functions - start_functions:.6f} секунд")

start_threads = time()

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_threads = time()

print(f"Работа потоков: {end_threads - start_threads:.6f} секунд")