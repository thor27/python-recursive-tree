python-recursive-tree
=====================

About
-----

A simple acumulative recursive tree-like class.
With this tree-like class, all child values will be automatically added to the parent attribute with the same name

You can also add meta information which is exclusive for the specific node, without changing anything on the parent node
And add hooks on the nodes, so you can execute special codes each time the hooked node is updated.

Example Usage
-------------

Basic Usage

```
>>> from recursive_tree import node
>>> brasil = node('Brasil')
>>> brasil.create_child('minas gerais','rio de janeiro','sao paulo','distrito federal')
>>> brasil.childs['minas gerais'].create_child('juiz de fora', 'belo horizonte')
>>> brasil.childs['rio de janeiro'].create_child('rio de janeiro', 'petropolis')
>>> brasil.childs['sao paulo'].create_child('sao paulo', 'campinas')
>>> brasil.childs['distrito federal'].create_child('brasilia')
>>> brasil.childs['minas gerais'].childs['juiz de fora'].population = 517872
>>> brasil.childs['minas gerais'].childs['belo horizonte'].population = 2375444
>>> brasil.childs['rio de janeiro'].childs['rio de janeiro'].population = 6323037
>>> brasil.childs['rio de janeiro'].childs['petropolis'].population = 296044
>>> brasil.childs['sao paulo'].childs['sao paulo'].population = 11316149
>>> brasil.childs['sao paulo'].childs['campinas'].population = 1088611
>>> brasil.childs['distrito federal'].childs['brasilia'].population = 2562963
>>> brasil.childs['minas gerais'].population
2893316
>>> brasil.childs['rio de janeiro'].population
6619081
>>> brasil.childs['sao paulo'].population
12404760
>>> brasil.childs['distrito federal'].population
2562963
>>> brasil.population
24480120
>>> 
```

Meta Attributes

```
>>> brasil.childs['rio de janeiro'].childs['rio de janeiro'].meta['capital'] = True
>>> brasil.childs['rio de janeiro'].childs['petropolis'].meta['capital'] = False
>>> brasil.childs['rio de janeiro'].childs['rio de janeiro'].meta
{'capital': True}
>>> brasil.childs['rio de janeiro'].childs['petropolis'].meta
{'capital': False}
>>> brasil.childs['rio de janeiro'].meta
{}
>>> brasil.meta
{}
```

Hooks

```
>>> brasil.childs['rio de janeiro'].childs['petropolis'].population
296044
>>> brasil.childs['rio de janeiro'].childs['petropolis'].area = 5801937
>>> 
>>> def density_hook(object, updated_attrs):
...     if not 'area' in updated_attrs.keys() and not 'population' in updated_attrs.keys():
...         return
...     object.density = object.population / float(object.area)
... 
>>> brasil.childs['rio de janeiro'].childs['petropolis'].hooks.append(density_hook)
>>> brasil.childs['rio de janeiro'].childs['petropolis'].population += 1
>>> brasil.childs['rio de janeiro'].childs['petropolis'].density
0.05102520072175896
>>> brasil.childs['rio de janeiro'].childs['petropolis'].population += 10000
>>> brasil.childs['rio de janeiro'].childs['petropolis'].density
0.05274876304241152
>>> brasil.childs['rio de janeiro'].childs['petropolis'].population += 100000
>>> brasil.childs['rio de janeiro'].childs['petropolis'].density
0.06998438624893721
```

Grand Childs

```
>>> cities = brasil.grand_childs()
>>> cities
<generator object grand_childs at 0x7f7920785230>
>>> [city for city in cities]
[<Node: brasilia Parent: distrito federal Childs: 0>, <Node: sao paulo Parent: sao paulo Childs: 0>, <Node: campinas Parent: sao paulo Childs: 0>, <Node: rio de janeiro Parent: rio de janeiro Childs: 0>, <Node: petropolis Parent: rio de janeiro Childs: 0>, <Node: belo horizonte Parent: minas gerais Childs: 0>, <Node: juiz de fora Parent: minas gerais Childs: 0>]
>>> brasil.childs['distrito federal'].childs['brasilia'].create_child('asa norte','asa sul','taguatinga','guara')
>>> places = brasil.grand_childs(2)
>>> [place for place in places]
[<Node: asa sul Parent: brasilia Childs: 0>, <Node: asa norte Parent: brasilia Childs: 0>, <Node: taguatinga Parent: brasilia Childs: 0>, <Node: guara Parent: brasilia Childs: 0>]
```
