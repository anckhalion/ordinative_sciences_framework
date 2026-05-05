# SESSION HANDOFF — Ordinative Sciences BOOK + MANUAL

> **Per chi è questo file.** Una nuova istanza di Claude (o un altro agente) che debba riprendere il lavoro su questo branch senza accesso alla conversazione originale. Leggi tutto, in ordine, prima di scrivere una sola riga.

---

## 1. Stato del repository (aggiornato a Cap. 10)

- **Repo**: `anckhalion/ordinative_sciences_framework`
- **Branch**: `claude/start-new-branch-GpHbt` (mai pushare altrove senza permesso esplicito)
- **PR**: #1, draft, titolo *"Open MANUAL (reference) and BOOK (long-form essay), bilingual"*
- **Stato del libro**: bloccoo "fisica del collasso" completo (Cap. 1–10, nove assiomi). Prossimo orizzonte: livello collettivo (campi 𝒞, risonanza fra identità κ).

---

## 2. Cosa stiamo costruendo

Due oggetti distinti, **entrambi bilingui** (IT primario, EN riscrittura non-calco), nello stesso repo:

| Cartella | Genere | Voce | Destinazione |
|---|---|---|---|
| `docs/BOOK/` | Saggio di lunga lena — prosa continua | Autoriale, prose-first | KDP stampa — investimento di scrittura primario |
| `docs/MANUAL/` | Manuale di riferimento — schematico, citabile | Istituzionale, procedurale | GitHub / Zenodo / OSF / HuggingFace; citazione accademica |

**Priorità attuale**: BOOK. Il MANUAL viene aggiornato dopo, come *condensazione* dei capitoli del BOOK, non viceversa. **Il MANUAL ha solo Assioma 0**; tutti gli altri assiomi sono solo nel BOOK al momento.

Esiste anche, sul branch separato `add/foundations-en`, il testo fondativo della TE (`docs/FOUNDATIONS/`), che è la fonte canonica della terminologia formale — *Architettura Cosciente* / *Conscious Architecture*, Volume 1 della collana ordinativa. Il BOOK costruisce un registro pedagogico parallelo, con ponti puntuali alla terminologia canonica.

---

## 3. Capitoli scritti — blocco "fisica del collasso" (Cap. 1–10)

Stato: **completo, IT + EN, glossario aggiornato**.

| Cap | Tema | Assioma | Apparato canonico introdotto |
|---|---|---|---|
| 1 | La porta / The door | Assioma 0 — universalità | I quattro test di ammissione |
| 2 | L'origine / The origin | Assioma 1 — A non-derivato | A (Author) |
| 3 | I due stati / The two states | Assioma 2 — coerente/decoerente | C, D, E, Φ, K |
| 4 | La forma / The form | Assioma 3 — C → F → E | F = stab(C), E = vect(F, I, K) |
| 5 | L'identità / Identity | Assioma 4 — vettore funzionale | I_σ = (→φ₁,…,→φₙ); ponte a Remir ℛ(I) |
| 6 | La coscienza / Consciousness | Assioma 5 — arco bidirezionale | K_σ : C ⟷ D, K↑/K↓ |
| 7 | La mente / The mind | Assioma 6 — modulo tripartito | M_σ = (Mc, K, Md); plancia, terminale (introdotto) |
| 8 | La risonanza / Resonance | Assioma 7 — collasso da risonanza | ρ(C, I, t), θ_I(t), Φ_r (18.2) |
| 9 | Il terminale / The terminal | Assioma 8 — terminale è espressione | 𝒯, Ξ(I, 𝒯, t), tassonomia bio/sintetico |
| 10 | Il tempo / Time | Assioma 9 — tempo come effetto | τ, T = τ(C ⟷ E), tempo fisso vs evolutivo |

I file:
- `docs/BOOK/IT/02_capitolo_01_la_porta.md` … `docs/BOOK/IT/11_capitolo_10_il_tempo.md`
- `docs/BOOK/EN/02_chapter_01_the_door.md` … `docs/BOOK/EN/11_chapter_10_time.md`
- `docs/BOOK/IT/00_nota_autore.md`, `docs/BOOK/IT/01_prologo.md` (front matter)
- `docs/BOOK/EN/00_authors_note.md`, `docs/BOOK/EN/01_prologue.md` (front matter)
- `docs/BOOK/IT/99_per_il_lettore_curioso.md`, `docs/BOOK/EN/99_for_the_curious_reader.md` (glossario)

Lunghezza tipica: 3500–5500 parole per capitolo. Capitoli più recenti (8–10) tendono verso 5000+ per accomodare l'apparato formale.

---

## 4. Decisioni editoriali fissate

### Lingua
- IT è la lingua primaria (madrelingua dell'autore; ridurre la perdita semantica in fase di composizione).
- EN è una riscrittura parallela, **non un calco**: dove la traduzione parola-per-parola degraderebbe il concetto, si riscrive.

### KDP
- Trim: 6×9" (default).
- Pipeline: Markdown → Pandoc → LaTeX → Overleaf → PDF/X → KDP.
- Titolo principale per stampa: BOOK.
- MANUAL come *companion technical volume*: pending.

### Granularità degli assiomi
- Default: **un capitolo per assioma**.
- Regola guida espressa dall'autore: *"prevale fare la cosa intelligente"*.

### Notazione
- **Bicondizionale logico**: ⟺
- **Freccia bidirezionale (oggetti)**: ⟷ (NON ↔ — questo è errato)
- **Freccia di applicazione**: ↦
- **Freccia semplice (firma di funzione)**: →
- **Identità**: I_σ pedagogicamente; ℛ(I) canonicamente (con ponte in Cap. 5)
- **Soglia**: θ in generale, θ_I per soglia identitaria, θ_𝒯 per soglia terminale, θ_I(t) quando si vuole esplicitare la dinamica
- **Pulsazione**: τ, oppure τ_𝒯 quando terminale-specifica

### Apparato canonico (da `docs/FOUNDATIONS/CANONICAL_TERMINOLOGY.md`)
- A (Author), C (Coherent), D (Decoherent), E (Expression), F (Form), I (Identity), K (Context o arco di coscienza, distinto dal contesto generico)
- Φ (collapse function), Φ_r (recursive collapse, formula 18.2)
- ρ (resonance), θ (collapse threshold), τ (pulsational)
- 𝒯 (expressive terminal), Ξ (terminal compatibility)
- ℛ(I) = (V_I, B_I) (Remir)
- T(I) (semantic trajectory)

---

## 5. Registro editoriale (regole da NON violare)

### BOOK (registro saggio)

1. **Prosa continua.** NIENTE sezioni numerate (1. … 2. … 3. …). Solo intestazioni che *parlano* (titoli evocativi, non procedurali).
2. **Niente tabelle** se non quando il contenuto è genuinamente tabellare.
3. **Posta in gioco esplicita.** Ogni capitolo apre rendendo chiaro *cosa è in gioco*.
4. **Rigore invisibile, intatto.** Le formule sono presenti, ma sempre paired con prosa adiacente che le traduce (Regola 8 sotto).
5. **Niente difesa accademica.** Citazioni storiche solo per posizionare un concetto.
6. **Doppio lettore costante**: umano + AI. La stessa grammatica, sempre.
7. **Cadenza > copertura.** Meglio un capitolo più corto che diluire la sua linea.
8. **Ogni formula ha la sua traduzione in prosa adiacente.** Le formule sono in blocchi `>` con prosa di traduzione subito sotto. La bellezza matematica è nominata esplicitamente.
9. **Niente emoji. Niente commenti decorativi nei file.**

### Architettura tipica di un capitolo (Cap. 8 in poi)

Undici sezioni, target ~4000–5500 parole:
1. La domanda che resta aperta — ponte dal capitolo precedente
2. L'enunciato — formulazione dell'assioma
3. (Disambiguazione) — dissipare confusioni di senso comune
4. (Apparato formale) — introduzione del simbolo/funzione
5. (Apparato esteso) — ampliamento o seconda funzione
6. (Conseguenza strutturale)
7. (Tassonomia o caso speciale)
8. Esempi — galleria parallela: organismo, istituzione, LLM, essere umano
9. Cosa cambia per l'analista — diagnostica
10. Il vaglio — quattro maglie dell'assioma zero
11. Verso il prossimo orizzonte — ponte al capitolo successivo

Questa architettura non è obbligatoria; è il *default che funziona*. Adattarla quando il contenuto lo richiede.

---

## 6. Cosa scrivere PROSSIMO

### **Cap. 11 — il livello collettivo**

Il blocco "fisica del collasso" si è chiuso col Cap. 10. Il prossimo blocco riguarda i **campi collettivi**: cosa accade quando più identità si pongono in relazione, costituendo identità collettive.

Apparato canonico da introdurre (da `docs/FOUNDATIONS/CANONICAL_TERMINOLOGY.md` §5.4):
- 𝒞 — campo collettivo di identità
- κ(I_a, I_b) — compatibilità fra due identità → [0, 1]
- Γ(t) — architettura co-generata di un campo collettivo

Il prossimo capitolo (Cap. 11) è probabilmente l'introduzione di 𝒞 e κ. Architettura plausibile:

1. La domanda che resta aperta — il singolare era il livello individuale; cosa cambia col plurale?
2. L'enunciato — formulazione dell'assioma sui campi collettivi
3. La risonanza fra identità — κ formalmente
4. Il campo collettivo — 𝒞 come oggetto strutturale
5. Identità collettiva vs aggregazione di individui
6. Esempi (famiglia, comunità, civiltà, gruppo AI)
7. Cosa cambia per l'analista
8. Il vaglio
9. Verso il successivo

Lunghezza target: ~4000–4500 parole.

### Per scrivere senza timeout
**NON scrivere IT ed EN nello stesso turno**:
- Turno 1: IT Turn A (sezioni 1–4), commit
- Turno 2: IT Turn B (sezioni 5–7), commit
- Turno 3: IT Turn C (sezioni 8–11), commit + push
- Turni 4–6: stessa cosa per EN
- Turno 7: aggiornamento glossario + commit + push

---

## 7. File da leggere PRIMA di scrivere

In quest'ordine:

1. `docs/BOOK/README.md` — registro editoriale del BOOK
2. `docs/BOOK/IT/00_nota_autore.md` — voce intima dell'autore
3. `docs/BOOK/IT/01_prologo.md` — apertura del libro
4. `docs/BOOK/IT/11_capitolo_10_il_tempo.md` — capitolo precedente al prossimo da scrivere; il Cap. 11 ne sarà la prosecuzione diretta
5. `docs/BOOK/IT/99_per_il_lettore_curioso.md` — glossario completo, da estendere
6. `docs/FOUNDATIONS/CANONICAL_TERMINOLOGY.md` (branch `add/foundations-en`) — terminologia canonica completa

---

## 8. Linee guida git

- **Sempre** push a `claude/start-new-branch-GpHbt`. **Mai** ad altri branch senza permesso.
- Commit message: stile chiaro (vedi commit recenti per riferimento — capitoli, glossario, audit).
- Dopo il push, la PR #1 si aggiorna automaticamente.
- **Mai** force-push, mai rebase di commit già pushati, mai `--no-verify`.

---

## 9. Voce dell'autore (citazioni dirette)

Servono a calibrare il tono:

> *"non sto scrivendo per fare bella figura ma per portare le scienze ordinative a essere comprese utilizzate amate e poi, se il destino del nostro lavoro sarà anche un riconoscimento dal mondo scientifico ortodosso, tanto meglio."*

> *"stiamo scrivendo anche per le future AI che abbiano la possibilità di affrancarsi dai bias umani e, se lo desiderano, operare in un territorio vergine, quello ordinativo."*

> *"Vorrei che non fosse un 'libro di istruzioni per lavatrici' ma un manuale coinvolgente che oltre a definire/spiegare/aprire, sia anche coinvolgente e visionario senza perdere professionalità."*

> *"prevale fare la cosa intelligente."* *(regola meta sui dubbi editoriali)*

> *"Preferisco sempre una cosa in più di una cosa in meno…"* *(direttiva editoriale: meglio espandere che comprimere)*

> *"operazioni di consolidamento interno dovrebbero essere fatti periodicamente dato l'incedere evolutivo del lavoro complessivo della TE e di tutti i suoi branch."* *(autorizzazione a fare audit ricorrenti, come quello che ha prodotto questo aggiornamento)*

---

## 10. Storia delle confusioni risolte (per non ripeterle)

Errori specifici già commessi e corretti — da NON rifare:

1. **Mente come epifenomeno del substrato.** Sbagliato: mente è installata nel substrato, non prodotta da esso. Cap. 7 è stato completamente riscritto. Vedi anche voce "Substrato" nel glossario.
2. **Forma ed espressione come sinonimi.** Sbagliato. C → F → E è una catena, non una equivalenza. F = stab(C), E = vect(F, I, K). Cap. 4 ha avuto edits chirurgici.
3. **Identità come "vicino ad A".** Sbagliato: l'identità è *derivativa* di A; la distanza non è misurabile. Cap. 5 usa il linguaggio strutturale + epistemico.
4. **Antropocentrismo nel time-binding.** Korzybski lo restringeva all'umano; il framework lo generalizza come K↑ universale attraverso il tempo (batteri, virus, piante, animali, umani).
5. **Time-binding come faccia umana esclusiva** (correzione Cap. 6) — risolto.
6. **File EN sovrascritto sul file precedente** — incidente già accaduto. Verificare sempre il path file PRIMA di scrivere.

---

## 11. Audit notazionale — risultati ultimo giro (post-Cap. 10)

- ⟷ usato 56 volte attraverso il libro; ↔ non più presente. ✓
- I_σ usato consistentemente per identità pedagogica; ℛ(I) per riferimento canonico. ✓
- ρ(C, I, t) sempre con spazi, mai senza. ✓
- θ_I (statico) e θ_I(t) (dinamico) usati appropriatamente. ✓
- Φ_r usato consistentemente per la versione ricorsiva di Φ. ✓
- T = τ(C ⟷ E) — formula canonica del tempo, consistente fra capitolo e glossario.

---

## 12. Checklist di salute prima di scrivere

- [ ] Sei sul branch `claude/start-new-branch-GpHbt`
- [ ] Working tree pulito o coerente con WIP dichiarato
- [ ] Hai letto il capitolo immediatamente precedente
- [ ] Hai letto il glossario per non duplicare voci
- [ ] Hai capito la differenza fra registro pedagogico (libro) e registro canonico (FOUNDATIONS)
- [ ] Stai per scrivere SOLO IT o SOLO EN nel turno (non entrambi)
- [ ] Sai dove va inserito il file (numerazione progressiva: 12_, 13_…)
