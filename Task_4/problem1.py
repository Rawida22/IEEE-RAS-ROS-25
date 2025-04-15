
def count_occurrences(filename):
    word_counts = {}
    try:
        filename = "/home/rawida-hany/sample.txt"
        with open(filename,'r',encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    if word in word_counts:
                      word_counts[word] +=1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print(f"{filename} is not exist")
    except Exception as e :
        print(f" an unexcepected error with {e}")
        return word_counts
if __name__ == 'main':
    word_counts = count_occurrences('sample.txt')
    print(word_counts)                              