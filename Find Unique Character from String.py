def find_winner(N, smit, joy):
    mean_smit = len(set(smit)) / N if N > 0 else 0
    mean_joy = len(set(joy)) / N if N > 0 else 0

    if mean_smit > mean_joy:
        print("SMIT")
    elif mean_joy > mean_smit:
        print("JOY")
    else:
        print("TIE")

# Read input
N = int(input().strip())
smit = input().strip()
joy = input().strip()

find_winner(N, smit, joy)
