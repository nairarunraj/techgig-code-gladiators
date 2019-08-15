'''
Elections (100 Marks)

Two national parties BJP and Congress are head to head in the election and are blaming each other as always. The Election has become interesting because of the importance of Regional parties. BJP is boasting on the work done during their tenure by the Government and how much they thought for the nation and people. On the other hand, Congress and other parties are calling it a hoax and urging people to vote for them. BJP star campaigners are just launching the missiles and making place amongst the people again. Congress is worried because of their track record and are breaking the boundaries to get to the people. The other Regional parties are also pulling out every trick in their book. The Election is taking ups and downs frequently.

The voting is done in various phases and News channels are on the edge of their seats covering the areas where elections are to be held. Opinion polls are being conducted in the areas and public opinion is taken to predict the winner of the elections. People are also talking whether the Modi led Government will continue to rule or the Congress and other parties would be able to pull out some magic.

There are many political pandits and experts in the news industry which are covering the elections for a long time now. With their experience in the political field, they have come out with a theory which they claim can predict if the BJP government will come to power again or not.

The experts have formed a matrix in the form of Phases and States.

The experts have provided the number of wins required by BJP in different phases and states to form the government. According to theory, if it is possible to arrange the wins required by BJP in the form of experts matrix, then they will definitely form the government otherwise there will be a new government.

If BJP can form the government as per the theory, then the output would be "YES" indicating that people are happy with the government otherwise the output would be "NO" indicating that people are unhappy with the government.

Note: There are different seats in States which are to be voted in different phases. The number of phases and states is not restricted to the actual number of states and phases in the Indian Election.

Input Format
The first line consists of T, number of test cases. 
The first line of each test case consists of r and c, number of phases and states respectively.
The second line of each test case consists of the number of wins ri required by BJP in the phases to win elections.
The third line of each test case consists of the number of wins ci required by BJP in the States to win the elections.

Constraints
1<=T<5
1<= r, c <=100000
0<= ri <=c
0<=ci <=r

Output Format
Print "YES" (without quotes) if BJP can form the government as per the experts theory otherwise print "NO" (without quotes).

Sample TestCase 1
Input
2
3 2
2 1 0 
1 2 
3 3
3 2 1 
1 2 2

Output
YES
NO

Explanation
Test Case 1:
As per the theory, to form the government, BJP should win 2 seats in the first phase, 1 seat in second phase and 0 in last phase.
BJP also needs to follow the number of wins in states column wise. There should be a single win in the seats of first state and 2 wins in the seats of second state.
It is possible for BJP to win the seats in this format and form the matrix as per the theory.The matrix can be successfully made thus BJP can form the government. Thus, the answer is YES.

Test Case 2: 
It is not possible to create the matrix with respective wins by BJP in phases and states. Thus, the answer is NO.
'''

def process(no_of_phases, no_of_states, phase_wins, state_wins):    
    phase_wins_sum = sum(phase_wins)
    state_wins_sum = sum(state_wins)
    
    if phase_wins_sum != state_wins_sum:
        print "NO"
        return
        
    if phase_wins_sum + state_wins_sum == 0:
        print "YES"
        return

    state_wins.sort(reverse=True)
    
    state_distributions = [0] * no_of_states
    phase_count = {}
    for phase in phase_wins:
        try:
            phase_count[phase-1]
        except:
            phase_count[phase-1] = 0
        phase_count[phase-1] = phase_count[phase-1] + 1
    
    prev_value = 0
    for index in range(no_of_states-1, -1, -1):
        try:
            state_distributions[index] = prev_value + phase_count[index]
        except:
            state_distributions[index] = prev_value
            
        prev_value = state_distributions[index]
        
    carry_forward = 0
    for state_distribution, state_win in zip(state_distributions, state_wins):
        if state_distribution + carry_forward < state_win:
            print "NO"
            return
            
        if state_distribution + carry_forward > state_win:
            carry_forward = state_distribution + carry_forward - state_win
        elif state_distribution + carry_forward == state_win:
            carry_forward = 0
            
    if carry_forward == 0:
        print "YES"
    else:
        print "NO"


def main():
    no_of_test_cases = int(raw_input(""))
    
    for tc in range(0, no_of_test_cases):
        (no_of_phases, no_of_states) = map(int, raw_input("").split())
        phase_wins = map(int, raw_input("").split())
        state_wins = map(int, raw_input("").split())
        process(no_of_phases, no_of_states, phase_wins, state_wins)
    
    return


main()