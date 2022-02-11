import pickle

with open("heart1.model", "rb") as f:
	model = pickle.load(f)

d = [[37, 1, 3, 145, 223, 1, 0, 150, 0, 2.3, 0, 0, 1]]
res = model.predict(d)
print(res)