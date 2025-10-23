from collections import defaultdict

text = "MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster."

# Mapper
mapped = [(w.lower(),1) for w in text.split()]

# Shuffle & Sort
shuffle = defaultdict(list)
for k,v in mapped: shuffle[k].append(v)

# Reducer
word_count = {k: sum(v) for k,v in shuffle.items()}

# Output
for w,c in sorted(word_count.items()): print(f"{w}: {c}")
