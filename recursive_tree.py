#-*- coding: utf-8 -*-
# A simple acumulative recursive tree-like class
# Copyright (C) 2012  Thomaz de Oliveira dos Reis
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

class node(object):
    """ This is a tree node that adds all parent arguments
        adding or subtracting values as the child node changes
    """
    def __init__(self,name, parent=None, **meta):
        """ Set initial information as node name, meta
            paramenters (values exclusive to this node, not added on parent)
            and parent information
        """
        self.__innerset__(
            name=name,
            meta=meta,
            parent=parent,
            childs={},
            hooks=[],
        )

    def __setattr__(self, name, value):
        """ replaces default setattr, so all changes made to the object
            attributes would be applied recursively through parent nodes
        """
        self.set(**{name:value})
        
    def __innerset__(self, **attrs):
        """ As setattr has been changed, this method was created to 
            REALLY change this node values.
        """
        for attr,value in attrs.iteritems():
            object.__setattr__(self,attr,value)
    
    def __repr__(self):
        """ Better string representation of the object
        """
        return '<Node: %s Parent: %s Childs: %d>' %(self.name,self.parent,len(self.childs))
    
    def __str__(self):
        """ Returns the name for the string version of this node
        """
        return self.name

    def create_child(self,*names, **meta):
        """ Add child nodes with names informed in *names,
            and with meta information as in **meta
        """
        
        for name in names:  
            child = node(name, self, **meta)
            self.childs[name] = child

    def grand_childs(self,level=1):
        """ A generator capable of returning all
            grandchilds nodes of any level.
            level 0 = all childs
            level 1 = all childs of the childs
            level 2 = all childs of the chidls of the childs
            and goes on
        """
        for child in self.childs.itervalues():
            if level:
                for grandChild in child.grand_childs(level-1):
                    yield grandChild
            else:
                yield child
    
    def execute_hooks(self,**attrs):
        """ Run all hooks """
        for hook in self.hooks:
            hook(self,attrs)
    
    def set(self, **attrs):
        """ Update all object attributes in attrs.keys
            ***SETTING*** inner values with values informed 
            in attrs.values. if the informed attribute doesn't 
            exists, the attribute is created with value informed
            Also all hooks is called after setting all values
        """
        new_attrs = {}
        for attr,value in attrs.iteritems():
            new_attrs[attr] = value - getattr(self,attr) if hasattr(self,attr) else value
            self.__innerset__(**{attr:value})
        
        self.execute_hooks(**attrs)
        
        if self.parent:
            self.parent.add(**new_attrs)
    
    def add(self, **attrs):
        """ Update all object attributes in attrs.keys
            ***ADDING*** values informed in attrs.values
            if the informed attribute doesn't exists,
            the attribute is created with value informed
            Also all hooks is called after setting all values
        """
        
        for attr,value in attrs.iteritems():
            new_value = getattr(self,attr) + value if hasattr(self,attr) else value
            self.__innerset__(**{attr:new_value})
        
        self.execute_hooks(**attrs)
        
        if self.parent:
            self.parent.add(**attrs)
