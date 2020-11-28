# pywikibot_wikidata_wrapper
Tools to make interfacing with Wikidata using pywikibot easier.

# Sample
```python
import pywikibot
import pwbwrapper
from pwbwrapper import WD_Instance

wd = WD_Instance()

website = wd.get_item("Website")
github = wd.get_item("GitHub")

print(website)  # [Q35127 Website: set of related web pages served from a single web domain]
print(github)   # [Q364 GitHub: hosting service for software projects using Git]

print(github.instance_of(website))  # True
print(github.instance_of("Q35127")) # True
```

# Provided structures
## Item
- **__init__(wd_inst, wd_id)**
  - Creates an Item object using a given Wikidata instance (**WD_Instance**) and entity ID.
- **claims()**
  - Returns all the claims associated with this item.
- **claim(claim)**
  - Returns the specified P-prefixed claim of this item.
- **has_claim(claim)**
  - Returns whether or not this item contains the specified claim.
- **id(numeric=False)**
  - Returns the ID of this item, default is Q-prefixed but can optionally be numeric.
- **desc()**
  - Returns the English description of this item.
- **label()**
  - Returns the label of this item.
- **aliases()**
  - Returns a list of aliases this item is known by.
- **subclass_of(entity)**
  - Returns whether or not this item is a subclass of the specified entity.
- **instance_of(entity)**
  - Returns whether or not this item is an instance of the specified entity.

## WD_Instance
- **__init__()**
  - Creates a WD_Instance object.
- **get_item(name)**
  - Returns an Item for the item identified by the English name provided.
