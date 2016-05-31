# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    artistas = db().select(db.artista.ALL,orderby=db.artista.id)
    return dict(artistas=artistas)
