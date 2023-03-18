import pandas as pd

states_data = pd.read_csv("50_states.csv")
states = states_data.state
x = states_data.x
y = states_data.y
state = []

data = {}

for i in range(0, len(states)):
    data[states[i]] = (x[i], y[i])
    state.append(states[i])
