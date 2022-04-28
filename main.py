
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
      return(len(T))
    elif (T == ""):
      return(len(S))
    else:
      if (S[0] == T[0]):
        return(MED(S[1:], T[1:]))
      else:
        return 1 + min(MED(S, T[1:]), MED(S[1:], T[1:]), MED(S[1:], T)) # insert, substitute, delete



def fast_MED(S, T, MED={}):
    r, c = (len(S), len(T))
    MED = [[0 for x in range(c+1)] for y in range(r+1)]

    for i in range(len(S)+1):
      for j in range(len(T)+1):
        if i == 0:
          MED[i][j] = j
        elif j == 0:
          MED[i][j] = i
        elif S[i-1] == T[j-1]:
          MED[i][j] = MED[i-1][j-1] 
        else:
          MED[i][j] = 1 + min(MED[i][j-1], MED[i-1][j-1], MED[i-1][j])
        
    return MED[-1][-1]



def fast_align_MED(S, T, MED={}):
    r, c = (len(S), len(T))
    MED = [[0 for x in range(c)] for y in range(r)]

    for i in range(len(S)):
      for j in range(len(T)):
        if i == 0:
          MED[i][j] = j
        elif j == 0:
          MED[i][j] = i
        elif S[i-1] == T[j-1]:
          MED[i][j] = MED[i-1][j-1] 
        else:
          MED[i][j] = 1 + min(MED[i][j-1], MED[i-1][j-1], MED[i-1][j])

    alignedS = ""
    alignedT = "" 

    if len(S) == 0:
      alignedS = '-' * len(T)
      return alignedS, T

    if len(T) == 0:
      alignedT = '-' * len(S)
      return S, alignedT

    if S[0] == T[0]:
      alignedS = (S[0]+ fast_align_MED(S[1:], T[1:])[0])
      alignedT = (T[0]+ fast_align_MED(S[1:], T[1:])[1])

    insert = fast_MED(S, T[1:])
    delete = fast_MED(S[1:], T)
    sub = fast_MED(S[1:], T[1:])

    if min(insert, delete, sub) == insert and insert != sub: 
      alignedS = ('-' + fast_align_MED(S, T[1:])[0])
      alignedT = (T[0] + fast_align_MED(S, T[1:])[1])
    
    if min(insert, delete, sub) == delete and delete != sub:
      alignedS = (S[0] + fast_align_MED(S[1:], T)[0])
      alignedT = ('-' + fast_align_MED(S[1:], T)[1])

    if min(insert, delete, sub) == sub: 
      alignedS = (S[0] + fast_align_MED(S[1:], T[1:])[0])
      alignedT = (T[0] + fast_align_MED(S[1:], T[1:])[1])


    return alignedS, alignedT

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

print(MED('elephant', 'relevant'))
print(fast_MED('elephant', 'relevant'))
print(fast_align_MED('elephant', 'relevant'))
