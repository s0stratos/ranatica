
# Annotation system for word order phenomena in latin

## Subordination

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
* complements of comparative or correlative *

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

## Coordination 

Limits of the conjuncts are indicated with ()
They can get a new line each and be aligned with each other especially if they are long

This includes:
* coordination with some conjunctions
* juxtaposition 

```
accepi tuas tris iam epistulas
    (unam a m cornelio [quam a tribus ei tabernis {ut opinor} dedisti])
    (alteram [quam mihi canusinus tuus hospes reddidit])
    (tertiam [quam {ut scribis} iam ora soluta de phaselo dedisti])
```

## Fronting

Unambiguously fronted elements can be marked with **

This includes:
- elements fronted before a left-periphery element (extracted constituent, conjunction) 
- initial nominal sentence element before subordinate clauses
- initial de topics
- left dislocation 

```
cesso [pultare ostium uicini]
    [*primum ex me* ut sciat [sibi filium redisse]]     
```

## Flattening 

When a subordinating verb feels to blend within its complement it can be annotated <>

Forms of esse which are not sentence final and not syncopated can be annotated with <> as well

## Right periphery elements

Right periphery elements such as elements appearing after a clause final verb can be annotated with _

It can be annotated with ~ instead if it forms a discontinuous constituent with a preceding element

## Correlatives

The announcing or resumptive element of a correlative can be marked $$
The correlative clause introduced is annotated with []

```
quiduis $potius$ [quam [quod cogitas]]    

($adeon$ [me ignauom] putas)
($adeon$ porro 
    [(ingratum) 
    (aut inhumanum) 
    (aut ferum)])
        [ut neque me consuetudo 
            (neque amor) 
            (neque pudor)
        commonueat 
            (neque commoneat)
                [ut seruem fidem]] 
```

## Incidental & Parenthetical Elements

Incidental & Parenthetical Elements can be annotated with {}

This includes:
* vocatives
* inquam, inquit
* comment-like expressions
* some adverbs

```
accepi tuas tris iam epistulas
    (unam a m cornelio [quam a tribus ei tabernis {ut opinor} dedisti])
    (alteram [quam mihi canusinus tuus hospes reddidit])
    (tertiam [quam {ut scribis} iam ora soluta de phaselo dedisti])
    
    {pro deum immortalium}
negat [phanium esse hanc sibi cognatam] _ demipho
*hanc* demipho negat [esse cognatam]    
```

# synthesis

| symbol | meaning                              |   |
|--------|--------------------------------------|---|
| []     | embedded clause                      |   |
| ()     | conjunct in coordination             |   |
| {}     | parenthetical/incidental element     |   |
| <>     | flattened clauses / non final 'esse' |   |
| **     | fronted/left periphery element       |   |
| $$     | correlative element                  |   |
| \_(\_) | right periphery element              |   |
| ~(~)   | right periphery element (tailing)    |   |
| «»     | other constituent (if interesting)   |   | 
| -      | new sentence (if ambiguous)          |   |