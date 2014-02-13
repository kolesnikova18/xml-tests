#!/usr/bin/env python

"""
To test the program:
    % python TestXML.py > TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py > TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest
from xml.etree.ElementTree import fromstring


from XML import xml_match, xml_find, xml_solve

# -----------
# TestXML
# -----------

class TestXML(unittest.TestCase) :
    # ----
    # match
    # ----

    # Normal test
    def test_match_1(self) :
        b = xml_match(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"), fromstring("<red><green></green></red>"))
        self.assertTrue(b == True)

    # Corner test- node does not match
    def test_match_2 (self) :
        b = xml_match(fromstring("<color><blue></blue><yellow></yellow></color>"), fromstring("<red><green></green></red>"))
        self.assertTrue(b == False)
        
    # Corner test- pattern does not match
    def test_match_3 (self) :
        b = xml_match(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"), fromstring("<red><blue></blue></red>"))
        self.assertTrue(b == False)


    # ----
    # find
    # ----
    
    # Normal test #1
    def test_find_1 (self) :
        v = xml_find(fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>"), fromstring("<Team><Cooly></Cooly></Team>"))
        self.assertTrue(v == [2,7])

    # Normal test #2
    def test_find_2 (self) :
        v = xml_find(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"), fromstring("<green><yellow></yellow><blue></blue></green>"))
        self.assertTrue(v == [2])

    # Corner test- pattern not found
    def test_find_3 (self) :
        v = xml_find(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"), fromstring("<green><purple></purple></green>"))
        self.assertTrue(v == [])
        

    # -----
    # solve
    # -----


    # Normal test- two results
    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n")

    # Normal test- one result
    def test_solve_2 (self) :
        r = StringIO.StringIO("<red><green><blue></blue><yellow></yellow></green></red><green><yellow></yellow><blue></blue></green>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n2\n")

    # Corner test- pattern not found
    def test_solve_3 (self) :
        r = StringIO.StringIO("<red><green><blue></blue><yellow></yellow></green></red><green><purple></purple></green>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "0\n")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
