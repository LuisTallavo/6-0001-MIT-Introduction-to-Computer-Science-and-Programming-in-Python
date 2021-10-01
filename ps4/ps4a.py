# Problem Set 4A
# Name: Luis Tallavo

def swap (sequence, a, b):
    if (a == b):
        return sequence
    return sequence[:a] + sequence[b] + sequence[a + 1:b] + sequence[a] + sequence[b + 1:]
    
def get_permutations(sequence):
    all_permutations = []

    if len(sequence) == 1:
        return [sequence]
    elif len(sequence) == 2:
        return [sequence, swap(sequence, 0, 1)]
    
    for i in range(len(sequence)):
        s = swap(sequence, 0, i)
        a = s[0]
        b = s[1:]
        if len(b) > 2:
            all_permutations = all_permutations + get_permutations(b)
        else:
            all_permutations.append(a + b)
            all_permutations.append(a + swap(b, 0, 1))
    return all_permutations

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    


