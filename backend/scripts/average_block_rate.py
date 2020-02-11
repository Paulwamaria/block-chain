import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS

blockchain = Blockchain()
times = []

for i in range(1000):
    start_time = time.time()
    blockchain.add_block(i)
    end_time = time.time()


    time_to_time = (end_time - start_time) / SECONDS

    times.append(time_to_time)


    average_time = sum(times) / len(times)


    print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_time}')
    print(f'Average time to add blocks: {average_time} s\n')