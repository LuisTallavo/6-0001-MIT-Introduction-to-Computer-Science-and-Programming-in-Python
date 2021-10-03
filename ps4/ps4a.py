# Problem Set 4A
# Name: Luis Tallavo

def swap (sequence, a, b):
    if (a == b):
        return sequence
    return sequence[:a] + sequence[b] + sequence[a + 1:b] + sequence[a] + sequence[b + 1:]
    
def get_permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]
    else:
        all_permutations = []
        for i in get_permutations(sequence[:-1]):
            for j in range(len(i)+1):
                all_permutations.append(i[:j] + sequence[-1] + i[j:])
        return all_permutations
if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
