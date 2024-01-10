""" Default nøgletal """
BRUTTO: int = 41_859
FRADRAG: float = 10_773.00
FORMUE: float = 264_947.5
LÅN: float = -1_298_490.35
RENTE: float = 0.032
AFDRAG: float = 6300.20

# Tillæg
TILLÆG = {
    'INTERNET': 372,
    'TELEFON': 258.33,
    'SUNDHEDSFSKR': 99.08,
}

# Pension/forsikring
PENS_FORS = {
    'ATP': 94.65,
    'PENSION_BIDRAG': 0.05,
    'AM_BIDRAG': 0.08,
}
DF_PENS_FORS = {
    'ATP': 94.65,
    'PENSION_BIDRAG': 0.04,
    'AM_BIDRAG': 0.08,
}

# A Skat
A_SKAT: float = 0.37

# Yderligere
YDERLIGERE = {
    'KANTINE': 365,
}


def udregn_skat(brt: int=BRUTTO, frdr: float=FRADRAG, tlg: dict=TILLÆG, pf: dict=PENS_FORS, skat: float=A_SKAT, ydl: dict=YDERLIGERE) -> float:
    """Tager nøgletal som input og returnerer nettoløn"""
    # Skattegrundlag
    T1 = brt * ( 1 - pf.get('PENSION_BIDRAG') )
    T2 = T1 + sum(tlg.values()) - pf.get('ATP')
    SKATTEGRUNDLAG = T2 * ( 1 - pf.get('AM_BIDRAG') )
    
    # A beskatning
    BESKATNING = ( SKATTEGRUNDLAG - frdr ) * skat
    
    # Pension/forsikringsposter
    PF_T1 = brt * pf.get('PENSION_BIDRAG') # Egen pensionsbidrag
    PF_T2 = ( brt - PF_T1 ) + sum(tlg.values()) - pf.get('ATP') # AM-Bidrag beskatningsgrundlag
    PF_T3 = PF_T2 * ( pf.get('AM_BIDRAG') ) # AM-Bidrag
    PF_TTL = ( PF_T1 + PF_T3 + pf.get('ATP'))

    # NETTO
    out = brt + tlg.get('INTERNET') - PF_TTL - BESKATNING - sum(ydl.values())

    return out


def tilskrivelse_mnd(l: float, r: float=RENTE, a: float=AFDRAG) -> float:
    """Tager lån, rente og mndl afdrag og returnerer en månedlig rentetilskrivelse"""
    return (l + a) / 12 * r


def simuler(f: float=FORMUE, l: float=LÅN, r: float=RENTE, a: float=AFDRAG) -> float:
    """Tager lån og nøgletal og returnerer totale måneder og afdrag"""
    temp_laan = l
    count_maaned = 0
    afdrag_ttl = 0
    while temp_laan < 0:
        count_maaned += 1
        afdrag_ttl += a
        temp_laan += a
        temp_laan += tilskrivelse_mnd(temp_laan, r, a)
    return count_maaned, afdrag_ttl
