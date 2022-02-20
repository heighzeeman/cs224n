# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
filepath = "../birth_dev.tsv"
with open(filepath) as fin:
    lines = [x.strip().split('\t') for x in fin]
    if len(lines[0]) == 1:
        print('No gold birth places provided; returning (0,0)')
    true_places = [x[1] for x in lines]
    total = len(true_places)
    predicted_places = [ "London" for _ in range(total) ]
    correct = len(list(filter(lambda x: x[0] == x[1],
      zip(true_places, predicted_places))))
    print("London baseline: (tot, correct)", (float(total),float(correct)))