"""AI Assignment 2."""
import sys, copy

class MDP:
    def __init__(self, board, end_states, walls, start_state, step_reward, policy):
        "Initializing the MDP."
        self.board = board;
        self.old_board = copy.deepcopy(self.board);
        # self.old_board = [[self.board[i][j] for j in range(len(self.board[i]))] for i in range(len(self.board))]
        self.end_states = end_states;
        self.probability = {
        'target' : 0.8,
        'alt':     0.1,
        }
        self.walls = walls;
        self.start_state = start_state;
        self.step_reward = step_reward;
        self.policy = policy
        self.delta = 0.01
        self.init_board()
        self.init_policy()
        self.value_iteration()
        self.policy_func()

    def init_board(self):
        """Initializing the board with the walls. Replacing walls with NaN."""
        for i in range(len(self.walls)):
            x, y = self.walls[i]
            self.board[x][y] = "NaN"

    def init_policy(self):
        """Initializing policy for the board."""
        for i in range(len(self.end_states)):
            x, y = self.end_states[i]
            print self.board[x][y]
            if self.board[x][y] > 0:
                self.policy[x][y] = "Goal"
            else:
                self.policy[x][y] = "Bad"

    def value_iteration(self):
        """Applying value iteration algorithm on the board."""
        while True:
            changed_pairs = []
            for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if (i, j) not in self.walls and (i, j) not in self.end_states:
                            # print('Iteration %d' % int(i + 1))
                            # print('Estimating S(%d,%d)' % (i, j))
                            self.board[i][j] = self.update((i, j))
                            if (self.old_board[i][j])!=0:
                                changed_pairs.append(abs(self.board[i][j]-(self.old_board[i][j]))/self.old_board[i][j])
            print changed_pairs
            # Adding code to check if change is less than delta and then terminate
            if max(changed_pairs) <= self.delta:
                return

            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (i, j) in self.walls or (i, j) in self.end_states:
                        continue
                    self.old_board[i][j] = self.board[i][j]

    def update(self, state):
        """Bellman update step."""

        # curVal represents the current utility of the state
        curVal = self.old_board[state[0]][state[1]]

        # Initializing value array for neighbours
        val = [float(0) for i in range(4)]
        # Value of neighbour above
        val[0] = (self.get_state_utility(curVal, tuple((state[0], state[1]+1))))
        # Value of neighbour below
        val[1] = (self.get_state_utility(curVal, tuple((state[0], state[1]-1))))
        # Value of neighbour on the left
        val[2] = (self.get_state_utility(curVal, tuple((state[0]-1, state[1]))))
        # Value of neighbour on the right
        val[3] = (self.get_state_utility(curVal, tuple((state[0]+1, state[1]))))

        # print val
        val[0] = val[0]*self.probability['target'] + (val[2]+val[3])*self.probability['alt']
        val[1] = val[1]*self.probability['target'] + (val[2]+val[3])*self.probability['alt']
        val[2] = val[2]*self.probability['target'] + (val[0]+val[1])*self.probability['alt']
        val[3] = val[3]*self.probability['target'] + (val[0]+val[1])*self.probability['alt']
        # print val
        # Discount factor is taken as 1 in this step.
        return self.step_reward + max(val)

    def get_state_utility(self, curVal, state):
        """Get utility of a state from old board after checking if state is valid."""
        x, y = state
        if x < 0 or y < 0:
            # Hit the edge of the board, return value of initial state from which
            # function was called.
            return float(curVal)
        try:
            value = self.board[x][y] or curVal
        except IndexError:
            return float(curVal)
        return float(self.old_board[x][y])

    def get_state_policy(self, curVal, state):
        """Get policy of a state from old board after checking if state is valid."""
        x, y = state
        if x < 0 or y < 0:
            # Hit the edge of the board, return value of initial state from which
            # function was called.
            return float(curVal)

        try:
            value = self.board[x][y] or curVal
        except IndexError:
            return float(curVal)

        return float(self.board[x][y])

    def policy_func(self):
        """Setting the policy after completion of value iteration."""

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if tuple((i, j)) not in self.walls and tuple((i, j)) not in self.end_states:

                    # curVal represents the current policy of the state
                    curVal = self.board[i][j]

                    # Initializing value array for neighbours
                    val = [0 for k in range(4)]
                    # Value of neighbour above
                    val[0] = (self.get_state_policy(curVal, tuple((i, j+1))))
                    # Value of neighbour below
                    val[1] = (self.get_state_policy(curVal, tuple((i, j-1))))
                    # Value of neighbour on the left
                    val[2] = (self.get_state_policy(curVal, tuple((i-1, j))))
                    # Value of neighbour on the right
                    val[3] = (self.get_state_policy(curVal, tuple((i+1, j))))
                    # print val
                    val[0] = val[0]*self.probability['target'] + (val[2]+val[3])*self.probability['alt']
                    val[1] = val[1]*self.probability['target'] + (val[2]+val[3])*self.probability['alt']
                    val[2] = val[2]*self.probability['target'] + (val[0]+val[1])*self.probability['alt']
                    val[3] = val[3]*self.probability['target'] + (val[0]+val[1])*self.probability['alt']

                    maxIndex = -1
                    for k in range(4):
                        if max(val) == val[k]:
                            maxIndex = k
                            break

                    self.policy[i][j] = k+1
                    self.print_policy()

    def print_policy(self):
        for i in range(len(self.policy)):
            for j in range(len(self.policy[i])):
                sys.stdout.write('%s ' % self.policy[i][j])
            print('\n')


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
            board[i][j] = float(rows[j])

    # Taking input for e and w, number of end states and number of walls
    inp = raw_input()
    inp = inp.split()
    e = int(inp[0])
    w = int(inp[1])

    # Initializing end states and walls arrays
    end_states = []
    walls = []

    # Taking input for all end states
    for i in range(e):
        inp = raw_input()
        inp = inp.split()
        end_states.append(tuple((int(inp[0]), int(inp[1]))))

    # Taking input for all walls
    for i in range(w):
        inp = raw_input()
        inp = inp.split()
        walls.append(tuple((int(inp[0]), int(inp[1]))))

    # Taking input for start state
    inp = raw_input()
    inp = inp.split()

    start = tuple((inp[0], inp[1]))

    # Taking input for unit step reward
    unit_step_reward = float(raw_input())

    m = MDP(board, end_states, walls, start, unit_step_reward, policy)
