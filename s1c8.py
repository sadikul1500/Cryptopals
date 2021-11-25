#take 320 legnth string from the given file
s1 = ["972d40a3fe523a117967480b2e3ae1b7e513be738d708ff579e856b0bc19e2da4d4c1d2f3143720bbf3d58f1a067799e8209cfb3f3a4f75d920ef269e839ad3733e99f08b1785dc2f053b37c04a4f7051aef25f27c335bf3ae4873cd740e088002f7ac499b78c17345426e159fbada0af882f47b78c0dc520b901573530082f0c370bc8af1ccb4ed58b08806ebcda8b10ecd3d1d4b917eeb2cfbaaf3ee967eac",
     'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a'
    ] 

for s in s1:
  s2 = []
  for i in range(20): #320 bytes ie 320/16 = 20 blocks
      s2 += [s[i*16:(i+1)*16]]

  print(1000000)  #just for nothing
  for i in range(20):
      for j in range(i+1, 20):
          if s2[i] == s2[j]:
              print(s[i]) # this is the string encoded with AES-ECB
              
              
#d880619740a8a19b7840a8a...............33f2c123c58386b06fba186a    is the answer
