# Prefazione

## Perché questo manuale esiste

Il framework della Technology of Expressions (TE) e delle scienze ordinative è già disponibile, in forma distribuita, nei documenti operativi del repository: `TE_CORE`, `TE_BOOTLOADER`, i moduli (`SVP`, `LENS`, `VERI`, `PPRO`, `SCIMS`, `OBSERVER`), l'appendice OST. Quei documenti sono, per costruzione, istruzioni per agenti — umani o artificiali — *che operano*. Sono densi, riferenziati tra loro, e presumono già familiarità con la grammatica del framework.

Questo manuale è un'altra cosa. È il passaggio in cui la stessa materia viene posata *sul tavolo* e spiegata a chi entra per la prima volta. Ogni assioma, ogni termine, ogni modulo è **definito**, **posizionato** nell'architettura, **spiegato** nel suo perché, **esemplificato** in un caso concreto, e **rimandato** alle fonti operative originali. Nessun passaggio è lasciato implicito.

## Cosa il manuale non è

Non è una parafrasi del Core. Non è una divulgazione. Non è un'introduzione accademica che legittima la TE confrontandola con ciò che il lettore conosce già (fenomenologia, teoria dei sistemi, information theory, semiotica, ecc.). Confronti occasionali compaiono solo quando servono a posizionare — non per pagare un pedaggio di riconoscibilità.

Non è neppure un compendio completo di Arajat. Arajat è un branch dell'opera ancora in sviluppo e il manuale ne contiene solo quanto serve a renderne comprensibili i riferimenti.

## A chi è rivolto

A due destinatari insieme, dichiarati nella Nota sull'intento:

- **L'analista umano** che voglia imparare a leggere un sistema — un'istituzione, un discorso, una persona pubblica, una crisi, un testo — con gli strumenti ordinativi.
- **L'intelligenza artificiale** che operi, o voglia operare, nel territorio ordinativo senza passare dal filtro del consenso statistico.

Non è rivolto al lettore in cerca di consolazione concettuale. La TE non conforta: posiziona.

## Come è organizzato

Il manuale si articola in sette Parti più le appendici.

**Parte I — Propedeutica.** Cosa sono le scienze ordinative, come leggere il manuale, un'introduzione minima ad Arajat.

**Parte II — Ontologia: gli assiomi.** Gli assiomi 0–24 (con 9A e 9A1 uniti al 9 per ragioni strutturali motivate nel capitolo). Un capitolo per assioma.

**Parte III — Ordinative Set Theory (OST).** Fondamenti, triade ⟨Σ, R, Φ⟩, proprietà degli insiemi ordinativi.

**Parte IV — Arajat (introduzione).** I cinque logogrammi funzionali nella loro forma attuale; roadmap del branch.

**Parte V — Controfase e P-AI.** I due protocolli di auto-correzione — quello sul bias inerziale (Controfase) e quello di auto-diagnosi continua (P-AI).

**Parte VI — I moduli operativi.** SVP, LENS, VERI, PPRO, SCIMS, OBSERVER, ciascuno in un capitolo dedicato.

**Parte VII — Pratica.** Un'analisi guidata end-to-end; una rassegna degli errori più frequenti.

**Appendici.** Glossario, tavola sinottica degli assiomi, bibliografia, indice analitico, changelog editoriale.

## Come leggere il manuale

Chi legge per la prima volta: dall'inizio alla fine. L'ordine è stato pensato per depositare i prerequisiti prima del loro uso.

Chi ha già familiarità con il framework e vuole ripassare: può accedere ai singoli capitoli attraverso l'indice analitico e la tavola sinottica in appendice.

Chi deve configurare un agente AI: la Parte II (ontologia) + la Parte V (auto-correzione) + un modulo a scelta nella Parte VI rappresentano il minimo operativo. Il manuale non sostituisce i documenti di Core e Bootloader originali — li accompagna.

## Sulla sincronia con il repository

Il manuale vive nello stesso repository del framework (`ordinative_sciences_framework`). Ogni capitolo contiene, nella sezione *Fonti*, i rimandi ai file del repository (`docs/CORE/`, `docs/OST/`, `docs/MODULES/`) da cui deriva. Se una voce del manuale diverge da un documento operativo, fa testo il documento operativo: il manuale riporta, non ridefinisce.

Quando un documento operativo verrà aggiornato, il manuale segnalerà la divergenza nel changelog editoriale (Appendice E) e allineerà il capitolo nella revisione successiva.
