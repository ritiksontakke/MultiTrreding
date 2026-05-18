from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n*n

if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:

        results = executor.map(square, [1,2,3,4])

    print(list(results))