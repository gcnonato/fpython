#!/usr/bin/python3
from requests import post
from parsel import Selector
from pprint import pprint
from datetime import datetime
import PySimpleGUI as sg
import urllib.request
import sys

class DiarioOficial:
    def __init__(self, month, url, year=2020):
        self.year = year
        self.month = month
        self.response = ''
        self.url = url
        self.url_base = 'http://www.imprensaoficial.com.br'
        self.cookies = {
            'PortalIOJoyRide': 'ridden',
            'ASP.NET_SessionId': 'xwgb4pqwuwvdxwwjricfy0r3',
            '_ga': 'GA1.3.343843048.1589019110',
            '_gid': 'GA1.3.946827584.1589019110',
            'PortalIOIntro': 'OK',
            '_gat_gtag_UA_129106988_1': '1',
        }
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.imprensaoficial.com.br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx?filtropalavraschave=24311856&f=xhitlist&xhitlist_vpc=first&xhitlist_x=Advanced&xhitlist_q=(24311856)&xhitlist_mh=9999&filtrotipopalavraschavesalvar=UP&filtrotodoscadernos=True&xhitlist_hc=%5bXML%5d%5bKwic%2c3%5d&xhitlist_vps=15&xhitlist_xsl=xhitlist.xsl&xhitlist_s=&xhitlist_sel=title%3bField%3adc%3atamanho%3bField%3adc%3adatapubl%3bField%3adc%3acaderno%3bitem-bookmark%3bhit-context',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.params = (
            ('filtropalavraschave', '24311856'),
            ('f', 'xhitlist'),
            ('xhitlist_vpc', 'first'),
            ('xhitlist_x', 'Advanced'),
            ('xhitlist_q', '(24311856)'),
            ('xhitlist_mh', '9999'),
            ('filtrotipopalavraschavesalvar', 'UP'),
            ('filtrotodoscadernos', 'True'),
            ('xhitlist_hc', '[XML][Kwic,3]'),
            ('xhitlist_vps', '15'),
            ('xhitlist_xsl', 'xhitlist.xsl'),
            ('xhitlist_s', ''),
            ('xhitlist_sel', 'title;Field:dc:tamanho;Field:dc:datapubl;Field:dc:caderno;item-bookmark;hit-context'),
        )
        self.data = {
                '__EVENTTARGET': 'ctl00$content$Coluna$Navegadores$dtlNavegadores$ctl02$ctl05',
                '__EVENTARGUMENT': '',
                '__VIEWSTATE': 'Dys7l8CFngq8Ua+0otsCkG3akclRxE6MunUwEVzF9tJiFLGDtU+WovOW4G1kJX5gaOzPuLesFB5aiiNAugInr5N+J2uC6KlOZwyt+kEyL4TJRs4uhFdAhe3R9COie9Un1lCgDklSz6pM/KFVZz9IdJyofNfGQTXtzxpWsIJkJBKlzHRCir30OlzEWY4Pioz1JPixqbgXvTYmMarzKrRo+ENdgAJIjOuSil6PeNMB1ZuMOD7CTP28eiB9I+SFzP+VQn9hWP4nol7JWqzzjlCUAoLlZAZGLf4SAgb+uxrIvP8ayKzgeD7LS4oKunrCgAHWlB4aCUam588SRqzmNbLnUFqHIwAQVCi53TJ/iEXCo9UQko14KkZWFI80CQTSOJn6kGhmCqvXd+pQt3CaZ6WZmal6C29OoZZzZKxL8LRtTZVtAkdQyQxZxO2zgoOXO5rE2llap7uBOYGcLPWjWLRPXJjrBseK+GNoUeyzKm96DE5/U249G8l6j8frLIbKraM0jzJxO4uAljDdJubBAadhWkHtXhnEGJ8CPdZ3oPI7B9rhxr2x8bhu/RokcGpBaiJEKiasW3RIJpZ7vsO6XwrL8hLJS/cyjPBqCH/8BnkSzb6T+k7Tn0RNKemP+3log/keqQwfrIsbtT7l6NWa67RwM3ZJgQ+ucX3bgZsuyuS+ezUFMNE4BtXAspyf9UMGVqK8wsPUF7IWSt8WtZlRjr9XPx1iE3HsTz5OZq6dn7Ex7NqrfI/c0rxkNceJHcxqewR7c+6DT58wTdvjlia78m/fSkYK06bqm5WGxy3Q3TvKbj5wC9JpiTOjJXxtaX44rAXOWBfBPum22a08APMVSIS/LCZV2BJH3T4/+nPj3ZwP8cnieyUs8vde04+DmOo+kMBKh7H1Me+Lc6G7yK4Z207hKryFt2eWEL7Mq/ng52pmOzK7nXz9RPGkdlCS2suV8YklSordW+umE7VQ+wcO8rxI4V89r6kcYsuKtswitiLdnjWF/Xy1XNfHLDKPw7JD9ojvIEqRc7wMql3oeUp0vlw2iS2iYnSOCkWcxl07Zt5YZtpG1lYfuC31lELp3WF99kadla/1EZK+gboOJhspYO2jXrNod5QqV0XBUka7bBzxkJhaKfQPhCQGNlZhALq85R7nAE5+P+cuUIKiIj2OPIrNqXfnRRO6PpjElyGEHvqETl//bC4Ie7vSQdE5kKaOpshUHfRS1G6hzZi/F6hf2J7daKhDduTs/7Sp2uFG1nKDm6cLFHEZuwXDRge7zXLqGrM18wTScdgiyai5jmt5d4iNhMkrSmluPJ/Qc7+Ob2Wafni4WodEZ4EDfCPd31Qc7gmO9aSBjjjebuvKf/5Koh11V8VEv76ljcotqktVOourtwtkvIEI13CUL+Lw71vVqCwCf03tQQt6sGhYCN5QGw0GsISvz7elLyli6TEFHFBFaEQZjvJGnonfwzxiYcfQ5UGSNWTfAs8HZBnrrnUfg/2VKCFdhFpNpsGU/b/shnk0t/0o4kFropZJD2ZQlz6xNlj6kIoTkYly5toVrDFRwRn5F/NLklHtzBasfKG+AjIK6gJAijCNgumW73PKWUbNXwGA+UIeJyqOjcTnX+UlS8CeAHOCCGx8IVSC350f3ER233IoAB5R6wwNa5gMeEtAPaZUOgB6tSGqOkf7AmFBjLJZ4sRqipZYi4Lwon8w/LjmHcVd3gX8tebDomhm/VRVwq+3ZDwAKHNwDpNzFy8cLSnH82xUoCNvnCdCgSlyMbGr8bh4bXdie0tVgfjD1y+xA7mCpA9RXDfBKbwDCacbZ75SjFFLg+ONZJ/UdQpQ196WlG4cebBCbb6WFZjx2y3OnEXBJC3CmnV83dzfXtD/cSTwxmmej4lPo/SWNXYbo//eHFk+tb8M/uVaExoZaewjubKdOa6LGIQr8qRbtNb82dIWcncNIW2BxWh2rygeC5qr02VLeaTafiAAGvU0o0KMJ8foD+MjMpWhbpeNJmpmxuO5UGruGq27tvPnxSt/vtTPlVaZBbq4IZKY2ROJzqZfrGMa01as5EaMhzms2oNjf2ic1FfKH3k14LoVl79dURTgdlca9CgXpFIZ49jkj2qM0I4bZ2n52o4BBSeyShmDpR3WG3lyHxgdY8DYDJo747+sw9RRqLvt1f84LJmL1gOwRY3vdHEqIO5B9p7AJFL7oa6GTSAQrtWtfYbiUvft45PVjmLxZ+RnzS2edehKnvhdtsFyy8YoPt73CsDhFYWuS5aTbVla23k4ok2tHrEPplm0xWKMFvamBmfQnTyMzgo2hI+jgsQ37nmKxHLNHhLu64Ttff/wPfYrG5IIzkSrvZF8V/MjBq2WelMUW1FG4P/x2LDDzJa/Unu4Cys5pNX+ZllcvhzLm2LWjpCE0YW2Lo5inyLGeXYmwdimaWOtJB+mey8oayu84/WpyAXcZy6XGpg/23gDYQrc7jbRR9T+bDIEf4m7RKPUR8x+iCPs+vS1VGUPHiypwyVdWdqzuJj/X6LUMabkS+MC+FMNGa+enZpRyK9tOK7bFSHkdOiWJHOaCAjm/9eb0Z+EBVem8JadrOU/aW9zZ4DJl45+rylG9nS1N2I8gwdongm2NJ/42xxrF+UnS9ZfKcIE+lwx0rDmct3jl4o/5nHdEKeAv+d/PlLuyqZzQPUV9WjkDuXsIqvofsXpdlqtXSM6gm6SjDaEYyFQ+xOoqGzQXP/GXbJMsUzD330H2PnSMwBW5r5XG8xNh69oljFR9TL7wqGdgWl9VpGa9ufuyAsGimm2ytgZ5jCO04z2JxTowlvyxFt3+aZTg32jJnO3Bqi2UsxlyNhsEdQQr7q2nHX8Qu3kFy2pSvmw31AUAuD2Kwib5JCyqeBtlEvw0/1aVWASBhgVrTfIxZGwHtzfUhdqHSd4shD/39H/RtpVOo4i12VjNJTXiGGQIZgUipGP4ltXWiV6ExMEMBc34fVv/HYDsooZlP9tUDzCBtsryphzNUinNdkm6/F3OjxP1rcvz+kN5ajFkiDsq6GpDAM2YacsZiarPbeJPTcFEfqeJWkDkKaC3OhetbetCYyMJ7SsGN089a1QHhn8lmt9fGfSroedgXpYKSsvubbrH3CGWOASj/xZb3+jy3chZ0qMeMttC2kLxmyMsW4pgLZsRvd1GPccTlb+ZRad3ECzjL/b9FR7BsAjfiP2a8beL9aAa9gohfsyOQTZcpJonYq6Qs25k1R1U+oPOOWZs69X2rUS1YMZPUTICVh22FgHTqdJtr2jjnywGQlUHb9cct9R+oz8Yy3HiBlzA78+nEZuSX0bcxbYX7s/4sWuvKeV0X7QRaONv/aOOiJFAWJqgTAlt0TQfJEbUYKExVnIIE252msDYRDj/P+YE+/Y9vzeN6E1qJr7OVo45A+xavEW3pYCEIIJvyBOeo9g4TpWRsJTkwVaCpcHhBipGi+lQBAlje262NPbFxiWpMrIPfygCPmEpUCstCZGd53ZcxmjxRXrfHRgpYgyau3KAcatTgbx1LBtmR/8RRYTM03iJUoU1uDdd+bwqAxT+nBg7xXNBRVTBGpBXX8Pg1k0MCJDntCrDgMvipufG3+L8xMemBAs/rh43dqYVwU3rUumofLRqLHgV9GMnj0fxHt5RMc7qxG25Mzik+fSfORG7byvy2cpjwcmALy4wlfish5WGcbPF7zNtMQ4BVvJH/p8WJ5P6g+iEIpfDgrzo72kWSlYluBwMcQemGgDDDi7M6d2xvXQxQ/wBq1Aaa6NA5sFu2wlWi5u5hVzJEE/DwtJmthsnSPlGgoTaIJSYcc6bFYHoBGOgpg4ivjMGu55dBQ12dP7IRfsh+Btuq61Eo1cJyuQMoPEX7LQYRQV+AS7Mvtjav/JvJVAvV0bxgpZU+6S5RssBQf2+q2RNfuSy3hUPYglFgPlEbYXzLfY2KzAv/g9b/kS7Y2Fqd78dZnG61SguPDiL2nL9ngegV/CWuINQnvJwm6TmtovU912XTV24t4I+RKiiWUjSYo5g/E/3g8gSKlq/k7B9cTUM/Hd8zWPRJy831Q/1QOCG2yRinByviyjr84AlPWUGT0JeERppCTzrSxeJNCS6ab3xYrnNo5wBHsgAWJpN6w4+Fj+GuAVkrT9k1RHJLVclnEtAzxmLL4z7vOAMzmAfGHeSKfypzcQAz5rkx6KivO7DWJ1lXKPedNYqkmUt9vVVyEcewhwoU+Ao0l+ANJL8IA80TJrJLISttgTqprGdi1cC0cdXrKUjn/NVPDC5sO9tYCDXCWW4z4oflJ+hR4WWBR5NQUN+r7XAH5w0RA70G+D+wEsMdLUU1uLmtubUgl6F6sfNsL+p2dmTF2xPnbVbmf3D/lAg1M0Ob6pTerUNC8wgwFDjn9vBuLz3mcixx87hAmQlj82EwsEtAnJmEYrOpiR93GgYtyvcWW5kQtsWT/wXExh0DVV32o6QFUJAUh3aodWyAKtMVOVpNlPY1/WmyBpkxOXc9AInZtkB/uRjOb3Wmhm+JeEHYMg3VfhqmjNLJncpMxN0BINR26ilvrsqKXog4ouZSyPuGUi6xhW+06NTWzz9Lj4WGhtjq+IHIn/Y23HkZElGx6ZomajkPCyLe2dHU+0TGfqlPcaEXDnFjVMLF3+AfQY9+OH8xoFpFlsR14UhREWGkAwZ4UmFM6Z8QmGDcgO8FJyhKg4oVVhfKLKyQHSMtCGgA378KhC/szCMyff4q4jh5nfNcZHnYuTKMXZzjCMjw6ShhlciJ88nB0ZxSbgJXEw84sGpr8/cR1lkSCVs2kHTBhoH2c4so7NzHhdPgR2mX7IcQGCq7FAARh+492iCg7jvdxW0Y/eEuFdc/oBkkBxng7dv83SiXWCQzQXZHhEWsgEoOUgqSJydDmfObuvJ1PnVZWNmUTTr2Ne4Fsc5/ZUDAuiPkJWX1jBWER94VR7oAdyHvglEMCSAe97R9SubxC5LovQ8HpfixmVsENIbEbSdB9wiR5/Icd08YmUvk8hch5m0mJGMIBVHSPIQs0X8C3neuliNjiBxYvOuQfzaphKOVCan3in4KKQMVtRjDIyMbUFC8Tdv/TLfKEoAXcu0h3OXRdaeshI+05+JqMBWo05+IR4QhTlnKOSlkOUo3g+/9PAooBJ8RZcNMny5izofg57+5vHZuvpDxbMvNdVBdPfvGUSpTDFvhyRsZLPUARqTiszJeHD7RDCeK0akb6MgxQH/SzYYuUOO19MCkmLfIk/7rNNd6jAmKpYsCYEsGxl6PBJGoiZZYDH8eRoOUH/DVywPkNVbeinwwOjgLfwf4nkS0ldXCvMLoUK6etlFjapbZf4NMDMJImc3Ak2GxuKl/tJX9Pv2/aJH0rqdvopLZDcZJPkP/IAJdlTYUWGwGhVMnly5u+QEs0JE5CIqltP64tun3s6s65Mz00CxLP0Nr+KV7miWidRaSE514dbh3dxOXdU8ozof1MKZaK7U+xBUWodog2IMHN9GvWN5SX+bvxbjgilvyJ4ictogfTomOS2QFwvX0c4PXxdf78u/o5GQU5Nlc21MEB252S5OSUAGcMM6qW1YdiG9P6062ZlJcsZHmnp2N+pFHFcxMQCRNwXP6jGj8XE/xrKe73lNzdOr4LT1tMLwN8qYuAPfo4Js9jEsLmzwBj+VacRvlpK2nRo3Gd0vfpK8Ps9D1L0zmMe5bxN0g+IXLj/QvUKUPOhlM64mw57QKyguQrwm8ZaWZvkPq5PII4f3dU6MYo13F9txXDWKq6lgKew4pmdlWqf1DPpzjLy5DsAltN2ztM1YyIWeCUm8o/8FpI0rcxd5IWJ+SYbIZ+ofKX255dyQYLDF/En3DgaZwHHEz8mMW3jGlp06NI96+0ri+lTWKD0kWioG556tlP6abhBZXw9KmcNOstfX4TyNm8Xrl5H4StQelGntctOzJRcJ1gnO9BMJlZdXPsfnVh6jqC/E/yxAsOOFmFvQe9EFglKeSRXBqGdBnX2hq/x4uaXV0MxePV3J0hNUg0JeJNGtzdX27Lqecmx3r+BzkFwaeV69hZtRkPjOjbCZpXFmopwRWkKuT8wr7hOovrqUObhG8tktFUInWA7PuCXlJCaV7iRqDzXagc2LKauzR3oUa5hrQmbOfDXlcWcyw2CY0E20PZaCXfUsqKeos2pDFQg9HR/14UY7+8doKEl0ubgjGzZP0Z0tles/wlegTCgqfCuIYa59z6GpS1/m/SGm9fplp0QSLam/5HWa9VxmXLuqsTrI3thC8EWPVZCbcAps15Pgm7LI/TTIvr2Kd6EyRMIqasssIZByM4iQxMUDxnaaEQWIXp7WuNtidIhjataqE8s8SOHj2IKNEPvehMC0rF45liriV7KskMfe+6c6XbD5U6dyMzDoOdDq3UbaRQ1+BcErqKgE0VyZEpKJDB5dhi049s3bfTQrOEb/LIOdARlP3XpI8fL0b2tA9IPDXvJ9BsYnvO/gEpDkEeT9VMp5V7Y6VSSZwBXCeQdXYYMbM19A6J07SR5McJ24nd3fSvAE5vo0wtYF0z5vTYnhlURkPAmy7S1JdNrXEd6iI8dJ803Igoxb0aRVjDlmQm20F6rklQ+pxNh3wStJt3Aqff5Ik2prJM5ejWBEyhO4hKeNRyLUt3BflLFFSHpIo7Trc7iHoJjdV8hk6od/I0RrjflQGRBZO2AhuJRPOxHfpHkCfCAnUOzNQb8zxx2LJPuCiIfLrOGKFUNrKa003X37W6h+jxD3VZJYdUop3cPKHVeNVokea4GzYK5ISjoM5mBSzJI2GUsRzuyGj6Ih4MPrjPYrI8piLB0LX0nqFQVLPIABwgn6quG3kTkYSwfdwG8Q7TmGrEXsjk6BD8a2qWkUofzDP3sN42Ept9P4AikA9z5VEQIWUxdDqDYdhR47dWxWtjlyHiBBiH4OTWYB7CGPYD3SzH4ztUpxs4mr/KZKPmoRx2AWIUoT/6BoQUcB2imDBjm3rOx0CQ7eUO3vZhmUknXIyT1bGk7mZMZtnRHV3w6Nzins0PY2xTDtcQeKMOJ7lechtOT5RbwH83BP95opbgIRq+QNZfBVYlekE7xMhuytWxRz/jFJ83avQs6TP5jdkD8e0/ir9h4ai0adCI0oB07zIYYXoov1/bI5an9pnLW5YDw39GIljMP9Gyr9JWCKPyDVOGw24TH4lPp44lVN1LagDSNod7cWMxfjW85h0MGXMZ7fivXlHDblUwd3pIY321AUNOOm0CoYOHs/wnmxq20JBf0S97jkfnvxkl87GT5r+jktF8kcGsb3hnR1LzjWRt0JHHf9kxeS6vXbKH7NegNwI5QKUIhPoBK3uNN6Iwt0c8E3Vdy6HInWidjEp6zIDKMoqd+S/S/1/PF5y+qGXzmPZ9pfQNVmifgxce0cdmuvX2pIJsuE4ISoZKmp7FKd/3c2lTTmguOKD1+CRtDLmmiPL33EV9nZQaNFNWem829aPbF6fRzusG7IAVhUsQKtPnoJ/kxryuHZupvN4eJSRvoCJjmqItNLmzdlNu9AoiCAIQ7mz9j9rxcvvHVEm0TNsjzAzkmcU4tP9BeNXNTfIcMr/ixNeKJ/yX01X9svblKgD8idV7BGXSgqcNeCNuZFPSIMDboH/r8EEVrTWsT88OgOVa/zsCu3asGfW2CZ7actOnO93BQNrjI+gAopc9evzSQjS1lMRsWcNn+89N3b96KUAaLRhXb5RPru2fgXN96/srmW0gseGBdsVV9XCGBAfcrChvo34U5E7kw240rpbw0fCtaMmviQ+KEeEj1sS35IqMg3IJSdvMWqdSMT4MTWq2ILc59YhtBeMVstGDl05l42s1NUxKDrzMndvSpC88Qz5NewreJhYH8+PR4+j3B1rdBYHK/ryXSdL6QNncU9Q2G2s2pfltFLfbGxA2W1ZdphTvW5vgABO92MXpI2pyUbOFf89OAy0ior4QGMO9KNBGO9FYN6qLIFvdIJCbVUrMeBbIZyLxY3HH5lyb0lkZ2X9l48j3cXNk6dQPqNl+edQD6htKI5HzwF1+EH6SLpwuTcHtunbqhpGied7rc0D07cp8s2z3shlh7zFfItJlom2bIzC3dVIYWPEHFMZ6lOEaCucTeVhaIyThIL8WtQ1HRgV4uZNLg+pzEg15tfdKQtedjnVyMMKQa4cpmIIkjel3ESSvL5TRFCc7JYwnE8ndrFF2MTrfjgy01WuQ4xh6AURjtKFQB0yslYzjD4yTItPNXU+jVH+nV/8EvRXsznyLb9jpGMq+04tF/HvDz9MGDw0uRWW+e7KRJ6U6YFzKL0q7qPyCvCJz7DXaIGwVTHNX6UtPH8N+PG3dz3RDanFmIQHkVtzV+nh0QtL1hihqTbhzcK2UZbfHtpgfKlEgpF7CEFeH8V6bqX2tqVPr9xuoBF2eMyWvUWMIXSCgCBkHHkirQSO29Opo4xwh3Jj1LloWcludTIKphwqg0mKUjmXoIwGRop6Ran44TXJNREqNJwfQXzOhlbTMkLeyLMxqsouNuGucjqATBzrqQZBKGCDwHcrPNj3QaemOjn9jr6WGy9lHbpngK+ZQfLJm3Xn/L42eN6a1xu7uLtZwUd/nTRVWghSDnRO3ziUuAnWeOIriWqlyfI7dthSXdui6BpApimXY9A8k3AKBbJOL0d06BP1wogGUDU3J5KGy6Z+pxUHpdl3eKkpAKK1tN6x5eStYv8BbqpBHd2fk6Vr8Tbl4DJLxgdaTFgfDeiH0vq8im3s9ZXJMGXLcDxmxsJgZYEaDtq2XrFkVi0Kp6e+bxQUIce2zhklShyWHnNvMpSe6NPmqxu8Nle4G+MrHE+ojXZ/4t+h4vwnnWWesJ12mD5v9c/ORLPLWJn6KPPpO9ySHmmf+Lem9ygdmjHFPlW81oKFMCfPhuH90Y3v12wN+R4y3YuFa4048k7tEhnpcalPCZ9URGMUsFneR4/YexH+BV74uzxUSmb4MkJCXMEUQLZ++JagZrpPHpoXua7xUNYLK1zVV6gHAd89gQbW8oYamVxwRhPIxFxN60Roxy7aquS65ko/aN02PNp30ha3YY1iAMXoKaTXWEgoxIBaAhWwASbofCn+qjNQ1uXG3bRh3LwlKDVblHsbLluYw4nxa5vgIt6B+p82nJIPr6MuK5uOePIZiRe/A8IAg5mbknM01wSgBzLZIeSb0yZkhRJF/7MdbNOYbTuiS3Yoyj2nBxwTUPZxifHk4hL+xQi+NzQV9XGSCibWNHNWwzOag5XNBuQ3DNSksPmW1P49q+nEQO0//MOfUiA+uYSIRmFiHndN2hwHD4TM90qi9mgMDJYkqvdSEnA/fWARDxP6rXuITUWwOSrZt1xr7MzGJQqkR5pcko7zn+LQVmjbouGNAEb4lejIhjuUAgpo9a4WrKNADGQmHMDTXGmJkWruma7NWauYf99aGDbcsjKmfv37Zx28IVWRxHS6RTa4V2WSN8SpXeMVZjtzIxCBTczRyjf5GXvCZBpNlucjyS8ZQo/9iYYqBFsFm/fiHdBss1iM/8BZ8lNIUqdMXpcUQd0IgEol0NqiS5177PrqaCmgMrj4Fa6Hawzavl0e9Rc4489y5kx3Ug6+9yEF1/TSuVbYTsRqN+bjMFykGQ+0jZU2t9yboWqJkVgw5yr1Ag6vgK3l7WqqHfvNPCiUZ86CwbW/28mnIhWw2hQviesJJjJeRcou56qY9rSPeUKeyTB3LpEGJZOvT0fKzbvsij0P+Bmmh56fyRNvVQOsuusOuriiicEBvy6vldUQYbmC71BVE4LAEjwsQwdqTinJF1R/9h1FBZYK421jwvYNYsamEXJuYTQ77lJauEO9J9IzAr1whOyoBVd+xK7oOqVzxS7Yif7/76KMs++t0U285NHMmhRdO9PqovQEjm4t502x5wG0DxxJQhsfk8ELjYOLnxWAgd7q9meZNP+P6w1WLPqWUc6lllGFuq2GOWK5dVCe5Ad/xw4Wx37lKSK/UxCx4nj4r8Ele+bq6K3PCBXqo6J5e9orJxPYMAppS0VyRssiN3dQ84Mp3kNyAWykn5BBHHe9/IOEEVRNTS0MDZr5dElHnP2XpE/NHaCCYMwM9I0gTNPscHa3e01D7q5pb/T79MeV6jyez3HabtWnDTki0aDkNbExb7wkgB73jPnsEgi6gjZK7LNacVKiV8ok39z1MyAYTrok9K+Cmxs0eprJakAATvZxFe63oV/PJIU2vVWkFWwsitP2DohBm/Oiri1hrwj9wJoYDm2XhedEWoT1wZTaVfcQ2NxpZXhbjKHJxNlTSfK73spq/D/KgmzSD18HHh0kVIRO+CGAuF14/zcbcqDu0qH4mO2mi2bl4LL34AKvW5i2yWM3bKHaZVeWFhTUhY+KJsAdouWQ+FIorIWcYT5e0KiHv+pEz5RwolUR3iGY2cUkJWSpNZpcnziLZu1EQ80S7lZp1/LXCw077VOmFoEizvNwBEoO2Z4iDVqYiJum74LktoiXr32ZgejGyRsTSIGqS/76LgLpNAu29jL1rwENZR2jiceu1SkKT7Y01baJAEqjkz1Uzu3tnmePpX8/y6fVyFySs4846l2usBaoT5+WRQkDvTgEsG6cZEasNsuunO+4Bh6U+Pt25ulQl4oPBAC4YYGpp1oUIm3UqAIiYkSDK/Uq59N/66pXV+VXKkZhLmwUGE+l9+BoDEa4WxzdE/nteLrfGBS9jDKknOpwbpO1ydxYySSaVAcRQqxp7FmhGscXTHWHtcAEWo9ue8JYUwkkYiMy0OP7gVHc+GGR42Zq8bPsHGGwl8HL3JXwxL2KH8pG9GyRZEX5AJi9V66wCMDNZu3gZOfyoP1rAdYNXJxos2UdJo4KfCl5tbhloGgoJV/puCrXItCGCTCctEoIInCGD3yGalBk3jMJTl/7TWljdKoSF7RPd7GQY/aQiq0Dry9j6V/EPEbcP+itfCDs+dN8rRQ1calVYHLqzDDpVVcev7o8g60Fb5hVNIk4WdP54xBxdZ1XiUy/lm8Xr6WfNHw6FU4/DGoFl2zkV6BZAlwMuLqBbEAXSlH4zDMvbxu92zrhHa05tfTVGNkZ7fwHoLVee6l7R0dzbLiXU/E/Vo2yENEUZalfDXoUWazwGySPKjc/fYKHxIPbpHk/BIt0hl6EIgnIKsZC+Avj8OFKY2yNi8Do1WxqgRAs/SoaKjebxoHlAL0reUlzHBsJM3Q62HPuB799TIAirkQtXy2ElXL+gNa6Hf0FxhgsN7Gz2sVeUSTftt1d/DFIyspnL92wVm9yL6abxlaELFQ2/1EqUFFvuRCRZkWuhBDhwhkeIpYp889yNghodLC8kTQvvtfapms3DSKNoy9APLfdfh80d/o0TCeXg/6HE2Z4RHM4AsEewNl6d5U49R09Rqd0TcnPVQG9r6Ds8H9n7yyWh6VxnB5hr5IV2KON3SB3q24s3WWPe6vFgqQODqqDZhj5RshsPR+C+ewtp5MIUiOXOAB4P4yEIePyiWrhyJD4VXILLtshF8qSiIdrHVdL4Eome+ItO6/YIgj+xnxXewTIvWRNrrqfZD6oBzsTWM2DI/vC5Mm3tfJbszOPGUIXpBmTQCxIjt4P0WO9mp5Zs4cDZf8OIUk/82u7JnzywXttDvLrWl9pOm4Xgfhci/xKqULJJL1IrtTVpsKsgRWbR73zUa2s2y1QxZdhyHoc8IOvWHQAZrgOqcq8go8EgscX2+f3mQyqh90tP9+QWbjtjSpk83gbT+X1mSfKTbjUOuIpCVXbWAbV4jp6UFipL9FkIcwe6p9opQ4FtevAc/sy6nLs3TEP55YbCR0k1Hl0ExYvuuZg2E8Y8DNAwUvZxiRdm8YJ6CPO0GCJEsJ26+BNC+Os61JfzEnT+GfvPOYarmqjzGga9wkxWJMcEjhiKCjcrUTKZzldqVutD5XlXx5ioPXjVCEt+6P/OuSYhQ8TpvbLn8GhT2pIkf21/qsZigoueCSEsy0v38fNqz2wWEXRClkHgUSDZK1biwA43MwVp1kZH8B3rKjeY8LTkReCcKRsGbc7jn7gCqUQb+0/sc0w/f3nOADUPxCYvU9TtaUovAoOYSMUd5hRwIdoTg3YrtCuy1zzCp/gOimDk6SIg1Q5hgvIRSyO/pIM9ucRnvf5+/lz7LXZykofNvP6DOsWJvwZn1L33Bp+3LQ2ggDH5VC81Rv/EFpzK5rVVnXnQ68ZBXESQ3evLlxXAnm1Fhs4HJDRRxts6bUzuNZpI5WhpxtaSqS7hpYlWU2ING1BQ/07On0khK28dsHMttoWwoDa1Cuv9XVRiUQLrG+d984rDA7k0gs+GthfhSkTVQ2SeNZqUIhTxturyBaB13AwJBueM02Wp0DpeYDp/uOxZ2kfq7A3Ct9fNrd16draCnpNVWXd4K8OdAZsipJmPvyWH0OPmFNx/FvAAVMX9/+wdj7TuT8CXzwrZgRH3CT4f+dqVFFWxK18uZXJEvcO1wAjDfPXDIgBuZ/8KF7SoH4dgV4O+QRR8ClUPP84oIwc+18w92pPbvpAmmybScwfG0JO7lYMd19eGsPnrdZgszsDspQgw/Q2JBgplQ4a/gbtu6PIf3JwnU3pCfS1FpJBEyo0q32Ruekiwe/AQGe67Yc8ZaZ/cEMspB1y4hrjVvu/fh9ImghWP0b8cXJi4jJOU5SC4HTFIkZUGb2sILvbDcM1v4VY+Ksea+vCoQN8+FLghb6O2NwCc5s77qr4fIr64/J2DtB4cujwrd6cLSL6ITdUNLnMVcT8K2Vh8gtiUAPnEO4piobIUSaNpCuGUwCBn0uEINIRBfhpT72/ncA5U4t7eR59t3/zvLIqXZEymV33u3AnGP3ONu0WzNzO0vp7GFRIhqU/rJQ8YgsZ+pRymr+/NTcJk17DdgARzczwdopuXgU03OCracb6T9fUNrD3QuXlY+KoY/5aZzqqPKW+vrW+Cy0Fa4yZ2H9C6E5VatVL6MA9/2m05Se67HY4D6ZOQvESBuCd74Vx8x4Op9B5tR5vsv4A7jIMT9lDA4ZakE6ojztAtf1gu0Ioeq0QYHG+Sd+MnEfooI329nc+AUhzb9PQ/1SWjON9trC+6Fx21jJEvjzhuSaG6+RY3eArlJY5EoBEE8srGZtmSLmoK6lihvma5Z+WCNH3CJir5MtG9uqbdd9kDEza9xBbr7dtR5dO8uczQdVfTs0dwNHXplk8HoP6fWFUbf0t2j9hZ+NbVa5v2xDoQHobyRwBi9kv18bbCYAXF9wyvkhnAy/SzC3cZpHUgIwa/9g2TQDJfJS+7cVnBCPBcjQ54V4svJFeRTs23v9OcUgdhu9PmM0Uj9TXn3gFqtgLl24AxNSMXO6WlsWMVGXdVxnKwGeFTIxTtbuMF5g723+2LWM465m7+YYfCm3wbjCmqV5ZrtoNln6TAfXvcMWfhIh9mj8ympuWMOmrpeqIVKM/xC3QweFhrjAkFq3UuLAXPAB0qR7P7B6xf/ybWaE2yFthsPgnlqJl6nlsJX7HI5nSV5iHz10To50fhKNVzyjKYs+Az8vI7xl5zv+mhwja9P0ytWuqC/GjC03X0UmWtBSV7+Y+cU2OB9sYHnV9TupBrrMEjxFrOv2VEnE1hC3RIo+Ye6QkbfnVg/uVsZnSIXlJjRovba+/Xk3SCaCsdWrwrJWcRYVutTHDgVYJ1wM60c5xDKrH+lQMkVxoyivNSTDhMYXUjJGqXAHu9UVXSRHhql9MB4lE6XmexeeGVkdO3ojm0vGCNpkyoMPaD79H6ED/bDRP5N2I9TBZ0+K9nIxYt8QkbPLEnsvlxcSVXPoT86XatVrEVYy55JLhBSFN/n+mXZPAFDlt2eKhH902J2mhOj9FY9ipwqhwCXYkm/HdADHtJl2BzekWZCQKQ9qKP8+P11H/HpE+CUBXmpKg/plCxZDWw1/QGSDmJ0MnxU5oDTpKPiwjrgwIOyPmum+UWvRCrKiPpj5izJZkL6cBdGt/kLuIHqzMdnsmtH3W1LQMl+6wKBlwsZu+px7PXP1vvJy75PbML1oEvTbqEn8teBc2POwiNDNZut11+8RswCl1Eg1Z8ukD5WCDzg3n3//s/YERkHyy/sYof2dNYfrpH40XdfcrMU7Bg8q2aGacfLt7Pkf7McImshj0JAxkcc+TQxU1fSdTzyRXKYASQTEFLyt1mxjgeEy9PAuKC0iFDLsK/KOJ0GIOu62aBegu6zEwr3iMtleBjbkgX2clQ6bWyfY9YWNbUDetNkKdEV/xoUUviRdXhycIAsMG3Pa92OMADrNj6X3jKn7p/uVXUbkcH+o37aqILB1XVeOuqSonNC3PNnB2k/ay2T6w8oVPEozHFKlVGk9hKPgTCyyCy2Rws0WEGEAglk1PP/Bh/K4icWmpLyOiWqQXqzZXT0rzSIXdczOOWCkOfueQhlu97yxm5TzJEp4T/reUhCOO4VYmBBjCy/Sdimpeg5c2ZGm4U3cPWtLttPPJbH5z3lrAtYmrniuL7U/X3dtvk6e7rKoVGmYE+XAM7NYQ+JQiXp6rSHYLLZuLZtUXGRXbpzgbthQYUUv67RSihiUE5tClMILRrxqeecFKH19BWmY9U8jQLuHDtJ2WLtrjmMm2ltRdq8WYwc7dZiKr49KV1+2swzc7r/DRRHIxuxyBDOuYsmuf18deSSB4CLPStDdGBEuEaEoZHTWTUPLtJSrKLa+OFlb4WOxWcvN0sfbd4uKREKJfDoYuzDsnD6MefsMLFmqKTleZT5f8tHSHkFDG9KVLNSJdfDOaKNYmcz2ZY1WhlA90paSXHopoGgxbCRj7EBcSdNNPKwXU7kJvuFGgx4F2jFSPnt3XUxH0bEOL/IUiQE1v+BNJ1pNhT3toA0IkS4cmzvjj/wz16DiUHcQDr+R9c4Ik73YBREoPYPQk0qQT2MXiyyZ8kBXSyCURb67zPYEqQVUmR5j/Bon/MXP5LPuKJv0REFKioHCayroNyrQEo+zdLLl1N1j2kZF4ljgdcXmK8fHKDbUjS3WrxXBDLTyMsaNrdkOHK1iDMkd/BHc6M13D0mQvi1rW61NDMfw4KtrHSx1P+mjQOvHchtoax41v+HJ9XPMargmmSnExpfNzZj9EZNP1QQMGERJJiRSp/HMeYWXGm4CsHEzA6xdVi4vjF98FGgKoT7d8vhYKD8sC0lUrIRXafx3TYoEJ6CTVMdekd/86bg0txpjV8rw/fDTe086KSTQGGCZhRb4rZOc6e1T7HKLU6htQMLy5BH4M3nHjkGK2tbUz4SbIm6qhqZlZ0fVG2a7GEfk9hzgpFgCnlv6r6GDsPNCzvSMv7li6AbY1DQT01JR43KTfa5AAc9SP+MwM7dVcqhn//WK+SdRKFdwO1KP6VwQs7YUwyr9Ce+LdHJf1nHGJd6bbofpX15SMh9Bk2NxLsw/nmvLq8T5Xk7u5myRCQLD0l3O8ibUFQoJ219su/yZ+le1j+J8WLd4Udt3biENnjImTCBTVNbSKuhcv1clevlL1ez7be95k6Vd1Act8OEDeCZpkmn0VBSr29Bf8VsuOm3mA==',
                '__VIEWSTATEGENERATOR': 'BDCE6B05',
                '__EVENTVALIDATION': 'enJUU2jHQsM1ep6zc+Py+UOhQojTVr6RvwvcR67WcQzSpG5eAHWPYdZHzDL6QBBgG5RlVALOVcIjmpMfijbPpzSMcjYjnx9IW9B91dzKDgNTLlPrUImnZweHdDq252zSaLu0SAUghn3QMDeE9mhJs3XeJ8w9iaU0kzqc4ezMqCf0pyvwVAVYqk3gQgyrz2bzFfzLASkhDobDyoVOvro4bbAGL9mUUMiDd+AFtuYLa5KFD9Qe/m3zpDC/j2eOdg0y4do+s6Imgcma6iBhQmed0ytpK9wn3ezOEBBuJw4ABp7vjNq7l0VEA4ob7Je1MR4fxWpYdBu9EgdZa2u+VCD3LdxXJsZr3o1uQhfAR9rQdxLE5o78iZzHT6PX4mkHliFIaVXhw8MwmdTQ3xihWoxafwWTjEo=',
                'ctl00$content$txt_nav': f'anonavigator|{self.year}',
                'ctl00$content$BuscaSimples$txtPalavrasChave': '24311856'
            }
        self.response = post(
            self.url,
            headers=self.headers,
            params=self.params,
            cookies=self.cookies,
            data=self.data
        )

    def encurtador_urls(self, url):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urllib.request.urlopen(apiurl + url).read()
        return tinyurl.decode("utf-8")

    def scrapy(self):
        parsel = Selector(text=self.response.text)
        list_urls = []
        for luciano in parsel.xpath("//b[contains(text(), '24311856')]"):
            url_extract = luciano.xpath("ancestor-or-self::a/@href").get()
            url_extract = ''.join(url_extract.split(' '))
            # pprint(luciano.xpath("ancestor-or-self::a/text()").getall()[1].strip())
            url_download = ''.join([self.url_base, url_extract])
            url_download = self.encurtador_urls(url_download)
            for nome in ''.join([e for e in luciano.xpath("ancestor-or-self::a/text()").getall()]).strip().split(
                'Art.191/193 - I EFP'):
                if 'Luciano da Silva Martins' in nome:
                    # print(nome)
                    # print(url_download)
                    # resul = [nome, url_download]
                    list_urls.append(nome)
                    resul = None
            list_urls.append(url_download)
        return list_urls

class Gui:
    def __init__(self):
        self.months = [
            '1:Janeiro', '2:Fevereiro', '3:Março', '4:Abril', '5:Maio', '6:Junho',
            '7:Julho', '8:Agosto', '9:Setembro', '10:Outubro', '11:Novembro', '12:Dezembro',
        ]
        self.years = [str(year) for year in range(2008, 2026)]

    def layout_inicial(self):
        # sg.theme('DARKTEAL')
        sg.change_look_and_feel('Dark Blue 3')

        default_month = self.months[int(datetime.now().month - 1)]
        default_year = int(datetime.now().year)
        layout = \
            [
                [sg.T('Escolha o mês')],
                [sg.Combo(self.months, size=(20, 12), enable_events=False, key='choicemonth',
                          default_value=default_month)],
                [sg.Combo(self.years, size=(20, 12), enable_events=False, key='choiceyear',
                          default_value=default_year)],
                [sg.Cancel(), sg.OK()]
            ]
        window = sg.Window('DO', grab_anywhere=False).Layout(layout)
        event, values = window.read()
        window.close()
        return values['choicemonth'], values['choiceyear']

    def view(self, list_finals):
        MLINE_KEY = '-MLINE-'+sg.WRITE_ONLY_KEY
        layout = [
            [sg.Multiline(size=(60, 10), key=MLINE_KEY)],
            # [sg.Listbox(
            #     values=list_finals,
            #     size=(110, 15),
            #     select_mode='LISTBOX_SELECT_MODE_SINGLE',
            #     key='_LISTBOX_',
            #     font=('Arial', 18),
            # )],
            [sg.B('Plain'), sg.Button('Text Blue Line'), sg.Button('Text Green Line'),
             sg.Button('Background Blue Line'), sg.Button('Background Green Line'), sg.B('White on Green'),
            sg.Button('Sair')]
        ]

        window = sg.Window('Demonstration of Multicolored Multline Text', layout)

        while True:
            event, values = window.read()  # type: (str, dict)
            print(event, values)
            if event in (None, 'Sair'):
                break
            if 'Text Blue' in event:
                window[MLINE_KEY].update('This is blue text', text_color_for_value='blue', append=True)
            if 'Text Green' in event:
                window[MLINE_KEY].update('This is green text', text_color_for_value='green', append=True)
            if 'Background Blue' in event:
                window[MLINE_KEY].update('This is Blue Background', background_color_for_value='blue', append=True)
            if 'Background Green' in event:
                window[MLINE_KEY].update('This is Green Backgroundt', background_color_for_value='green', append=True)
            if 'White on Green' in event:
                window[MLINE_KEY].update('This is white text on a green background', text_color_for_value='white',
                                         background_color_for_value='green', append=True)
            if event == 'Plain':
                window[MLINE_KEY].update('This is plain text with no extra coloring', append=True)
        window.close()
if __name__ == '__main__':
    url = 'http://www.imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx'
    month = 2
    year = 2011 #default 2020
    gui = Gui()
    month, year = gui.layout_inicial()
    # print(month.split(':')[0], year)
    do = DiarioOficial(month, url, year)
    list_finals = do.scrapy()
    # for pericia in list_finals:
    #     print(pericia)
    gui.view(list_finals)