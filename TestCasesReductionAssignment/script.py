import sys

f1 = open("all_branches.txt")
tests = open(sys.argv[1]) #Test case (T.txt)
final = open("test/S", "w")
rec = open("test/record.txt", "w")

test_cases = [] #contain all the test cases
for x in tests:
    test_cases.append(x)

f2 = open("branches.txt")

test_case_bc = [] #contain the branch coverages of all tests 
for x in f2:
    test_case_bc.append(x.split())


branches = set(f1.readline().split()) #contain the line numbers of all branches

k = int(sys.argv[2])
done = set() #store the indices of all the tests selected yet 

for i in range(k):
    mx = 0
    tc = 0
    cnt = 0
    rec.write(str(branches))
    rec.write("\n")

    for x in test_case_bc: 
        if cnt in done:
            cnt += 1 
            continue

        cur_set = set(x)
        z = cur_set & branches
      
        if(len(z) >= mx):
            mx = len(z)
            tc = cnt
        cnt += 1

    for x in test_case_bc[tc]:
        branches.discard(x)

    final.write(test_cases[tc])
    done.add(tc)

f1.close()
tests.close()
final.close()
rec.close()





