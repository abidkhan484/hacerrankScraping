# Accepted
# Python 3

m, n = map(int, input().split())
p = int(input().strip())

# see on the khan accademy tutorial for geometric distribution
# https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-geometric/v/cumulative-geometric-probability-less-than-a-value
print(round(1-((1-(m/n))**p), 3))

