class ReversedList:

    def __init__(self, some_list):
        self.some_list = some_list

    def __getitem__(self, indx):
        return self.some_list[len(self.some_list) - indx - 1]

    def __len__(self):
        return len(self.some_list)

