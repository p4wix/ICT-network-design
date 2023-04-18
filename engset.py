def engset(alpha, V, N):
    if(V):
        eng = alpha * (N - V + 1) * engset(alpha, V - 1, N)
        return (eng / (V + eng))
    else:
        return 1

def find_max_users(alpha, channelsPerLink, blockingProbability):
    maxUsers = 1
    engsetValue = engset(alpha, channelsPerLink, maxUsers)

    while(engsetValue <= blockingProbability):
        #print(f"engsetValue: {engsetValue}")
        maxUsers += 1
        engsetValue = engset(alpha, channelsPerLink, maxUsers)

    return maxUsers - 1

blockingProbability = 0.005
channelsPerLink = 30 * 2
trafficIntensity = 0.05 * 2
alpha = trafficIntensity / (1 - trafficIntensity) # średni ruch oferowany przez jedno źródło

maxUsers = find_max_users(alpha, channelsPerLink, blockingProbability)

print(f"Max liczba uytkowników w systemie = {maxUsers}")
