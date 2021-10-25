import re
import argparse

class Trail:
    def __init__(self,sum=0,points=[]):
        self.sum=sum
        self.points=points

def prune(trails):


def main(args):
    trails=[]
    lower_triangular_matrix_file=open(args.filename,'r')
    for line in lower_triangular_matrix_file:
        row=re.findall('(\d+)',line)
        # Top of the pyramid
        if y==0:
            sum=row[0]
        # Top-down layers
        else:

            if row[x]>row[x+1]:
                sum+=row[x]
            else:
                sum+=row[x+1]
                x+=1
        y+=1

    txt='The sum is '+str(sum)
    print(txt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',   type=str,   nargs=1)
    args=parser.parse_args()
    main(args)
