# pywikibot_wikidata_wrapper
Tools to make interfacing with Wikidata using pywikibot easier.

# Installation
`pip install pywikibot`

Include `user-config.py` and `user-password.py` in the same directory as your code (and update the `"username"` and `"password"` strings to match your Wikidata login.

# Sample
Downloadable as `github_sample.py`

```python
import pywikibot
import pwbwrapper
from pwbwrapper import Item, WD_Instance

wd = WD_Instance()

#
# Get items by name or identifier
#
website = wd.get("Website")
github = wd.get("GitHub")
earth = wd.get("Q2")

print(website)  # [Q35127 Website: set of related web pages served from a single web domain]
print(github)   # [Q364 GitHub: hosting service for software projects using Git]
print(earth)    # [Q2 Earth: third planet from the Sun in the Solar System]

#
# Compare relationships between items
#
print(github.instance_of(website))  # True
print(github.instance_of("Q35127")) # True
print(website.subclass_of(earth))   # False

#
# Parse structured information from items using properties
#
CAST_MEMBER = "P161"

bcs = wd.get("Better Call Saul")
bb = wd.get("Breaking Bad")

bcs_cast = bcs.get_claim_targets(CAST_MEMBER)
bb_cast = bb.get_claim_targets(CAST_MEMBER)

#Identify common cast members between the two shows
overlap = set(bcs_cast) & set(bb_cast)
for actor in overlap:
    print(actor)
    
# Output:
# [Q726142 Giancarlo Esposito: American film and television actor]
# [Q934506 Mark Margolis: American actor]
# [Q198638 Jonathan Banks: American actor]
# [Q888178 Bob Odenkirk: American actor, comedian, writer, director and producer]
```

# Provided structures
## Item
- `__init__(wd_inst, wd_id)`
  - Creates an **Item** object using a given Wikidata instance (**WD_Instance**) and entity ID.
- `claims()`
  - Returns all the claims associated with this item.
- `claim(claim)`
  - Returns the specified P-prefixed claim of this item.
- `has_claim(claim)`
  - Returns whether or not this item contains the specified claim.
- `id(numeric=False)`
  - Returns the ID of this item, default is Q-prefixed but can optionally be numeric.
- `desc()`
  - Returns the English description of this item.
- `label()`
  - Returns the label of this item.
- `aliases()`
  - Returns a list of aliases this item is known by.
- `subclass_of(entity)`
  - Returns whether or not this item is a subclass of the specified entity.
- `instance_of(entity)`
  - Returns whether or not this item is an instance of the specified entity.

## WD_Instance
- `__init__()`
  - Creates a WD_Instance object.
- `get_item(name)`
  - Returns an Item for the item identified by the English name provided.
