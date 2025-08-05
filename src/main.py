from utils.queue import Queue

def check_adv():                              # We assume these ara some filters that user enter and we wanna check'em
    for i in range(100):
        q = Queue()
        if i % 5 == 0:
            q.push('alert:1', i)
        elif i % 13 == 0:
            q.push('alert:2', i)
        elif i % 24 == 0:
            q.push('alert:3', i)
        elif i % 22 == 0:
            q.push('alert:4', i)
    print('Done')

if __name__ == "__main__":
    check_adv()