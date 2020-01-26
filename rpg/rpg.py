class Rpg:
    def __init__(self):
        self.player_vida = 250
        self.player_sp = 100
        self.inimigo_vida = 50
        self.soma_vida_inimigo = 0
        self.n_rodadas_antes_b = 0
        self.n_rodadas = 0
        self.n_rodadas_b = 0
        self.n_inimigos = 0
        self.n_super_cura = True
        self.lista_inimigo = []
        self.erro_skill = True


    def setNroInimigos(self, nroInimigo):
        self.n_inimigos = nroInimigo


    def getNroInimigos(self):
        return self.n_inimigos


    def setListaInimigos(self, item):
        self.lista_inimigo.append([item + 1, self.getInimigoVida()])


    def getListaInimigos(self):
        return self.lista_inimigo


    def getDeleteListaInimigos(self, item):
        return self.lista_inimigo.remove(item)


    def setInimigoVida(self, item):
        self.inimigo_vida -= item


    def getInimigoVida(self):
        return self.inimigo_vida


    def setNRodadaB(self, item):
        self.n_rodadas_b += item


    def getNRodadaB(self):
        return self.n_rodadas_b


    def setNroInimigos(self, item):
        self.n_inimigos += item


    def setDeadInimigos(self):
        self.n_inimigos -= 1


    def getNroInimigos(self):
        return self.n_inimigos


    def setNRodada(self, item):
        self.n_rodadas += item


    def getNRodada(self):
        return self.n_rodadas

    def setPlayerSP(self, item):
        self.player_sp += item


    def getPlayerSP(self):
        return self.player_sp


    def setPlayerVida(self, item):
        self.player_vida += item


    def getPlayerVida(self):
        return self.player_vida


    def getErroSkill(self):
        return self.erro_skill


    def setErroSkill(self, item):
        self.erro_skill = item
