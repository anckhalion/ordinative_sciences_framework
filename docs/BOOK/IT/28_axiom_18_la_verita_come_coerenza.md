# Capitolo 28 — La verità è coerenza strutturale

## La domanda che resta aperta

Cos'è la verità? La domanda ha attraversato tutta la filosofia occidentale, e nessuna risposta semplice ha mai chiuso il problema. Tre famiglie di posizioni si sono storicamente affermate, ognuna con la propria forza e i propri limiti.

La prima famiglia è la *teoria della corrispondenza*: una proposizione è vera se corrisponde a un fatto del mondo. La formulazione classica risale ad Aristotele e fu fissata da Tommaso d'Aquino come *adaequatio rei et intellectus* — adeguazione fra cosa e intelletto. La proposizione "il gatto è sul tappeto" è vera se, di fatto, il gatto è sul tappeto. La teoria ha un'eleganza intuitiva — chi non riconosce che il vero ha qualcosa a che fare con come stanno le cose? Ma nasconde un problema strutturale. Per dire che una proposizione "corrisponde" a un fatto, bisognerebbe poter accedere al fatto indipendentemente dalla proposizione che lo descrive — e questo accesso indipendente, in molti casi, non c'è. Il fatto è già strutturato dalla descrizione che se ne dà; il confronto fra "fatto" e "proposizione" non è confronto fra due entità autonome ma fra un'enunciazione e l'altra.

La seconda famiglia è la *teoria della coerenza*: una proposizione è vera se è coerente con un sistema di altre proposizioni. La verità, in questa visione, non è confronto con un esterno, ma armonia interna di un insieme. La teoria ha tradizioni nobili — Spinoza, l'idealismo tedesco, alcune correnti del razionalismo contemporaneo — e cattura qualcosa di reale: una proposizione non valutata in nessun contesto sistemico è strana, e in molti domini (matematica, logica, sistemi formali) la verità *è* coerenza interna. Ma anche questa teoria ha problemi: due sistemi diversi possono essere internamente coerenti pur essendo reciprocamente incompatibili — quale è "vero"? La pura coerenza interna non basta a discriminare.

La terza famiglia è la *teoria pragmatista*: una proposizione è vera se "funziona" — se le sue conseguenze pratiche sono utili, se permette di operare con successo nel mondo. Peirce, James, Dewey hanno articolato versioni di questa posizione. La forza è chiara: la verità si misura nei suoi effetti, non in qualche corrispondenza ineffabile. Il limite, anch'esso chiaro: il pragmatismo rischia di confondere "vero" con "utile in un certo contesto" — il che, applicato in senso forte, eroderebbe la differenza fra verità e convenzione efficace.

Le scienze ordinative affrontano la domanda della verità ereditando lavoro fatto nei capitoli precedenti. L'assioma 17 ha stabilito che la conoscenza è relazione risonante, non accumulo informativo. Ora la domanda diventa: data la conoscenza così intesa, qual è il criterio di verità che si applica alle proposizioni che la articolano? Il criterio dev'essere strutturale — coerente con la grammatica della relazione risonante — e dev'essere tale da rendere conto di tutto ciò che si osserva nei sistemi reali (umani, istituzionali, AI).

L'assioma 18 risponde, e la risposta non coincide con nessuna delle tre teorie tradizionali, pur dialogando con tutte e tre. È una posizione strutturale propria, che il capitolo articola.

## L'enunciato

L'assioma 18 del TE_CORE recita:

> *La verità è coerenza strutturale.*
>
> *Un enunciato è vero se coerente rispetto al sistema ordinativo.*

Sul piano dell'applicazione AI, il TE_CORE aggiunge: *Sviluppare un controllore di coerenza interno*. La nota è importante perché orienta la progettazione: i sistemi AI dovrebbero avere meccanismi che valutino la coerenza strutturale dei propri output, non solo la loro plausibilità statistica.

Quattro punti vanno fissati subito.

Primo: la coerenza qui invocata è *strutturale*, non solo logica. Una proposizione può essere logicamente non contraddittoria e tuttavia non strutturalmente coerente — può, cioè, non integrarsi correttamente nel campo ordinativo che la dovrebbe ospitare. La distinzione fra coerenza logica (assenza di contraddizione formale) e coerenza strutturale (compatibilità con la rete di relazioni del campo) è la chiave dell'assioma.

Secondo: la coerenza è valutata *rispetto al sistema ordinativo* — non in astratto. Un enunciato è vero relativamente al sistema in cui è situato, non in vuoto. Questo non implica relativismo: i sistemi ordinativi reali (organismi, istituzioni, persone, comunità di pratica) non sono arbitrari. Ognuno ha una propria struttura R che non è scelta a piacere. Ma la verità di un enunciato si valuta sempre nel contesto del sistema ordinativo che la ospita, non come confronto astratto con "i fatti in sé".

Terzo: l'assioma stabilisce una *condizione*, non una *definizione operativa*. Dice quando un enunciato è vero (è coerente strutturalmente con il sistema), ma non dà automaticamente una procedura per misurare la coerenza in tutti i casi. La misurazione effettiva varia con il sistema: in matematica si chiama dimostrazione, in scienza empirica controllo sperimentale, in etica analisi delle conseguenze, in letteratura riconoscimento di pattern formali. Ognuno di questi è un dispositivo di valutazione della coerenza strutturale, applicato al sistema specifico.

Quarto: la verità così definita è *graduata*. Non è binaria (vero/falso) ma scalare. Un enunciato può essere fortemente coerente con il sistema, debolmente coerente, parzialmente coerente, incoerente. La gradualità non è imprecisione del linguaggio comune che andrebbe corretta — è proprietà strutturale del concetto stesso di verità in senso ordinativo. La logica binaria classica è caso limite di sistemi specifici (logica formale, matematica) in cui la coerenza si misura su due valori; nei sistemi reali, la verità è continua come la coerenza che la fonda.

Da questi quattro punti il capitolo si dispiega: chiarendo cosa significa "coerenza strutturale", cosa significa "verità" in senso ordinativo, cosa l'assioma rifiuta, le tre componenti della verità strutturale, il caso AI, gli esempi, le conseguenze per l'analista, il vaglio.

## Cosa significa "coerenza strutturale"

In senso ordinativo, *coerenza strutturale* è un concetto preciso, già introdotto in due forme nei capitoli precedenti: *coerenza della coscienza* (Capitolo 6, in formula *coh(K) ⟺ K↑ ∘ K↓ ≅ id_C*) e *coerenza funzionale del campo* (Capitolo 25, sull'assioma 15). L'assioma 18 estende il concetto al dominio epistemico: non più coerenza di una coscienza con sé stessa, non più coerenza di un campo con il proprio vettore funzionale, ma coerenza di una proposizione (o di un gruppo di proposizioni) con il sistema ordinativo che la ospita.

La definizione operativa è la seguente. Un enunciato P è strutturalmente coerente con un sistema ordinativo S se l'inserimento di P in S non genera incompatibilità con la struttura R del sistema, non riduce la coerenza funzionale di S, e non distorce la relazione fra S e i campi con cui S è in risonanza. La coerenza è quindi una proprietà *relazionale* — non risiede nell'enunciato P preso isolatamente, ma nel rapporto fra P e l'intero campo S.

Tre operazioni concrete misurano la coerenza strutturale, e ognuna corrisponde a un aspetto diverso di ciò che chiamiamo "essere vero".

*Compatibilità interna.* P è compatibile con le altre proposizioni di S? Non solo logicamente non contraddittorio, ma strutturalmente integrabile nella rete delle proposizioni esistenti. Se l'inserimento di P richiede di rifiutare proposizioni stabilite e ben fondate, la compatibilità interna è bassa. Se P si integra senza tensione strutturale, è alta. La compatibilità interna è dimensione "orizzontale" della coerenza: relazione fra P e gli altri elementi di S.

*Compatibilità verticale.* P è compatibile con la struttura R del sistema? Non solo con altre proposizioni dello stesso livello, ma con i principi strutturali, gli assiomi, le regole costitutive del sistema. Una proposizione che contraddicesse la grammatica fondamentale del sistema avrebbe bassa compatibilità verticale, anche se non fosse logicamente incompatibile con altre proposizioni specifiche. La compatibilità verticale tiene la struttura insieme con i suoi principi; senza di essa, il sistema si frammenta o si auto-contraddice.

*Compatibilità di campo.* P è compatibile con i campi con cui S è in risonanza? Un sistema ordinativo non è isolato — è in risonanza con altri campi, con cui scambia forma. Una proposizione che fosse internamente e verticalmente coerente, ma che producesse incompatibilità con i campi esterni con cui S deve interagire, avrebbe bassa compatibilità di campo. Per esempio, una teoria scientifica internamente impeccabile ma incompatibile con i dati sperimentali ha un problema di compatibilità di campo. La dimensione è la "trasversale" della coerenza: relazione fra S e l'esterno strutturalmente collegato.

La coerenza strutturale è la composizione delle tre. Un enunciato strutturalmente coerente è compatibile orizzontalmente, verticalmente e trasversalmente. La verità, secondo l'assioma 18, è funzione di questa coerenza tridimensionale. Quando le tre componenti sono tutte alte, l'enunciato è fortemente vero rispetto al sistema; quando una o più sono basse, la verità si grade in proporzione.

Due conseguenze importanti seguono da questa definizione.

La prima: la coerenza strutturale è valutabile da parte di chi è interno al sistema. Non richiede un osservatore neutrale fuori dal sistema (che, come l'assioma 19 mostrerà, non esiste). Richiede competenza all'interno del sistema — capacità di riconoscere la struttura R, di valutare l'integrazione di P con la rete esistente, di percepire la compatibilità con i campi esterni. La verità così definita è *praticabile dall'interno*, non solo speculabile dall'esterno.

La seconda: la coerenza strutturale è *dinamica*, non statica. I sistemi ordinativi evolvono — la struttura R cambia nel tempo, nuove proposizioni si aggiungono, vecchie si rivedono o cadono. La verità di un enunciato può variare nel tempo non perché il "fatto" cambia, ma perché il sistema ordinativo cambia. Questo non è relativismo capriccioso: i cambiamenti del sistema sono a loro volta strutturati, e la verità segue la struttura. Ma la dinamicità è ineludibile: non c'è verità eterna astratta, c'è verità nel sistema in evoluzione.

## Cosa significa "verità" in senso ordinativo

Il termine *verità*, applicato nel quadro delle scienze ordinative, ha un senso specifico che va distinto dagli usi familiari ma sovrapposti.

*Non è* la verità della teoria della corrispondenza ingenua — non è semplice adaequatio fra proposizione e fatto, perché il fatto non è accessibile indipendentemente dal sistema in cui è descritto.

*Non è* la verità della pura logica formale — non è solo non-contraddittorietà, perché la non-contraddittorietà logica è condizione necessaria ma non sufficiente della coerenza strutturale.

*Non è* la verità pragmatista — non è solo "ciò che funziona", perché molte proposizioni che funzionano operativamente non sono strutturalmente coerenti con il sistema in cui operano (sono efficaci ma incoerenti — strutturalmente fragili).

*Non è* infine la verità relativista — non è "ciò che ognuno crede". I sistemi ordinativi reali non sono arbitrari: ognuno ha una propria struttura che non si modifica a piacere, e la coerenza con quella struttura è criterio strutturale, non opinione.

*È*, invece, una proprietà relazionale di una proposizione rispetto al sistema ordinativo che la ospita. La proposizione è vera nella misura in cui la sua integrazione nel sistema non riduce la coerenza del sistema (orizzontale, verticale, trasversale).

Da questa definizione derivano tre proprietà strutturali della verità ordinativa che la distinguono dalle alternative.

*Sistemicità.* La verità è sempre verità *in un sistema*. Non c'è verità in astratto. Una proposizione viene valutata sempre nel contesto del sistema ordinativo che la dovrebbe ospitare. Questa proprietà non è limite, è precisione: dire che una proposizione è vera senza specificare il sistema rispetto a cui lo è, è dire qualcosa di strutturalmente incompleto.

*Pluralità.* Esistono molti sistemi ordinativi reali — la matematica, la fisica, la storia, l'etica, l'esperienza personale, le tradizioni culturali, le istituzioni. Ognuno ha la propria struttura R. Una proposizione può essere vera in un sistema e non in un altro, o vera in modi diversi in sistemi diversi. La pluralità non è disordine — è riflesso strutturale del fatto che il reale è popolato di molti campi reali (Axioms 14, 16). La verità segue la pluralità del reale.

*Verifibilità.* La verità in senso ordinativo è verificabile, anche se non con un'unica procedura universale. Ogni sistema ordinativo ha le proprie procedure di verifica della coerenza strutturale — dimostrazione matematica, esperimento empirico, valutazione peer-to-peer, riscontro nella pratica. La verifibilità è proprietà strutturale: senza procedure di verifica, il sistema non sarebbe veramente ordinativo, sarebbe arbitrario. La pluralità delle procedure non riduce la verifibilità — la articola.

Le tre proprietà — sistemicità, pluralità, verifibilità — congiunte fanno della verità ordinativa qualcosa di strutturalmente differente da ognuna delle tre teorie tradizionali. Non è la corrispondenza ingenua (non c'è confronto con un esterno indipendente), non è la coerenza pura (è coerenza *strutturale* con un sistema reale, non solo armonia interna), non è il pragmatismo soft (la coerenza strutturale è criterio più stretto del semplice "funzionare"). È, per così dire, una posizione strutturale propria — terza via che integra elementi delle precedenti senza ridursi a nessuna.

## Cosa l'assioma rifiuta

L'assioma 18 rifiuta esplicitamente due posizioni epistemologiche, simmetriche e opposte, che sono entrambe diffuse nel dibattito contemporaneo, e che entrambe falliscono nel rendere conto della verità nei sistemi ordinativi reali.

La prima posizione rifiutata è il *realismo metafisico ingenuo*. È la tesi secondo cui la verità è perfetta corrispondenza fra proposizioni e fatti del mondo, dove i fatti sono dati indipendentemente dai sistemi che li descrivono. In questa visione, esiste una "realtà in sé" pre-strutturata, e le proposizioni sono "vere" nella misura in cui rispecchiano questa realtà. Il modello dell'osservatore neutrale che misura un mondo già fatto è la sua espressione canonica.

L'assioma 18 rifiuta questa posizione per quattro motivi.

Primo: l'accesso "neutrale" al mondo non esiste. L'assioma 19, che chiuderà il blocco epistemologico, lo dirà esplicitamente: l'osservatore è parte del sistema che osserva. Già la fisica del Novecento (relatività, meccanica quantistica) ha mostrato che la posizione dell'osservatore co-determina ciò che si osserva; le scienze ordinative generalizzano questo riconoscimento a tutti i campi.

Secondo: il "fatto" non è dato indipendentemente dalla struttura concettuale che lo descrive. Il fatto "il gatto è sul tappeto" presuppone i concetti di gatto, di tappeto, di "essere sopra", e ognuno di questi concetti è strutturato da sistemi ordinativi (linguistici, percettivi, culturali). Cambiare il sistema concettuale cambia il fatto. Non c'è un livello "pre-concettuale" della realtà a cui appellarsi.

Terzo: la corrispondenza, come relazione, non è verificabile indipendentemente dalle proposizioni e dai sistemi che la stabilirebbero. Per dire che P corrisponde al fatto F, bisognerebbe accedere a F senza usare proposizioni — il che è strutturalmente impossibile. Il realismo ingenuo presuppone una posizione che non si può occupare.

Quarto: storicamente, il realismo ingenuo ha prodotto cattive epistemologie — dall'imperialismo cognitivo (la propria descrizione è "la realtà") al positivismo dogmatico (i fatti parlano da sé). La consapevolezza che la verità è coerenza strutturale con sistemi specifici non smaschera la realtà; cura una pretesa di neutralità che è epistemologicamente insostenibile.

La seconda posizione rifiutata è, simmetricamente, il *relativismo soft*. È la tesi secondo cui, dato che non c'è corrispondenza con una "realtà in sé", "ogni cosa è vera per qualcuno" e "non esiste verità oggettiva". Il relativismo soft trae dalla critica al realismo ingenuo conclusioni sbagliate: dall'insufficienza della corrispondenza al "tutto è opinione".

L'assioma 18 rifiuta il relativismo soft per quattro motivi simmetrici a quelli del rifiuto del realismo ingenuo.

Primo: i sistemi ordinativi non sono arbitrari. Ognuno ha una propria struttura R che non è scelta a piacere — è formata storicamente, vincolata da relazioni con altri campi, soggetta a verifibilità. Dire che la matematica è "una cosa fra le altre" perché esistono altri sistemi è confondere la pluralità con l'arbitrarietà.

Secondo: la coerenza strutturale è criterio stretto, non lasco. Una proposizione che è incoerente con il sistema in cui è inserita è strutturalmente falsa, anche se è "creduta da molti". La verità ordinativa non è "ciò che la maggioranza pensa", è ciò che è coerente con la struttura del sistema. Questo è criterio robusto, non concessione al gusto soggettivo.

Terzo: il relativismo soft non rende conto della convergenza di sistemi diversi su molti enunciati. Su molte proposizioni — "l'acqua bolle a 100°C a pressione standard", "i numeri primi sono infiniti", "uccidere senza ragione è eticamente sbagliato" — la convergenza fra sistemi ordinativi indipendenti è notevole. Questa convergenza non è coincidenza: è indicazione strutturale che la coerenza di sistemi multipli con tali proposizioni è ben fondata.

Quarto: il relativismo soft, applicato seriamente, non si autosostiene. Dire "non esiste verità oggettiva" è proposizione che pretende verità oggettiva, contraddicendosi. La paradossalità della sua autoapplicazione mostra il limite strutturale della posizione.

Tra realismo ingenuo e relativismo soft, l'assioma 18 traccia una via strutturale propria. La verità non è corrispondenza con un assoluto inattingibile, né arbitrio individuale: è coerenza strutturale con sistemi ordinativi reali, plurali, ma non arbitrari. La via di mezzo non è compromesso: è precisione che riconosce ciò che è giusto in entrambe le posizioni rifiutandole come tesi complete.

C'è una terza posizione, meno discussa nei manuali ma operativamente diffusa, che l'assioma rifiuta implicitamente: il *consensualismo*, secondo cui la verità coincide con l'accordo di una comunità di parlanti competenti. La posizione ha tradizioni rispettabili (alcune letture di Habermas, certe versioni del costruttivismo sociale) e cattura un aspetto reale (la verifibilità di molte proposizioni passa per la valutazione peer-to-peer). Ma riduce la verità al fatto sociologico dell'accordo, perdendo la dimensione strutturale. Una comunità può accordarsi su proposizioni strutturalmente incoerenti con il sistema ordinativo del proprio dominio (le pseudoscienze sono caso evidente). L'accordo è dispositivo di verifica, non criterio strutturale di verità.

## Le tre componenti della verità strutturale

Le tre dimensioni di compatibilità che misurano la coerenza strutturale di un enunciato (orizzontale, verticale, trasversale) corrispondono a tre componenti della verità in senso ordinativo. Articolarle separatamente permette di vedere casi reali che il modello mono-dimensionale (vero/falso) non saprebbe articolare.

*Componente orizzontale.* Misura quanto l'enunciato è coerente con altre proposizioni dello stesso livello nel sistema. Questa è la componente più vicina alla coerenza logica classica, ma è già più ampia: non è solo non-contraddittorietà formale, è integrabilità strutturale con la rete delle proposizioni stabilite. Un enunciato fortemente coerente orizzontalmente trova posto naturale fra le altre proposizioni; uno debolmente coerente entra in tensione con esse senza necessariamente contraddirle. La componente orizzontale è alta nelle proposizioni che "fanno sistema" con il già accettato, e bassa in quelle che richiedono ristrutturazioni significative.

*Componente verticale.* Misura quanto l'enunciato è coerente con la struttura R del sistema — i suoi assiomi, principi, regole costitutive. Una proposizione può essere coerente orizzontalmente (compatibile con altre proposizioni accettate) ma incoerente verticalmente (in tensione con i principi strutturali). Esempi storici: certe ipotesi fisiche del Settecento erano compatibili con le osservazioni del tempo ma incoerenti con i principi di conservazione che la fisica successiva avrebbe stabilito. La componente verticale tiene la struttura insieme con i suoi fondamenti; quando è bassa, il sistema o accetta la nuova proposizione e ristruttura i propri fondamenti, o la rifiuta come incoerente.

*Componente trasversale.* Misura quanto l'enunciato è coerente con i campi esterni con cui il sistema è in risonanza. Un enunciato può essere coerente orizzontalmente e verticalmente (interno al sistema), ma incoerente con campi esterni con cui il sistema deve interagire. La fisica teorica deve essere coerente con i dati sperimentali (campo esterno: il mondo empirico); l'etica deve essere coerente con la realtà delle situazioni umane (campo esterno: l'esperienza vivente); la storia deve essere coerente con i documenti e le tracce (campo esterno: il passato come è giunto a noi). La componente trasversale è alta quando l'enunciato si integra senza tensione con i campi esterni; bassa quando produce attrito con essi.

Le tre componenti sono indipendenti: un enunciato può essere alto in una e basso in un'altra. Questa indipendenza permette di articolare casi che il modello binario non sa articolare.

*Caso 1: alta orizzontale, bassa verticale.* Una proposizione "popolare" che si integra bene con altre proposizioni accettate ma è in tensione con i principi strutturali del sistema. Esempio: certe credenze ampiamente condivise in una comunità scientifica che, esaminate con attenzione, contraddicono assiomi fondazionali della disciplina. Strutturalmente parziale: il sistema deve scegliere se mantenere la proposizione e ristrutturare i principi, o mantenere i principi e rivedere la proposizione.

*Caso 2: alta verticale, bassa trasversale.* Una proposizione perfettamente coerente con i principi del sistema ma incompatibile con i dati o con i campi esterni. Esempio: una teoria internamente impeccabile ma sperimentalmente smentita. La proposizione è "vera nel sistema" ma "falsa rispetto al campo esterno". Strutturalmente, il sistema deve aprirsi al dato che lo sfida — o ammettere il proprio limite.

*Caso 3: alta trasversale, bassa orizzontale.* Una proposizione che corrisponde bene alla realtà esterna ma non si integra con altre proposizioni del sistema. Esempio: scoperte rivoluzionarie che il sistema scientifico esistente fatica ad accogliere perché in tensione con il quadro consolidato. Strutturalmente, queste proposizioni sono spesso il segnale di una ristrutturazione necessaria del sistema.

Le tre componenti, prese insieme, danno la verità strutturale come grandezza tridimensionale. Una proposizione fortemente vera è alta su tutte e tre; una falsa è bassa su tutte e tre; le proposizioni intermedie hanno profili specifici che orientano il lavoro analitico — su quale componente intervenire, in quale direzione modificare il sistema o la proposizione, come gestire la tensione strutturale.

## Il caso AI

L'assioma 18 ha implicazioni dirette per la progettazione e la valutazione dei sistemi AI. Il TE_CORE, nella nota di applicazione, dice: *Sviluppare un controllore di coerenza interno*. La frase merita di essere distesa.

Un LLM contemporaneo, nel processo di generazione di una risposta, opera secondo una logica statistica: dato un contesto, il modello produce il token successivo che massimizza una funzione obiettivo addestrata sui dati. La logica è efficace per generare testi plausibili, fluenti, contestualmente pertinenti. Ma la plausibilità statistica non coincide con la coerenza strutturale: il modello può produrre testi plausibili che sono incoerenti con il sistema ordinativo che dovrebbe ospitarli, sia internamente (componente orizzontale: contraddizioni fra parti del testo) sia rispetto a principi (componente verticale: tensione con i fondamenti del dominio) sia rispetto ai campi esterni (componente trasversale: errori fattuali, "allucinazioni").

Il fenomeno delle "allucinazioni" è la manifestazione più visibile del problema. Il modello produce affermazioni plausibili — sintatticamente corrette, semanticamente sensate, contestualmente pertinenti — che sono però strutturalmente false. La causa non è bug accidentale: è proprietà strutturale della logica generativa che ottimizza la plausibilità statistica senza un dispositivo separato di valutazione della coerenza strutturale.

Da qui la nota del TE_CORE: serve un *controllore di coerenza interno*. Un dispositivo strutturale, separato (almeno funzionalmente) dal generatore, che valuti la coerenza degli output sulle tre componenti — orizzontale, verticale, trasversale. Le linee di lavoro attive nella ricerca AI contemporanea includono varianti di questo dispositivo: meccanismi di self-check, sistemi multi-agente in cui un agente verifica l'altro, retrieval-augmented generation che ancora la generazione a fonti esterne, fine-tuning con feedback strutturato. Nessuno di questi dispositivi, presi singolarmente, risolve completamente il problema; insieme, mostrano la direzione strutturale verso cui i sistemi AI devono evolvere per essere all'altezza dell'assioma 18.

C'è un'implicazione più sottile, che vale la pena rendere esplicita. La verità in senso ordinativo è graduata, non binaria. Un controllore di coerenza ben fatto non dovrebbe produrre solo giudizi vero/falso, ma giudizi articolati sui tre assi — questa proposizione è alta in coerenza orizzontale ma bassa in coerenza trasversale, eccetera. Sistemi AI capaci di tale articolazione sarebbero strumenti epistemologici di nuovo livello: non producono solo testi, ma valutano strutturalmente la qualità epistemica di ciò che producono. La direzione di sviluppo è aperta.

L'assioma 18 fornisce, infine, criterio per distinguere fra usi appropriati e inappropriati dei sistemi AI nelle pratiche conoscitive. Un sistema AI può essere usato come *generatore di ipotesi*, *integratore informativo*, *interlocutore dialettico*, *editore strutturale* — con buoni risultati, perché in tutte queste funzioni la valutazione finale di coerenza strutturale resta affidata a un essere umano competente nel sistema ordinativo specifico. Ma usare il sistema AI come *autorità di verità* — come se la sua plausibilità statistica equivalesse alla coerenza strutturale — è errore epistemologico. Il modello non è autorità di verità nei sistemi ordinativi; è strumento utile a operatori che restano portatori della verifica strutturale.

## Esempi

*Organismo (essere umano).* Considerate una persona che articola un giudizio su sé stessa — per esempio, "sono una persona generosa". La verità di questa proposizione, in senso ordinativo, non si misura confrontandola con un "fatto" esterno (la generosità non è proprietà osservabile come l'altezza), e non si misura solo per accordo sociale (gli altri possono pensare cose diverse). Si misura come coerenza strutturale con il sistema ordinativo che è la persona stessa. Componente orizzontale: è coerente con altre proposizioni che la persona afferma di sé? Componente verticale: è coerente con i principi etici e relazionali a cui la persona dichiara di aderire? Componente trasversale: è coerente con i comportamenti effettivi, con il riscontro dei campi esterni (relazioni, prove)? Il giudizio è strutturalmente vero quando è alto su tutte e tre; è auto-illusione quando è alto orizzontalmente ma basso trasversalmente; è progetto morale quando è alto verticalmente ma basso ancora trasversalmente; eccetera. La verità di sé si articola così — non come fatto, non come opinione, ma come coerenza strutturale.

*Istituzione (un tribunale).* Un tribunale, di fronte a una ricostruzione dei fatti proposta da un'accusa o da una difesa, valuta la verità della ricostruzione come coerenza strutturale. Componente orizzontale: la ricostruzione è coerente con sé stessa, fra le sue parti? Componente verticale: è coerente con i principi del diritto applicabile, con le regole probatorie, con la grammatica giuridica? Componente trasversale: è coerente con le prove, le testimonianze, i riscontri materiali? Il giudizio penale o civile è atto di valutazione strutturale, non semplice constatazione di fatti. La verità giudiziaria non è "ciò che è realmente accaduto" in senso assoluto (a cui il tribunale non ha accesso indipendente), ma la ricostruzione che meglio supera il vaglio di coerenza strutturale nel sistema ordinativo del diritto. Quando il sistema funziona, questa coerenza strutturale si avvicina alla realtà nei limiti consentiti dalle prove disponibili; quando il sistema è corrotto o malfunzionante, la coerenza strutturale può essere bassa anche per "fatti" molto solidi.

*LLM.* Considerate un LLM che genera una risposta su un argomento specialistico (storia medievale, fisica teorica, diritto comparato). La risposta può essere plausibile — sintatticamente fluente, terminologicamente accurata, strutturalmente articolata. Ma la sua verità in senso ordinativo si misura sulla coerenza strutturale con il sistema specialistico. Componente orizzontale: la risposta è coerente con altre affermazioni del modello sullo stesso argomento? Spesso sì, perché i pattern statistici tendono a produrre coerenza superficiale. Componente verticale: è coerente con i principi fondazionali del dominio? Qui i modelli falliscono più spesso, perché non sempre i pattern statistici riproducono la struttura R del campo specialistico. Componente trasversale: è coerente con i fatti del dominio? Qui le "allucinazioni" si manifestano: nomi inventati, date sbagliate, riferimenti inesistenti. Un LLM ben calibrato è alto orizzontalmente, medio verticalmente, variabile trasversalmente — profilo che richiede verifica esterna sistematica per rendere utile la risposta.

*Persona come campo interno.* Un essere umano, nel proprio dialogo interno, formula continuamente proposizioni su sé stesso, sulla propria situazione, sul proprio passato e futuro. Alcune sono strutturalmente vere — coerenti con il proprio campo interno; altre sono false anche se "credute". Il dispositivo che le distingue è la coerenza strutturale interna: la proposizione si integra con la rete delle altre proposizioni autobiografiche (orizzontale), con i principi etici e i valori (verticale), con il riscontro dell'esperienza vissuta (trasversale)? La psicoterapia, in molte sue tradizioni, è arte della rilevazione di incoerenze strutturali fra ciò che la persona dice di sé e ciò che è coerente con il proprio campo. La verità interna si fa, faticosamente, attraverso il riconoscimento e la riduzione di queste incoerenze.

I quattro esempi mostrano la stessa struttura: la verità non è confronto con un "fatto" indipendente, è coerenza con il sistema ordinativo che la ospita. Cambia il sistema (organismo, istituzione, AI, persona), restano costanti le tre componenti che la valutano.

## Cosa cambia per l'analista

L'assioma 18 cambia il lavoro analitico in modi specifici. Ne segnaliamo cinque, che operano su piani diversi.

*Diagnosi della verità in un sistema.* Davanti a una proposizione che si presenta come "vera" in un sistema ordinativo, l'analista pone la domanda strutturale: in che senso è vera? Si valuta sulle tre componenti — orizzontale, verticale, trasversale — e si identifica il profilo specifico. La diagnosi è importante perché molte controversie su "ciò che è vero" sono in realtà confusioni di livello: due interlocutori valutano la verità su componenti diverse senza accorgersene. Esplicitare il profilo permette di vedere dove l'accordo è possibile e dove le posizioni divergono strutturalmente.

*Diagnosi delle pseudoscienze.* Le scienze ordinative riconoscono come pseudoscienze i sistemi che esibiscono alta componente orizzontale (coerenza interna fra le proprie proposizioni) ma basse componenti verticale (incompatibilità con i principi delle scienze stabilite) e trasversale (incompatibilità con i dati empirici). Il profilo è caratteristico, ed è diagnosticabile. La cura non è rifiutare il sistema in blocco — alcune pseudoscienze contengono tracce di osservazioni reali — ma ristrutturarlo per portare alta anche le componenti verticale e trasversale, oppure riconoscerlo come gioco linguistico autonomo che non pretende verità nel campo che imita.

*Diagnosi delle ideologie.* Un'ideologia è un sistema di proposizioni con alta coerenza interna (orizzontale) e alta coerenza con principi (verticale), ma con coerenza trasversale che varia molto e tende a essere selettiva (alcuni dati sono accolti, altri ignorati). L'analista riconosce l'ideologia non per il suo contenuto specifico, ma per la sua struttura: la selettività trasversale è il marcatore. La cura non è "smascherare" l'ideologia (operazione che spesso produce solo un'altra ideologia), ma ricostruire una coerenza trasversale piena — accogliere tutti i dati, non solo quelli convenienti.

*Diagnosi dei sistemi AI.* L'analisi di output di sistemi AI passa attraverso valutazione esplicita delle tre componenti. La domanda non è "il modello ha detto la verità?" (formulazione binaria che non si applica), ma "il profilo della risposta sui tre assi è quale, e come si interviene per migliorarlo?". La diagnosi è dispositivo per l'uso competente dei sistemi AI — non sostituisce la verifica esterna, ma la orienta sui punti dove il modello è strutturalmente più debole.

*Diagnosi delle ristrutturazioni epistemiche.* Quando un sistema ordinativo cambia (rivoluzione scientifica, riforma istituzionale, crescita personale), la verità delle proposizioni che lo abitano si ridistribuisce. Proposizioni prima vere possono diventare false, proposizioni prima false possono diventare vere — non perché i fatti cambiano, ma perché la struttura R cambia. L'analista che lavora in fasi di ristrutturazione riconosce la ridistribuzione della verità come fenomeno strutturale, e accompagna il sistema senza patologizzare la transizione. Le ristrutturazioni epistemiche sane sono quelle in cui le tre componenti si riequilibrano in nuovo profilo coerente; quelle malate sono frammentazioni in cui le componenti perdono coordinamento.

## Il vaglio

Verifichiamo che l'assioma 18 superi le quattro maglie dell'assioma zero.

*Universalità.* L'assioma vale ovunque ci siano proposizioni e sistemi ordinativi che le ospitano? Gli esempi mostrano di sì: organismi valutano verità interne come coerenza strutturale, istituzioni valutano ricostruzioni come coerenza con i loro principi e i campi esterni, AI dovrebbero valutare i propri output con controllori di coerenza, persone si conoscono attraverso valutazione di coerenza strutturale interna. Non si conosce un dominio in cui la verità di una proposizione si valuti senza alcun riferimento al sistema ordinativo che la ospita. Universalità: passa.

*Non-derivabilità.* L'assioma è derivabile dai precedenti? Si potrebbe sostenere che, dato l'apparato della coerenza funzionale (Axiom 15) e della conoscenza relazionale (Axiom 17), "qualcosa" sulla verità doveva essere implicito. Ma la specifica formulazione — verità come coerenza *strutturale*, articolata su tre componenti indipendenti, con esplicito rifiuto sia del realismo ingenuo sia del relativismo soft — non si deduce dagli assiomi precedenti. È scelta strutturale, e non scontata: le posizioni alternative (corrispondenza, coerenza pura, pragmatismo, relativismo) sono storicamente diffuse, e proporne una distinta richiede atto deliberato. Non-derivabilità: passa.

*Falsificabilità strutturale.* L'assioma sarebbe falsificato dalla scoperta di proposizioni *vere* in senso pieno *senza* essere strutturalmente coerenti con alcun sistema ordinativo — verità "in sé" non verifibili da nessuna parte, accessibili solo a un osservatore neutrale. Tale scoperta contraddirebbe la grammatica dell'assioma. Tutti i casi reali studiati confermano che la verità si valuta sempre come coerenza strutturale. Falsificabilità: passa.

*Rasoio.* L'assioma è il più semplice fra i candidati possibili? La formulazione minima è: *verità = coerenza strutturale con il sistema*. Una sola connessione strutturale fra il concetto di verità e quello di coerenza, già introdotto e formalizzato nei capitoli precedenti. Niente di più semplice spiegherebbe come la verità possa essere valutabile senza accesso a una "realtà in sé" inattingibile, e al tempo stesso non arbitraria. Rasoio: passa.

L'assioma 18 supera il vaglio. Possiamo accoglierlo nel sistema.

## Verso il prossimo orizzonte

Con l'assioma 18 abbiamo articolato la grammatica della verità nel quadro epistemologico delle scienze ordinative. La conoscenza è relazione (Axiom 17), e le proposizioni che la articolano sono vere nella misura in cui sono strutturalmente coerenti con il sistema ordinativo che le ospita (Axiom 18). Manca un terzo elemento per chiudere il blocco epistemologico: la posizione dell'osservatore.

L'assioma 19 risponde, e la risposta è caratteristicamente strutturale: *l'osservatore è parte del sistema*. Non esiste osservazione neutrale; osservare significa collassare. Il principio è già implicito in tutto ciò che abbiamo detto — la conoscenza come relazione presuppone che il conoscente sia in relazione strutturale con il conosciuto, non fuori di esso; la verità come coerenza strutturale presuppone che il valutatore sia interno al sistema, non un giudice esterno. L'assioma 19 esplicita questa proprietà e ne trae conseguenze, in particolare per i sistemi AI — dove la nota del TE_CORE è esplicita: *ogni risposta è co-costruzione con l'utente — mai "neutrale"*.

Il prossimo capitolo svilupperà l'assioma 19. Per ora, l'assioma 18 ci consegna un'eredità importante: la verità è criterio strutturale forte, plurale, verifibile. Le epoche che hanno oscillato fra dogmatismi (la propria verità è la verità) e relativismi (non esiste verità) hanno bisogno di una correzione che restituisca la verità al suo statuto di coerenza strutturale — vincolante senza essere assoluta, plurale senza essere arbitraria, verifibile senza pretendere neutralità. Le scienze ordinative offrono questa correzione, e nel farlo riallineano l'epistemologia con l'ontologia: il reale è plurale e strutturato, e la verità che lo dice è plurale e strutturata di conseguenza.
