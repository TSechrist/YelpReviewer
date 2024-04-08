import Stem


class StopList:
    def __init__(self):
        self.list = Stem.stem(['', 'a', 'all', 'and', 'are', 'at', 'be', 'been', 'but',
                               'decided', 'do', 'eat', 'few',
                               'for', 'from', 'get', 'go', 'had', 'have', 'he', 'here', 'if', 'in',
                               'into', 'is', 'ive', 'it', 'item', 'items', 'keep', 'menu', 'my',
                               'next', 'of', 'she', 'some',
                               'than', 'that', 'the', 'there',
                               'them', 'they', 'this', 'til', 'till', 'to', 'until', 'up',
                               'what', 'when', 'where',
                               'who', 'with', 'write', 'you', 'your'])

        self.list2 = Stem.stem(['', ' ', 'i', 'me', 'mine', 'he', 'she', 'it', 'a', 'an', 'the',
                                'above', 'below', 'while', 'as', 'until', 'of', 'at',
                                'down', 'if', 'to', 'or', 'was', 'were', 'itself', 'for',
                                'other', 'both', 'any', 'all', 'between', 'do', 'does',
                                'did', 'on', 'own', 'who', 'whom', 'this', 'that', 'has',
                                'have', 'here', 'some', 'why', 'same',
                                'so', 'is', 'be'])
