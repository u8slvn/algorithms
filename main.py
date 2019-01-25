from fixture import test_list
from search import binary_search, classic_search

if __name__ == "__main__":
    test_list.sort()

    name = 'Racheal'

    index = classic_search(sample=test_list, item=name)
    print(f'Index: {index} for name: {name}')

    index = binary_search(sample=test_list, item=name)
    print(f'Index: {index} for name: {name}')
