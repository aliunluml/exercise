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
        self.pos=points[-1].pos if points is not None else (0,0)

    def add_point(self,point):
        self.points.append(point)
        self.sum+=point.value
        self.pos=point.pos


def prune_same_end(trails,points):
    f=lambda trail,point:(trail.pos is point.pos)
    result=[]
    for p in points:
        same_end_trails=list(filter(lambda x:f(x,p),trails))
        end_best_trail=Trail()
        for trail in same_end_trails:
            if trail.sum>end_best_trail.sum:
                end_best_trail=trail
        result.append(end_best_trail)
    return result


def prune_dead_end(trails,y):
    dead_ends=[]
    result=[]
    for trail in trails:
        if trail.pos[1]<y:
            dead_ends.append(trail)
        else:
            result.append(trail)
    threshold=min([trail.sum for trail in result]) if len(result)!=0 else 0
    alive_ends=list(filter(lambda x:(x.sum>=threshold),dead_ends))
    result=result+alive_ends
    return result


def prune(trails,row_points):
    y=row_points[0].pos[1]
    trails=prune_same_end(trails,row_points)
    trails=prune_dead_end(trails,y)
    return trails


# Taken from https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def is_non_prime(n):
    if (n!=1) and (n==largest_prime_factor(n)):
        return False
    else:
        return True


def filter_non_prime(points):
    result=list(filter(lambda x:is_non_prime(x.value),points))
    return result


def main(args):
    start=Trail()
    trails=[start]
    y=0
    lower_triangular_matrix_file=open(args.filename,'r')
    for line in lower_triangular_matrix_file:
        row=re.findall('(\d+)',line)
        row_points=[Point(int(row[i]),(i,y)) for i in range(0,len(row))]
        non_prime_points=filter_non_prime(row_points)
        new_trails=[]
        for trail in trails:
            pos=trail.pos
            s_points=list(filter(lambda x:(x.pos[0]==pos[0]),non_prime_points))
            se_points=list(filter(lambda x:(x.pos[0]==(pos[0]+1)),non_prime_points))
            if len(s_points+se_points)==0:
                continue
            elif len(s_points+se_points)==1:
                point=(s_points+se_points)[0]
                trail.add_point(point)
            else:
                new_trail=copy.deepcopy(trail)
                trail.add_point(s_points[0])
                new_trail.add_point(se_points[0])
                new_trails.append(new_trail)
        trails=trails+new_trails
        trails=prune(trails,non_prime_points)
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
