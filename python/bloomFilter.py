#for non-cryptographic hash function import pyhash

import pyhash

bitVector = [0] * 20

#Non-cryptoraphic hash functions (Murmur and FNV)

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

#calculate the output of FNV and Murmur hash funnction for pikatchu
fnvPick = fnv("Pikachu") % 20
fnvChar = fnv("Charmender") % 20

murmurPick = murmur("Pikachu") % 20
murmurChar = murmur("Charmender") % 20

print(fnvPick)
print(fnvChar)

bitVector[fnvPick] = 1
bitVector[murmurPicK] = 1

bitVector[fnvChar] = 1
bitVector[murmurChar] = 1

