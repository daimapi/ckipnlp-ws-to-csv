import numpy as np
import os
from ckipnlp.pipeline import CkipPipeline, CkipDocument


#import csv

def get_tars() -> list:
    f = open("tar.txt", 'r', encoding='UTF-8')
    tars = []
    for line in f.readlines():
        if line != '\n':
            tars.append(line.partition('\n')[0])
    f.close()
    return tars


def segword(path: str):
    f = open(path, 'r', encoding='UTF-8')
    doc = CkipDocument(raw=f.read())
    CkipPipeline().get_ws(doc)
    f.close()
    return doc.ws


if __name__ == '__main__':
    tars = get_tars()
    srcs = os.listdir("src")
    output = np.zeros([len(tars), len(srcs)], dtype=int)
    n = 0
    for tar in tars:
        m = 0
        for src in srcs:
            c = 0
            for line in segword(path="src/" + src):  #sentence
                words = line.to_text().split()
                #print(tar)
                #print(words)
                c += words.count(tar)
            #    print(c)
            #print(c)
            #print("//")
            output[n, m] = str(c)
            #output[0, m] = str(src)
            m += 1
        #output[n, 0] = str(tar)
        n += 1
    #add tags
    outstr = np.array(output.astype(str))
    #put src(path) in row0
    srcar = np.array(srcs)
    outstr = np.insert(outstr, 0, srcar, axis=0)
    #put tar in col0
    tarar = np.insert(np.array(tars), 0, 0)
    outstr = np.insert(outstr, 0, tarar, axis=1)
    np.savetxt('output_data.csv', outstr, delimiter=',', fmt="%s", encoding='UTF-8')