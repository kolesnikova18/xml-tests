#!/usr/bin/env python3
# -------------------------------
# Project 2/XML/TestXML.py
# Author: Roberto Salinas, Xiaoqin LI
# -------------------------------

"""
To test the program:
    % python3 TestXML.py > TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py > TestXML.out
"""

# -------
# imports
# -------

import io
import unittest

from XML import xmlRead, xmlPrint, xmlSolve, xmleval, get_Target_String
from xml.etree.ElementTree import Element, fromstring

# ------------------------
# TestCollatz
# 19 unit tests in total
# ------------------------

class TestXML (unittest.TestCase) :
    # ---------------------------------------------------
    # xmlread fuction test with corner test, 4 in total
    # ---------------------------------------------------

    def test_read_1 (self) :
	#added new line delimiter
        r = io.StringIO("<THU>\n<team>\n</team>\n</THU>")
        b = xmlRead(r)
        self.assertTrue(b == "<xml><THU>\n<team>\n</team>\n</THU></xml>")

    def test_read_2 (self) :
	#added content to tag
        r = io.StringIO("<a>dog</a>")
        b = xmlRead(r)
        self.assertTrue(b == "<xml><a>dog</a></xml>")

    def test_read_3 (self) :
	#Added tab delimiter
        r = io.StringIO("<a><b>\t<c></c></b>\t</a>")
        b = xmlRead(r)
        self.assertTrue(b == "<xml><a><b>\t<c></c></b>\t</a></xml>")
      
    def test_read_4 (self) :
        #Added White Space
        r = io.StringIO("<a><b>  </b>   </a><c></c>")   
        b = xmlRead(r)
        self.assertTrue(b == "<xml><a><b>  </b>   </a><c></c></xml>")

    # -------------------------------------------------------
    # collatz_eval fuction test with corner test, 6 in total
    # -------------------------------------------------------

    def test_eval_1 (self) :
        # Test source string from SPOJ
        a = fromstring("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>" \
                       +"<JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon>"\
                       +"<Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        b = fromstring("<Team><Cooly></Cooly></Team>")  
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [2,2,7])
    
    def test_eval_2 (self) :
        # Query tree have more than 2 layers
        a = fromstring("<a><b><c></c><d><f></f></d></b></a>")  
        b = fromstring("<b><d><f></f></d></b>")
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [1,2])

    def test_eval_3 (self) :
        # Query tree does not exist in source tree
        a = fromstring("<a><b><c></c><d></d></b></a>")  
        b = fromstring("<b><e></e></b>")
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [0])

    def test_eval_4 (self) :
        a = fromstring("<a><c><f></f></c><c><d><e></e></d><f></f></c><g><h><c><f></f></c></h></g></a>")  
        b = fromstring("<c><f></f></c>")
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [3,2,4,10])

    def test_eval_5 (self) :
        # children in query tree have siblings
        a = fromstring("<a><c><f></f><h></h></c><c><d><e></e></d><f></f><h></h></c>"\
                       +"<g><h><c><f></f><h><i></i></h></c></h></g></a>")  
        b = fromstring("<c><f></f><h></h></c>")
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [3,2,5,12])
        
    def test_eval_6 (self) :
        # query tree is on top root
        a = fromstring("<a><c><f></f><h></h></c><c><d><e></e></d><f></f><h></h></c>"\
                       +"<g><h><c><f></f><h><i></i></h></c></h></g></a>")  
        b = fromstring("<a><c><f></f></c></a>")
        v = xmleval(a,b)
        print (str(v))
        self.assertTrue(v == [1,1])

    # --------------------------------------
    # xmlprint fuction test, 3 in total
    # --------------------------------------

    def test_print_1 (self) :
        w = io.StringIO()
        xmlPrint(w, [0])
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "0\n\n")

    def test_print_2 (self) :
        w = io.StringIO()
        xmlPrint(w, [2,2,7])
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "2\n2\n7\n\n")

    def test_print_3 (self) :
        w = io.StringIO()
        xmlPrint(w, [4,9,13,15])
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "4\n9\n13\n15\n\n")

    # ------------------------------------------------------------
    # get_Target_String fuction test with coner test, 3 in total
    # ------------------------------------------------------------

    def test_getString_1 (self) :
        # Query tree have more than 1 layer1
        a = fromstring("<b><d><c></c></d></b>")
        v = get_Target_String(a, ".//")
        print (str(v))
        self.assertTrue(v == ".//b/d/c/../..")

    def test_getString_2 (self) :
        # children in query tree have siblings
        a = fromstring("<a><b><c></c><d></d></b></a>")
        v = get_Target_String(a, ".//")
        print (str(v))
        self.assertTrue(v == ".//a/b/c/../d/../..")

    def test_getString_3 (self) :
        # no child on query tree
        a = fromstring("<a></a>")
        v = get_Target_String(a, ".//")
        print (str(v))
        self.assertTrue(v == ".//a")
            
    # ---------------------------------------
    # xmlSolve fuction test, 3 in total
    # ---------------------------------------

    def test_solve_1 (self) :
        # Test source string from SPOJ
        r = io.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>" \
                        "<JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber>" \
                        +"</Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = io.StringIO()
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "2\n2\n7\n\n")
     
    def test_solve_2(self) :
        r = io.StringIO("<a><b><c></c><d></d></b></a><b><d></d></b>")
        w = io.StringIO()
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "1\n2\n\n")

    def test_sovle_3(self) :
        r = io.StringIO("<a><c><f></f></c><c><d><e></e></d><f></f></c><g><h><c><f></f></c></h></g></a><c><f></f></c>")
        w = io.StringIO()
        xmlSolve(r, w)
        self.assertTrue(w.getvalue() == "3\n2\n4\n10\n\n")

# ----
# main
# ----

print("TestXML.py")
print()
unittest.main()


