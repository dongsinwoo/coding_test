length, cut = map(int,input().split())
score = list(map(int, input().split()))
print(sorted(score)[length-cut])