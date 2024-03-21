import random
import CanalBSC
import HammingCodifier
import HammingDecodifier

hc = HammingCodifier.HammingCodifier()
hd = HammingDecodifier.HammingDecodifier()

def generate1MBits():
    return [random.randint(0, 1) for _ in range(1_000_000)]

# agrgar os 1M bits em sub vetores de 4 bits
def split_into_4bit_subvectors(bits):
    subvectors = []
    for i in range(0, len(bits), 4):
        subvectors.append(bits[i:i+4])
    return subvectors

def testHamming(p, subvectors):
    cBSC = CanalBSC.CanalBSC(p)
    numErrors = 0
    for subvector in subvectors:
        print(subvector)
        codified = hc.codify(subvector)
        received = cBSC.canal(codified)
        decoded = hd.decodify(received)
        if (codified == decoded).all():
            numErrors += 0
        else:
            numErrors += 1
    return numErrors/len(subvectors), numErrors

if __name__ == "__main__":
    bits = generate1MBits()
    subvectors = split_into_4bit_subvectors(bits)
    print(testHamming(0.5, subvectors))