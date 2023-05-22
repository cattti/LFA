
f = open("graf.txt",'r')
tr = open("tranzitii.txt",'r')

states = []
alphabets = []
start_state = ""
final_states = []
transition = {}
drum = []
bucle = []
delet = []

statess = f.readline().strip().split()
alphabetss = f.readline().strip().split()
start_statee = f.readline().strip().split()
final_statess = f.readline().strip().split()
start_statee = start_statee[0]

inputt = ""
drum.append(start_statee)

for state in statess:
    for lit in alphabetss:
        dr = tr.readline().strip().split()
        dr = dr[0]
        if dr == "-":
            transition[(state, lit)] = None
        else:
            transition[(state, lit)] = dr

print(transition)
def minimize_dfa(states, alphabet, start_state, final_states, transition):
    partition = [final_states, list(set(states) - set(final_states))]
    new_partition = partition[:]
    while new_partition != partition:
        partition = new_partition[:]
        new_partition = []
        print(new_partition)
        print(partition)
        for group in partition:
            splits = {}
            for state in group:
                row = []
                for symbol in alphabet:
                    row.append(transition[state][symbol])
                if row not in splits:
                    splits[row] = [state]
                else:
                    splits[row].append(state)

            new_partition += list(splits.values())
        while True:
            split_found = False
            for group in partition:
                for symbol in alphabet:
                    splits = {}
                    for state in group:
                        next_state = transition[state][symbol]
                        for split_group in partition:
                            if next_state in split_group:
                                splits.setdefault(tuple(split_group), []).append(state)
                                break

                    if len(splits) > 1:
                        new_partition.remove(group)
                        new_partition += list(splits.values())
                        split_found = True
                        break

                if split_found:
                    break

            if not split_found:
                break

            partition = new_partition[:]
    while True:
        split_found = False
        for group in partition:
            for symbol in alphabet:
                splits = {}
                for state in group:
                    next_state = transition[(state,symbol)]
                    for split_group in partition:
                        if next_state in split_group:
                            splits.setdefault(tuple(split_group), []).append(state)
                            break

                if len(splits) > 1:
                    new_partition.remove(group)
                    new_partition += list(splits.values())
                    split_found = True
                    break

            if split_found:
                break

        if not split_found:
            break

        partition = new_partition[:]
    minimized_states = []
    minimized_transition = {}
    minimized_start_state = ""
    minimized_final_states = []

    for group in partition:
        new_state = "_".join(group)
        minimized_states.append(new_state)

        if start_state in group:
            minimized_start_state = new_state

        if any(state in final_states for state in group):
            minimized_final_states.append(new_state)

        for symbol in alphabet:
            next_state = transition[(group[0],symbol)]
            next_group = [g for g in partition if next_state in g][0]
            new_next_state = "_".join(next_group)
            minimized_transition[new_state] = minimized_transition.get(new_state, {})
            minimized_transition[new_state][symbol] = new_next_state

    return minimized_states, alphabet, minimized_start_state, minimized_final_states, minimized_transition


newstates,newalphabets,newstartstate,newfinalstates,newdfa = minimize_dfa(statess,alphabetss,start_statee,final_statess,transition)
print("new states are: ",newstates)
print("new start state is: ", newstartstate)
print("new final state/s: ",newfinalstates)
print("new dfa: ",newdfa)


# graf
# q0 q1 q2 q3 q4 q5
# 0 1
# q0
# q5

# tranz
# q1
# q2
# q0
# q3
# q5
# q4
# q5
# q4
# q4
# q4
# q5
# q4