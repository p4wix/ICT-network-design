def pascal(alpha, V, N):
    if(V):
        pas = (-alpha) * (-N - V + 1) * pascal(alpha, V - 1, N)
        return (pas / (V + pas))
    else:
        return 1

def find_max_users(alpha, channelsPerLink, blockingProbability):
    maxUsers = 1
    pascalValue = pascal(alpha, channelsPerLink, maxUsers)

    while (pascalValue <= blockingProbability):
        #print(pascalValue)
        maxUsers += 1
        pascalValue = pascal(alpha, channelsPerLink, maxUsers)

    return maxUsers - 1

blockingProbability = 0.005
channelsPerLink = 30 * 2
trafficIntensity = (-2) * 0.05
alpha = trafficIntensity / (trafficIntensity - 1)

maxUsers = find_max_users(alpha, channelsPerLink, blockingProbability)

print(f"Max liczba uytkowników w systemie = {maxUsers}")
