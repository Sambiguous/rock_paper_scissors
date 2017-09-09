from random import randint


class RockPaperScissors(object):
    l_rec = {}
    s_rec = {'wins': 0, 'losses': 0, 'ties': 0}
    text = ['Computer chooses rock.',
            'Computer chooses paper',
            'Computer chooses scissors',
            ' You win!',
            ' You lose!',
            ' Tie game!',
            ]
    results = [
        [[text[0] + text[5], 0, 0, 1], [text[1] + text[4], 0, 1, 0], [text[2] + text[3], 1, 0, 0]],
        [[text[0] + text[3], 1, 0, 0], [text[1] + text[5], 0, 0, 1], [text[2] + text[4], 0, 1, 0]],
        [[text[0] + text[4], 0, 1, 0], [text[1] + text[3], 1, 0, 0], [text[2] + text[5], 0, 0, 1]],
    ]

    def __init__(self):
        pass

    def display_s_rec(self):
        w = self.s_rec['wins']
        l = self.s_rec['losses']
        t = self.s_rec['ties']
        record = '%s - %s - %s' % (w, l, t)
        return record

    def display_l_rec(self):
        w = self.l_rec['wins']
        l = self.l_rec['losses']
        t = self.l_rec['ties']
        record = '%s - %s - %s' % (w, l, t)
        return record

    def get_record(self):
        with open('save.txt', 'r') as save_file:
            self.l_rec['wins'] = int(save_file.readline())
            self.l_rec['losses'] = int(save_file.readline())
            self.l_rec['ties'] = int(save_file.readline())
        return None

    def save_record(self):
        self.l_rec['wins'] += self.s_rec['wins']
        self.l_rec['losses'] += self.s_rec['losses']
        self.l_rec['ties'] += self.s_rec['ties']
        with open('save.txt', 'w') as save_file:
            save_file.write('%s\n%s\n%s' % (self.l_rec['wins'], self.l_rec['losses'], self.l_rec['ties']))

    def throw(self, user):
        cpu = randint(0, 2)
        outcome = self.results[user][cpu]
        self.s_rec['wins'] += outcome[1]
        self.s_rec['losses'] += outcome[2]
        self.s_rec['ties'] += outcome[3]
        output = [outcome[0], cpu]
        return output


RPS = RockPaperScissors()
RPS.get_record()
