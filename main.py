from pprint import pprint
class Storage:
    def __init__(self):
        self.data = {}

    def add(self,prof,subj):
        if prof not in self.data:
            self.data.update({prof:[subj]})
        else:
            self.data[prof].append(subj)


    def add_professor(self):
        professor = input('Enter professors name: ')
        while True:
            subject = input('\nEnter proffesors subject,\n ONLY one each time\n type stop when you are done \n Subject: ')
            if subject == 'stop':
                break
            self.add(prof=professor,subj=subject)

    def add_subject(self):
         subject = input('Enter Subject: ')
         professor = input('Enter subject\'s professor: ' )
         self.add(prof=professor,subj=subject)

    def show_subjects(self):
        try:
            prof = input('\nSearch for professor\'s subjects\n Enter professor\'s name: ' )
            print('\n Subjects under that professor:')
            subjects = self.data[prof]
            subjects.sort()
            print(subjects)
        except :
            print('Not found')

    def search_subject(self):
        target = input('Enter subject: ')
        for key, val in self.data.items():
            if target in val:
                message = ('Professor: ' + key)
                return message
            else:
                message = 'Not found'
                return message







    def print_data(self):
        pprint(self.data)


    def start(self):
        while True:
            task = input('Choose a task \n Search by subject[Search], Search by professor[F], add Professor[P], add subject[S], show All[A], Leave[L]: ').lower()
            if task == 'a':
                self.print_data()
            if task == 'p':
                self.add_professor()
            if task == 's':
                self.add_subject()
            if task == 'f':
                self.show_subjects()
            if task == 'search':
                self.search_subject()

            if task == 'l':
                break


if __name__ == '__main__':
    storage = Storage()
    storage.start()
