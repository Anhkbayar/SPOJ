def find_orts_davhar_haalga(F, E, D, haalga):
    davhriin_haalga = F * D
    orts = (haalga - 1) // davhriin_haalga + 1
    ortsnii_bairlal = (haalga - 1) % davhriin_haalga
    davhar = ortsnii_bairlal // D + 1
    davhar_haalga = ortsnii_bairlal % D + 1
    
    return orts, davhar, davhar_haalga

orts_davhar_haalga = input()
haalga = int(input())
res = [int(i)for i in orts_davhar_haalga.split()]
F = res[0]
E = res[1]
D = res[2]
orts, davhar, davhar_haalga = find_orts_davhar_haalga(F, E, D, haalga)

print(orts, davhar, davhar_haalga)
