#!/usr/bin/python2.6
# -*- coding: utf8 -*-


import chinux
import android

droid = android.Android()

def dial(titre,message):
    droid.dialogCreateAlert(titre,message)
    droid.dialogSetPositiveButtonText('Next')
    droid.dialogSetNegativeButtonText('Menu')
    droid.dialogSetNeutralButtonText('Exit')
    droid.dialogShow()
    return droid.dialogGetResponse().result['which']

def menu():
    droid.dialogCreateAlert("Chinux settings")
    droid.dialogSetItems(['Seed','HSK level','Merge levels','Language'])
    droid.dialogShow()
    response = droid.dialogGetResponse().result('item')
    print response

def main():
    nwords = 0
    ch = chinux.chinux()
    Nwords = ch.getnwords()
    word = ch.lookupnewword()
    while Nwords<0 or nwords!=Nwords:
        choice = dial(word[1],word[2]+"\n"+word[3])
        if choice == 'positive':
            word = ch.lookupnewword()
            nwords += 1
        elif choice == 'neutral':
            break;
        elif choice == 'negative':
            menu()

if __name__ == "__main__":
    main()


