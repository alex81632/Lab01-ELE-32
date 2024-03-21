import random
import CanalBSC
import HammingCodifier
import HammingDecodifier
import OwnCodifier
import OwnDecodifier
import numpy as np
import matplotlib.pyplot as plt

hc = HammingCodifier.HammingCodifier()
hd = HammingDecodifier.HammingDecodifier()

oc = OwnCodifier.OwnCodifier()
od = OwnDecodifier.OwnDecodifier()

def generate1MBits():
    return [random.randint(0, 1) for _ in range(1_000_000)]

# agrgar os 1M bits em sub vetores de 4 bits
def split_into_4bit_subvectors(bits):
    subvectors = []
    for i in range(0, len(bits), 4):
        subvectors.append(bits[i:i+4])
    return subvectors

def split_into_5bit_subvectors(bits):
    subvectors = []
    for i in range(0, len(bits), 5):
        subvectors.append(bits[i:i+5])
    return subvectors

def testHamming(p, subvectors):
    cBSC = CanalBSC.CanalBSC(p)
    numErrors = 0
    for subvector in subvectors:
        codified = hc.codify(subvector.copy())
        received = cBSC.canal(codified.copy())
        decoded = hd.decodify(received.copy())
        if (codified != decoded).any():
            numErrors += 1
    return numErrors/len(subvectors)

def testOwn(p, subvectors):
    cBSC = CanalBSC.CanalBSC(p)
    numErrors = 0
    for subvector in subvectors:
        codified = oc.codify(subvector.copy())
        received = cBSC.canal(codified.copy())
        decoded = od.decodify(received.copy())
        if (np.array_equal(codified, decoded) == False):
            numErrors += 1
    return numErrors/len(subvectors)

def testChanel(p, subvectors):
    cBSC = CanalBSC.CanalBSC(p)
    numErrors = 0
    for subvector in subvectors:
        received = cBSC.canal(subvector.copy())
        if (np.array_equal(subvector, received) == False):
            numErrors += 1
    return numErrors/len(subvectors)

if __name__ == "__main__":
    bits = generate1MBits()
    subvectors4 = split_into_4bit_subvectors(bits)
    subvectors5 = split_into_5bit_subvectors(bits)
    probs = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    oerros = []
    herros = []
    cerros = []
    for(p) in probs:
        oerros.append(testOwn(p, subvectors5))
        herros.append(testHamming(p, subvectors4))
        cerros.append(testChanel(p, subvectors4))
    
    print(oerros)
    print(herros)
    print(cerros)

    fig, ax = plt.subplots()
    ax.plot(probs, oerros, label="Own")
    ax.plot(probs, herros, label="Hamming")
    ax.plot(probs, cerros, label="Canal")
    ax.legend()
    plt.show()