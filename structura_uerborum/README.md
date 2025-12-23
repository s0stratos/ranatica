
# Annotation system for word order phenomena in latin

## Goal 

The annotation system presented here has the following goals :

 - being **less ambiguous** than other punctuation systems for latin.
 - making **reading faster** and easier (once you get used to the system).
 - helping **visualize and conceptualize word order phenomena** in latin.
 - generating the **least false ambiguity as possible** with annotations.

The annotation system is compatible with different ways of presenting the text.
Either preserving lines (verses for instance) or presenting the text following
the annotations to further improve the visual effect.

```
[sī quisquamst
    [quī placēre sē <studeat> bonīs quam plūrumīs
    (et minumē multōs laedere)]]
*in hīs* «poēta hic» nōmen profitētur ~ suom

[*tum* sīquis est
    [quī dictum in sē inclēmentius <exīstumāuit> esse]]
*sīc* exsīstumet 
    [respōnsum (nōn dictum) esse
        [quia laesit prior
            [quī [bene uortendō
                 (et eāsdem scrībendō male)]
             ex graecīs bonīs latīnās fēcit ~ nōn bonās]]]

īdem menandrī pasma nunc nūper dedit
(atque in tēsaurō scrīpsit
    [caussam dīcere $prius$ [unde petitur] [*aurum* quā rē sit ~ suom]]
    [quam illic [quī petit] [unde is sit tēsaurus sibi
                            (aut unde in patrium monumentum peruēnerit)]])
```                            

or preserving verses:

```
[sī quisquamst [quī placēre sē <studeat> bonīs 
quam plūrumīs (et minumē multōs laedere)]]
*in hīs* «poēta hic» nōmen profitētur ~ suom.
[*tum* sīquis est [quī dictum in sē inclēmentius 
<exīstumāuit> esse]] *sīc* exsīstumet 
[respōnsum (nōn dictum) esse [quia laesit prior
[quī [bene uortendō (et eāsdem scrībendō male)]
ex graecīs bonīs latīnās fēcit ~ nōn bonās.]]]
īdem menandrī pasma nunc nūper dedit
(atque in tēsaurō scrīpsit [caussam dīcere 
$prius$ [unde petitur] [*aurum* quā rē sit ~ suom]]
[quam illic [quī petit] [unde is sit tēsaurus sibi
(aut unde in patrium monumentum peruēnerit.)]])
```

**Remark:** the symbol stacks at the end of segments are a 
side effect of using paired symbols all the time. some people may find this distracting
and prefer a general "forward symbol" like `:` or no symbol at the end of sentence yielding :

```
[sī quisquamst
    [quī placēre sē <studeat> bonīs quam plūrumīs
    (et minumē multōs laedere):
*in hīs* «poēta hic» nōmen profitētur ~ suom.

[*tum* sīquis est
    [quī dictum in sē inclēmentius <exīstumāuit> esse:
*sīc* exsīstumet 
    [respōnsum (nōn dictum) esse
        [quia laesit prior
            [quī [bene uortendō
                 (et eāsdem scrībendō male)]
             ex graecīs bonīs latīnās fēcit ~ nōn bonās.

īdem menandrī pasma nunc nūper dedit
(atque in tēsaurō scrīpsit
    [caussam dīcere $prius$ [unde petitur] [*aurum* quā rē sit ~ suom]]
    [quam illic [quī petit] [unde is sit tēsaurus sibi
                            (aut unde in patrium monumentum peruēnerit.
```                   

or

```
[sī quisquamst [quī placēre sē <studeat> bonīs 
quam plūrumīs (et minumē multōs laedere):
*in hīs* «poēta hic» nōmen profitētur ~ suom.
[*tum* sīquis est [quī dictum in sē inclēmentius 
<exīstumāuit> esse: *sīc* exsīstumet 
[respōnsum (nōn dictum) esse [quia laesit prior
[quī [bene uortendō (et eāsdem scrībendō male)]
ex graecīs bonīs latīnās fēcit ~ nōn bonās.
īdem menandrī pasma nunc nūper dedit
(atque in tēsaurō scrīpsit [caussam dīcere 
$prius$ [unde petitur] [*aurum* quā rē sit ~ suom]]
[quam illic [quī petit] [unde is sit tēsaurus sibi
(aut unde in patrium monumentum peruēnerit.
```

Since its easier to derive the second from the first (although not fully trivial),
the annotations provided here are for now using the full opening/closing symbols.

At this point you may wonder why latin needs such a system in the first place when
standard punctuation systems are the norm. latin makes an active use of 
word order in a way that gives a more 'spoken language' flavor to many texts, 
which is perfectly clear once you recognize it. it makes «fast reading especially» quite hard
because you must infer structure and word order _from meaning_ as you go ~~from meaning~~.
(see what I did there :D). not being latin speakers, 
nor having access to intonation, modern readers have a harder time anticipating patterns
or spotting some structural phenomena, which is the very point of this annotation system.

The system is of course fully compatible with many punctuation symbols like : `.!?,;:` 
although some information will be quite redundant. Remember this is a tool which can be tweaked
to personal preferences.

## Word order and structural annotation

There are the phenomena covered by the annotation system.
They are detailed enough to help both with structural overview of the
text and observing and learning word order phenomena in latin.


| symbol | meaning                                       | category   |
|--------|-----------------------------------------------|------------|
| []     | embedded clause                               | structural |
| ()     | conjunct in coordination                      | structural |
| {}     | parenthetical/incidental element              | structural |                                                                           |
| <>     | flattened clauses / non final 'esse'          | word order |                                                                          |
| **     | fronted/left periphery element                | word order |                                                                         |
| $$     | correlative element                           | structural |
| ::::   | connectors and pronoun stack (if interesting) | word order |
| _      | right periphery element                       | word order |                                                                       
| ~      | right periphery element (tailing)             | word order |                                                                      |
| «»     | other constituent (if interesting)            | structural |                                                                      
| -      | new sentence (if ambiguous)                   | structural |                                                                    

## Embedded clauses []

Embedded clauses are annotated with []
They can get a new line and be indented to show structure visually especially if they are long

This includes:
* finite embedded clauses in the indicative
* finite embedded clauses in the subjunctive
* infinitive embedded clauses
* -tum supine embedded clauses
* -tu supine embedded clauses
* gerund embedded clauses
* gerundive embedded clauses
* ablative absolute clauses
* clausal or fragmentary complements of comparative or correlative

```
rogitas
    [quid siet]

sed uereor
    [ne mulier [me absente] hic corrupta sit]
    
cesso [pultare ostium uicini]
    [*primum ex me* ut sciat [sibi filium redisse]] 
    
    [quod editis] 
nihil est
-   [si uultis [quod cacetis]] 
copia est    
        
```

## Conjuncts in Coordination ()

Limits of the conjuncts are indicated with ()
They can get a new line each and be aligned with each other especially if they are long

This includes:
* coordination with some conjunctions
* juxtaposition 

```
accepi tuas tris iam epistulas
    (unam a m. cornelio [quam a tribus ei tabernis {ut opinor} dedisti])
    (alteram [quam mihi canusinus tuus hospes reddidit])
    (tertiam [quam {ut scribis} iam ora soluta de phaselo dedisti])
```

## Incidental & Parenthetical Elements {}

Incidental & Parenthetical Elements can be annotated with {}

This includes:
* vocatives
* incidental verbs or clauses
* comment-like (parenthetical) clauses interrupting another statement
* some incidental adverbs

```
accepi tuas tris iam epistulas
    (unam a m cornelio [quam a tribus ei tabernis {ut opinor} dedisti])
    (alteram [quam mihi canusinus tuus hospes reddidit])
    (tertiam [quam {ut scribis} iam ora soluta de phaselo dedisti])
    
    {pro deum immortalium}
negat [phanium esse hanc sibi cognatam] _ demipho
*hanc* demipho <negat> esse cognatam.
```

## Clause domain "flattening" / Non-post-predicate esse <>

This annotates cases where the subordinating verb appears in the
middle of its clausal complement. This actually happens quite
frequently in latin especially when the subordinating verb has
no other complement or if its other complements are not at risk
of being interpreted as part of its complement.

These clauses cannot be annotated with series of brackets because
elements of the complement are discontinuous. 

`nunc ea propter me <cupis> concidere`

```
[ut *uos* «in uostris <uoltis> mercimoniis
emundis (uendundisque)» «me laetum» lucris afficere]
```

Forms of esse which do not appear finally after their predicative complement
can be annotated with <> as well.

`*quibus epistulis* <sum> equidem abs te lacessitus [ad rescribendum]
    (sed $idcirco$ <sum> tardior
        [quod non inuenio _ fidelem tabellarium])`

Those cases cannot satisfactorily be annotated with _ or ~ after the 
head verb. We didn't find useful to use this annotation for 
non-clausal or non-predicative complement. Those are annotated with _ or ~
when post-verbal.

## Fronting / Left periphery **

Unambiguously fronted elements can be marked with **. This is one of the most 'ambiguous' symbol.
Its aim it to signal when something is fronted because it's significantly prominent (topical, focused). 
I typically don't use it for clauses or QU words. I also typically don't use it for sentence initial subjects.
The idea is to use it as a cue that something "interesting" is happening.

This includes:
- elements fronted before a left-periphery element (extracted constituent, conjunction) 
- initial nominal sentence element before subordinate clauses
- initial de topics
- left dislocation 

```
cesso [pultare ostium uicini]
    [*primum ex me* ut sciat [sibi filium redisse]]     
```

`*hanc* demipho negat [<esse> cognatam].`

`*terram* caue [cariosam tractes].`

## Correlatives $$

The announcing element of a correlative pair can be marked $$.

```
quiduis $potius$ [quam [quod cogitas]].    

($adeon$ [me ignauom] putas)
($adeon$ porro 
    [(ingratum) 
    (aut inhumanum) 
    (aut ferum)])
        [ut neque me :::: consuetudo 
            (neque amor) 
            (neque pudor)
        commoueat 
        (neque commoneat)
            [ut seruem _ fidem]].
```

## Connectors and pronoun stack ::::

Latin has a strong tendency to group sentence connectors and pronouns early in clauses.
This symbol comes after that group as a way to make it visually salient. It doesn't
assist with faster reading or disambiguation but it's an added reinforcement tool to
learn proper word order.

```
nunc te :::: obsequentem (atque hilarem) <dixi> praebeas.
```
```
[si ille haec :::: nunc <sentit> facere _ illi satis]
uis quanta illius mors <sit> maceries _ tibi
```

Because of its nature, the pronoun stack is good evidence than a verb
preceding it is fronted in the way imperative verbs often are.

```
*uideō* egō tē :::: {mulier} more multārum ūtier
[ut uim contendās ~ tuam _ ad maiestatem uirī].
```

## Right periphery elements _ and ~

Right periphery elements such as elements appearing after a clause final verb can be annotated with _.
In fact this is pretty much the criterion I use. Anything after the verb which is not a clause gets the
_ symbol whatever the exact reason why it is after the verb. This prevents too many assumptions and
leaves the reader with a clear visual cue this is post-verbal/right periphery without forcing interpretation
as linked to topic/focus or other things.

```
    {pro deum immortalium}
negat [phanium <esse> hanc sibi cognatam] _ demipho.

*hanc* demipho negat [<esse> cognatam].
```

It can be annotated with ~ instead if it forms a "discontinuous constituent" with a preceding element.

`*in hīs* «poēta hic» nōmen profitētur ~ suom.`

`ex graecīs bonīs latīnās fēcit ~ nōn bonās.`

## Other constituents/groups «»

This symbol is to help regrouping elements when you think it can help readers. 
I would use it sparingly. The goal is not to have a dependency tree but a readable text.

`*in hīs* «poēta hic» nōmen profitētur ~ suom.`

## New Sentence symbol - 

This symbol can be useful if you don't use any sentence-end punctuation symbol or if you don't trust `.` alone 
become it can be other things like an abbreviation symbol.

```
    [quod editis] 
nihil est
-   [si uultis [quod cacetis]]
copia est    
```

as alternative or complement to :

```
    [quod editis] 
nihil est.
    [si uultis [quod cacetis]]
copia est    

```
## Common annotation dilemmas

Many annotation dilemmas has to do with the use of ** 
and its interaction with other annotations.

### Initial verbs with complements

`interdixi tibi de medicis.`

There are three options here.

**Option 1**: Apply the usual logic to complements.
`interdixi _ tibi de medicis.`

**Option 2**: Apply the usual logic to complements and mark the verb as fronted.
`*interdixi* _ tibi de medicis.`

**Option 3**: Mark the verb as fronted and lose the usual mark for post-verbal complements
`*interdixi* tibi de medicis.`

I would recommend the most coherence possible for such cases but there may be cases when 
marking the verb may feel more or less interesting. Option 1 is interesting to minimize
interpretation on the part of the annotator. Option 2/3 are interesting to attract 
attention on that verb placement.

### Initial adverbs

### Initial subordinate clauses



## Conclusion

As you can see, it's not easy to evacuate alternative annotation completely.
But my own use of the system has been a satisfactory experience in spite of
the occasional change of annotation or missed symbol here and there.
