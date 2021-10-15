# Question 2:
#!/usr/bin/python3

DNA_code = input("Please give me a DNA string:")

def dna_complement(DNA_code):
    if DNA_code == "":
        return None
    else:
        complement = []
        for i, value in enumerate(DNA_code):
            if (DNA_code[i] == "A" or DNA_code[i] == "a"):
                complement.append("T")
                i +=1
            elif (DNA_code[i] == "T" or DNA_code[i] == "t"):
                complement.append("A")
                i +=1
            elif (DNA_code[i] == "G" or DNA_code[i] == "g"):
                complement.append("C")
                i +=1
            elif (DNA_code[i] == "C" or DNA_code[i] == "c"):
                complement.append("G")
                i +=1
            else:
                return None
    return print(f"here is your complement: {complement}")

dna_complement(DNA_code)

#Example of empty string
DNA_code = ""
print(f"Here is the empty string input: {DNA_code}")
print(dna_complement(DNA_code))

#Example of wrong string
DNA_code = "TGB"
print(f"Here is the empty string input: {DNA_code}")
print(dna_complement(DNA_code))
