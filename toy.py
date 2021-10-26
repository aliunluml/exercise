import re
import argparse

class Point:
    def __init__(self,value,pos):
        self.value=value
        self.pos=pos


class Trail:
    def __init__(self,points=[]):
        self.points=points
        self.sum=sum([p.value for p in points]) if len(points)!=0 else 0
        self.end=points[-1].pos if len(points)!=0 else (0,0)

    def add_point(self,point):
        self.points.append(point)
        self.sum+=point.value
        self.end=point.pos

def prune(trails,new_trails):
    len_same_end=len(trails)


def main(args):
    start=Trail()
    trails=[start]
    y=0
    lower_triangular_matrix_file=open(args.filename,'r')
    for line in lower_triangular_matrix_file:
        row=re.findall('(\d+)',line)
        row_points=[Point(int(row[i]),(i,y)) for i in range(len(row))]
        new_trails=[]
        for trail in trails:
            pos=trail.end
            new_trail=trail.copy()
            trail.add_point(row_points[pos[0]])
            new_trail.add_point(row_points[pos[0]+1])
            new_trails.append(new_trail)
        trails=prune(trails,new_trails)
        y+=1



    txt='The sum is '+str(sum)
    print(txt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',   type=str,   nargs=1)
    args=parser.parse_args()
    main(args)
