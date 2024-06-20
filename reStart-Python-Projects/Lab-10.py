# Read the sequence from the file
with open('preproinsulin-seq.txt', 'r') as file:
    lines = file.readlines()

# Process the lines to remove unwanted characters
sequence = ''
for line in lines:
    if line.startswith('ORIGIN') or line.startswith('//'):
        continue
    sequence += ''.join(filter(str.isalpha, line))

# Write the cleaned sequence to a new file
with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(sequence)

print(f"Cleaned sequence: {sequence}")
print(f"Length: {len(sequence)}")

# Read the cleaned sequence
with open('preproinsulin-seq-clean.txt', 'r') as file:
    sequence = file.read().strip()

# Define the segments
lsinsulin = sequence[:24]
binsulin = sequence[24:54]
cinsulin = sequence[54:89]
ainsulin = sequence[89:110]

# Save each segment to its respective file
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin)
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin)
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin)
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin)

# Verify the lengths
print(f"Length of Lsinsulin: {len(lsinsulin)}")
print(f"Length of Binsulin: {len(binsulin)}")
print(f"Length of Cinsulin: {len(cinsulin)}")
print(f"Length of Ainsulin: {len(ainsulin)}")
