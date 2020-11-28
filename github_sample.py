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