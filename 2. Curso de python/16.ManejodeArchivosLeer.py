
def run():
    with open('aleph.txt') as f:
        counter = 0
        for line in f:
            counter += line.count('Beatriz')

        print('Beatriz se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
    run()
