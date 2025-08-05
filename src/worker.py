from redis import Redis
import sys

client = Redis()

def watch_links_data(name):

    while True:
        print(f'Worker {name} started')
        link = client.blpop('links')  # Blocking Left Pop
        print(link)
        print(f'Worker {name} ended')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise KeyError("Worker name is required")
    watch_links_data(sys.argv[1])