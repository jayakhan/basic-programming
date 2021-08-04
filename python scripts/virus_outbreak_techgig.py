import sys
def result(blood_comp, virus_comp):
    a, b = 0, 0 #local variables to compare subsequence of composition in blood samples with virus
    while len(blood_comp) > a and len(virus_comp) > b:
        if blood_comp[a] == virus_comp[b]:
            a += 1
        b += 1
    if len(blood_comp) == a:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'      


def main():
    # Read input variables
    sample_data = sys.stdin.readlines()
    V = sample_data[0].lower()
    N = int(sample_data[1])
    size_of_V = sys.getsizeof(V)
    if N >= 1 and N <= 10 and size_of_V >= 1 and size_of_V <= 100000:
        j = 1
        while j <= N:
            for samples in range(2, len(sample_data)):
                size_of_B = sys.getsizeof(sample_data[samples].lower())
                if size_of_B >= 1 and size_of_B <= size_of_V:
                    print(result(sample_data[samples].lower(), V))
                    j += 1                

main()