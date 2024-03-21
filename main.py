import HammingCodifier
import CanalBSC
import HammingDecodifier

if __name__ == "__main__":
    u = [1, 0, 1, 1]
    hc = HammingCodifier.HammingCodifier()
    cBSC = CanalBSC.CanalBSC(0.2)
    hd = HammingDecodifier.HammingDecodifier()
    v = hc.codify(u)
    print(v)
    r = cBSC.canal(v)
    print(r)
    s = hd.decodify(r)
    print(s)
