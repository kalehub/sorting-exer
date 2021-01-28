# selection sort
# python

class CustomList:
    def __init__(self, mylist):
        self.mylist = mylist

    def selection_sort(self):
        """ find the minimum element and put it in front """
        print('before sorted : ', self.mylist)

        for i in range(0, len(self.mylist)):
            for j in range(i+1, len(self.mylist)):
                if self.mylist[i] > self.mylist[j]:
                    self.mylist[i], self.mylist[j] = self.mylist[j], self.mylist[i]
            print('iterasi  : ', self.mylist)
            # swapping
        print(self.mylist)


if __name__ == '__main__':
    # [8, 4, 6, 9, 2, 5, 3]

    clist = CustomList([64, 25, 12, 22, 11])
    clist.selection_sort()
