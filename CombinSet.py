# coding:utf-8

class CombinSets():
    def __init__(self,set_list = []):
        '''

        :param set_list:
        '''
        self.set_list = set_list

    def CombinSets(self):
        '''

        :return:
        '''
        ds = []
        for iset in self.set_list:
            tds = []
            tset = iset.copy()
            for jset in ds:
                if len(iset&jset)>0:
                    tset |= jset
                else:
                    tds.append(jset)
            tds.append(tset)
            ds = tds
        return ds