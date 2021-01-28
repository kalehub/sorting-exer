# selection sort
# python

class CustomList:
    def __init__(self, mylist):
        self.mylist = mylist

    def bubble_sort(self):
        """ swap every element found """
        print('\n--Bubble Sort')
        print('before sorted : ', self.mylist)

        for i in range(0, len(self.mylist)):
            for j in range(i+1, len(self.mylist)):
                if self.mylist[i] > self.mylist[j]:
                    self.mylist[i], self.mylist[j] = self.mylist[j], self.mylist[i]
            print('iterasi  : ', self.mylist)
            # swapping
        print('sorted : ', self.mylist)

    def selection_sort(self):
        """ find the minimum value and swap it to front """
        print('\n--Selection Sort')
        print('before sorted : ', self.mylist)

        for i in range(0, len(self.mylist)):
            min_index = i
            for j in range(i+1, len(self.mylist)):
                if self.mylist[min_index] > self.mylist[j]:
                    min_index = j
            self.mylist[i], self.mylist[min_index] = self.mylist[min_index], self.mylist[i]
            print('proses : ', self.mylist)
        print('sorted : ', self.mylist)


if __name__ == '__main__':

    clist = CustomList([64, 25, 12, 22, 11])
    # clist.bubble_sort()
    clist.selection_sort()
