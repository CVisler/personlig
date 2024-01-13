import finc_utils as data

"""Simulering af låns løbetid"""
# Overførsel fra formue til lån fra dd
overførsel: float = 0
frm: float = data.FORMUE - overførsel
lån: float = data.LÅN + overførsel

tid, pris, formue_efter = data.simuler()

print(f'Ud fra simulering er du gældfri efter {(tid / 12):,.1f} år.\n\
Det vil koste {pris:,.2f} kr. i alt.\n\
Og din formue til sidst vil være {formue_efter:,.2f} kr.\n\n\
Antagelser: Ingen ændring i udgifter (gnmsnitlig) eller rente. Afdrag og indtægt stiger med 0% om året som default.')
