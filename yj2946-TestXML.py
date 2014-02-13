#!/usr/bin/env python3

# -------------------------------
# projects/xml/XML.py
# Copyright (C) 2014
# Al Jin and Kevin Boening
# -------------------------------

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestXML.py
% TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import io
import unittest

import XML
from xml.etree.ElementTree import fromstring, tostring

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat><cat><dog><bird></bird></dog></cat>")
        b, c = XML.xml_read(r)
        self.assertTrue(tostring(b,encoding='unicode') == tostring(fromstring("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat>"),encoding='unicode'))
        self.assertTrue(tostring(c,encoding='unicode') == tostring(fromstring("<cat><dog><bird></bird></dog></cat>"),encoding='unicode'))

    def test_read_2(self) :
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        b, c = XML.xml_read(r)
        self.assertTrue(tostring(b, encoding = 'unicode') == tostring(fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>"),encoding='unicode'))
        self.assertTrue(tostring(c, encoding = 'unicode') == tostring(fromstring("<Team><Cooly></Cooly></Team>"),encoding='unicode'))

    def test_read_3(self) :
        r = io.StringIO("<red><green><blue></blue><yellow></yellow></green></red><red><green></green></red>")
        b, c = XML.xml_read(r)
        self.assertTrue(tostring(b, encoding = 'unicode') == tostring(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"),encoding = 'unicode'))
        self.assertTrue(tostring(c, encoding = 'unicode') == tostring(fromstring("<red><green></green></red>"),encoding = 'unicode'))

    # ----
    # find
    # ----

    def test_find_1 (self) :	
        my_list = [0]
        XML.xml_find(fromstring("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat>"), fromstring("<cat><dog><bird></bird></dog></cat>"), my_list)
        self.assertTrue(my_list == [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_find_2 (self) :
        my_list = [0]
        XML.xml_find(fromstring("<red><green><blue></blue><yellow></yellow></green></red>"),fromstring("<Team></Team>"), my_list)
        self.assertTrue(my_list == [0,0,0,0,0])

    def test_find_3 (self) :
        my_list = [0]
        XML.xml_find(fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>"), fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>"), my_list)
        self.assertTrue(my_list == [0,1,0,0,0,0,0,0,0,0,0,0])
        
    # ----
    # match_gen
    # ----

    def test_match_gen_1 (self) :
        x = fromstring("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat>")
        l = list(fromstring("<cat><dog><bird></bird></dog></cat>"))
        v = XML.xml_match_gen(x,l)
        self.assertTrue(v == 1)

    def test_match_gen_2 (self) :
        x = fromstring("<Cooly><Amber><Team></Team></Amber></Cooly>")
        l = list(fromstring("<Cooly><Team></Team></Cooly>"))
        v = XML.xml_match_gen(x,l)
        self.assertTrue(v == -1)

    def test_match_gen_3 (self) :
        x = fromstring("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat>")
        l = list(fromstring("<chicken><goose></goose></chicken>"))
        v = XML.xml_match_gen(x,l)
        self.assertTrue(v == -1)

    # -----
    # match_allchild
    # -----

    def test_match_allchild_1 (self) :
        self.assertTrue(XML.xml_match_allchild(fromstring("<cat><dog></dog></cat>"), [fromstring("<dog></dog>")]))

    def test_match_allchild_2 (self) :
        self.assertTrue(not XML.xml_match_allchild(fromstring("<Team></Team>"), [fromstring("<Cooly></Cooly>")]))

    def test_match_allchild_3 (self) :
        self.assertTrue(not XML.xml_match_allchild(fromstring("<Team><Amber><Cooly><Carl></Carl></Cooly></Amber></Team>"), [fromstring("<Carl></Carl>")]))

    # -----
    # track
    # -----
    def test_track_1 (self) :
        b, c = XML.xml_track([0, 1, 2])
        self.assertTrue(b == 2)
        self.assertTrue(c == [1, 2])

    def test_track_2 (self) :
        b, c = XML.xml_track([0, 5, 7, 9, 13])
        self.assertTrue(b == 4)
        self.assertTrue(c == [1, 2, 3, 4])

    def test_track_3 (self) :
        b, c = XML.xml_track([0])
        self.assertTrue(b == 0)
        self.assertTrue(c == [])

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO("")
        XML.xml_print(w, 2, [2, 7])
        self.assertTrue(w.getvalue() == "2\n2\n7\n")

    def test_print_2 (self) :
        w = io.StringIO("")
        XML.xml_print(w, 0, [])
        self.assertTrue(w.getvalue() == "0\n")

    def test_print_3 (self) :
        w = io.StringIO("")
        XML.xml_print(w, 1, [5])
        self.assertTrue(w.getvalue() == "1\n5\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat><cat><dog><bird></bird></dog></cat>")
        w = io.StringIO("")
        XML.xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n1\n")

    def test_solve_2 (self) :
        r = io.StringIO("<cat><dog><bird><rat></rat></bird><chicken><goose></goose></chicken><egg></egg></dog><toy><car><race></race></car><computer><keyboard></keyboard></computer><monitor><mouse><pad></pad></mouse></monitor></toy></cat><cat><mouse><monitor></monitor></mouse></cat>")
        w = io.StringIO("")
        XML.xml_solve(r,w)
        self.assertTrue(w.getvalue() == "0\n")

    def test_solve_3 (self) :
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = io.StringIO("")
        XML.xml_solve(r,w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
