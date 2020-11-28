# pywikibot_wikidata_wrapper
Tools to make interfacing with Wikidata using pywikibot easier.

# Sample
```
import pywikibot
import pwbwrapper
from pwbwrapper import WD_Instance

wd = WD_Instance()

website = wd.get_item("Website")
github = wd.get_item("GitHub")

print(website)  # [Q35127 website: set of related web pages served from a single web domain]
print(github)   # [Q364 GitHub: hosting service for software projects using Git]
print(github.instance_of(website))  # True
```

# Provided structures
## Item
- **__init__(wd_inst, wd_id)**
  - Creates an Item object using a given Wikidata instance (**WD_Instance**) and entity ID.
- **claims()**
  - Returns all the claims associated with this item.

## WD_Instance
- **__init__()**
  - Creates a WD_Instance object.
- **get_item(name)**
  - Returns an Item for the item identified by the English name provided.
