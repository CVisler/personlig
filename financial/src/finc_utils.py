from sys import exit

""" Default nøgletal """
BRUTTO: int = 41_859
FRADRAG: float = 10_773.00
FORMUE: float = 257_498.3
LÅN: float = -1_298_490.35
RENTE: float = 0.032
AFDRAG: float = 6300.20
UDGIFTER_DB_GNSNIT: float = 31_333.91
INDTÆGTER_DB_GNSNIT: float = 35_033.62
LUFT_PR_MÅNED: float = INDTÆGTER_DB_GNSNIT - UDGIFTER_DB_GNSNIT


# Dicts af dicts med månedlige udgifter
# Faste og variable udgifter står i samme dict da jeg kun skal bruge gennemsnit

udgifter = {
    'JAN': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'FEB': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'MAR': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'APR': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'MAJ': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'JUN': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'JUL': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'AUG': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 5000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'SEP': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'streaming': 160.00,
        'forsikring': 100.00,
        'mad': 4000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'OKT': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'forsikring': 100.00,
        'mad': 4000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'NOV': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'forsikring': 100.00,
        'mad': 4000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
    'DEC': {
        'husleje': 4300.00,
        'el': 300.00,
        'varme': 50.00,
        'forsikring': 100.00,
        'mad': 4000.00,
        'transport': 80.00,
        'tøj': 20.00,
    },
}

# TODO: Udvikling af udgifter og indtægter over tid
def udvikling():
    """Udvikling af udgifter og indtægter over tid"""
    pass


# Tillæg
TILLÆG = {
    'INTERNET': 372.00,
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
    'KANTINE': 365.00,
}


def udregn_skat(
        brt: float=BRUTTO, 
        frdr: float=FRADRAG, 
        tlg: dict[str, float]=TILLÆG, 
        pf: dict[str, float]=PENS_FORS, 
        skat: float=A_SKAT, 
        ydl: dict[str, float]=YDERLIGERE) -> float:
    """Tager nøgletal som input og returnerer nettoløn"""
    # Tjek at input er korrekt format
    # Tilføj tjekker, der returnerer fejl, hvis input ikke er korrekt format
    internet = tlg.get('INTERNET') if isinstance(tlg.get('INTERNET'), float) else 0
    pns_bidrag = tlg.get('PENSION_BIDRAG') if isinstance(tlg.get('PENSION_BIDRAG'), float) else 0
    am_bidrag = pf.get('AM_BIDRAG') if isinstance(pf.get('AM_BIDRAG'), float) else 0
    atp = pf.get('ATP') if isinstance(pf.get('ATP'), float) else 0

    # Skattegrundlag
    T1 = brt * ( 1 - pns_bidrag )
    T2 = T1 + sum(tlg.values()) - atp
    SKATTEGRUNDLAG = T2 * ( 1 - am_bidrag )
    
    # A beskatning
    BESKATNING = ( SKATTEGRUNDLAG - frdr ) * skat
    
    # Pension/forsikringsposter
    PF_T1 = brt * pns_bidrag # Egen pensionsbidrag
    PF_T2 = ( brt - PF_T1 ) + sum(tlg.values()) - atp # AM-Bidrag beskatningsgrundlag
    PF_T3 = PF_T2 * ( am_bidrag ) # AM-Bidrag
    PF_TTL = ( PF_T1 + PF_T3 + atp)

    # NETTO
    out = brt + internet - PF_TTL - BESKATNING - sum(ydl.values())

    return out


def tilskrivelse_mnd(l: float, r: float=RENTE, a: float=AFDRAG) -> float:
    """Tager lån, rente og mndl afdrag og returnerer en månedlig rentetilskrivelse"""
    # TODO error handling
    return (l + a) / 12 * r


def simuler(f: float=FORMUE, luft: float=LUFT_PR_MÅNED, l: float=LÅN, r: float=RENTE, a: float=AFDRAG, udv_pa: float=0.00) -> tuple[int, float, float]:
    """Tager lån og nøgletal og returnerer total løbetid, sammenlagt afdrag, og sammenlagt formue ultimo
    ---
    * f: formue
    * luft: luft pr måned
    * l: lån
    * r: rente
    * a: afdrag (default 'AFDRAG')
    * udv_pa: lønudvikling pr år, dvs. luft og afdrag øges hvert år med 'udv_pa' (defaulttmp_ 0.00)
    """
    # Tjek at input er korrekt format
    if not all(isinstance(i, float) for i in [f, luft, l, r, a, udv_pa]):
        exit('Format skal være decimaltal')
    formue = f
    laan = l
    rente = r
    afdrag = a 
    afdr_iter = 1 + udv_pa
    # Hvis afdrag ikke er default, så tilskriv formue med differencen på a og AFDRAG plus luft
    luft = luft if a == AFDRAG else ( luft + ( AFDRAG - a ) )
    count_maaned = 0
    afdrag_ttl = 0
    formue_ttl = formue # Giver mening når der er tilføjet error handling
    while laan < 0:
        count_maaned += 1
        if count_maaned % 12 == 0:
            afdrag *= afdr_iter
            luft *= afdr_iter
        afdrag_ttl += afdrag
        formue_ttl += luft
        laan += afdrag
        laan += tilskrivelse_mnd(laan, rente, afdrag)
    return count_maaned, afdrag_ttl, formue_ttl
