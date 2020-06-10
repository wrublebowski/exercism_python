'''
Excercise goal was to organize a kindergarten garden. Each kid has to plant 4 plants, 2 plants each row.
Method 'plants' shows a kid's plants collection.
'''

diagram = 'VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV'
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
przydzial = {}

class Garden:

    def __init__(self,diagram,students=None):

        self.diagram=diagram
        if students==None:
            self.students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.students=sorted(students)

        row1 = diagram.split('\n')[0]
        row2 = diagram.split('\n')[1]
        for s in range(len(self.students)):
            przydzial[self.students[s]]=row1[(2*s):(2*s+2)]+row2[(2*s):(2*s+2)]

    def plants(self,name):
        rosliny = []

        for x in przydzial[name]:
            if x=="V":
                rosliny.append("Violets")
            if x=="G":
                rosliny.append("Grass")
            if x=="C":
                rosliny.append("Clover")
            if x=="R":
                rosliny.append("Radishes")
        print(rosliny)
        return rosliny

garden = Garden(diagram,students)
garden.plants("Bob")
