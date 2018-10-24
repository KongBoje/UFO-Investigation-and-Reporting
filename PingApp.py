import timeit

URLSERVERS = [
    'http://128.199.144.199:8080',
    'http://167.99.51.33:8080',
    'http://46.101.253.149:8080'
]

snippet = '''
import requests
requests.get('{}')
'''

def take_ping_time(snippet, iteration):
    setup = '''print()'''

    time_total = timeit.timeit(setup = setup,
                               stmt = snippet,
                               number = iteration)

    average_time = time_total / iteration

    print('time_total = {}'.format(time_total))
    print('average_time = {}'.format(average_time))

def main():
    for URL in URLSERVERS:
        take_ping_time(snippet.format(URL), 100)

if __name__ == '__main__':
    main()