# -*- coding: utf-8 -*-

from objetos.mensagem import Mensagem
from objetos.mensgem_status import MensagemStatus
from objetos.mensagem_operadora import MensagemOperadora
from conexoes.conexao import Conexao
from pymongo import MongoClient


conexao_bd = MongoClient("localhost")
banco = conexao_bd["sms"]
conexao = Conexao(banco)

m = Mensagem(status=MensagemStatus.AGUARA_ENVIO, telefone="3111", texto="ola",
             operadora=MensagemOperadora.TIM)

conexao.inserir(m)


print(m.dados_para_inserir)