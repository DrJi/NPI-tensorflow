import numpy as np
from random import randint

K = 10 # base
N = 100
Q_size = 4

progs = {
    'ADD': 0,     # Perform multi-digit addition
    'ADD1': 1,    # Perform single-digit addition
    'CARRY': 2,   # Mark a 1 in the carry row one unit LEFT
    'LSHIFT': 3,  # Shift a specified pointer one step LEFT
    'RSHIFT': 4,  # Shift a specified pointer one step RIGHT
    'ACT': 5,     # Move a pointer or write to the scratch self.Q
}

arg1s = {
    'OUT': 0,
    'CARRY': 1,
    'INP1': 2,
    'INP2': 3,
}

arg2s = {
    'WRITE': 0,
    'LEFT': 1,
    'RIGHT': 2,
}

progs_rev = {v:k for k,v in progs.items()}
arg1s_rev = {v:k for k,v in arg1s.items()}
arg2s_rev = {v:k for k,v in arg2s.items()}

class copy_generator(object):
    def __init__(self, K=K, N=N, Q_size=Q_size):
        self.Q_size = Q_size
        self.N = N
        self.K = K

        self.i1, self.i2, self.i3, self.i4 = 0, 0, 0, 0
        self.Q = np.zeros([self.Q_size, self.N, self.K])

    def generate_executions(self, len_a, len_b=None):
        if not len_b:
            len_b = len_a

        self._E_out = []

        num_a = str(randint(10**(len_a-1), 10**len_a-1)).zfill(self.N)
        num_b = str(randint(10**(len_b-1), 10**len_b-1)).zfill(self.N)

        self.Q = np.zeros([self.Q_size, self.N, self.K])
        self.Q[0, np.arange(self.N), map(int, list(num_a)) + [0] * (self.N-len(num_a))] = 1
        self.Q[1, np.arange(self.N), map(int, list(num_b)) + [0] * (self.N-len(num_b))] = 1

        self.i1, self.i2, self.i3, self.i4 = 0, 0, 0, 0
        carry = 0

        e = [self.Q, self.i1, self.i2, self.i3, self.i4]
        self.E('ADD')

        while True:
            self.E('ADD1')
            try:
                result = int(num_a[-1-self.i1]) + int(num_a[-1-self.i2]) + carry
            except:
                import ipdb; ipdb.set_trace()
            if  result >= 10:
                self.E('ACT', ['OUT', 'WRITE', result-10])
                self.E('CARRY')
                self.E('ACT', ['CARRY', 'LEFT'])
                self.E('ACT', ['CARRY', 'WRITE', 1])
                self.E('ACT', ['CARRY', 'RIGHT'], True)
                carry = 1
            else:
                self.E('ACT', ['OUT', 'WRITE', result], True)
                carry = 0

            self.E('LSHIFT')
            self.E('ACT', ['INP1', 'LEFT'])
            self.E('ACT', ['INP2', 'LEFT'])
            self.E('ACT', ['CARRY', 'LEFT'])
            self.E('ACT', ['OUT', 'LEFT'], True)

        return self._E_out

    def E(self, prog, args=None, r=False):
        p_idx = progs[prog]
        r = 1 if r else 0
        if args:
            arg1 = arg1s[args[0]]
            arg2 = arg2s[args[1]]
            arg3 = args[2] if len(args) == 3 else None

            if args[0] == 'OUT':
                import ipdb; ipdb.set_trace()
                if args[1] == 'LEFT':
                    self.i4 += 1
                elif args[1] == 'RIGHT':
                    self.i4 -= 1
                elif args[1] == 'WRITE':
                    self.Q[3, self.i4, arg3] = 1
                else:
                    raise Exception(' [!] Wrong arg2 : %s' % args[1])
            elif args[0] == 'CARRY':
                if args[1] == 'LEFT':
                    self.i3 += 1
                elif args[1] == 'RIGHT':
                    self.i3 -= 1
                elif args[1] == 'WRITE':
                    self.Q[2, self.i3, arg3] = 1
                else:
                    raise Exception(' [!] Wrong arg2 : %s' % args[1])
            elif args[0] == 'INP1':
                if args[1] == 'LEFT':
                    self.i1 += 1
                elif args[1] == 'RIGHT':
                    self.i1 -= 1
            elif args[0] == 'INP2':
                if args[1] == 'LEFT':
                    self.i2 += 1
                elif args[1] == 'RIGHT':
                    self.i2 -= 1
            else:
                raise Exception(' [!] Wrong arg1 : %s' % args[0])

            args = [arg1, arg2, arg3]

        self._E_out.append([p_idx, args, r])

    @property
    def E_out(self):
        new_E_out = []
        for E_out in self._E_out:
            new_prog = progs_rev[E_out[0]]
            args = E_out[1]
            if args:
                new_args = []
                new_args.append(arg1s_rev[args[0]])
                if args[1]:
                    new_args.append(arg2s_rev[args[1]])
                else:
                    new_args.append(None)
                new_args.append(args[2])
            else:
                new_args = None
            new_r = E_out[2]
            new_E_out.append([new_prog, new_args, new_r])
        return new_E_out
