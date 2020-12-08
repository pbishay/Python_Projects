import random

bucket = [0 for _ in range(13)]

print(bucket)

def run_experiment():
    heads = 0
    tails = 0
    for month in range(12):
        coin = random.random()
        if coin >=.0833333:
            heads = heads + 1
        else:
            tails = tails + 1

    return tails

for i in range(1000):
        experiment_output = run_experiment()
        bucket[experiment_output] += 1

print(bucket)



