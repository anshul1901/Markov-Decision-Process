inp = raw_input()
inp = inp.split()

n = int(inp[0])
m = int(inp[1])

board = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    rows = raw_input()
    rows = rows.split()
    for j in range(m):
        board[i][j] = rows[j]

inp = raw_input()
inp = inp.split()

e = int(inp[0])
w = int(inp[1])

end_states = [[0 for j in range(2)] for i in range(e)]
walls = [[0 for j in range(2)] for i in range(w)]

for i in range(e):
    inp = raw_input()
    inp = inp.split()
    end_states[i][0] = int(inp[0])
    end_states[i][1] = int(inp[1])

for i in range(w):
    inp = raw_input()
    inp = inp.split()
    walls[i][0] = int(inp[0])
    walls[i][1] = int(inp[1])

inp = raw_input()
inp = inp.split()

start = (inp[0], inp[1])

unit_step_reward = int(raw_input())
