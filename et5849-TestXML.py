#!/usr/bin/env python

# --------------------------------------
# cs327e-xml/XML/TestXML.py
# Adjustments made from Collatz skeleton
# James Gu & Elizabeth Tram
# ---------------------------------------

"""
To test the program:
  % python TestXML.py >& TestXML.out
  % chmod ugo+x TestXML.py
  % TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import XML
from xml.etree.ElementTree import Element, fromstring
from XML import read_XML, match_finder, traverse_tree, count_query, matching_pats, count_tree, write_XML_out
# ------------
# TestXML
# ------------

class TestXML (unittest.TestCase) :

    # -----
    # read
    # -----
    def test_read (self) :
        r = StringIO.StringIO("<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><Team><Cooly></Cooly></Team>")
        o = []
        i = read_XML(r, o)
        self.assertTrue (type(i) == list)
        self.assertTrue (type(j) == Element for j in i)

    def test_read2 (self) : # testing where query is not found in input
        r = StringIO.StringIO("<red><green></green></red><yellow></yellow>")
        o = []
        i = read_XML(r, o)
        self.assertTrue (type(i) == list)
        self.assertTrue (type(j) == Element for j in i)

    def test_read3 (self) : # testing with new lines case
        r = StringIO.StringIO("<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team><Team>\n<Cooly></Cooly>\n</Team>\n\n")
        o = []
        i = read_XML(r, o)
        self.assertTrue (type(i) == list)
        self.assertTrue (type(j) == Element for j in i)

    # -----------
    # count_query
    # -----------

    def test_count_query1 (self) :
        input1 = "<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>"
        tree = fromstring(input1) 
        XML.query_lst = []
        lengthQuery = count_query(tree)  
        self.assertTrue (lengthQuery == 4)
        self.assertTrue(lengthQuery == 4)    

    def test_count_query2 (self):
        input1 = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>"
        tree = fromstring(input1)
        XML.query_lst = []
        lengthQuery = count_query(tree)
        self.assertTrue (lengthQuery == 11)

    def test_count_query3 (self):
        input1 = "<Team></Team>"
        tree = fromstring(input1)
        XML.query_lst = []
        lengthQuery = count_query(tree)
        self.assertTrue(lengthQuery == 1)

    # ------------
    # match_finder
    # ------------
    
    def test_match_finder(self) :
        input1 = "<Team><Cooly></Cooly></Team>"
        tree = fromstring(input1)
        input2 = "<Team><Cooly></Cooly></Team>"
        pattern = fromstring(input2)
        match_finder(tree, pattern)
        self.assertTrue(XML.count[0] == 2)
        self.assertTrue(type(XML.count) == list)

    def test_match_finder2(self) :
        input1 = "<THU></THU>"
        tree = fromstring(input1)
        input2 = "<Team><Cooly></Cooly></Team>"
        pattern = fromstring(input2)
        match_finder(tree, pattern)
        self.assertTrue(XML.count[0] == 2)
        self.assertTrue(type(XML.count) == list)

    def test_match_finder3(self) :
        input1 = "<THU><Team><Cooly><Team><Cooly></Cooly></Team></Cooly></Team><Team><Cooly></Cooly></Team></THU>"
        tree = fromstring(input1)
        input2 = "<Team><Cooly></Cooly></Team>"
        pattern = fromstring(input2)
        match_finder(tree, pattern)
        self.assertTrue(XML.count[0] == 2)
        self.assertTrue(type(XML.count) == list)

 
    # ---------
    # traverse
    # ---------

    def test_traverse (self) : # this function doesnt return anything
        input1 = "<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>"
        input2 = "<Team><Cooly></Cooly></Team>"
        tree = fromstring(input1)
        query = fromstring(input2)
        root_query = query
        t = traverse_tree(tree, query, root_query)
        self.assertTrue (type(tree) == Element)
        self.assertTrue (type(query) == Element)
        self.assertTrue (type(root_query) == Element)

    def test_traverse2 (self) : # test where query is not found in input 
        input1 = "<red><green></green></red>"
        input2 = "<yellow></yellow>"
        tree = fromstring(input1)
        query = fromstring(input2)
        root_query = query
        t = traverse_tree(tree, query, root_query)
        self.assertTrue (type(tree) == Element)
        self.assertTrue (type(query) == Element)
        self.assertTrue (type(root_query) == Element)

    def test_traverse3 (self) : # test case with new lines 
        input1 = "<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n"
        input2 = "<Team><Cooly></Cooly></Team>\n\n"
        tree = fromstring(input1)
        query = fromstring(input2)
        root_query = query
        t = traverse_tree(tree, query, root_query)
        self.assertTrue (type(tree) == Element)
        self.assertTrue (type(query) == Element)
        self.assertTrue (type(root_query) == Element)
    
    # ----------
    # count_tree
    # ----------

    def test_count_tree (self) :
        input1 = "<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>"
        all_tree = []
        tree = fromstring(input1)
        count_tree(tree, all_tree)
        self.assertTrue (len(all_tree) == 4)
 
    def test_count_tree2 (self) :
        input1 = "<Team><Cooly></Cooly></Team>"
        all_tree = []
        tree = fromstring(input1)
        count_tree(tree, all_tree)
        self.assertTrue (len(all_tree) == 2)

    def test_count_tree3 (self) :
        input1 = "<Team><Cooly><Green><Red></Red></Green></Cooly><ACRush></ACRush><Jelly></Jelly></Team>"
        all_tree = []
        tree = fromstring(input1)
        count_tree(tree, all_tree)
        self.assertTrue (len(all_tree) == 6)

    # -----------------
    # matching patterns
    # -----------------

    def test_matching_pats(self) : 
        tree = fromstring("<Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>")
        query = fromstring("<Team><Cooly></Cooly></Team>")
        root_query = fromstring("<Team><Cooly></Cooly></Team>")
        all_tree = []
        count_tree(tree, all_tree)
        count_query(root_query)
        traverse_tree(tree, query, root_query)
        final = matching_pats(XML.count_pat, all_tree)
        self.assertTrue (type(final) == list)
        self.assertTrue (type(XML.count_pat) == list)
        self.assertTrue (type(i) == Element for i in XML.count_pat)
        self.assertTrue (type(all_tree) == list)
        self.assertTrue (type(i) == Element for i in all_tree)  

    def test_matching_pats2(self) : # testing case where there is no match
        tree = fromstring("<red><green></green></red>")
        query = fromstring("<yellow></yellow>")
        root_query = fromstring("<yellow></yellow>")
        all_tree = []
        count_tree(tree, all_tree)
        count_query(root_query)
        traverse_tree(tree, query, root_query)
        final = matching_pats(XML.count_pat, all_tree)
        self.assertTrue (type(final) == list)
        self.assertTrue (len(final) == 0)
        self.assertTrue (type(XML.count_pat) == list)
        self.assertTrue (type(i) == Element for i in XML.count_pat)
        self.assertTrue (type(all_tree) == list)
        self.assertTrue (type(i) == Element for i in all_tree)            

    def test_matching_pats3(self) : # testing case where there is new lines
        tree = fromstring("<red>\n<green>\n</green>\n</red>\n")
        query = fromstring("<yellow>\n</yellow>\n\n")
        root_query = fromstring("<yellow>\n</yellow>\n\n")
        all_tree = []
        count_tree(tree, all_tree)
        count_query(root_query)
        traverse_tree(tree, query, root_query)
        final = matching_pats(XML.count_pat, all_tree)
        self.assertTrue (type(final) == list)
        self.assertTrue (len(final) == 0)
        self.assertTrue (type(XML.count_pat) == list)
        self.assertTrue (type(i) == Element for i in XML.count_pat)
        self.assertTrue (type(all_tree) == list)
        self.assertTrue (type(i) == Element for i in all_tree)                

    # --------------
    # write_XML_out
    # --------------

    def test_write_XML_out(self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        XML.count_pat = []
        XML.count = [0]
        XML.query_lst = []
        XML.count_q = []
        write_XML_out(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n\n")

    def test_write_XML_out2(self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly><Foo></Foo></Team>")
        w = StringIO.StringIO()
        XML.count_pat = []
        XML.count = [0]
        XML.query_lst = []
        XML.count_q = []
        write_XML_out(r, w)
        self.assertTrue(w.getvalue() == "0\n\n")

    def test_write_XML_out3(self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        w = StringIO.StringIO()
        XML.count_pat = []
        XML.count = [0]
        XML.query_lst = []
        XML.count_q = []
        write_XML_out(r, w)
        self.assertTrue(w.getvalue() == "1\n1\n\n")

print("TestXML.py")
unittest.main()
print("Done.")
