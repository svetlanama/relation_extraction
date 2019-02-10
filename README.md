# relation_extraction

### To Run 

```pip3 install textblob```

```python3 wordnet.py```


### Output example
```
TREE
hyperonymy is-a
[Synset('woody_plant.n.01')]
[Synset('plane_figure.n.01')]

meronymic part of
[Synset('burl.n.02'), Synset('crown.n.07'), Synset('limb.n.02'), Synset('stump.n.01'), Synset('trunk.n.01')]
```

```
TIME

hyperonymy is-a:
[Synset('case.n.01')]
[Synset('time_period.n.01')]
[Synset('time_period.n.01')]

meronymic part of
[]
```

```
SECOND
hyperonymy is-a:
[Synset('time_unit.n.01')]
[Synset('time.n.03')]
[Synset('position.n.09')]

meronymic part of
[Synset('millisecond.n.01')]

```

```
INTERVAL

hyperonymy is-a:
[Synset('measure.n.02')]
[Synset('set.n.02')]
[Synset('distance.n.01')]

meronymic part of
[]
```

