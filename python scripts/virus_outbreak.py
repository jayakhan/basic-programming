
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
    # Initialize input variables
    virus_comp = 'coro'
    num = 9
    j = 0 # Initialize variable to limit blood samples list to just 10
    list = ['    ', 'con', 'bhu', 'cc', "cfff", 'ffff', 'coronavirus' ,'gh', 'ww', 'c', 'we']
    for i in list:
        if j < num:
            #Constraints check
            if num <= 10 and num > 0 and len(virus_comp) <= 10^5 and len(i) > 0 and len(i) <= len(virus_comp):
                print(result(i, virus_comp))
                j += 1
            else:
                break
main()