
f = open("graf.txt",'r')
tr = open("tranzitii.txt",'r')

states = []
alphabets = []
start_state = ""
final_states = []
transition = {}
drum = []

states = f.readline().strip().split()
alphabets = f.readline().strip().split()
start_state = f.readline().strip().split()
final_states = f.readline().strip().split()
start_state = start_state[0]

inputt = ""
drum.append(start_state)

for state in states:
    for lit in alphabets:
        dr = tr.readline().strip().split()
        dr = dr[0]
        if dr == "-":
            transition[(state, lit)] = None
        else:
            transition[(state, lit)] = dr

print("Enter input string: ")
inputt = input()

current_state = start_state

for lit in inputt:

    current_state = transition[(current_state, lit)]
    drum.append(current_state)

    if current_state is None:
        print("Neacceptat")
        break
else:

    if current_state in final_states:
        print("Acceptat")
        print(drum)
    else:
        print("Neacceptat")

f.close()
tr.close()