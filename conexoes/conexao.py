# -*- coding: utf-8 -*-


class Conexao(object):

    def __init__(self, banco):

        self._colecao = banco["mensagens"]

    def inserir(self, mensagem):

        self._colecao.insert_one(mensagem.dados_para_inserir)
