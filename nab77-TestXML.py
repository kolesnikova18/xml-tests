#Unit tests for project 2:XML
#Nathanael Bonney 2-10-14

"""
To test the program:
    % python TestXML.py > TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import XML

from xml.etree.ElementTree import Element, fromstring, tostring

# -------
# classes
# -------

class TestXML(unittest.TestCase):
  
# -------
# Test Functions
# -------

  #read
  def testRead1(self):
    sInput = StringIO.StringIO("<tag1><tag2></tag2></tag1><tag3></tag3>")
    x = XML.read(sInput)
    self.assert_(x is True)

  def testRead1(self):
    sInput = StringIO.StringIO("<xml><tag1><tag2></tag2></tag1><tag3></tag3></xml>")
    x = XML.read(sInput)
    self.assert_(x is False)

  def testRead2(self):
    sInput = StringIO.StringIO("")
    x = XML.read(sInput)
    self.assert_(x is False)

  def testRead3(self):
    sInput = StringIO.StringIO("Hello World")
    x = XML.read(sInput)
    self.assert_(x is False)

  #search
  def testSearch1(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='3'></tag4></tag3><tag5 id='4'></tag5></tag2>")
    searcher = fromstring("<tag3><tag4></tag4></tag3>")
    count, ids = XML.search(elem, searcher)
    self.assert_(count == 1)
    self.assert_(ids == [2])
    

  def testSearch2(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='3'></tag4></tag3><tag5 id='4'><tag4 id='5'></tag4></tag5></tag2>")
    searcher = fromstring("<tag4></tag4>")
    count, ids = XML.search(elem, searcher)
    self.assert_(count == 2)
    self.assert_(ids == [3, 5])

  def testSearch3(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='4'></tag4></tag3><tag5 id='3'><tag4 id='5'></tag4></tag5></tag2>")
    searcher = fromstring("<tag6></tag6>")
    count, ids = XML.search(elem, searcher)
    self.assert_(count == 0)
    self.assert_(ids == [])

  #checkChildren
  def testCheckChildren1(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='4'></tag4></tag3><tag5 id='3'><tag4 id='5'></tag4></tag5></tag2>")    
    searcher = fromstring("<xml><tag3><tag4></tag4></tag3></xml>")
    self.assert_(XML.checkChildren(elem, searcher) is True)

  def testCheckChildren2(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='4'></tag4></tag3><tag5 id='3'><tag4 id='5'></tag4></tag5></tag2>")    
    searcher = fromstring("<tag3><tag7></tag7></tag3>")
    self.assert_(XML.checkChildren(elem, searcher) is False)
    
  def testCheckChildren3(self):
    elem = fromstring("<tag2 id='1'><tag3 id='2'><tag4 id='4'></tag4></tag3><tag5 id='3'><tag4 id='5'></tag4></tag5></tag2>")    
    searcher = fromstring("<tag3></tag3>")
    self.assert_(XML.checkChildren(elem, searcher) is True)

  #solve
  def testSolve1(self):
    sInput = StringIO.StringIO("<tag1><tag2></tag2></tag1><tag3></tag3>")
    sOutput = StringIO.StringIO()
    XML.solve(sInput, sOutput)
    self.assert_(sOutput.getvalue() == "0\n")

  def testSolve2(self):
    sInput = StringIO.StringIO("<xml><tag1><tag2></tag2></tag1><tag3></tag3></xml>")
    sOutput = StringIO.StringIO()
    XML.solve(sInput, sOutput)
    self.assert_(sOutput.getvalue() == "Unexpected input encountered. Could not pharse XML.")

  def testSolve3(self):
    sInput = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
    sOutput = StringIO.StringIO()
    XML.solve(sInput, sOutput)
    self.assert_(sOutput.getvalue() == "2\n2\n7\n")
    

def main():
  print "TestXML.py"
  unittest.main()
  print "Done."

main()
