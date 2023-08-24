

import random, tqdm, time

stuff=[]

for i in tqdm.tqdm(range(50)):
	stuff.append(random.random())
	time.sleep(0.1)

print(stuff)