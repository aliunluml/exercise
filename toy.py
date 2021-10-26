import re
import argparse
import copy

class Point:
    def __init__(self,value,pos):
        self.value=value
        self.pos=pos


class Trail:
    def __init__(self,points=None):
        self.points=points if points is not None else []
        self.sum=sum([p.value for p in points]) if points is not None else 0
        self.end=points[-1].pos if points is not None else (0,0)

    def add_point(self,point):
        self.points.append(point)
        self.sum+=point.value
        self.end=point.pos

def prune(trails,new_trails):
    result=[trails[0]]
    for trail,new_trail in zip(trails[1:],new_trails[:-1]):
        assert (trail.end is new_trail.end)
        if trail.sum>new_trail.sum:
            result.append(trail)
        else:
            result.append(new_trail)
    result.append(new_trails[-1])
    return result



def main(args):
    start=Trail()
    trails=[start]
    y=0
    lower_triangular_matrix_file=open(args.filename,'r')
    for line in lower_triangular_matrix_file:
        row=re.findall('(\d+)',line)
        row_points=[Point(int(row[i]),(i,y)) for i in range(0,len(row))]
        if y!=0:
            new_trails=[]
            for trail in trails:
                pos=trail.end
                new_trail=copy.deepcopy(trail)
                trail.add_point(row_points[pos[0]])
                new_trail.add_point(row_points[pos[0]+1])
                new_trails.append(new_trail)
            trails=prune(trails,new_trails)
        else:
            start.add_point(row_points[0])
        y+=1

    lower_triangular_matrix_file.close()


    best_trail=Trail()
    for trail in trails:
        if trail.sum>best_trail.sum:
            best_trail=trail

    txt='The sum is '+str(best_trail.sum)
    print(txt)
    txt='The summed up element indices are:\n'+str([p.pos for p in best_trail.points])
    print(txt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',   type=str)
    args=parser.parse_args()
    main(args)
