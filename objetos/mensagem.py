# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from datetime import datetime
from objetos.mensgem_status import MensagemStatus


class Mensagem(object):

    def __init__(self, id_=None, data_hora=None, status=None, telefone=None,
                 texto=None, operadora=None):

        if not isinstance(status, MensagemStatus):
            raise Exception("Valor da propriedade [status] é inválido")

        self._id = id_ if id_ else ObjectId()
        self._data_hora = data_hora if data_hora else datetime.now()
        self._status = status
        self._telefone = telefone
        self._texto = texto
        self._operadora = operadora


    @property
    def dados_para_inserir(self):

        return {
            "_id": self._id,
            "data_hora": self._data_hora,
            "status": self._status.value,
            "telefone": self._telefone,
            "texto": self._texto,
            "operadora": self._operadora.value
        }

