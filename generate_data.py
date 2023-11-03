from enum import Enum
import random, os

class DATASET(Enum):
    SMALL = 2**9
    MEDIUM = 2**13
    BIG = 2**16
    
def generate_dataset(variance: str) -> (list[int], list[int], list[int]):
    if variance == "small":
        size = DATASET.SMALL.value
    elif variance == "medium":
        size = DATASET.MEDIUM.value
    elif variance == "big":
        size = DATASET.BIG.value
    else:
        raise ValueError("Invalid variance parameter. Use 'small', 'medium', or 'big'.")

    random_dataset = [random.randint(1, DATASET.BIG.value) for _ in range(size)]

    sorted_dataset = sorted(random_dataset)
            
    reversed_dataset = sorted_dataset[::-1]
    
    return random_dataset, sorted_dataset, reversed_dataset

def write_to_file(dataset, filename):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    
    with open(filename, "w") as file:
        for i, number in enumerate(dataset):
            if i == len(dataset) - 1:
                file.write(str(number))
            else:
                file.write(str(number) + "\n")
            
random_small_dataset, sorted_small_dataset, reversed_small_dataset = generate_dataset("small")
random_medium_dataset, sorted_medium_dataset, reversed_medium_dataset = generate_dataset("medium")
random_big_dataset, sorted_big_dataset, reversed_big_dataset = generate_dataset("big")

write_to_file(random_small_dataset, "dataset/small/random.txt")
write_to_file(sorted_small_dataset, "dataset/small/sorted.txt")
write_to_file(reversed_small_dataset, "dataset/small/reversed.txt")
write_to_file(random_medium_dataset, "dataset/medium/random.txt")
write_to_file(sorted_medium_dataset, "dataset/medium/sorted.txt")
write_to_file(reversed_medium_dataset, "dataset/medium/reversed.txt")
write_to_file(random_big_dataset, "dataset/big/random.txt")
write_to_file(sorted_big_dataset, "dataset/big/sorted.txt")
write_to_file(reversed_big_dataset, "dataset/big/reversed.txt")