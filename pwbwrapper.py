import pywikibot
from pywikibot.exceptions import NoPage

class Item:
    """
    Class representing a single Wikidata item,
    identified using a unique Q-prefixed ID code.
    """

    def __init__(self, wd_inst, wd_id):
        """
        Creates an Item object.

        Keyword arguments:
        wd_inst -- a Wikidata instance (WD_Instance type)
        wd_id   -- a Q-prefixed Wikidata ID
        """
        self.item = pywikibot.ItemPage(wd_inst.repo, wd_id)
        self.item.get()

    def __str__(self):
        """Creates a string representation of this item."""
        return "[" + str(self.item.id) + " " + self.label() + "]"

    def claims(self):
        """Returns all of this item's claims."""
        return self.item.claims

    def has_claim(self, claim):
        """
        Checks if the item has a provided claim.

        Keyword arguments:
        claim   -- a P-prefixed claim ID
        """
        return claim in self.item.claims

    def instance_of(self, entity):
        """
        Returns whether or not this item is an 
        instance of (P31) the specified entity.

        Keyword arguments:
        entity  -- a Q-prefixed Wikidata ID
        """
        if self.has_claim("P31"):
            for claim in self.claim("P31"):
                if claim.getTarget().id == entity:
                    return True
        return False

    def subclass_of(self, entity):
        """
        Returns whether or not this item is a
        subclass of (P279) the specified entity.

        Keyword arguments:
        entity  -- a Q-prefixed Wikidata ID
        """
        if self.has_claim("P279"):
            for claim in self.claim("P279"):
                if claim.getTarget().id == entity:
                    return True
        return False

    def claim(self, claim):
        """
        Returns a claim of this item.

        Keyword arguments:
        claim   -- a P-prefixed claim to find
        """
        return self.item.claims[claim]

    def id(self, numeric=False):
        """
        Returns the Wikidata ID of this item.

        Keyword arguments:
        numeric -- whether to return an integer
                    id without a Q prefix (default False)
        """
        if numeric:
            return int(self.item.id[1:])
        return self.item.id

    def label(self):
        """Returns this item's singular label."""
        return self.item.get()['labels']['en']

    def aliases(self):
        """Returns a list of this item's aliases."""
        return self.item.get()['aliases']['en']

class WD_Instance:
    """
    Class representing a Wikidata instance.
    """

    def __init__(self):
        """Creates a Wikidata instance object."""
        site = pywikibot.Site("wikidata", "wikidata")
        self.repo = site.data_repository()

    def get_item(self, name):
        """
        Returns a Wikidata item based on the provided
        English name.

        Keyword arguments:
        name    -- an English name to search for
        """
        site = pywikibot.Site("en", "wikipedia")
        page = pywikibot.Page(site, name)
        try:
            item = pywikibot.ItemPage.fromPage(page)
            return Item(self, item.id)
        except NoPage:
            return None
        