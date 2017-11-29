# coding:utf-8

from CombinSet import CombinSets as cs

if __name__ == '__main__':
    set_list = [set([1,2,3,4,5]),set([6,7,8,9,10]),set([11,12,1,31,4]),set([55,88]),set([99,111,55])]
    cs = cs(set_list)

    print (cs.CombinSets())