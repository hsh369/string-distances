#levenshtein distance 

#Levenshteyn algoritmi
# 'a' va 'b' qiymatlarni aniqlash:
a = "matematika"
b = "maktab"

def levenshein_dist():
  # lev o'zgaruchi massivini rows = len(a) + 1 va columns = len(b) + 1 orqali kiritish
  lev = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

  # Birinchi qatordagi(row) sonlarni aniqlash:
  for i in range(len(a) + 1):
      lev[i][0] = i
  # Birinchi ustundagi(column) sonlarni aniqlash:
  for j in range(len(b) + 1):
      lev[0][j] = j

  for i in range(1, len(a) + 1):
      for j in range(1, len(b) + 1):
          if a[i - 1] == b[j - 1]:
              lev[i][j] = lev[i - 1][j - 1]
          else:
              insertion = 1 + lev[i][j - 1] #cost of insertion
              deletion = 1 + lev[i - 1][j] #cost of deletion 
              replacement = 1 + lev[i - 1][j - 1] #cost of replacement

              # Eng foydali o'zgarishni tanlash:
              lev[i][j] = min(insertion, deletion, replacement)
