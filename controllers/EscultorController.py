# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    escultores = db().select(db.escultor.ALL,orderby=db.escultor.id)
    return dict(escultores=escultores)
