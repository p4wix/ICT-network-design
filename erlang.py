def erlang(A, V):
    if(V):
        erl = A * erlang(A, V - 1)
        return (erl / (V + erl))
    else:
        return 1

# channelsPerLink = V

def find_max_users(trafficIntensity, channelsPerLink, blockingProbability):
    maxUsers = 1
    A = trafficIntensity * maxUsers
    erlangValue = erlang(A, channelsPerLink)

    while(erlangValue <= blockingProbability):
        # print(erlangValue)
        maxUsers += 1
        A = trafficIntensity * maxUsers
        erlangValue = erlang(A, channelsPerLink)

    return maxUsers - 1

blockingProbability = 0.005
channelsPerLink = 30 * 2
trafficIntensity = 0.05 * 2

maxUsers = find_max_users(trafficIntensity, channelsPerLink, blockingProbability)

print(f"Max liczba uytkowników w systemie = {maxUsers}")
