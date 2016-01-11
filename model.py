import tensorflow as tf

class NPI(object):
    def __init__(self, env_dim, enc_dim, hid_dim,
                 prog_dim, prog_count,
                 arg_dim=3, lstm_size=2, r_dim=1, k_dim=1, alpha=0.5):
        self.env_dim = env_dim # Dimension of environment

        self.enc_dim = enc_dim # Dimension of encoder [D]
        self.hid_dim = hid_dim # Dimension of program [M]
        self.prog_dim = prog_dim # Dimension of program [P]
        self.prog_count = prog_count # Current number of programs in memory [N]

        self.arg_dim = arg_dim # Dimension of arguments
        self.lstm_size = lstm_size # The number of layers in LSTM [l]

        self.r_dim = r_dim
        self.k_dim = k_dim # Dimension of key embedding for retrieving the next program
                           # Can be P>>K because key is just identifier [K]

        self.env = tf.placeholder(tf.float32, [e_dim], name='environment')
        self.arg = tf.placeholder(tf.float32, [a_dim], name='arguments')

        self.self.alpha = alpha

        self.h_prev = 0
        self.c_prev = 0

        self.core_cell = 

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
