

class Ensemble(object):

    def __init__(self, classifiers=None):
        if classifiers == None:
            self.classifiers = []
        else:
            self.classifiers = classifiers

    def add(self, classifier):
        self.classifiers.append(classifier)

    def add_classifiers(self, classifiers):
        self.classifiers = self.classifiers + classifiers


    def add_ensemble(self, ensemble):
        self.classifiers = self.classifiers + ensemble.classifiers

    def __len__(self):
        return len(self.classifiers)

