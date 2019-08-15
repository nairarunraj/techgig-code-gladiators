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

def is_phase_win_satisfied(phase_wins_remaining):
    for phase_win in phase_wins_remaining:
        if phase_win > 0:
            return False
            
    return True

    
def is_state_win_satisfied(state_wins_remaining):
    for state_win in state_wins_remaining:
        if state_win > 0:
            return False
            
    return True
    
    
def should_current_phase_satisfy_current_state(no_of_phases, no_of_states, state_wins_required, current_phase):
    if no_of_phases - current_phase == state_wins_required:
        return True
        
    return False
    
    
def can_remaining_phases_satisfy_current_state(phase_wins_remaining, state_wins_required, current_phase):
    print("\tcan_remaining_phases_satisfy_current_state")
    phase_win_possible_for_current_state = 0
    for remaining_phase in phase_wins_remaining[current_phase:]:
        if remaining_phase > 0:
            phase_win_possible_for_current_state = phase_win_possible_for_current_state + 1
    
    if state_wins_required > phase_win_possible_for_current_state:
        return False
        
    return True
    

def can_remaining_states_satisfy_current_phase(state_wins_remaining, phase_wins_required, current_state):
    print("\tcan_remaining_phases_satisfy_current_state")
    state_win_possible_for_current_phase = 0
    for state in state_wins_remaining:
        if state > 0:
            state_win_possible_for_current_phase = state_win_possible_for_current_phase + 1
    
    if phase_wins_required > state_win_possible_for_current_phase:
        return False
        
    return True
    
    
def find_path(no_of_phases, no_of_states, phase_wins_remaining, state_wins_remaining, current_state, current_phase):
    print("Current state: %d, phase: %d" % (current_state, current_phase))
    print("\tState count - %s" % state_wins_remaining)
    print("\tPhase count - %s" % phase_wins_remaining)

    if current_state == no_of_states:
        # All states have been processed
        print "\t\tAll states processed"
        if is_phase_win_satisfied(phase_wins_remaining):
            print "\t\t\tReturn true - 1"
            return True
            
        print "\t\t\tReturn false"
        return False
        
    if state_wins_remaining[current_state] == 0:
        # Current state's wins have been satisfied
        # Go to next state
        print "\t\tState wins zero, go to next state"
        ret_state_finish = find_path(no_of_phases, no_of_states, phase_wins_remaining, state_wins_remaining, current_state+1, 0)
        
        return ret_state_finish

    if current_phase == no_of_phases:
        # All phases have been processed
        print "\t\tAll phases processed"
        if is_state_win_satisfied(state_wins_remaining):
            print "\t\t\tRetunr true - 3"
            return True
            
        print "\t\t\tRetunr false - 3"
        return False
        
    if phase_wins_remaining[current_phase] == 0:
        # Current phase cannot satisfy the current state's win
        # Go to next phase
        print "\t\tCurrent phase cannot satisfy the current state's req"
        ret_phase_finish = find_path(no_of_phases, no_of_states, phase_wins_remaining, state_wins_remaining, current_state, current_phase+1)
        
        if ret_phase_finish:
            return True
    else:
        if not can_remaining_states_satisfy_current_phase(state_wins_remaining, phase_wins_remaining[current_phase], current_state):
            print("\t\tCannot satisfy current phase")
            return False

        if can_remaining_phases_satisfy_current_state(phase_wins_remaining, state_wins_remaining[current_state], current_phase):
            inc_state_wins_remaining = list(state_wins_remaining)
            inc_phase_wins_remaining = list(phase_wins_remaining)
            
            inc_state_wins_remaining[current_state] = inc_state_wins_remaining[current_state] - 1
            inc_phase_wins_remaining[current_phase] = inc_phase_wins_remaining[current_phase] - 1
            
            ret_include_current_phase = find_path(no_of_phases, no_of_states, inc_phase_wins_remaining, inc_state_wins_remaining, current_state, current_phase+1)
            
            if ret_include_current_phase:
                return True
            
            new_state_wins_remaining = list(state_wins_remaining)
            new_phase_wins_remaining = list(phase_wins_remaining)

            ret_exclude_current_phase = find_path(no_of_phases, no_of_states, new_phase_wins_remaining, new_state_wins_remaining, current_state, current_phase+1)
            
            if ret_exclude_current_phase:
                return True
                
    return False
    

def process(no_of_phases, no_of_states, phase_wins, state_wins):
    phase_wins_remaining = list(phase_wins)
    state_wins_remaining = list(state_wins)
    
    phase_wins_sum = sum(phase_wins_remaining)
    state_wins_sum = sum(state_wins_remaining)
    
    if phase_wins_sum != state_wins_sum:
        print "NO"
        return

    phase_wins_remaining.sort(reverse=True)
    state_wins_remaining.sort(reverse=True)
    
    
    success = find_path(no_of_phases, no_of_states, phase_wins_remaining, state_wins_remaining, 0, 0)
    if success:
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