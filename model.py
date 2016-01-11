import tensorflow as tf

env_dim = None # Dimension of environment
arg_dim = 3 # Dimension of arguments

enc_dim = None # Dimension of encoder [D]
hid_dim = None # Dimension of program [M]
prog_dim = None # Dimension of program [P]
prog_count = None # Current number of programs in memory [N]

lstm_size = 3 # The number of layers in LSTM [l]

r_dim = 1
k_dim = 1 # Dimension of key embedding for retrieving the next program, can be P>>K because key is just identifier [K]

# feed-forward steps

h_prev = 0 #[]
c_prev = 0 #[]

env = tf.placeholder(tf.float32, [e_dim], name='environment')
arg = tf.placeholder(tf.float32, [a_dim], name='arguments')
# arg = [arg_1, arg_2, arg_3]

def __init__(self, alpha, ):
    self.alpha= alpha

def init_module(self):
    self.h = 0
    self.r = 0

    # N : The current number of programs in memory
    M_key = tf.Variable(tf.float32, [prog_count, k_dim]) # N x K, storing program keys
    M_prog = tf.Variable(tf.float32, [prog_count, prog_dim]) # N x P, storing program embeddings

    p_emb = tf.Variable(tf.float32, [prog_dim], name='program') # the current program embedding
    p_true  = tf.placeholder(tf.float32, [], name='ground-truth program identifier')

def run(self, e, p_idx, args):
    h = 0
    r = 0
    p = tf.nn.embedding_lookup(M_prog, p_idx)

    while self.r < self.alpha:
        s = encoder('image', env, enc_dim)
        h = lstm(s, p_emb, h_prev)

        r = linear(h, r_dim) # The end-of-program probability
        k = linear(h, k_dim) # The lookup key embedding
        args = linear(h, arg_dim) # The output arguments
        p_idx = tf.argmax(tf.matmul(M_key, k))

        if p_idx == 'ACT':
            e = env(e, p, arg)
        else:
            self.run(p_idx, args)

def forward(self.)
    def encoder(env, arg, domain):
        """Domain specific encoder"""
        if domain == 'image':
            s = tf.conv2(e, [])

        return s

    s = encoder('image', env, enc_dim)

    def lstm(s, p_emb, h_prev):
        input_ = tf.concat(1, [s, p_emb])

        h = tf.nn.relu()
        return h

    h = lstm(s, p_emb, h_prev)

    r = linear(h, r_dim) # The end-of-program probability
    k = linear(h, k_dim) # The lookup key embedding
    arg = linear(h, arg_dim) # The output arguments

    p_true  = tf.placeholder(tf.float32, [], name='ground-truth program identifier')
    p_ = tf.nn.embedding_lookup(M_prog, tf.argmax(tf.matmul(M_key, k)))

    def env(e, p, arg):
        """Domain specific environmental state"""
        return e

    e = env(e, p, arg)
