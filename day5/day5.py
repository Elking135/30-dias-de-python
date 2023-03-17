1
e_list = list()

2
f_list = ["ou","yea", "banana", 5, 34, "apple"]

3
len(f_list)

4
f_list[0]
f_list[2]
f_list[5]

5
mixed_data_types = ["Hector", 17, 1.78, "Bachelor", "Jerez"]

6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

7
print(it_companies)

8
print(len(it_companies))

9
print(it_companies[0], it_companies[3], it_companies[6])

10
it_companies.remove("Google")
print(it_companies)

11
it_companies.append("Corsair")

12
it_companies.insert(4, "Steam")

13
it_companies[2] = it_companies[2].upper()

14
it_companies2 = "#".join(it_companies)

15
if "Steam" in it_companies:
    print("Steam is in it_companies")
else:
    print("Steam isn't in it_companies")

16
it_companies.sort()

17
it_companies.reverse()
print(it_companies)

18
it_companies_3 = it_companies[:3]

19
it_companies_1 = it_companies[3:]

20
it_companies_2 = it_companies[:4][3:]
print(it_companies_2)

21
it_companies.remove("Steam")

22
it_companies.remove("IBM")

23
it_companies.remove("APPLE")
print(it_companies)

24
it_companies.clear()

25
del it_companies

26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.append(back_end)

27
full_stack = front_end
