import numpy as np

dna = np.array([
    120, 450, 780, 220,
    560, 900, 310, 640,
    150, 820
])
#no.of fragments
print(dna.size)

#the longest fragement
print(dna.max())

#the shortest fragement
print(dna.min())

#average fragement length
print(dna.mean())

#fragements whose length is greater than 500bp
print(dna[dna>500])

#add 50bp as correction
print(dna + 50)

#sort the fragements from short to long
print(np.sort(dna))


