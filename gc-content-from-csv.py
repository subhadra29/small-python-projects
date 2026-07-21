import pandas as pd
import matplotlib.pyplot as plt

sequence= pd.read_csv("dna-sequences.csv")

gc_contents=[]

for i in sequence["Sequence"]:
    g_count= i.count("G")
    c_count= i.count("C")
    total_lenght= len(i)

    gc_content= ((g_count + c_count )/ total_lenght) * 100

    gc_contents.append(gc_content)

sequence["gc_content"] = gc_contents

plt.bar(sequence["Sample"],gc_contents)

plt.xlabel("Samples")
plt.ylabel("G-C content")
plt.title("G-C content graph")
plt.grid()

plt.savefig("GC_content graph.png")
