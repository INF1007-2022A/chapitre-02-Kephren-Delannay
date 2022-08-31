#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    nouveau_mot = ""
    for lettre in mot:
        if ord("a") <= ord(lettre) <= ord("z"):
            nouveau_mot += chr(ord(lettre) - 32)
        else:
            nouveau_mot += lettre
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'Riz &  Pates',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
