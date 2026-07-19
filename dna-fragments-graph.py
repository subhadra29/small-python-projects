import matplotlib.pyplot as plt

fragments = [
120,
200,
150,
340,
500,
600,
610,
620,
630,
700,
720,
730,
800
]

plt.hist(fragments)

plt.title("DNA Fragments lenght distribution")
plt.xlabel("Fragment lenghts (bp)")
plt.ylabel("Frequency")

plt.grid()
plt.savefig("fragmentsgraph.png")
