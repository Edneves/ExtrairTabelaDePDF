import tabula

lista_tabelas = tabula.read_pdf("ResultadoVale.pdf",stream=True,  pages="10")
print("Quantidade de tabelas: ", len(lista_tabelas))

tabela = lista_tabelas[0]
tabela.columns = tabela.iloc[0]
tabela[[0,1]] = tabela["Variação percentual"].str.split(" ", expand=True)
tabela = tabela[1:9]
tabela = tabela.set_index("R$ milhões")
tabela.columns = tabela.iloc[0]
tabela = tabela[1:]
tabela = tabela.drop("1T21/4T20 1T21/1T20", axis=1)

tabela.to_csv("ResultadoVale.csv", encoding="utf-8")