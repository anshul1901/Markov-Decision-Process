"""AI Assignment 2."""

class MDP:
    def __init__(self, board, end_states, walls, start_state, step_reward, policy):
        "Initializing the MDP."
        self.board = board;
        self.end_states = end_states;
        self.walls = walls;
        self.start_state = start_state;
        self.step_reward = step_reward;
        self.policy = policy



if __name__ == '__main__':

    # Taking input for size of board
    inp = raw_input()
    inp = inp.split()
    n = int(inp[0])
    m = int(inp[1])

    # Initializing board with 0
    board = [[0 for i in range(m)] for j in range(n)]

    # Initializing policy
    policy = [["NaN" for i in range(m)] for j in range(n)]

    # Taking row wise input
    for i in range(n):
        rows = raw_input()
        rows = rows.split()
        for j in range(m):
            board[i][j] = rows[j]

    # Taking input for e and w, number of end states and number of walls
    inp = raw_input()
    inp = inp.split()
    e = int(inp[0])
    w = int(inp[1])

    # Initializing end states and walls arrays
    end_states = [[0 for j in range(2)] for i in range(e)]
    walls = [[0 for j in range(2)] for i in range(w)]

    # Taking input for all end states
    for i in range(e):
        inp = raw_input()
        inp = inp.split()
        end_states[i][0] = int(inp[0])
        end_states[i][1] = int(inp[1])

    # Taking input for all walls
    for i in range(w):
        inp = raw_input()
        inp = inp.split()
        walls[i][0] = int(inp[0])
        walls[i][1] = int(inp[1])

    # Taking input for start state
    inp = raw_input()
    inp = inp.split()

    start = (inp[0], inp[1])

    # Taking input for unit step reward
    unit_step_reward = float(raw_input())

    m = MDP(board, end_states, walls, start, unit_step_reward, policy, )
