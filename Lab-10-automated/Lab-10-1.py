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

# Extract Linsulin segment (amino acids 1-24)
lsinsulin = sequence[:24]

# Save Linsulin segment to a new file
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin)

# Verify the length
print(f"Length of Linsulin: {len(lsinsulin)}")

# Extract Binsulin segment (amino acids 25-54)
binsulin = sequence[24:54]

# Save Binsulin segment to a new file
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin)

# Verify the length
print(f"Length of Binsulin: {len(binsulin)}")

# Extract Cinsulin segment (amino acids 55-89)
cinsulin = sequence[54:89]

# Save Cinsulin segment to a new file
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin)

# Verify the length
print(f"Length of Cinsulin: {len(cinsulin)}")

# Extract Ainsulin segment (amino acids 90-110)
ainsulin = sequence[89:110]

# Save Ainsulin segment to a new file
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin)

# Verify the length
print(f"Length of Ainsulin: {len(ainsulin)}")
