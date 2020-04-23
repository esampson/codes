# Chronicles of Darkness Evennia Support <img src="https://github.com/esampson/codes/blob/master/web/static_overrides/website/images/evennia_logo.png" width=100>
Character support code for Chronicles of Darkness running under Evennia.

This project is heavily inspired by Thenomain's nWoD character support system:
https://github.com/thenomain/nWoDCG

## Core Concept

At its heart the idea is to use a bunch of small 'scriptlet' objects to represent the various stats. 'Strength' is one, 'Brawl' is another, and 'Pipes of the Beastcaller' is a third.

The various types of stats (e.g. Merits, Contracts, Attributes, Skills) are represented by different typeclasses. This means that whenever something about a stat needs to be determined the basic idea is to identify the script object that corresponds to the stat in question and then access its methods and attributes. To determine if someone meets the prerequisites for a given stat a call is made to the stat's `meets_prereqs()` method with the character in question and what they want to purchase being passed. The script itself then returns an answer as to whether the character can make the purchase.

This means that rather than having a long piece of hardcode examining stats to determine various details and handling methods each individual attribute type has more compact scripts dedicated to their particular requirements. When a new type of stat needs to be introduced a new typeclass is created for it with its particular methods requiring no modifications to the base code and preventing the breaking of operational systems.

## Implementation

All scripts have the following methods:

* `get(<target>, <entry>[, <subentry>])`: Returns the current value of the stat on the target.
* `meets_prereqs(<target>[, <value>][, <subentry>])`: Determines if someone meets the prerequisites to make a purchase.
* `cost(<target>, <value>[, <subentry>])`: Returns the cost for the target to purchase the stat to a given level.
* `set(<target>, <value>[, <subentry>])`: Sets the attribute to a given value on the target. In some cases specific values may clear the attribute.

Accessing a particular stat is done by first making a call to the `find()` method in codes.data with the format of `find(<entry>[,<statclass>])`. Because this function may be indirectely called by players in various situations such as rolling dice, proving a stat, or requesting info `<entry>` works via partial matching. The is why `find('str')` will return the scrripts for Strength, Streetwise, Street Fighting, and Striking Looks. To help narrow the list and to deal with naming conflicts `<statclass>` may be used to narrow the search. `find('str','skill')` would only return the script object for Streetwise.

`find()` works by querying a small script of `typeclasses.scripts.dictionaryScript` that contains a look up table of all partial name matches. This look up table is rebuilt every time the server is reloaded.

There are 6 different typeclasses of stat scripts used by all or nearly all characters:

* advantageScripts: Handle advantages such as Initiative, Speed, and Health
* attributeScripts: Handle attributes such as Strength or Presence
* skillScripts: Handle skills such as Brawl or Streetwise
* meritScripts: Handle merits such as Resources or Contacts
* sphereScripts: Handle miscellaneous sphere specific stats such as kith or tribe
* basicStatScripts: Handle miscellaneous stats such as character concept.

In addition all major templates access a `powerStatScript`.

At present there are 16 other scripts to handle the various characteristics exclusive to each sphere such as contracts, disciplines, gifts, and rites.

## Installation ##

Relatively simply modifications need to be made to typeclasses.scripts. 

Additionally, to ease programming and reduce load it is suggested that modifications to typeclass.characters be made so that the 34 most commonly queried stats (attributes, skills, and character template ) can be queried directly from the character object via commands such as `<target>.strength()`, `<target>.animal_ken()` or `<target>.template()`. These methods do not support any other functionality such as telling programs how much it will cost to raise the stat in question. Additionally character objects possess `get()` and `meets_prereqs()` methods. These function largely as a combination of the `find()` and `get()` method under codes.data or the `find()` and `meets_prereqs()` methods under codes.data and the located script. The exception is that they must find only a single stat script or they will abort.

Finally `@py from codes.statInit import initStats` will generate a bunch of initial scripts
