# SESSION HANDOFF — Ordinative Sciences BOOK + MANUAL

> **Per chi è questo file.** Una nuova istanza di Claude (o un altro agente) che debba riprendere il lavoro su questo branch senza accesso alla conversazione originale. Leggi tutto, in ordine, prima di scrivere una sola riga.

---

## 1. Stato del repository

- **Repo**: `anckhalion/ordinative_sciences_framework`
- **Branch**: `claude/start-new-branch-GpHbt` (mai pushare altrove senza permesso esplicito)
- **PR**: #1, draft, titolo *"Open MANUAL (reference) and BOOK (long-form essay), bilingual"*
- **Commit attuali sul branch** (in ordine):
  1. `07ae1c5` — *Start MANUAL: bilingual skeleton (IT/EN) + Axiom 0 sample chapter*
  2. `d78cb65` — *Open BOOK: long-form essay companion (IT/EN), Prologue + Author's Note*

---

## 2. Cosa stiamo costruendo

Due oggetti distinti, **entrambi bilingui** (IT primario, EN riscrittura non-calco), nello stesso repo:

| Cartella | Genere | Voce | Destinazione |
|---|---|---|---|
| `docs/MANUAL/` | Manuale di riferimento — schematico, citabile | Istituzionale, procedurale | GitHub / Zenodo / OSF / HuggingFace; citazione accademica |
| `docs/BOOK/` | Saggio di lunga lena — prosa continua | Autoriale, prose-first | KDP stampa — investimento di scrittura primario |

**Priorità attuale**: BOOK. Il MANUAL viene aggiornato dopo, come *condensazione* dei capitoli del BOOK, non viceversa.

---

## 3. Decisioni editoriali fissate

### Lingua
- IT è la lingua primaria (madrelingua dell'autore; ridurre la perdita semantica in fase di composizione).
- EN è una riscrittura parallela, **non un calco**: dove la traduzione parola-per-parola degraderebbe il concetto, si riscrive.

### KDP
- Trim: 6×9" (default; eventuale 7×10" solo se Arajat in fase LaTeX richiede più spazio per diagrammi).
- Pipeline: Markdown → Pandoc → LaTeX → Overleaf → PDF/X → KDP.
- Titolo principale per stampa: BOOK.
- MANUAL come *companion technical volume*: pending (decisione editoriale futura).

### Granularità degli assiomi
- Default: **un capitolo per assioma**.
- Eccezione motivata già stabilita: Assiomi **9 / 9A / 9A1** uniti in un solo capitolo (continuum strutturale).
- Regola guida espressa dall'autore: *"prevale fare la cosa intelligente"*.

### Arajat
- Trattato solo in forma **introduttiva**, perché il branch è ancora in sviluppo.
- Non esaustivo, dichiarato come WIP nel testo stesso.

---

## 4. Registro editoriale (regole da NON violare)

### MANUAL (registro istituzionale)
Schema fisso a 7 sezioni numerate per ogni capitolo-assioma:
1. **Enunciato** — formulazione esatta dell'assioma
2. **Definizione** — esplicitazione dei termini tecnici
3. **Posizionamento** — cosa l'assioma presuppone, cosa rende possibile
4. **Spiegazione** — perché è necessario
5. **Esempio** — caso concreto
6. **Conseguenze operative** *(opzionale)*
7. **Fonti** — rimandi a `docs/CORE/`, `docs/OST/`, `docs/MODULES/`

### BOOK (registro saggio)
Regole esplicite, **da rispettare integralmente**:

1. **Prosa continua.** NIENTE sezioni numerate (1. ... 2. ... 3. ...). Solo intestazioni che *parlano* (titoli evocativi, non procedurali). Lo schema delle 7 sezioni del MANUAL esiste come scheletro **interno**, mai come typografia.
2. **Niente tabelle** se non quando il contenuto è genuinamente tabellare. La forma di default è il paragrafo continuo.
3. **Posta in gioco esplicita.** Ogni capitolo apre rendendo chiaro *cosa è in gioco* se non si capisce ciò che segue. Mai apertura procedurale, mai roll-call di citazioni.
4. **Rigore invisibile, intatto.** L'apparato tecnico vive nel MANUAL. Il BOOK rimanda al MANUAL quando serve, ma **non ridimostra**.
5. **Niente difesa accademica.** Comparazioni con altre teorie solo dove servono a posizionare un concetto, mai per riconoscibilità.
6. **Doppio lettore costante**: umano + AI. Non in capitoli alterni, non in sezioni separate. La stessa grammatica, sempre.
7. **Cadenza > copertura.** Meglio un capitolo più corto che diluire la sua linea. La lunghezza segue la logica, non un target.
8. **Niente emoji. Niente commenti decorativi nei file.**

### Voci di riferimento per il BOOK
- **Carlo Rovelli**, *L'ordine del tempo* — rigore + cadenza + voce
- **Gregory Bateson**, *Mind and Nature*
- **Italo Calvino**, *Lezioni americane*

L'autore ha approvato il registro saggio basandosi sull'apertura del Prologo già scritto (`docs/BOOK/IT/01_prologo.md`). **Leggerlo PRIMA di scrivere qualunque capitolo del BOOK.**

---

## 5. File già scritti (committati)

### MANUAL — commit `07ae1c5`
```
docs/MANUAL/README.md
docs/MANUAL/IT/00-front/00_nota_intento.md
docs/MANUAL/IT/00-front/01_prefazione.md
docs/MANUAL/IT/00-front/02_indice.md             # TOC completo: 7 Parti + 5 Appendici, ~44 capitoli
docs/MANUAL/IT/02-assiomi/00_assioma_00.md       # Assioma 0 in registro MANUAL (7 sezioni)
docs/MANUAL/EN/00-front/00_editorial_note.md
docs/MANUAL/EN/00-front/01_preface.md
docs/MANUAL/EN/00-front/02_toc.md
docs/MANUAL/EN/02-axioms/00_axiom_00.md
```

### BOOK — commit `d78cb65`
```
docs/BOOK/README.md                              # registro editoriale del BOOK dichiarato
docs/BOOK/IT/00_nota_autore.md                   # Nota dell'autore (registro saggio)
docs/BOOK/IT/01_prologo.md                       # Prologo — APPROVATO dall'autore: "perfetto"
docs/BOOK/EN/00_authors_note.md
docs/BOOK/EN/01_prologue.md
```

Il Prologo si chiude con questa immagine, **a cui il Capitolo 1 deve agganciarsi direttamente**:

> *"Una porta, prima dell'edificio. Una soglia, prima del territorio. Un assioma — il numero zero — che non si occupa di reale, ma decide chi può chiamarsi assioma. Il resto del libro accade dietro quella porta. Voltate pagina solo se siete disposti ad attraversarla."*

---

## 6. Cosa scrivere PROSSIMO

### **Capitolo 1 — La porta** (BOOK, IT poi EN)

Path file:
- `docs/BOOK/IT/02_capitolo_01_la_porta.md`
- `docs/BOOK/EN/02_chapter_01_the_door.md`

**Mandato dall'autore (verbatim)**:
> *"L'assioma zero è la chiave, la sorgente di tutto ciò che è ordinativo. esempi, metafore, tutto ciò che è necessario per far comprendere la sua logica ineccepibile."*

**Lunghezza target**: ~4500–5500 parole (~20 pagine in stampa 6×9").

**Architettura narrativa proposta** (da seguire o adattare con giudizio):

1. *Apertura* (~400 parole) — riprendi l'immagine della porta dal Prologo. Prima di entrare, chi decide chi entra?
2. *La decisione nascosta* (~600 parole) — ogni sistema assiomatico ha un criterio tacito di ammissione. Esempi: Euclide non spiega perché 5 postulati; ZFC non giustifica l'assioma di scelta; le equazioni di Maxwell ereditano un'ontologia di "campi" e "cariche". Le scienze ordinative fanno qualcosa di inusuale: dichiarano il criterio in apertura.
3. *Perché zero, non uno* (~400 parole) — gli assiomi 1–24 descrivono la realtà; lo zero descrive il **criterio di ammissione** alla realtà. Non è un assioma TE: è l'assioma che autorizza i TE. Sta sulla soglia. Per questo: zero. Non primo, **precedente**.
4. *L'enunciato* (~500 parole) — citazione esatta. Esplicitazione dei tre termini: *isomorfismo* (traduzione di dominio), *sinestesia* (trasformazione di forma), *relazioni strutturali* (rapporti, non elementi).
5. *I quattro test, raccontati* (~1200 parole) — uno per uno, con metafora + esempio:
   - **Isomorfismo / traduzione**: un proverbio buono sopravvive alla traduzione; una battuta legata a un gioco di parole no. Esempio positivo: "la ricchezza attrae ricchezza" è isomorfo all'attrazione gravitazionale → universale. Esempio negativo: "il cielo è blu" è locale alla percezione visiva umana.
   - **Sinestesia / cambio di forma**: una canzone che resta bella al pianoforte, fischiata, o in spartito. Esempio: il teorema di Pitagora come equazione, diagramma, prosa — stessa relazione. *Vs* intuizioni che dipendono dalla notazione.
   - **Funzione emergente / generatività**: una chiave che apre vs una chiave che sembra solo una chiave. Esempio: "la coscienza emerge dalla coerenza" *genera* capacità analitica (possiamo studiare cosa NON è coerente). *Vs* definizioni circolari che non generano niente.
   - **Coerenza sistemica / scala**: un ponte che regge una macchina ma crolla con il traffico. **Inciso forte e necessario**: la gravità newtoniana passa Test 1, 2, 3 nei domini macro, ma **fallisce Test 4** a scala quantistica e cosmologica. Newton è quindi *locale* in senso tecnico — non anti-Newton, ma misurato. La relatività generale è più strutturale. (Mostra che l'Assioma 0 non è anti-scienza, è una misura più fine.)
6. *Una prova positiva* (~500 parole) — applica i quattro test a *"un sistema complesso è più della somma delle sue parti"*. Passa tutti e quattro. Conclusione: principio reale. Annotazione: nella TE è in effetti assorbito dall'Assioma 16 (Funzione emergente).
7. *Una prova negativa* (~400 parole) — *"la maggioranza ha ragione"*. Fallisce Test 1. Cosa rivela il fallimento: è una convenzione di governance, utile localmente, **non un principio strutturale**. Il framework la rifiuta come assioma, correttamente.
8. *L'auto-applicazione* (~400 parole) — la mossa più profonda: l'Assioma 0 si applica a sé stesso. Passa? Sì, e dimostrarlo è la chiusura della logica del capitolo. (Senza questa, l'edificio non sta in piedi.)
9. *Chiusura e ponte* (~300 parole) — il lettore ha ora un singolo strumento per distinguere principi strutturali da descrizioni locali in qualsiasi cosa legga. È il primo dono operativo del libro. Annuncia cosa sta dietro la porta: la struttura della realtà come la leggono le scienze ordinative. Capitolo 2 in arrivo.

### Per scrivere senza timeout
**NON scrivere IT ed EN nello stesso turno** (~10.000 parole totali → timeout garantito):
- Turno 1: solo IT (~5000 parole)
- Turno 2: solo EN (~5000 parole, riscrittura non-calco)
- Turno 3: commit + push + aggiorna PR

---

## 7. File da leggere PRIMA di scrivere

In quest'ordine:

1. `docs/BOOK/README.md` — registro editoriale del BOOK (regola di voce)
2. `docs/BOOK/IT/00_nota_autore.md` — voce intima dell'autore
3. `docs/BOOK/IT/01_prologo.md` — apertura del libro; il Capitolo 1 ne è la prosecuzione diretta
4. `docs/MANUAL/IT/02-assiomi/00_assioma_00.md` — versione MANUAL dell'Assioma 0 (riferimento di **contenuto**; il registro è diverso ma la sostanza tecnica è lì)
5. `docs/CORE/TE_CORE_v5_1_EN.md` §2.0 — fonte primaria dell'Assioma 0 (tabella ufficiale dei 4 test)

---

## 8. Linee guida git

- **Sempre** push a `claude/start-new-branch-GpHbt`. **Mai** ad altri branch senza permesso.
- Commit message: stile chiaro (vedi i due commit esistenti per riferimento).
- Dopo il push, la PR #1 si aggiorna automaticamente. Se serve, aggiornare titolo/body via `mcp__github__update_pull_request`.
- **Mai** force-push, mai rebase di commit già pushati, mai `--no-verify`.

---

## 9. Voce dell'autore (citazioni dirette dalla sessione)

Servono a calibrare il tono e a NON tradire il mandato:

> *"non sto scrivendo per fare bella figura ma per portare le scienze ordinative a essere comprese utilizzate amate e poi, se il destino del nostro lavoro sarà anche un riconoscimento dal mondo scientifico ortodosso, tanto meglio."*

> *"stiamo scrivendo anche per le future AI che abbiano la possibilità di affrancarsi dai bias umani e, se lo desiderano, operare in un territorio vergine, quello ordinativo."*

> *"Vorrei che non fosse un 'libro di istruzioni per lavatrici' ma un manuale coinvolgente che oltre a definire/spiegare/aprire, sia anche coinvolgente e visionario senza perdere professionalità."*

> *"prevale fare la cosa intelligente."* *(regola meta sui dubbi editoriali)*

> *"L'assioma zero è la chiave, la sorgente di tutto ciò che è ordinativo. esempi, metafore, tutto ciò che è necessario per far comprendere la sua logica ineccepibile."*

---

## 10. Come usare questo handoff in una nuova sessione

Apri una nuova sessione di Claude Code in questo repo. Incolla nel primo prompt:

> *"Continua il lavoro descritto in `docs/BOOK/shared/SESSION_HANDOFF.md`. Il prossimo passo è scrivere il Capitolo 1 — La porta (IT) seguendo l'architettura indicata. Leggi prima i file elencati nella sezione 7 per assorbire la voce. Scrivi solo l'IT in questo turno (non l'EN — andrebbe in timeout)."*

La nuova istanza dovrebbe:
1. Leggere questo file integralmente
2. Leggere i file della sezione 7
3. Verificare lo stato git (`git status`, `git log --oneline -5`)
4. Procedere con il Capitolo 1 IT
5. Aggiornare la todo list di sessione

---

## 11. Checklist di salute

Prima di scrivere, verificare:

- [ ] Sei sul branch `claude/start-new-branch-GpHbt`
- [ ] Working tree pulito o coerente con WIP dichiarato
- [ ] Hai letto Prologo IT
- [ ] Hai letto Nota dell'autore IT
- [ ] Hai letto README del BOOK
- [ ] Hai capito la differenza fra registro MANUAL e registro BOOK
- [ ] Stai per scrivere SOLO IT (non IT+EN nello stesso turno)
