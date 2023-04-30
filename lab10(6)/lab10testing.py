# 1
""" def count_chars(filename):
    with open(filename, 'r', encoding='windows-1251') as f:
        text = f.read().lower()
        char_count = {}
        for char in text:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count


filename1 = 'Dostoevskiy Fedor. Prestuplenie i nakazanie - BooksCafe.Net.txt'
filename2 = 'Dostoevskiy Fedor. Igrok - BooksCafe.Net.txt'

char_count1 = count_chars(filename1)
char_count2 = count_chars(filename2)

print('Character count in', filename1, ':', char_count1)
print('Character count in', filename2, ':', char_count2) """

# 2
""" import os
import multiprocessing as mp


def count_chars(file_path, output):
    with open(file_path, 'r', encoding='windows-1251') as file:
        text = file.read().lower()
        char_count = {}
        for line in text:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        output.put(char_count)


if __name__ == '__main__':
    file_names = ['Dostoevskiy Fedor. Prestuplenie i nakazanie - BooksCafe.Net.txt',
                  'Dostoevskiy Fedor. Igrok - BooksCafe.Net.txt']
    output = mp.Queue()
    processes = []
    for file_name in file_names:
        p = mp.Process(target=count_chars, args=(file_name, output))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = [output.get() for p in processes]
    final_count = {}
    for count in results:
        for char, count in count.items():
            if char in final_count:
                final_count[char] += count
            else:
                final_count[char] = count

    print(final_count) """
