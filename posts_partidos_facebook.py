# -*- coding: utf-8
""" Abraji (https://www.abraji.org.br)
    Reinaldo Chaves (reinaldo@abraji.org.br)
    Script para acessar postagens de partidos políticos no Facebook
    Seleciona os posts relacionados a pandemia de coronavírus
    Faz gráficos a partir do arquivo de análise gerado pela equipe do projeto
"""
import pandas as pd
from facebook_scraper import get_posts
# Cria dataframe com páginas dos partidos políticos do Brasil"
dados = {
    'partido': ["MDB", "PTB", "PDT", "PT",  "DEM", "PCdoB", "PSB", "PSDB", "PTC", "PSC", "PMN", "Cidadania", "PV",  "Avante", "PP", "PSTU", "PCB", "PRTB",  "DC",  "PCO", "PODE", "PSL", "Aliança pelo Brasil", "REPUBLICANOS", "PSOL", "PL", "PSD", "PATRIOTA", "PROS", "SOLIDARIEDADE",  "NOVO", "REDE",  "PMB", "UP"],
    'url': ["MDBNacional15",  "PTBNacional", "pdt.org.br", "pt.brasil", "democratas", "pcdob65", "psbnacional40", "PSDBoficial", "ptc36nacional", "PSC20", "PMNNACIONAL", "Cidadania23Brasil", "partidoverde43", "70.avante","progressistas", "pstu16", "PartidoComunistaBrasileiroPcb",  "prtboficial", "democracia.crista.nacional",  "pco29", "podemos19",  "PartidoSocialLiberalBR", "aliancapelobr", "Republicanos10",  "psol50", "Partido-Liberal-22-109795543775931",  "psd.br",  "Patriota51Oficial", "pros.nacional", "solidariedadebr",  "NOVO30", "RedeSustentabilidade18", "pmbnacional35", "unidadepopularUP"]
}
partidos = pd.DataFrame(dados)

# Função que coleta os posts no Facebook
def procura_fb(nome, partido):
    conta = 0
    # Trabalha com as últimas 50 páginas de posts
    # Envia credenciais de uma conta - opcional
    # Intervalo de sleep e timeout para segurança
    for post in get_posts(nome, pages=50, credentials=('usuario', 'senha'), sleep=2, timeout=10):
        lista = [post]

        df = pd.DataFrame(lista)
        df['partido'] = partido

        if conta == 0:
            df_posts_get = df
        else:
            df_posts_get = df_posts_get.append(df)

        conta += 1

    return df_posts_get

conta_vez = 0
erros = []

# Iteração entre todas as páginas dos partidos
for num, row in partidos.iterrows():
    url = row['url']
    partido = row['partido']
    print(url)

    try:
        df_posts_vez = procura_fb(url, partido)

        if df_posts_vez.empty is False:
            if conta_vez == 0:
                df_posts_final = df_posts_vez
            else:
                df_posts_final = df_posts_final.append(df_posts_vez)

            conta_vez += 1
        else:
            print("Falha em: ", url)
            dicionario = {
                "url_com_erro": url,
                "partido": partido
                    }
            erros.append(dicionario)

    except UnboundLocalError as error:
        print("+++++++++++++")
        print("URL COM ERRO: ", url)
        print(error)
        print("+++++++++++++")
        dicionario = {
            "url_com_erro": url,
            "partido": partido
                }
        erros.append(dicionario)

    except Exception as exception:
        print("+++++++++++++")
        print("URL COM ERRO: ", url)
        print(exception)
        print("+++++++++++++")
        dicionario = {
            "url_com_erro": url,
            "partido": partido
                }
        erros.append(dicionario)

# Armazena todos os erros para consulta posterior
df_erros = pd.DataFrame(erros)
# A depender da qualidade da conexão ou do tráfego é normal algumas páginas apresentarem erro
# Por isso as que tiveram mensagem de erro são executadas novamente individualmente"
df_posts_2 = procura_fb("PMNNACIONAL", "PMN")
# Une todas as extrações, caso necessário"
frames = [df_posts_final, df_posts_2]
df_acumula_semanal = pd.concat(frames)
df_acumula_semanal = df_posts_final.copy()
"""
DAQUI PARA BAIXO AINDA NÃO EDITEI
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "Int64Index: 6307 entries, 0 to 0
      "Data columns (total 12 columns):
      "post_id        6239 non-null object
      "text           6307 non-null object
      "post_text      6307 non-null object
      "shared_text    6307 non-null object
      "time           6256 non-null object
      "image          5013 non-null object
      "likes          6307 non-null int64
      "comments       6307 non-null int64
      "shares         6307 non-null int64
      "post_url       5413 non-null object
      "link           2428 non-null object
      "partido        6307 non-null object
      "dtypes: int64(3), object(9)
      "memory usage: 640.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df_acumula_semanal.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_acumula_semanal.to_excel('resultados/brutos_semanais/posts_partidos_ate_19_abr_2020.xlsx',sheet_name='Sheet1', index=False)
    "df_acumula_semanal.to_csv('resultados/brutos_semanais/posts_partidos_ate_19_abr_2020.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carrega o dataframe do ultimo arquivo bruto consolidado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_bruto_acumulado = pd.read_excel('resultados/brutos_acumulados/posts_partidos_ate_14_abr_2020.xlsx',sheet_name='Sheet1', dtype = str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "RangeIndex: 9328 entries, 0 to 9327
      "Data columns (total 12 columns):
      "post_id        8855 non-null object
      "text           8716 non-null object
      "post_text      8017 non-null object
      "shared_text    3223 non-null object
      "time           8868 non-null object
      "image          7175 non-null object
      "likes          8929 non-null object
      "comments       8929 non-null object
      "shares         8929 non-null object
      "post_url       7225 non-null object
      "link           3488 non-null object
      "partido        8929 non-null object
      "dtypes: object(12)
      "memory usage: 874.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df_bruto_acumulado.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compara os dois pelo id do post e adiciona os novos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "frames = [df_acumula_semanal, df_bruto_acumulado]#order here is important 
    "df_result = pd.concat(frames).drop_duplicates('post_id')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "Int64Index: 9633 entries, 0 to 9327
      "Data columns (total 12 columns):
      "post_id        9632 non-null object
      "text           9578 non-null object
      "post_text      9369 non-null object
      "shared_text    7502 non-null object
      "time           9632 non-null object
      "image          7732 non-null object
      "likes          9633 non-null object
      "comments       9633 non-null object
      "shares         9633 non-null object
      "post_url       7792 non-null object
      "link           3809 non-null object
      "partido        9633 non-null object
      "dtypes: object(12)
      "memory usage: 978.4+ KB\n"
     ]
    }
   ],
   "source": [
    "df_result.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_result.to_excel('resultados/brutos_acumulados/posts_partidos_acumulados_ate_19_abr.xlsx',sheet_name='Sheet1', index=False)
    "df_result.to_csv('resultados/brutos_acumulados/posts_partidos_acumulados_ate_19_abr.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Filtra só posts relacionados a pandemia da covid-19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_post_filtra = df_result[pd.notnull(df_result['post_text'])].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_post_filtra['post_text_upper'] = df_post_filtra['post_text'].str.upper()
    "search_list = ['CORONAVÍRUS', 'CORONAVIRUS', 'CORONA', 'CORONA VIRUS', 'CORONA VÍRUS', 'EPIDEMIA', 'PANDEMIA', 'COVID19', 'COVID 19', 'COVID', 'VÍRUS', 'VIRUS', 'COVID-19']
    "mask = df_post_filtra['post_text_upper'].str.contains('|'.join(search_list))
    "seleciona = df_post_filtra[mask]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "Int64Index: 2122 entries, 0 to 8569
      "Data columns (total 13 columns):
      "post_id            2122 non-null object
      "text               2122 non-null object
      "post_text          2122 non-null object
      "shared_text        1905 non-null object
      "time               2122 non-null object
      "image              1795 non-null object
      "likes              2122 non-null object
      "comments           2122 non-null object
      "shares             2122 non-null object
      "post_url           1701 non-null object
      "link               1077 non-null object
      "partido            2122 non-null object
      "post_text_upper    2122 non-null object
      "dtypes: object(13)
      "memory usage: 232.1+ KB\n"
     ]
    }
   ],
   "source": [
    "seleciona.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "seleciona.to_excel('resultados/covid19/posts_partidos_ate_19_abr_2020_relacionados_covid19.xlsx',sheet_name='Sheet1', index=False)
    "seleciona.to_csv('resultados/covid19/posts_partidos_ate_19_abr_2020_relacionados_covid19.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carrega o arquivo manual criado pela equipe do projeto
    "# Com manifestações e propostas encontradas dos partidos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "compilado = pd.read_excel('resultados/relatorios_partidos/COMPILADO_PARTIDOS_COVID_20_abril_2020.xlsx',sheet_name='Planilha1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "RangeIndex: 146 entries, 0 to 145
      "Data columns (total 35 columns):
      "MANIFESTAÇÃO / PROPOSTA    146 non-null object
      "ALIANÇA                    0 non-null float64
      "AVANTE                     6 non-null object
      "CIDADANIA                  3 non-null object
      "DC                         0 non-null float64
      "DEMOCRATAS                 5 non-null object
      "MDB                        11 non-null object
      "NOVO                       17 non-null object
      "PATRIOTA                   0 non-null float64
      "PCB                        18 non-null object
      "PC do B                    33 non-null object
      "PCO                        2 non-null object
      "PDT                        21 non-null object
      "PL                         0 non-null float64
      "PMB                        3 non-null object
      "PMN                        0 non-null float64
      "PODEMOS                    15 non-null object
      "PP                         9 non-null object
      "PRTB                       0 non-null float64
      "PROS                       4 non-null object
      "PSB                        34 non-null object
      "PSC                        3 non-null object
      "PSD                        5 non-null object
      "PSDB                       3 non-null object
      "PSL                        17 non-null object
      "PSOL                       39 non-null object
      "PSTU                       18 non-null object
      "PT                         27 non-null object
      "PTB                        1 non-null object
      "PTC                        0 non-null float64
      "PV                         13 non-null object
      "REDE                       17 non-null object
      "REPUBLICANOS               4 non-null object
      "SDD                        6 non-null object
      "UP                         6 non-null object
      "dtypes: float64(7), object(28)
      "memory usage: 40.0+ KB\n"
     ]
    }
   ],
   "source": [
    "compilado.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Opções para mostrar conteúdos totais de texto sem abreviação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pd.set_option('display.max_rows', None)
    "#pd.set_option('display.max_columns', None)
    "#pd.set_option('display.width', None)
    "#pd.set_option('display.max_colwidth', -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Faz uma contagem de quantas manifestações/propostas cada partido apresentou"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/abraji/Documentos/Code/ferramentas/lib/python3.6/site-packages/pandas/core/ops/__init__.py:1115: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      "  result = method(y)\n"
     ]
    }
   ],
   "source": [
    "lista = []
    "for (columnName, columnData) in compilado.iteritems():
    "    #print('Colunm Name : ', columnName)
    "    #print('Column Contents : ', columnData.values)
    "    if columnName != \"MANIFESTAÇÃO / PROPOSTA\":
    "        coleta = compilado["MANIFESTAÇÃO / PROPOSTA\", columnName]].copy()
    "        
    "        teste_coleta = coleta[(coleta[columnName] == 'x')].copy()
    "        #print(\"-------\")
    "        #print(teste_coleta)
    "        #print(\"O partido\", teste_coleta.columns[1], \"tem\", teste_coleta.shape[0],  \"manifestações ou propostas\")
    "        
    "        dicionario = {\"partido\": teste_coleta.columns[1].strip(),
    "                      \"total_manifestacoes_propostas\": teste_coleta.shape[0]}
    "        lista.append(dicionario)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_contagem = pd.DataFrame(lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>
      "RangeIndex: 34 entries, 0 to 33
      "Data columns (total 2 columns):
      "partido                          34 non-null object
      "total_manifestacoes_propostas    34 non-null int64
      "dtypes: int64(1), object(1)
      "memory usage: 672.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "df_contagem.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_contagem.sort_values(by=['total_manifestacoes_propostas'], inplace=True, ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>
       "<style scoped>
       "    .dataframe tbody tr th:only-of-type {
       "        vertical-align: middle;
       "    }
       "
       "    .dataframe tbody tr th {
       "        vertical-align: top;
       "    }
       "
       "    .dataframe thead th {
       "        text-align: right;
       "    }
       "</style>
       "<table border=\"1\" class=\"dataframe\">
       "  <thead>
       "    <tr style=\"text-align: right;\">
       "      <th></th>
       "      <th>index</th>
       "      <th>partido</th>
       "      <th>total_manifestacoes_propostas</th>
       "    </tr>
       "  </thead>
       "  <tbody>
       "    <tr>
       "      <th>0</th>
       "      <td>24</td>
       "      <td>PSOL</td>
       "      <td>39</td>
       "    </tr>
       "    <tr>
       "      <th>1</th>
       "      <td>19</td>
       "      <td>PSB</td>
       "      <td>34</td>
       "    </tr>
       "    <tr>
       "      <th>2</th>
       "      <td>9</td>
       "      <td>PC do B</td>
       "      <td>33</td>
       "    </tr>
       "    <tr>
       "      <th>3</th>
       "      <td>26</td>
       "      <td>PT</td>
       "      <td>27</td>
       "    </tr>
       "    <tr>
       "      <th>4</th>
       "      <td>11</td>
       "      <td>PDT</td>
       "      <td>21</td>
       "    </tr>
       "  </tbody>
       "</table>
       "</div>"
      ],
      "text/plain": [
       "   index  partido  total_manifestacoes_propostas
       "0     24     PSOL                             39
       "1     19      PSB                             34
       "2      9  PC do B                             33
       "3     26       PT                             27
       "4     11      PDT                             21"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_contagem.reset_index().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gráfico de barras barplot 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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AFBESAIAAACgiJAEAAAAQBEhCQAAAIAiQhIAAAAARYQkAAAAAIoISQAAAAAUEZIAAAAAKCIkAQAAAFBESAIAAACgiJAEAAAAQBEhCQAAAIAiQhIAAAAARYQkAAAAAIoISQAAAAAUEZIAAAAAKCIkAQAAAFBESAIAAACgiJAEAAAAQBEhCQAAAIAixSHpoYceygsvvJAkWbp0ab7+9a/nG9/4Rv7whz/UbBwAAAAAjaM4JJ177rnp1KlTkmTatGlZv359KpVKzjnnnJqNAwAAAKBxdC5945IlS9KvX7+sX78+999/f+bOnZttttkmBx98cC33AQAAANAgikPS9ttvn1deeSW/+c1vMnDgwHTr1i3r1q3L+vXra7kPAAAAgAZRHJJOOOGEfPrTn84bb7yRCRMmJEkee+yxfPjDH97kZ5cvX57x48fn+eefT3Nzcz70oQ9l6tSp6dWrV3bffffstttuaWr6011206dPz+677/4Ofx0AAAAAaqU4JJ166qk57LDD0qlTp3zwgx9MkvTt2zfnn3/+Jj9bqVRyyimnZP/990/yp2csXXLJJbnwwguTJLfccku6dev2TvYDAAAAUCfFISlJ/uZv/uZt//1Wevbs2R6RkmSvvfbKzTffvDmnBgAAAGALKw5JK1euzLe//e3Mmzcvy5cvT7VabX/tvvvuKz5hW1tbbr755owYMaL92IknnpgNGzbkH//xH3PGGWekubm5+PuSZMGCBUmSYcOGbdbn3o1HH330TY/bUN/zv9UGAAAAoOMVh6QpU6ZkyZIlGT16dM4888zMmDEj1113XQ4//PDNOuF5552Xrl275oQTTkjypwjV0tKSlStX5swzz8zMmTPzta99bbO+c+jQoenSpctmfebdqncssaGxNwAAAMDWorW1tf2inb/WVPolDzzwQK644op89KMfTadOnfLRj3403/rWt3LHHXcUD5k2bVp+//vf51vf+lb7w7VbWlqS/Omvwn3mM5/JY489Vvx9AAAAANRPcUhqa2tL9+7dkyRdu3bN66+/nt69e+f3v/990ecvu+yyLFiwIDNnzmy/de2Pf/xj1q5dmyRZv3597rnnngwZMmRzfwcAAAAA6qD41rbBgwdn3rx5OfDAAzN8+PBMmTIl3bp1y4ABAzb52d/85je5+uqrM2DAgBx33HFJkl122SWnnHJKJk2alEqlkvXr12fvvffOmDFj3vEvAwAAAEDtFIek888/v/0B2xMnTsxll12W1157LdOnT9/kZwcNGpSnn376TV+bPXt26QQAAAAAtqDikLRs2bLsueeeSZIdd9wxF1xwQZLkv//7v2uzDAAAAICGUvyMpFGjRr3p8VNOOaXDxgAAAADQuDZ5RVJbW1uq1epG//mz559/Pp06darpQAAAAAAawyZD0t/93d+lUqm0//yXmpqactppp9VmGQAAAAANZZMh6Ze//GWq1WpOPPHE3Hjjje3HK5VKevXqlW233bamAwEAAABoDJsMSf3790+S3HvvvRsdX7t2bZqaih+xBAAAAMB7XHEJmjZtWvtfaLvvvvuy3377Zd99983cuXNrNg4AAACAxlEckmbPnp1BgwYlSWbOnJkZM2bkyiuvzDe/+c2ajQMAAACgcWzy1rY/W7NmTbbbbrssX748L7zwQg4//PAkyUsvvVSzcQAAAAA0juKQNGDAgPznf/5nnn/++fyf//N/kiTLli3zsG0AAACA94nikDR58uRceOGF6dy5cy688MIkyf33398elQAAAADYuhWHpD322CO33HLLRseOOuqoHHXUUR0+CgAAAIDGUxySkuThhx/OrFmzsnTp0vTp0ydHH310DjjggFptAwAAAKCBFP/Vtttuuy1f/epX07t37xx22GHp06dP/u3f/i233nprLfcBAAAA0CCKr0i69tpr8/3vfz+DBw9uP/axj30sX/nKVzJy5MiajAMAAACgcRRfkbRixYoMHDhwo2Mf/vCH88c//rHDRwEAAADQeIpD0j777JOLL744a9asSZKsXr0606dPz957712zcQAAAAA0juJb284999x87Wtfy/Dhw9OjR4/88Y9/zN57751LL720lvsAAAAAaBDFIalPnz656aab8vLLL7f/1badd965ltsAAAAAaCDFt7YlyWuvvZZHHnmk/T+vvfZarXYBAAAA0GCKQ9KDDz6YESNG5IYbbsivfvWr3HjjjRkxYkQefPDBWu4DAAAAoEEU39p23nnnZerUqfn4xz/efmzOnDk599xzc/fdd9dkHAAAAACNo/iKpKVLl+bwww/f6Nhhhx2WV155pcNHAQAAANB4ikPS0UcfnZtuummjYzfffHOOOeaYDh8FAAAAQOMpvrXtySefzC233JJrr702ffv2zZIlS7Js2bLsscce+dznPtf+vr+OTQAAAABsHYpD0siRIzNy5MhabgEAAACggRWHpGOPPbaWOwAAAABocMUhKUl+/OMf54477siSJUvSt2/fHH300fmXf/mXWm0DAAAAoIEUh6Qrr7wys2bNyhe+8IX069cvixYtyrXXXpulS5fm9NNPr+VGAAAAABpAcUi67bbbcsMNN6R///7txw466KCccMIJQhIAAADA+0BT6RvXrFmTXr16bXSsZ8+eWbt2bYePAgAAAKDxFIekgw8+OOPGjcvvfve7rF27Ns8++2zOOuusHHTQQbXcBwAAAECDKA5JkyZNSrdu3XLUUUdl7733zjHHHJPtttsu55xzTi33AQAAANAgip6R1NbWll/96lc5//zzc/HFF2f58uX5wAc+kKam4g4FAAAAwHtcUQlqamrK6NGj09zcnKampuy4444iEgAAAMD7THEN2nffffPEE0/UcgsAAAAADazo1rYk6devX774xS/m0EMPzc4775xKpdL+2pgxY2oyDgAAAIDGURySWltb89GPfjRJsmTJkpoNAgAAAKAxFYekiy66qJY7AAAAAGhwxSEpSf7nf/4nc+bMydKlS9OnT5987GMfy4ABA2o0DQAAAIBGUvyw7dmzZ+fYY4/N008/ne222y7PPPNMjj322MyePbuW+wAAAABoEMVXJH3rW9/KNddck3333bf92Pz58zN+/PgceeSRNRkHAAAAQOMoviJp1apV2WuvvTY6tueee2b16tUdPgoAAACAxlMckkaNGpXLLrssra2tSZK1a9fmm9/8ZkaNGlWzcQAAAAA0juJb2374wx/mlVdeyQ033JAddtghr732WqrVanr37p2bb765/X333XdfLXYCAAAAsIUVh6QZM2bUcgcAAAAADa44JO23336bfM+pp55a9D4AAAAA3nuKn5FUYv78+R35dQAAAAA0kA4NSQAAAABsvYQkAAAAAIoISQAAAAAU6dCQVK1WO/LrAAAAAGggHRqSTjvttI78OgAAAAAaSHFI+v73v5+nnnoqSfLEE0/kkEMOyYgRI/L444+3v+dLX/pSxy8EAAAAoCEUh6Trr78+u+yyS5Lk0ksvzec///mcfvrpufDCC2s2DgAAAIDGURySXn/99XTv3j0rV67M008/nRNPPDGf+cxn8txzz9VyHwAAAAANonPpG1taWvLYY4/lt7/9bYYPH55OnTpl5cqV6dSpUy33AQAAANAgikPS+PHj85WvfCXNzc254oorkiT33ntv/uEf/qFm4wAAAABoHMUh6SMf+Ujuv//+jY4dccQROeKIIzp8FAAAAACNpzgkJcmzzz6bu+++O6+++momTZqU559/Pm+88UYGDx5cq30AAAAANIjih23PmTMnn/vc57JkyZLMmjUrSbJ69epcfPHFNRsHAAAAQOMoviLpiiuuyPXXX5/Bgwdnzpw5SZLBgwdn4cKFNRsHAAAAQOMoviJp2bJl2X333ZMklUql/f/++WcAAAAAtm7FIenv//7vc8cdd2x07Kc//Wn22GOPDh8FAAAAQOMpvrVt4sSJOfnkk/OjH/0oq1evzsknn5znnnsu3/ve92q5DwAAAIAGURySBg4cmDlz5uTee+/NIYcckpaWlhxyyCHp1q1bLfcBAAAA0CCKQ1KSbLfddtlrr73S0tKSvn37ikgAAAAA7yPFIWnp0qUZO3ZsnnjiifTs2TMrVqzInnvumcsuuyx9+/at5UYAAAAAGkDxw7anTJmSwYMH55FHHsn999+fRx55JEOGDMnkyZNruQ8AAACABlEckh599NF8/etfT9euXZMkXbt2zfjx4/P444/XbBy8U23r122V5wIAAIAtqfjWth49euTZZ5/N4MGD24/97ne/yw477FCTYfBuNHVuzuNXHVmXc+192uy6nAcAAAC2tOKQdMopp+Tzn/98Pv3pT6dfv35ZtGhRfvKTn2TMmDG13AcAAABAgygOSSNHjsyuu+6aO++8M08//XT69OmTSy+9NAceeGAt9wEAAADQIIpDUpIceOCBwhEAAADA+1Txw7a//OUvZ/78+Rsdmz9/fr7yla90+CgAAAAAGk9xSJo3b1723nvvjY7ttddeefjhhzt8FAAAAACNpzgkNTc3Z82aNRsdW716dTp33qy74wAAAAB4jyoOSQcddFAmTZqUlStXJklWrlyZqVOn5uCDD67ZOAAAAAAaR3FIOuuss7Jy5crst99+OfDAA7Pffvtl5cqVmTBhQi33AQAAANAgiu9L69GjR6655posXbo0L7/8clpaWtK7d+9abgMAAACggWz2A4769OmT3r17p1qtpq2tLUnS1FR8YRMAAAAA71HFIWnJkiWZOnVq5s+fn9dee22j15566qkOHwYAAABAYym+lGjy5MnZZpttcv3116dr1665/fbbM2LEiJx77rm13AcAAABAgyi+Iunxxx/Pvffem65du6ZSqWTw4MG54IILctxxx2XkyJG13AgAAABAAygOSU1NTenc+U9v32GHHbJs2bJsv/32WbJkySY/u3z58owfPz7PP/98mpub86EPfShTp05Nr1698sQTT2TSpElpbW1N//79M2PGjOy4447v/DcCAAAAoCaKb23bc88981//9V9JkoMOOihf/epX8+UvfzlDhw7d5GcrlUpOOeWU3HPPPZk9e3Z23XXXXHLJJWlra8uZZ56ZSZMm5Z577snw4cNzySWXvPPfBgAAAICaKQ5J06dPz7777pskmTBhQg444IAMGjQol1122SY/27Nnz+y///7t/95rr72yaNGiLFiwIF26dMnw4cOTJMcdd1zuvvvuzf0dAAAAAKiD4lvbHnjggXzsYx9Lkmy77bYZPXp0kuTuu+/OEUccUXzCtra23HzzzRkxYkQWL16cfv36tb/Wq1evtLW1ZcWKFenZs2fxdy5YsCBJMmzYsOLPvFuPPvromx63ob7nb+QNAAAAsLUpDkkTJ05sD0l/adKkSZsVks4777x07do1J5xwQn7+858Xf+7tDB06NF26dOmQ7ypV71Bhgw0AAABQD62tre0X7fy1TYakF154IUlSrVbbf/7L15qbm4uHTJs2Lb///e9z1VVXpampKS0tLVm0aFH768uWLUtTU9NmXY0EAAAAQH1sMiQddthhqVQqqVarOeywwzZ6baeddsoZZ5xRdKLLLrssCxYsyDXXXNMen4YOHZq1a9dm/vz5GT58eG655ZbNuroJAAAAgPrZZEhauHBhkuSEE07IjTfe+I5O8pvf/CZXX311BgwYkOOOOy5Jsssuu2TmzJmZPn16Jk+enNbW1vTv3z8zZsx4R+cAAAAAoLaKn5H01xHphRdeSKVSyS677LLJzw4aNChPP/30m762zz77ZPbs2aUzAAAAANhCmkrfOHbs2Dz22GNJkh//+Mf5xCc+kU9+8pO57bbbajYOAAAAgMZRHJIefPDBDB06NEly/fXX5/vf/35uu+22fPe7363ZOAAAAAAaR/GtbW+88Uaam5uzZMmSrFixov3Pnb/yyis1GwcAAABA4ygOSUOGDMnVV1+dl156KYccckiSZMmSJdl+++1rtQ0AAACABlJ8a9sFF1yQZ555Jq2trfnqV7+aJHn88cdz5JFH1mwcAAAAAI2j+IqkD37wg7n00ks3OnbEEUfkiCOO6PBRAAAAADSe4iuSqtVqbr311px00kntVyHNmzcvd911V83GAQAAANA4ikPS5Zdfnh/96EcZOXJkFi9enCTZeeedc+2119ZsHAAAAACNozgk3X777bnqqqvyiU98IpVKJUmyyy675IUXXqjZOAAAAAAaR3FI2rBhQ7p165Yk7SFp1apV6dq1a22WAQAAANBQikPSRz7ykVx00UVZt25dkj89M+nyyy/PP/3TP9VsHAAAAACNozgkfeMb3wL1xKgAACAASURBVMgf/vCHDBs2LK+//nr23nvvLFq0KOPGjavlPgAAAAAaROe3e/GXv/xlDj300CRJly5dMnPmzLz66qt56aWX0tLSkt69e9dlJAAAAABb3ttekXTmmWe2/7z//vsnSXbcccfsscceIhIAAADA+8zbXpHUu3fv3HjjjRk4cGA2bNiQhx56KNVq9X+978ADD6zZQAAAAAAaw9uGpIsuuihXXHFFfvCDH+SNN97IhAkT/td7KpVKfvnLX9ZsIAAAAACN4W1D0j777JPrr78+SXLYYYfl5z//eT02AQAAANCAiv9qm4gEAAAA8P72tlcknXzyybnuuuuSJMcff3wqlcqbvu+mm27q+GUAAAAANJS3DUnHHHNM+8+f+cxnaj4GAAAAgMb1tiHpyCOPbP/52GOPrfkYAAAAABrX24akv3b//ffnqaeeyurVqzc6PmbMmA4dBQAAAEDjKQ5JU6dOzZw5c7L//vtnu+22q+UmAAAAABpQcUi68847c8cdd6SlpaWWewAAAABoUE2lb/zABz6Q7t2713ILAAAAAA2s+IqkUaNGZdy4cfnSl76UnXbaaaPXdt111w4fBgAAAEBjKQ5JU6ZMSZLcd999Gx2vVCp56qmnOnITAAAAAA2oOCQtXLiwljsAAAAAaHDFz0gCAAAA4P2t+Iqk9evX54c//GHmzZuX5cuXp1qttr9200031WQcAAAAAI2j+Iqkiy66KP/xH/+R4cOH59e//nX++Z//Oa+++moOOOCAWu4DAAAAoEEUh6Sf/exn+e53v5uTTjopnTp1ykknnZSZM2fm4YcfruU+eM9qW79ui59nQ5021Os8AAAAbFnFt7atXbs2LS0tSZJtt902a9asycCBA/Pkk0/WbBy8lzV1bs7/991P1Pw8//jFn77la506N+eu6z5e8w0fP/mump8DAACALa84JA0cODC/+tWvsscee2To0KH59re/ne233z59+/at5T4AAAAAGkTxrW0TJkxIp06dkiRnnXVWnnzyydx7770577zzajYOAAAAgMZRfEXSHnvs0f7zgAEDcv3119diDwAAAAANqjgkJclLL72UhQsXZvXq1RsdP/LIIzt0FAAAAACNpzgkXX311fnOd76TgQMHZtttt20/XqlUhCQAAACA94HikPS9730vP/7xj/O3f/u3tdwDAAAAQIMqfth2z549079//1puAQAAAKCBFV+RNGHChJxzzjk56aSTsuOOO270Wr9+/Tp8GAAAAACNpTgkvfHGG3nggQdy5513bnS8Uqnkqaee6vBhAAAAADSW4pB07rnnZuzYsfn4xz++0cO2AQAAAHh/KA5JGzZsyKc+9al06tSplnsAAAAAaFDFD9v+whe+kGuuuSbVarWWewAAAABoUMVXJN1www155ZVXcvXVV6dnz54bvXbfffd19C4AAAAAGkxxSJoxY0YtdwAAAADQ4IpD0n777bfJ95x66qm55ppr3tUgAAAAABpT8TOSSsyfP78jvw4AAACABtKhIQkAAACArZeQBNTUhvXrtvh51m+oz4a3Ok+9zl/vcwEAAO8/xc9IAngnOnVuzq3fP6Lm5xk56u63fK1zp+Z87//+c803fOGkn73l+b990+E1P3+SnPG5e+pyHgAA4P2pQ69IqlarHfl1AAAAADSQDg1Jp512Wkd+HQAAAAAN5G1vbbv88suLvmTMmDFJki996UvvfhEAAAAADeltQ9LLL79crx0AAAAANLi3DUkXXXRRvXYAAAAA0OA2+6+2rVy5MsuXL9/o2K677tphgwAAAABoTMUh6be//W3GjRuXhQsXplKppFqtplKpJEmeeuqpmg0EAAAAoDEU/9W2c889N/vvv38eeeSRbL/99pk3b14++9nP5uKLL67lPgAAAAAaRHFIWrhwYcaNG5cddtgh1Wo13bt3z/jx44v/shsAAAAA723FIalLly5Zv359kuQDH/hAFi1alLa2tqxYsaJm4wAAAABoHMXPSBo2bFjmzJmTT33qUzn88MPzxS9+Mc3NzTnggANquQ8AAACABlEckv7yFraxY8dm0KBBWbVqVY49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Llz4jqQyKytLRYoUsaV+UlKSnn/+eXXt2lV9+vTRuXPnNGXKFF29elUzZ85UyZIlVa9ePXl7e9tSX5Ief/xxnTt3TjNnzlRoaKieeeYZvfLKK2revLkuX76ss2fPqkOHDrbVl27fPfj444/Vr18/FStWTDExMapWrZrzjr87REZGas6cOZo8ebK2bNmivXv3qnPnzipUqJDb7iTcunXL+VnXrl1bXl5e+vHHH3XmzBlVrVrV9ieTdu3apbFjx2rSpEnq2rWr0tLSFBkZqevXr+v06dOqV6+erfUlaffu3Zo8ebKmT5+u5557TiEhIc4nUSpWrKg6derY/nkUKVJEubm5+uqrr1ShQgXVqlVL0p13MHJzc229m7F3716NHj1ab7zxhtq0aaOkpCT9+c9/Vu3atfXAAw/YVregW7duafny5erdu7fatGmjy5cva9++ffryyy918OBB1atXT0WLFrWt/q5du5Sdna3ChQs775yULVtWe/fuVaNGjVS+fHnbt4WUlBQNGjRI/fv3V7du3ZSenq6ZM2fq8uXLioiI0O7du9W8eXNbn8pJTU3VkCFD9Kc//UnPPPOMKlWqpIyMDKWkpKhjx4621XVISUlRQkKC0tLSVK9ePZUpU0ZvvfWW2rRpoy5duthev6DLly9rz549qlKlivz8/OTr66uYmBhVrVpVTZs2tbV2cnKy3njjDbVs2VL9+vWTJOXk5Mjb21vt27fX0qVLlZqaqlatWtnWQ3h4uD799FONGTNG3bt3V4sWLdShQwft379fCQkJatiwoVueYD18+LDS09M1aNAgZWVladWqVZo9e7ZWrlypY8eOKTAw0Nb9Mjk5WRMnTtS4cePUvHlz5eTk6Pr164qLi9P9999v65jJISMjQ5MmTdKrr76q1q1bKysrS6mpqdq+fbtycnJUvnx5W/s4cOCARo4cqWHDhqlt27by9fXVnDlzdPz4cW3cuFGVKlVS1apVbavvcPXqVR08eFB//etfnXOWFfza5YULF2x9QunUqVN6/fXX1b9/fz311FPKzMzU9OnTdebMGW3ZskXx8fG2b4+SVLFiRRUtWlReXl5655135Ofnp1WrVmnJkiW6deuWbty4oRo1atjWR2RkpKZNm6bJkydryJAhCgkJUWxsrJYvX67WrVurdOnStp4vjx07pmHDhmnQoEHq1q2brl27pmnTpun8+fOaPXu2mjVrpooVK9p+zj527Jiys7P17LPPOr/WV3B7TE9PV/HixW2rX6hQIVWuXFknT57UY489pkKFCunTTz/VuXPnlJmZqbp169q+LZ4/f16lSpXSrVu3VKNGDdWoUUOrV6/W1atXVb16dbc8MXjx4kWlpaWpZs2aWr16tXx8fNSgQQN5eXndMX6+efOmbd968fLyUtmyZXXhwgWVLFlS3t7eCg0N1e7du1WuXDn5+vq65amchQsXqk+fPmrdurXbn4SSbj+tOXv2bI0fP14DBw7U8ePHlZqaquLFi+v69etufWLvDxUkOT7Mxx9/XKdPn1ZsbKzy8/NVrVo158XRqlWrtHPnTj388MMuHxAYY1S0aFGVKFFCO3bsUF5enhYsWKB+/fppzJgxKlmypObOnavAwECVL1/epbUdHO9B27ZtdenSJefAxNfXV4UKFVJCQoISExPVoUMHeXt723LwS09P16ZNmzR48GB169ZNxhjn15qqV69u+waen5+v7Oxsffrppxo8eLCeeOIJhYSEaObMmYqPj1enTp2cc5HYefA/evSotm7dqqpVqzovSh944AF5e3srISFBGRkZaty4sW093Lp1SwsXLlSRIkXUs2dPZWVl6b333lOdOnXk7e2tmTNnqnTp0mrUqJEt9R02b97svDhyXKQ98sgjSk9P17x589SzZ0/bLtr37duno0eP6oEHHlCDBg1kjNGiRYtUqVIl1apVyzkYWbdunbZv367mzZvb9nkcOXJEe/fuVdu2bXX9+nW9++676t27t4KDg52/Y9c2af778WNvb29t375dhw4dkr+/vz744APt379f6enpio6OVmJiom1BxpUrV/SPf/xDGzZsUGJiotLS0tSwYUOVL19eUVFRioyMVNeuXW17/x3vga+vr3Jzc7Vlyxb5+vrqo48+Uv/+/fXuu++qYsWK2rVrlypXrmxbuJeSkqK0tDQFBAQoIiJCPj4+ql+/vr799lvl5uaqXbt2ttR1iIiI0MqVK9WlSxdVrFhR69at04wZM/Tcc89p0KBBzvcpKipK169ft+1x7ZiYGF24cEFNmjRRgwYN9OWXX+r69ev69ttvlZSUpDFjxtg+OM/JyVGJEiV04sQJZWZmKiAgQN7e3s6BcHJysm7evKnWrVvbUt9x46lHjx4KCQlRXl6e8vLydN9996lJkyb6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LiMjwzRt2tQsXrzY+Vp8fLwZNmyYc5JIY25Ppjl16lRbJjANDw83HTt2NAsXLjSLFi0yAwYMMK+++qpZt27dHRPhXbt2zQQFBdkySV1kZKQJDg52TlhqjDGrVq0yw4cPN19++aVJSkoyxhjz7bffmh49erj8fdi+fbvp0aPHXZMSJiUlmbFjx5r33nvPJCYmmtDQUNOrVy9z7Ngxl9Z3cLzHUVFRJj093XTq1Mm888475vLly87f2bBhg+natastn8OsWbPMJ598Yowx5vLly+a7774z7777rhk+fLj56aefjDHGfPbZZ6Z169bm8OHDLq9vzO1tvWfPnubNN980QUFBpmvXrmbhwoUmJyfHbNu2zQwYMMCEhoaaZcuWmT59+tjyWYSHh5v27dubefPmmcmTJ5snnnjCDBkyxLndOY4h33zzjenVq5fzmOkqv3Zc+Nvf/nbH723cuNFMmDDBtvegY8eO5ssvvzRfffWVGTx4sOnVq5dz4vX58+eb4OBg88EHH5g+ffq49Bjt8GvvwxtvvGGuXLli1q5da/r162eWL1/u8trG/M9x4f333zdvvfWWWbFixV39ffvtt6ZXr16mVatWth0XHBOJF5xQ/J///Kdp27atiYuLM8YYs2/fPhMSEmIWLFjgnNDVVQpuC5MmTTJjx441Xbt2NREREcYYY7788kszfPhwM2LECNO3b19btoWIiAjToUMHEx4e7pzY/erVq2bZsmUmJCTEOXHomjVrTNeuXV2+MEN+fr65deuWCQkJMfXr1zeDBw82H330kXNxEIeUlBSzbNkyExwcbMv7UHAS4d69e5uePXv+4iTC69evNz179rRl/PL99987Jyvt3Lmz+ctf/mIWL1581wII69atM927d7dlv8jMzDQvvfSSefjhh027du2c58Pw8HAzcOBAs2rVKrNo0SJbjs/G3D2GLTiu3L59u3nzzTfN448/boYNG2bbOPqXJpsfOnSo2bFjhzHGmAkTJpi///3v5uOPPzZPP/20y7fHhIQE0759e+fnvmHDBjNw4ECzYsUKk5GRYS5fvmyCg4PN119/bYyxbzLfyMhI89xzz5klS5aYa9eumQMHDpiGDRuaJUuW3PF7jmN1enq6S+v/0gI5DjExMea9994zM2bMMHPnzjX9+vWz5bjwWz1MmTLF9O7d2wQFBZlRo0aZoKAgl+8TZ8+eNZ07dzbffvvtHa/n5eWZ3NxcM2vWLDNo0CDn63Yt3nP8+HFTv3590759e5OammqMuT2mHDhwoFmwYMEdx6gTJ07YuijEzp07TUhIiPO6ZvLkyWbMmDHGGGOys7PNqlWrzFNPPWUOHTrk8tqRkZGmadOmZsaMGXf9bN++faZt27ZmzZo1xhhjcnJyjDGu3z8d44bVq1ebmTNnmunTp5t+/fqZhx9+2AwZMsTMmjXLeZzu3LmzLftFZGSkCQwMND/88IMxxjjHRrt37zbt2rUzy5YtM8bcPnYFBwebkydPuryHX/NvHSSdOHHCvP7668aY2zuz4429evWq+ctf/nLH6lRXrlyxpQerF6yBgYEuPeAV3FHWrVtnJk2aZObMmWOioqLu+D13rlD284PNlClTnAebgv1mZ2e7vHZYWJjp16/fHaFidna2mTJlinn55ZedA0DHBYwdAwHHCXDYsGF3reCwevVqM2bMGPPMM8+YDz/80AQFBbn8YJOcnGz69Oljdu3aZYz5n7/RcXA9e/asmTBhgnn22WdNp06dbLtYzM3NNTk5OWbq1Klm5syZxpjbq8B06dLFDB8+3Lz22mtm7ty5pmvXri4flCYlJZnk5GSzadMm884775jvvvvOvPLKK+bNN980w4YNM++8845p27atuXLlisnKyrLtuBAZGWlCQkKcB31jjFm4cKF58cUXzdKlS40xxoSGhpouXbrYduI5fPiweeqpp+7YJ65fv2769OljXn75ZWPM7WPW6tWrTY8ePWy5SDHm148L+fn5d+wndhyrtm/fbnr16nXXyhpTpkwxPXv2dK4ANG/ePBMYGGjbPmGMtcHYoEGDTEZGhkuPT2lpaWbgwIHObXHVqlXmlVdeMStXrrzj965evWo2btxo24qSaWlppkWLFubcuXPGmLvDpEcffdScP3/eGHP7ws7xe67i2CcdgZUxt1egmT9/vgkKCjKHDh0yGRkZZuHChSYkJMQtF+0OBW889e/f34wbN862CzWHqKgoM378eLNy5Uozb94807lzZzNlyhSzceNGY8zt7XXSpEm2vA+O1Wb27dtncnNzzc2bN83rr79uunXrZs6cOWOMMeb8+fNm/vz5plu3bra8D7t37zYdO3a8Y/Wlzz//3IwYMcIsWrTI5OTkmDNnzpiPPvrIlvN1Qdu2bTPr1683EyZMMI899pgzTIqIiDBBQUG2nq9/aQw7ZswYM2LECOf+ePz4cZOWlnbHjSBXcYzdCt78Sk1NNWPHjjVDhw51rnb89ttvm27durn0fSh4nH3uuedMly5dnOPTDRs2mAEDBjjD/a+//tq88MIL5vr167aMH3/tJmB4eLhp2LChef/9980nn3xiFi1aZLp16+byG2BhYWGme/fuZv78+WbatGlm6tSpd12M/vDDD2bEiBHmqaeesmV/sNJDYmKiiY6ONvHx8bbchPzuu++cK4bm5eXd9VlnZGSYNm3a3LHKqB1+L2BeuHChc/90h127dpmgoCAzYsQI8/LLL99xk+f69et3hX6uEBERYUJCQsz48ePNkCFDzIYNG+6qM336dPPyyy/btvqxY4XfguOG1NRU8/XXX5v+/fubYcOGmVmzZpm//vWvZurUqbYcpyMiIsyTTz5pmjZtasLCwpzbpWPbjIqKMh07djTDhg2z7Wbob/m3DJIcb97Ro0dNmzZt7jigOgany5YtMyNHjrSth//NBWtmZqbLLlgdf7vjv0uXLjUhISFm2bJlzgHPpk2bXFLr/+LnBxvHALngRu9qFy9eNK1atTJTTCzuAAAgAElEQVSTJk1y1nJsBzdu3DC9e/e+K812dS+OQcDcuXPN1KlTzccff3zXSe748eMmNDTUfP3117ZcrCUnJ5vBgwc73+ufh1np6enm0qVLZtq0aebEiRMur/9zu3fvNo8++qhzWe20tDSzdetWM3fuXPPVV1+5vIfw8HATHBxsevToYR577DEzYsQI06VLFzNhwgTz448/mry8PJOZmWlee+01W+/e7N+/3wQEBDgvUAoGp//1X/9lunbt6hyQR0dHOy+cXO377783o0aNMsbc3t4dgWJ2drZp06aNWb9+vTHm9rLvKSkptvTg8FvHBbukpKSYnj17Ot8DY+4ML/785z/f8TPH0yF2cvdgLCEhwaxevdr52Rtzez9ctWqVefXVV+8Kk+xeNnfr1q3miSeecAZ4Bft64403zMKFC22pe/78edOwYUOzevVqY8ydoWVycrIZNWqUcznjy5cvm6tXr9rSh6duPDkcOHDAua8fOXLEvPDCC87j1NKlS80jjzxiunfvbgYMGGA2b97s8u3R8TTUhAkTzHfffWeMMXfsA0OHDjVPP/20Meb257Js2TLbnqT+7LPPnHdxHcfomzdvmvnz55uXXnrJ2dfGjRtdvtz63r1773ji4cCBA6ZXr14mIyPDTJkyxbRs2dL5OcXFxZmzZ8+6tL4xvz+GHTNmjGnbtq2t58oLFy6YRx55xHnT13ETypjbx6lu3bqZBQsWOH/fESq5ys+feHzppZdMhw4d7ngyadCgQWbRokUmISHBtvfi924CHjx40MyePduMGjXKTJs2zeUXimlpaebjjz923uSIiooyY8eONR988MFd2/6PP/5oS4Dzv+nBTjNmzDAvvvjiL/4sMTHR7Ny508yePdu2J9kL+rWA2fHNh2XLlrn1YYHY2FjTokULZ9hpZ+3k5GQzfPhwZ4CzePFiM2jQIBMaGmoyMzOdvxcVFWXefvttW4Ksnz9JXvDvvXjxopk0aZJZtGiRMca+sVNsbKzp2bOnOXHihNm5c6dp166d8wmsgnUd24S7QyRjjPm3myOp4ISAZcuW1fHjx3X58mXnhICOuQWioqJUuHBhW5btjYiI0JgxYxQaGqoNGzbIz89PGzZsUP369TVgwAANGjRIjz/+uOLj49W2bVuVLl3aZZPXXrx40TnxYXp6upYsWaL3339fTzzxhJo3b66SJUtq8+bNatmypYoVK+aWJe4LqlatmurXr69//vOfGjNmjHOya8fn4moFV0CKjIyUl5eXc3LvmzdvqmjRorp48aIuXbqkJ5980vnvXNnLlStXtGbNGr3wwgvq2bOnsrOzdeTIEZ04cUK1a9d2ztxfrlw5Pfjgg/L393fp93dTUlKUnp6u0qVLa/78+XrooYfk5+d3x+SMxhitWLFCzZs31xNPPOHyeZliYmK0adMm3bx50zkBZrVq1XT58mVdvnxZTZo0UcmSJVW7dm21aNFCjRo1UtmyZV1W3/Ed6tGjR+u1117Trl27JEkLFixQx44dValSJXl5eWnjxo2KiYmxZZ4Jh9TUVCUmJurmzZtq2bKlChcufMdqdUuXLlWFChXUoEEDWyeeP3v2rHbu3KmgoCBJt+eHysnJUbFixZSYmKiyZcuqcePGKl26tG2rADn81nHBDvHx8Tp58qTq1q2rpKQknT171rlS540bN+Tj46PU1FRdv35dgYGBkmTbyjMF/dL74NhHfXx8XDrnRk5OjrZt26YtW7aoaNGiqlevniSpePHiqlKlivLz8xUdHa3U1FQ1adJEkmuPi7+kdu3aqlWrloYMGaIuXbqoTJkyzvnS9u7dq8qVK6thw4YurXn8+HHVrFlTV65cUWRkpBo2bHjHfBa+vr7atm2bLly44Jxo3tXbQnJysrKysnTr1i0lJCQoNzdXn3zyic6cOaPr16/L19dXc+fOVUhIiJo0aaK+ffu6fJn3qKgojRo1Su3atVPFihVVoUIFnTp1Stu3b1fhwoX16aefavLkyRo1apTOnTun9u3bu/w8YXUS4ZYtW8rPz0+NGjWyZQEEY4yWL1+urKwsBQYGqnDhwsrPz5ePj4+aNm2qOXPmqFq1aqpdu7YefPBBl87VdfHiRfXt21cbN27U2bNndevWLQUEBKh06dIKCwvTyJEjdfLkSY0aNUp9+/ZV3bp1XT7XhpUxbMuWLfXjjz+qbdu2tkxaayxONp+RkeGcbN6V5+yIiAjNmDFDvr6+SklJUdWqVRUcHKxDhw7p448/Vu/evdWwYUMZY5wr+dm14nBWVpZ27NihV155RdKdq6xKkre3t9q1a6cOHTqoZcuWLl2Q4n+7QE6lSpVcvhqVpxfpSUtL09mzZ1WhQgUVKVJEsbGxqlmzpu6//35Jt1dz9Pb21sGDB3Xy5EmFhISoZs2aLu9j3759io2Ndc4xdO3aNc2ePVvTpk3T1atXNWnSJAUHBysgIEA1a9ZU06ZNbV246OeqVKmihx56SB988IFq1qxp26JR0u3zcmBgoPN6okmTJsrKytK6det03333yc/PzzmhdbNmzWzZN4sWLaomTZroiy++UJ06dZwL4RhjVLJkSUVFRenYsWPq0qWLbWOnn376SZ06dZK/v7+qV6+uSpUqOVfcbtCggXPRqJo1a+rpp59220ptBf1bBUk/nxCwRIkSyszMVHh4uNLT01WsWDHdf//9Wrt2rZYtW6aRI0faMpGxpy5YU1NT9fLLLys3N1cPPfSQihcvrn/961/y8vJSkyZN5O3trUKFCmnXrl3q0qWLWy6Mfom7DjY/XwGpbdu22rBhg3M5SsfKOzt27FDlypX1yCOPuHzlnf379+vEiRMKDg5WnTp1JEl16tRRfn6+jhw5ouPHj6tOnToqWbKkLSsQRUREaPTo0Vq7dq3CwsJUvnx55eTkqHLlyipTpswdS3Ju27ZNHTp0sGXJ3sOHD2vXrl0KDQ1VbGysSpcurYoVKyo3N1dfffWVnn76afn4+NiyvP0vTQZYt25dxcfHq2vXrs7B2KpVq7R8+XJNnTrV5Rdp0u2J3k+fPq1HH31U9erV04YNG7R3714FBgY6B8fe3t6KjY1Vp06dXL6qhXR7IuGMjAxVqFBBmZmZWrRokXO1JceFkiTt3r1b5cqVU+PGjW1dGasgdx0XkpKS1L37/2PvvgOqLvvH/z8PG8EBIsiULUtAQMCROHHhwDS1tGxaVnZny6xQc49Kkcr6WI7S3KIoDpSpoDJEQUXDRFFwgSgqm+v3hz/ONxv37d19DgfxevyTccTz4s37vN/X+3Vd1+s1jLq6Ojp27IiVlRXp6ekUFxfj6+v70DFo1aoVAQEBjXYMoPGOg7a2NmZmZsqON/X19coBakMyqaKighMnThAcHNxo9wsHBwccHR2ZPHkyPXr0oHXr1iQlJbFjxw5efvlllQ4Ik5KS+Oyzz7C1tWX8+PHk5ubyyy+/4Ovri5mZmfL3fu7cORwdHdXS2l2TE08NUlJSmDdvHvPmzcPHx0f5YGRjY0NcXBxbtmxhxowZygf24OBgtbUurqmpITs7m6qqqr8tIty3b19atWql8s/kb7/9RmlpKaampujo6JCdnY2DgwNmZmbK1va6urrk5uby1FNPqfwafe3aNcrKyujcuTP379/n/v37ODk5MWvWLKqqqsjLyyM8PJy+fftSWlqKm5ubSidc4L8fww4bNkzlky5Nodj8l19+SVxcHFVVVRw6dIh9+/Zx8eJFXn/9dQ4cOMCePXsYOHAg3t7e9OrVSy0Nch5lEhAejF0aOoeB6hL+TaFBjqZjqKqq4v/+7/9ITU3F1tYWGxsbEhISuHbtGm3atMHCwgJtbW1ycnL49NNPGTZsGB4eHg/9flThv00wu7m5qaVb3n9iY2ODjY0Ny5cvJywsTDmeUpX09HTi4+PZtm0bbdq0oa6uTvk79/b25t69e+zevRtdXV2sra0xNDRUS6K7ga2tLfb29soOcVZWVsrPX15eHjY2Nvj6+qr8fQsLC6msrMTW1hY7Ozuqq6tRKBS4uroqk0lt2rRRJpPgwZivsRePwGOUSPq7Lkxubm6YmpqSlZVFVFQUJ0+e5NChQ2rpTqbpB1ZtbW1MTEzYvHkzCoUCDw8PZbve+vp67O3tyc7OJjMzkwEDBqglYfCo1H2x+bsOSH9sRxkdHc3mzZt5++23Vd55Jzk5mU8++YQ+ffpgbW2Nvr6+cnbd0dGR+vp6zp07x8mTJ3Fzc1P5qo+GAeH06dN5++232bNnD1lZWRgYGFBcXIyWlhbt2rVjx44drF69mtmzZ6u8HeWdO3eAB13oBgwYQO/evTl69ChZWVls2LCBQYMGKVcq+fv7q+Ui9/tZAzc3N9q3b8/KlStRKBT079+fW7dusXfvXnbs2MHs2bOVKzNUKTk5mcWLF9OvXz8sLS0xNzfH0dGRuLi4h5JJ0dHRHD58mNGjR6v8fLhy5QojR44kNzcXHx8fPDw8qK2t5dNPP6Vz5860bdsWPT09oqOj2bp1K5MnT1b5Z+I/Ufd1AaCiooLs7Gxqa2sxNjamdevW2NnZcfToUa5evYqvry+7d+9m3bp1vPPOO41+DEC9x+Hs2bNcu3YNc3NzWrZsibOzM/fu3SMxMZGamhpl11JDQ0Ps7Ozo3bt3ow9IHRwc6NixI3PnzuXo0aMkJSUxd+5cZTJeFRITE1m2bBkRERHKtvG9evXi4sWLrFmzRplMiomJYf369bz++usqn9VsCislU1JSmDp1Kra2towePRoDAwNlV8ZWrVqRnp6Ovr4+U6ZMAVBLUrWwsJD79+9TU1ODsbExLVu2ZMaMGbRs2VK5KkmhUCi7Sz799NMqPw5lZWWsWLGCnJwcHB0dsbCwIDExkVu3btGmTRtl0jU2Npa9e/fyzDPPqDSZ1jDxtX//fnJzc+nTpw/nzp3Dz8+PV199lUuXLgFgb29P27ZtCQkJUXkSSdNjWPjrLsf29vZoa2uzevVqZTIpOjqabdu2MXnyZJUmDxomswYNGsSvv/7KhQsXWLlyJcbGxpw+fZrt27djbGxMamoqubm5DBs2DD09PY1NAm7fvp0DBw4QFham7HqrCn91Lri5uXH8+HH69OmDjo4OdnZ2CCG4du0awcHBjdIRrLFjaLj3FhUVkZOTg6+vL35+fuzZs4fjx49z8OBBiouLWbhwIT179uTChQt069ZNpZ1tm0KC+b/R0FFR1dfogwcPMnv2bDw9PSksLCQrK4ujR48+1DnP29ubGzdukJKSQmhoqFo6J/6RjY2N8vfRkEyKiYnh559/ZvLkySr/XSQlJTFt2jTS09PZuHEjXbt2VS6KUSgUuLi40L59eyIiIrC1tVXmOjSRRILHKJG0ZcsW3NzcCA8PVy5R//HHH4mNjWXw4MGEh4fTr18/+vTpw4gRI5TL4VRJUw+sDQM7HR0dCgoKKCsrY8eOHVhYWDBo0CCOHz9OTEwM+/fv58CBA8yePVu5BE+T1HWxeZR2lBs3biQtLY20tDQWLVqk0gcU+PvEZl1dnXIw5ujoSEVFBcXFxQQGBqr0OPz+GAwePFg5IKyrq6NPnz6cP3+e77//nhMnTpCdnc2cOXNUnkBJSEjgq6++Yvv27WzZsoW7d+/SvXt3+vbtS1BQEDdu3GDXrl2cPn0aLS0tBgwYoDw2qmZra0uHDh2YNWsWmZmZlJSUsHjxYrS0tDA0NMTU1JSwsDC1fC5SUlKIiopi6tSpBAYGUlJSwuXLl/Hw8MDe3p4DBw6Qn59PWVkZa9asYe7cuWpZhdKwPSg/P5/c3Fw8PT0ZOHAgOjo6LFu2jPj4eA4fPsy+ffuIjIxU+WfiUanrutDAyMiI2tpaTpw4gY6ODmVlZVhaWmJnZ8eJEyfYsmULR48eZfHixRo7BqCe41BYWMiwYcPYsmULmZmZFBYWIoTA3d2dFi1akJKSgkKhUP7c6tjG9ajs7Ozo06cP/v7+DB8+XKWficrKSiIjI3n99dcJCgrizp07nD9/ntjYWEJDQzl//jx79+6luLiYnTt3quUe0RQe2o8cOcLChQuZPXs2paWlpKSkYGNjQ7t27ZSDTk9PTzZu3IiDgwM2NjZqeWCeNm0aGRkZbNq0iaCgINzd3fHw8OCTTz7h9u3b5OTkcPr0adauXcuCBQvUMn5r2OpfWFjIqVOnCA4OxtXVlbi4OFJTU0lOTub06dOsX7+eL774Ant7e5W99x8nvnbu3Mm1a9cYN24c33//PXZ2djz77LOEhISodWuCpidd/m7cpKOjg4+PD1VVVWzcuJGcnBySkpJYtGgRjo6OKo1BoVA8lEyKiYlhz549vP/++/Tt2xdfX18CAgJo1aoVr776Kqampir/TPyTSUBLS0uVxvBX58IPP/yAQqEgNDRU+dxhb2+Pv7+/WiYbNBlDeXm5cvugra0trVu35vTp02RmZtK1a1f69+9Pu3btuHDhAra2trzwwgv4+Pjw5ZdfMmLECJVNBDaFBPM/ocpEGkBubi4zZ85kyZIlDBgwgAEDBmBlZcXVq1c5fPgwnTp1Uq4K9PPz46mnnmrUCTAbGxucnZ2ZP38+V65cITY2lkWLFuHs7KzS90lMTOTbb7/l008/pVevXly7do0LFy4QHByMQqFQLlZwdnbGyckJNzc3tW25fVRNPpH072oLVFZW0qJFC5YuXcrQoUOxsrLC2NhYbQ8ooJkH1oab2Nq1a/n5558ZOnQoenp67N69GzMzM55//nmCg4Nxdnbm+eefV8ve3X9K1Rcb+PvBkBBCuRxWW1ubffv2sXDhQrWsQPmrxOaaNWvYtWsXLi4uyuyxi4sL/v7+Kl+O+1fH4Pvvv6empoZJkybx1FNPMXToUAYNGkRYWJjKVyIlJCSwePFi3n33XXr06IGLiwsLFizgzp07dO/enRYtWtC1a1cCAwPp2rUrAwcOVMtWrt/7d/Vn1HVdyM3NZcKECSxYsIBu3bpRWFjIe++9h5OTE46OjrRr1w4HBwd++uknduzYwbfffquW8xFAT08POzs75bVn3bp1dO7cmQEDBtC9e3c6d+6Mh4cHEydO1Pg1QtXXhdTUVPLy8mjXrp2yHtDNmzcZMmQI58+f5/Lly9ja2tK2bVtyc3OZMWOG2n4P/w1VH4e6ujqMjIyUtUe8vLz4+uuvOX/+PGlpacqtQ05OTmqtb/CoWrRoQZs2bVS+Oq+2tpb169fj4uKCjY0NixYtIj4+nuTkZJKSknjuuee4f/8+0dHRLF++XOWrl0HzD+0NNbLGjh1LUFAQgYGBJCQkkJOTg5WVlTKZVF1dTVFREaGhoSqf7f/joPj69esUFBQQFBSEg4MDPXr04MqVKxQVFVFXV8e//vUv5fZLVbl58yYKhQJdXV3s7e0xMjLi5MmT5OTk0Lt3b3r27ImdnR1XrlzBxsaG119/XaXnw99NfOXl5TF+/HjatGnD2rVrqa+vV9YqUydNTrr81bhp9erVyq2evXr1oqysjF27dvHll1+q9DNx+PBhVq5ciZ2dHTo6OsoV+6NGjWLLli38/PPPjBkzRrk67ferAFSpKUwCNvh350KDhs+OumgihmvXrjFo0CASExPJy8tT1u+0t7fnwoULym10fn5+9OvXDy8vL8zNzSkoKGDcuHEqS3Q3lQRzU5CXl4cQgtGjR1NRUYGuri7t27enRYsWpKWl4e3tjbm5uTIJrIkdNzY2NtjZ2fH1118TGRmp8nHDjRs3mDRpEt26dWPcuHGYmZlRXl5OYWEh7u7uVFVVPTRWcnR01HgSCZp4IulRCwLm5uaqrSDgX9HEA2tZWRkrV65k1qxZdO3alYCAAAwMDPjuu+/Q19cnODgYa2trtdU1aGr+6uazaNEitLS00NXVxcnJiVGjRqk8gfLvEpv379+nVatWREZGMnz4cOV5oK6ll388BqWlpSxcuBBtbW3q6+tp1aoV+vr6Kl9xcPv2bebPn88HH3xAUFAQ5ubmODs7061bN2bPnk3r1q2VtUaMjY2xs7NTy4DsrzRmMUB4sLWvoKCAu3fv4uDgwMcff0y/fv0YOXIk8GAAZGFhgbe3N88//7xKZ7nhwQxvYmKistZRfX09W7duZfr06VRUVLBixQr8/PxwdXXF2toaGxubZneNKC8vJywsTLl1KzU1laCgILZu3UpNTQ2vvfYaGRkZnDt3Dk9PT15//XWVXxeaiobaR3V1dRQWFhISEsKUKVPw9/enpKSEmpoazp8/zyuvvNKoRTobm46ODrq6unz11VesXr0aGxsbhg8fTkREBBUVFSQkJLBgwQLCw8PVUi+tgaYe2oUQ6OjoKAt0VldXY2hoSM+ePTl48CA5OTlYW1tjamqKkZERwcHBKq8B83eD4suXL+Pu7s79+/dxdHQkODhYLUWE4UHR/UGDBnHkyBF+++03tLW1lQW8L126RGZmJh4eHnh6ehISEkKnTp1UPtv/KBNfOjo67Nq1i379+qllG9UfNfYYVtPF5qurq1m+fDnR0dHo6emxfv16rKys0NPTw8jIiKeffpo9e/awfPlyJkyYoNbjr+lJwD9q7AY5TSGGwsJC8vPz0dbWpqioiLKyMpYsWYKenh4FBQVUVVVx/PhxnJycHroeWFlZqWws29QSzJqWlJREQkICY8aMUTY/UCgUWFpasnv3bm7fvk3Xrl01tn2rga2tLePGjVN5Yu/3jaOSkpLQ0dGhY8eO/PTTT8TGxpKSksLKlSspKiqisrJSo6vp/6jJJpL+m9oCR44cUUtBwH+nsR9YDQwM2L9/P/fv38fX1xcDAwP09PQ4fPgwv/76a6MNQJqSxuyABI9eNDU3N5eePXs2SmLzj8fAzs6O+vp6tW0hgwfbRrZs2cKwYcOUN9X6+nrat29P+/btiYuLo1+/fhor/NYYdXiuXLnC9evXcXZ2xsvLS7ml9IUXXuCFF15Q3gR37dpFYWEhgYGBKl2GK4Tg1q1bjBo1ivj4eO7du0deXh4dO3ZECMH27duZPn06BQUFREVF0bVrV7V0P2oK9PX16datGwkJCYSGhnLu3DkyMzPR0tJi3759DBs2DD8/P86ePcvAgQObxAyOKv3222/cvHlT+ftt2bIlJiYmVFRUEBMTQ4sWLfD29qZbt26EhoYyduxYta8ObArc3Nzo2bMnTz31FC+88AJ2dnZoaWmRn59PcXExffr0UXu3Qmj8h/Zjx46RkZGhrJEFKIv96+vr07NnT5KSkjh8+DBOTk60a9dO5Q9sjzooLi4u5t69e2qr8XDp0iWuXr1KixYtlDEtXbpUWSbg1q1bnD59Gk9PT7Um2B9l4mvQoEG0bNmy2RX9bwrF5hsaDxw/fpxRo0bRqlUrtm/fzpEjR7h16xadOnUiPDycEydO4OnpqfYku6YmAf9OYz/PaDqGdu3aKZtNWFlZ8eyzz9K7d2/q6+s5ceIE+fn5HDt2jGeeeUblye0GTTHB3NhOnz7N4cOHcXNzw9bWlvj4eGWRcS0tLWWDmrNnz+Lo6Kis76hpqn6m+GPjqF69ehETE8OOHTtQKBT88ssvDBw4EEdHRyorK5VNSpqKJplIagq1BR6Fuh5Y/9jZSggBoFziVl1djZOTE9nZ2cqWkJooGNsUNNbNpyknNhvrGGRkZJCfn4+1tTUpKSn4+PjQvn175fmqUCi4efMmOTk5hIeHa/R8VGcdnsTERKZPn05MTAzx8fEMHjyYgIAACgsLqaiooE+fPigUCqKjo1m9ejXPPPOMyldkVVZW0qpVK9zd3cnNzcXAwIDg4GAiIiKUzQfCwsLo27cv169fb/Q2sY3N0tIST09Pvv/+e95//33s7e2Vs1p+fn60b9+e4ODgRkkcNBYhBIWFhQwcOJBdu3YBD+4d1tbWtG7dGktLSyoqKoiPj3+oY5uuru4Tc68wMTFRjg20tLSUBTI/+uijRt0q0FjX6IZVDbt372b//v0YGhpSVVWFpaWlctyko6ND9+7dyczMJCQkBGNjY5WeD//toPipp56idevWajknra2tMTExoaqqCgsLC1577TWCgoLQ1dXl+PHjnD9/nrNnzzJ+/Hi1T/w09sTXo8ak7qYomi42Dw+ui6amply6dIn27dvzzDPPUF5ezvbt2zl9+jQHDx7kzp07fPTRR412n9TEJOB/ikfdE3CajOHevXtUV1crP2fW1tbK7sqnT58mMDCQwMBAhg4dytChQxk5cqRatjz/XlNMMDeWhq3Xe/bsUdZIu379OidPnqSkpIROnTopmx9s3LhR5R1dm4q/axz17LPPsnv3bkaPHo2Pjw/6+vp07NgRf3//pnccRBOVmpoqwsPDRXZ2thBCiDlz5ojp06cLIYQoLS0V27ZtE+PHjxdnz57VZJhCCCHu37+vsn8rKytL7Nq1S1y8ePFPr5WUlIhly5aJl156SYwfP14MGjRInDlzRmXv/ThLSUkRY8aMERUVFSr/t+/cuSN8fX3FmjVrlF87efKkmDJliqiurlZ+bePGjSI8PFycO3dO5TE8CnUeAyGE+OGHH0SPHj1EZmamiIiIEP379xf37t176O9s2bJFvP3222qLQdOSk5PF008/LdLT00VFRYUYM2aM+Pzzz4UQQvz666/izTffFJ9++qmIjo4WzzzzjPj1119VHkNiYqKYPHmy8rqTmJgounbtKuLi4sT169fFunXrxLRp00ReXp7K37upS01NFUOHDhUZGRlCCCHKy8s1HJF61NfXK/8cEREhZs6cKd5//30xefJk8eqrr4pz584pf/ZvvvlGvPfee832WDyKmzdviu+++04MGTJEY9dnIdR/jRZCiJ9//lksW7ZM7Nu3T0yfPl2MGTNGzJ49W5w8eVJt79kgOTlZjBw5Uhw5ckTcv39fjBkzRrzyyiti7969IiQkRGzatEkIIURtbe1D/1WlkpKSP92X4uLixKeffiqWLFkirl69KoQQoqqqSpSVlSn/v7EcOSnSM+kAACAASURBVHJEjBgxQqSmpjbq+/47qhzDNmgK46Y/nl9RUVHixRdfFOnp6SI0NFQcO3ZMCCFETEyMKC4uVvn7P4qmdj6o41zQdAzFxcWiV69e4o033hCHDh0Sd+/eVb52+PBhERERIRYsWPCXz1O/v9eqS0ZGhggMDBRHjx4VQqjnutgUFRUVifXr14tJkyaJAwcOiKqqKvH999+L8ePHiyFDhohp06aJIUOGNNvn3L+7Rr777ruirKxMREdHizFjxoh169ZpMMr/rMkmkoQQIi0tTYSFhYmpU6eK119//aEP19WrV0VpaakGo1O95ORkMWLECLFz584/DfoaLmYVFRXi6tWrIj09vdEHQE2dOm+Aj0tiU92DgO+//14MHTpU5OTkiDfffFP0799fHDp0SOTk5IitW7eKsLCwZpvA+KuL/q+//ipmzpwp8vPzRX19vThz5ox48803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
      "text/plain": [
       "<Figure size 1440x1008 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns
    "import matplotlib.pyplot as plt
    "
    "%matplotlib inline
    "
    "sns.set(style=\"whitegrid\")
    "
    "fig_dims = (20, 14)
    "fig, ax = plt.subplots(figsize=fig_dims)
    "plt.xticks(rotation=45, ha='right')
    "
    "ax = sns.barplot(x=\"partido\", y=\"total_manifestacoes_propostas\", data=df_contagem)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gráfico de barras barplot 2 - com o uso de plotly e dash"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pode ser aberto em servidor interno temporário e salvo como arquivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on http://127.0.0.1:8050/
      "Running on http://127.0.0.1:8050/
      "Debugger PIN: 379-327-869
      "Debugger PIN: 379-327-869
      " * Serving Flask app \"__main__\" (lazy loading)
      " * Environment: production
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m
      " * Debug mode: on\n"
     ]
    }
   ],
   "source": [
    "import plotly.express as px
    "
    "df = df_contagem
    "fig = px.bar(df, y='total_manifestacoes_propostas', x='partido', text='total_manifestacoes_propostas')
    "fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    "fig.update_layout(uniformtext_minsize=8, 
    "                  uniformtext_mode='hide', 
    "                  title = \"Total de manifestações e propostas de partidos políticos sobre a covid-19 postadas no Facebook (coleta até 19/04/2020)\",
    "                  width=1800,
    "                  height=800,)
    "
    "import dash
    "import dash_core_components as dcc
    "import dash_html_components as html
    "
    "app = dash.Dash()
    "app.layout = html.Div([
    "    dcc.Graph(figure=fig)
    "])
    "
    "app.run_server(debug=True, use_reloader=False) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Faz uma contagem das manifestações/propostas que mais tiveram apoio de partidos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista_2 = []
    "for num, row in compilado.iterrows():
    "    nome = row['MANIFESTAÇÃO / PROPOSTA']
    "    
    "    conta = 0
    "    for vez in range(1, 35):
    "        valor = str(row[vez]).strip()
    "        if valor == 'x':
    "            conta += 1
    "        
    "    dicionario = {\"manifestacao_proposta\": nome,
    "                  \"total_de_partidos_apoiando\": conta}
    "    lista_2.append(dicionario)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_contagem_propostas = pd.DataFrame(lista_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_contagem_propostas.sort_values(by=['total_de_partidos_apoiando'], inplace=True, ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>
       "<style scoped>
       "    .dataframe tbody tr th:only-of-type {
       "        vertical-align: middle;
       "    }
       "
       "    .dataframe tbody tr th {
       "        vertical-align: top;
       "    }
       "
       "    .dataframe thead th {
       "        text-align: right;
       "    }
       "</style>
       "<table border=\"1\" class=\"dataframe\">
       "  <thead>
       "    <tr style=\"text-align: right;\">
       "      <th></th>
       "      <th>index</th>
       "      <th>manifestacao_proposta</th>
       "      <th>total_de_partidos_apoiando</th>
       "    </tr>
       "  </thead>
       "  <tbody>
       "    <tr>
       "      <th>0</th>
       "      <td>13</td>
       "      <td>Apoio ao isolamento social.</td>
       "      <td>17</td>
       "    </tr>
       "    <tr>
       "      <th>1</th>
       "      <td>138</td>
       "      <td>Testagem em massa.</td>
       "      <td>12</td>
       "    </tr>
       "    <tr>
       "      <th>2</th>
       "      <td>67</td>
       "      <td>Favorável à Renda Básica Emergencial.</td>
       "      <td>11</td>
       "    </tr>
       "    <tr>
       "      <th>3</th>
       "      <td>139</td>
       "      <td>Tributação de grandes fortunas.</td>
       "      <td>10</td>
       "    </tr>
       "    <tr>
       "      <th>4</th>
       "      <td>3</td>
       "      <td>Afastamento do presidente Bolsonaro.</td>
       "      <td>9</td>
       "    </tr>
       "    <tr>
       "      <th>5</th>
       "      <td>40</td>
       "      <td>Contra MP 936/2020, que permite redução de sal...</td>
       "      <td>9</td>
       "    </tr>
       "    <tr>
       "      <th>6</th>
       "      <td>14</td>
       "      <td>Apoio ao PLP 149/19,  que prevê ajuda financei...</td>
       "      <td>9</td>
       "    </tr>
       "    <tr>
       "      <th>7</th>
       "      <td>121</td>
       "      <td>Suspensão da cobrança de de serviços básicos p...</td>
       "      <td>8</td>
       "    </tr>
       "    <tr>
       "      <th>8</th>
       "      <td>116</td>
       "      <td>Saque emergencial do FGTS.</td>
       "      <td>8</td>
       "    </tr>
       "    <tr>
       "      <th>9</th>
       "      <td>112</td>
       "      <td>Renda Básica permanente para desempregados e t...</td>
       "      <td>8</td>
       "    </tr>
       "  </tbody>
       "</table>
       "</div>"
      ],
      "text/plain": [
       "   index                              manifestacao_proposta  \\
       "0     13                        Apoio ao isolamento social.   
       "1    138                                 Testagem em massa.   
       "2     67              Favorável à Renda Básica Emergencial.   
       "3    139                    Tributação de grandes fortunas.   
       "4      3               Afastamento do presidente Bolsonaro.   
       "5     40  Contra MP 936/2020, que permite redução de sal...   
       "6     14  Apoio ao PLP 149/19,  que prevê ajuda financei...   
       "7    121  Suspensão da cobrança de de serviços básicos p...   
       "8    116                         Saque emergencial do FGTS.   
       "9    112  Renda Básica permanente para desempregados e t...   
       "
       "   total_de_partidos_apoiando  
       "0                          17  
       "1                          12  
       "2                          11  
       "3                          10  
       "4                           9  
       "5                           9  
       "6                           9  
       "7                           8  
       "8                           8  
       "9                           8  "
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_contagem_propostas.reset_index().head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "recorte = df_contagem_propostas.reset_index().head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gráfico de barras barplot - com o uso de plotly e dash"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pode ser aberto em servidor interno temporário e salvo como arquivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on http://127.0.0.1:8050/
      "Running on http://127.0.0.1:8050/
      "Running on http://127.0.0.1:8050/
      "Running on http://127.0.0.1:8050/
      "Debugger PIN: 608-697-926
      "Debugger PIN: 608-697-926
      "Debugger PIN: 608-697-926
      "Debugger PIN: 608-697-926
      " * Serving Flask app \"__main__\" (lazy loading)
      " * Environment: production
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m
      " * Debug mode: on\n"
     ]
    }
   ],
   "source": [
    "import plotly.express as px
    "
    "df = recorte
    "fig = px.bar(df, y='total_de_partidos_apoiando', x='manifestacao_proposta', text='total_de_partidos_apoiando')
    "fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    "fig.update_layout(uniformtext_minsize=8, 
    "                  uniformtext_mode='hide', 
    "                  title = \"Vinte manifestações e propostas sobre a covid-19 com mais apoio de partidos políticos postadas no Facebook (coleta até 19/04/2020)\",
    "                  width=1800,
    "                  height=800,)
    "
    "import dash
    "import dash_core_components as dcc
    "import dash_html_components as html
    "
    "app = dash.Dash()
    "app.layout = html.Div([
    "    dcc.Graph(figure=fig)
    "])
    "
    "app.run_server(debug=True, use_reloader=False) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""