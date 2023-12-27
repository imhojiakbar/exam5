from pprint import pprint
import httpx
import asyncio
import requests

class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file
    def __exit__(self):
        self.file.close()


def description_data():
    with FileManager("../exam/005.txt", "r") as f:
        pprint(f)



def desriptions_request():
    url = 'http://164.92.64.76/desc/'
    response = requests.post(url).json()
    pprint(response)



if __name__ == '__main__':
    description_data()
    desriptions_request()

# def run():
#     # await desriptions_request()
#     # await description_data()
#     tasks = (asyncio.create_task(desriptions_request()),
#              asyncio.create_task(description_data()))
#     await asyncio.gather(*tasks)




if __name__ == '__main__':
    desriptions_request()
    description_data()


#Task 2
def printer(func):
    def inner (n):
        result = func(n)
        return result
    return inner
@printer
def answer(n):
        reversed_num = int(str(n)[::-1])
        print(reversed_num)


if __name__ == '__main__':
    n = input(": ").split()
    answer(n)