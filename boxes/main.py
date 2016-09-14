
import unittest

class Boxes:

    # Returns integer, the minimum number of boxes needed to hold a given number of items
    # large boxes take 5 items
    # small boxes take only one item
    # every box must be completely full
    @staticmethod
    def minimalNumberOfBoxes(products, availableLargeBoxes, availableSmallBoxes):

    	qtd_large_boxes = 0
    	qtd_small_boxes = 0
    	resto = products

    	qtd_large_boxes = products / 5

    	if qtd_large_boxes > availableLargeBoxes:
    		qtd_large_boxes = availableLargeBoxes
    	
    	resto -= qtd_large_boxes * 5

    	if availableSmallBoxes > 0:
    		if resto <= availableSmallBoxes:
    			qtd_small_boxes = resto
    		else:
    			qtd_small_boxes = availableSmallBoxes

    		resto -= qtd_small_boxes

    	if resto == 0:
    		return qtd_large_boxes + qtd_small_boxes
    	else:
    		return -1
    		
    	

#print(Boxes.minimalNumberOfBoxes(16, 2, 10))


class TestBoxes(unittest.TestCase):
	def test_no_boxes(self):
		self.assertEqual(Boxes.minimalNumberOfBoxes(16,0,0),-1)

	def test_no_small_boxes(self):
		self.assertEqual(Boxes.minimalNumberOfBoxes(16,2,0),-1)
		self.assertEqual(Boxes.minimalNumberOfBoxes(16,5,0),-1)
		self.assertEqual(Boxes.minimalNumberOfBoxes(15,4,0),3)
		self.assertEqual(Boxes.minimalNumberOfBoxes(15,3,0),3)

	def test_no_large_boxes(self):
		self.assertEqual(Boxes.minimalNumberOfBoxes(12,0,5),-1)
		self.assertEqual(Boxes.minimalNumberOfBoxes(12,0,13),12)
		self.assertEqual(Boxes.minimalNumberOfBoxes(12,0,12),12)

	def test_no_few_small_produtcs(self):
		self.assertEqual(Boxes.minimalNumberOfBoxes(4,1,3),-1)
		self.assertEqual(Boxes.minimalNumberOfBoxes(4,1,4),4)
		self.assertEqual(Boxes.minimalNumberOfBoxes(5,1,3),1)
		self.assertEqual(Boxes.minimalNumberOfBoxes(5,0,6),5)

		
		


if __name__ == '__main__':
	unittest.main()