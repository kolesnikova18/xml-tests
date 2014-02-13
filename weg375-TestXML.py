"""
# Name: William Gunn and Patrick Jackson
# ID: weg375, paj478
# Date Created: 8 Feb 2013
# Date Last Modified: 10 Feb 2013


#!/usr/bin/env python
"""


# -------
# imports
# -------


import StringIO
import unittest


from xml.etree.ElementTree import Element, fromstring
from XML import xml_solve, traverse, makeSearchStr
import XML


# -------
# TestXML
# -------


class TestXML (unittest.TestCase):
  # -------------
  # makeSearchStr
  # -------------


  def test_mkStr_1 (self):
    r = "<Test><Moo></Moo></Test>"
    key = fromstring(r)
    s = ".//" + str(key.tag)
    v = makeSearchStr(key, s)
    self.assert_(v == ".//Test/Moo/..")


  def test_mkStr_2 (self):
    r = "<Test><Moo></Moo><Cow></Cow></Test>"
    key = fromstring(r)
    s = ".//" + str(key.tag)
    v = makeSearchStr(key, s)
    self.assert_(v == ".//Test/Moo/../Cow/..")


  def test_mkStr_3 (self):
    r = "<Team><Dragon></Dragon><Cooly><Amber></Amber></Cooly><Ahyangyi><Will></Will><Teresa><Dingle></Dingle></Teresa></Ahyangyi></Team>"
    key = fromstring(r)
    s = ".//" + str(key.tag)
    v = makeSearchStr(key, s)
    self.assert_(v == ".//Team/Dragon/../Cooly/Amber/../../Ahyangyi/Will/../Teresa/Dingle/../../..")
   
  # ---------
  # xml_solve
  # ---------


  def test_solve_1 (self) :
    XML.position = 0 # Resets global position
    r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "2\n2\n7\n")

  def test_solve_2 (self) :
    XML.position = 0
    r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly><Dragon></Dragon></Team>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n7\n")

  def test_solve_3 (self) :
    XML.position = 0
    r = StringIO.StringIO('<color><red><blue><green></green></blue><purple><green></green></purple></red></color>\n<red><blue><green></green></blue><purple><green></green></purple></red>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n2\n")

  def test_solve_4 (self) :
    XML.position = 0
    r = StringIO.StringIO('<color><red><blue><red></red></blue><purple><green></green></purple></red></color>\n<red><blue><red></red></blue></red>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n2\n")

  def test_solve_5 (self) :
    XML.position = 0
    r = StringIO.StringIO('<Book><Author></Author><Author></Author></Book>\n<Author></Author>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "2\n2\n3\n")

  def test_solve_6 (self) :
    XML.position = 0
    r = StringIO.StringIO('<Dog><Dog></Dog></Dog>\n<Dog><Dog></Dog></Dog>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "1\n1\n")

  def test_solve_7 (self) :
    XML.position = 0
    r = StringIO.StringIO('<Dog></Dog>\n<Wolf></Wolf>')
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assertTrue(w.getvalue() == "0\n")

# ----
# main
# ----


print "TestXML.py"
unittest.main()
print "Done."

