import requests

headers = {
    "authority": "minhaconta.semparar.com.br",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://minhaconta.semparar.com.br",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://minhaconta.semparar.com.br/minhaconta/",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": """f5avraaaaaaaaaaaaaaaa_session_=
    JHFKCGDKDNKABGPLPAKIMMNDMDJBEILDFEJCBPEFIEFCMGDBMLDBFPCBHNIODGPEO
    PMDNDBICGEDFPDAICOAKNKGKLAPPAJPKJMFJAIBECENHHBOHHLHHPPPKAJOPEEA;
    clienteLogado=0; croct.cid=a3ac65fcc8b9e36788c28400eb69e448;
    cookie_custom=^!oLV5CuccSDUAse2FfAUn9m2wzCzDEzAM2DBoAgRNMLNgYtqM8+1ZPGAigXT0GzgRt6f7hR0Z1bSGxA==;
    f5avraaaaaaaaaaaaaaaa_session_=HLLJOBEDJMBKENBPOCIAPFKIJCPLBLGFPHHGOCJEHFLMNGOGJINNIAOOIOPCNEILMDODFNCOKKBCACEPHDNA
    BIPKDKBJBGFBBEHPHADOFOLCEJCKFABNAAMIOLLMAECG; visid_incap_1822685=PHa0ofusSwmrOxHjsjhtyoSqeV8AAAAAQUIPAAAAAACmN5sMB
    i5fyuLfP487hZz0;
     TS00000000076=08fde82362ab28006b02cd1160dca7d994cb745f13ef29e4ff9a0183ac1acd2a918e4bd81c741fbdfee7aef41c0bd7a408af
     cf798509d000c5b5e8eef119091d032bc24b16a6a033123f42a85b9cbb49606dbed1c012b152619d4f90a976a0624b3173e46d9e988a2bee00
     98f0d8d71d2bd37b5d2ef3a80a0e055018237aed58dcd173756d6b0329cbf8600c0cfcdc45e3d2bb8cb3cad00fb1ba6d967e2cf9af428bc930
     e22f5c226362162e10961a318c85c8c5cd36431f00435a3366e6865887747ee68c8d0baf3e3f51fc40eff49373581997e038e487744bbcd155
     1e75f97fe30ab29fea2dfa08da41a18c04527d3f58a0757e426f36d974d8c6dd5cc2485e75a69e1094541e;
      TSPD_101_DID=08fde82362ab28006b02cd1160dca7d994cb745f13ef29e4ff9a0183ac1acd2a918e4bd81c741fbdfee7aef41c0bd7a408af
      cf79850638001545a13570004dbc956aecf38a082042063e52d1ba75cc3ce2d83eb3cf0e2069cd35c21565d9dd51f99ffc512f2e3fb2d2e5a
       2468a6894d6;G_ENABLED_IDPS=google; JSESSIONID=Dkjzco6bq_4P9L6T9aTHj4VbXCD27y5bDtI_NpnBCwNUxcHVALbC^!669561335^!1
        281155758incap_ses_789_1822685=FVixOW6rFAwTQr2FeRfzCuy2eV8AAAAAOPwp1SiKdHxdVYoLXc6Plw==
         ADRUM_BTa=R:0^|g:eb4634eb-be7b-4d63-a7eb-4a734315f3bb^|n:semparar_31ad92ff-4bb1-44f0-a429-314e4808b341;
          TS016b6a4f=014fda136740f5b5a56e37ef0661df6d7352b51294d70d77da4afc9d52e8e874a5ef6a8c9281374a9d73e2d7c9
          6519fcc62e873bd601fc896002e8d119dbe77a628e0210c8b56513bfedfce17ec604ff93bdf3504ee9478c613c4f0efe4531f
          61ecca7da2ae1575c3adbbf9d4de71b0204f372676e193bc0cb7be4d9fe232bf98073fac9abd184342feb2d91f53f362908ba9dd35b89
          8be3483e44ba0c7693ad06d99ae287a659a24822ab4a40ce6202e923979238;
           TS6e212488029=08fde82362ab2800978a99c7d38c2ce81f4891653ccae8e78bb8120329a52a61a9ca01f61085cbe59800e523a3787a
           27;TSa8140305027=08fde82362ab20006a9410c45ba55543a1f8cf217e2c349e6c118389118392068c0e494dae07294908190039351
           1300070ec4ae21add73c21e5fab0f5978c55011435f4ff00c8c88bd24d5728b06a2c1a3304cd112917e9fee65018852ed697f""",
}

data = (
    "{"
    "dataDisparo:2020-09-01T03:00:00.000Z,"
    "dataFim:2020-10-02T02:59:59.999Z,"
    "index:1,"
    "quantidade:100"
    "}"
)

url = "https://minhaconta.semparar.com.br/minhaconta/api/disparoPersonalizadoContaConsumoTrio"
response = requests.post(url, headers=headers, data=data)
print(response.text)
