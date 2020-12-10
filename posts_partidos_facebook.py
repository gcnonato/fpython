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
    "partido": [
        "MDB",
        "PTB",
        "PDT",
        "PT",
        "DEM",
        "PCdoB",
        "PSB",
        "PSDB",
        "PTC",
        "PSC",
        "PMN",
        "Cidadania",
        "PV",
        "Avante",
        "PP",
        "PSTU",
        "PCB",
        "PRTB",
        "DC",
        "PCO",
        "PODE",
        "PSL",
        "Aliança pelo Brasil",
        "REPUBLICANOS",
        "PSOL",
        "PL",
        "PSD",
        "PATRIOTA",
        "PROS",
        "SOLIDARIEDADE",
        "NOVO",
        "REDE",
        "PMB",
        "UP",
    ],
    "url": [
        "MDBNacional15",
        "PTBNacional",
        "pdt.org.br",
        "pt.brasil",
        "democratas",
        "pcdob65",
        "psbnacional40",
        "PSDBoficial",
        "ptc36nacional",
        "PSC20",
        "PMNNACIONAL",
        "Cidadania23Brasil",
        "partidoverde43",
        "70.avante",
        "progressistas",
        "pstu16",
        "PartidoComunistaBrasileiroPcb",
        "prtboficial",
        "democracia.crista.nacional",
        "pco29",
        "podemos19",
        "PartidoSocialLiberalBR",
        "aliancapelobr",
        "Republicanos10",
        "psol50",
        "Partido-Liberal-22-109795543775931",
        "psd.br",
        "Patriota51Oficial",
        "pros.nacional",
        "solidariedadebr",
        "NOVO30",
        "RedeSustentabilidade18",
        "pmbnacional35",
        "unidadepopularUP",
    ],
}
partidos = pd.DataFrame(dados)


# Função que coleta os posts no Facebook
def procura_fb(nome, partido):
    conta = 0
    # Trabalha com as últimas 50 páginas de posts
    # Envia credenciais de uma conta - opcional
    # Intervalo de sleep e timeout para segurança
    for post in get_posts(
        nome, pages=50, credentials=("usuario", "senha"), sleep=2, timeout=10
    ):
        lista = [post]

        df = pd.DataFrame(lista)
        df["partido"] = partido

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
    url = row["url"]
    partido = row["partido"]
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
            dicionario = {"url_com_erro": url, "partido": partido}
            erros.append(dicionario)

    except UnboundLocalError as error:
        print("+++++++++++++")
        print("URL COM ERRO: ", url)
        print(error)
        print("+++++++++++++")
        dicionario = {"url_com_erro": url, "partido": partido}
        erros.append(dicionario)

    except Exception as exception:
        print("+++++++++++++")
        print("URL COM ERRO: ", url)
        print(exception)
        print("+++++++++++++")
        dicionario = {"url_com_erro": url, "partido": partido}
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
    "df_acumula_semanal.to_excel('resultados/brutos_semanais/
    posts_partidos_ate_19_abr_2020.xlsx',sheet_name='Sheet1', index=False)
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
   "df_bruto_acumulado = pd.read_excel('resultados/brutos_acumulados/
   posts_partidos_ate_14_abr_2020.xlsx',sheet_name='Sheet1', dtype = str)"
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
    "df_result.to_excel('resultados/brutos_acumulados/
    posts_partidos_acumulados_ate_19_abr.xlsx',sheet_name='Sheet1', index=False)
    "df_result.to_csv('resultados/brutos_acumulados/
    posts_partidos_acumulados_ate_19_abr.csv', index=False)"
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
    "search_list = ['CORONAVÍRUS', 'CORONAVIRUS', 'CORONA', 'CORONA VIRUS',
    'CORONA VÍRUS', 'EPIDEMIA', 'PANDEMIA', 'COVID19',
    'COVID 19', 'COVID', 'VÍRUS', 'VIRUS', 'COVID-19']
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
   "seleciona.to_excel('resultados/covid19/
   posts_partidos_ate_19_abr_2020_relacionados_covid19.xlsx',sheet_name='Sheet1', index=False)
   "seleciona.to_csv('resultados/covid19/
   posts_partidos_ate_19_abr_2020_relacionados_covid19.csv', index=False)"
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
    "compilado = pd.read_excel('resultados/relatorios_partidos/
    COMPILADO_PARTIDOS_COVID_20_abril_2020.xlsx',sheet_name='Planilha1')"
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
      "/home/abraji/Documentos/Code/ferramentas/lib/
      python3.6/site-packages/pandas/core/ops/__init__.py:1115:
      FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform
       elementwise comparison
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
    "        teste_coleta = coleta[(coleta[columnName] == 'x')].copy()
    "        #print(\"-------\")
    "        #print(teste_coleta)
    "        #print(\"O partido\", teste_coleta.columns[1], \"tem\", teste_coleta.shape[0],
      \"manifestações ou propostas\")
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
      "image/png": "
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
    "                  title = "Total de manifestações e propostas de partidos políticos sobre
     a covid-19 postadas no Facebook (coleta até 19/04/2020)",
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
    "    conta = 0
    "    for vez in range(1, 35):
    "        valor = str(row[vez]).strip()
    "        if valor == 'x':
    "            conta += 1
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
       "   index                              manifestacao_proposta
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
    "uniformtext_mode='hide',
    "title = "Vinte manifestações e propostas sobre a covid-19 com mais apoio de partidos
    políticos postadas no Facebook (coleta até 19/04/2020)",
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
