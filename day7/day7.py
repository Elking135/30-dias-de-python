#level_1
1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

2
it_companies.add("Twitter")

3
it_companies.update(["Github", "Twitch"])

4
it_companies.remove("Twitter")

5
#remove() is for deleting an item, but if the item we want remove isn' in the set, this will raise errors, but discard(), even the item isn't, won't raise errors

#level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
1
A.union(B)

2
A.intersection(B)

3
A.issubset(B)

4
A.isdisjoint(B)

5
A.union(B)
B.union(A)

6
A.symmetric_difference(B)

7
del A
del B
del it_companies