LUOTI_KERROIN = 13.3
NAULA_KERROIN = 32 * LUOTI_KERROIN
LEIVISKÄ_KERROIN = 20 * NAULA_KERROIN * LUOTI_KERROIN


leiviskätGrammoina = float(input('Anna leiviskät: ')) * LEIVISKÄ_KERROIN
naulatGrammoina = float(input('Anna naulat: ')) * NAULA_KERROIN
luoditGrammoina = float(input('Anna luodit: ')) * LUOTI_KERROIN


grammatYhteensä = leiviskätGrammoina + naulatGrammoina + luoditGrammoina

kilogrammat = grammatYhteensä / 1000
grammat = grammatYhteensä % 1000

print(kilogrammat)
print(grammat)