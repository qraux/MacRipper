# -*- coding: utf-8 -*-
import unittest
import logging
from modules.spotlight.base_spotlight import *


class TestBaseSpotlight(unittest.TestCase):

    def test_convert_to_array(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        spotlight = BaseSpotlight("/",'/tmp/', "Asia/Tokyo",logger)
        
        file_path = "/Applications/Mock.app"
        data = {}
        spotlight.add_optional_attribute(data, file_path)
        
        attrs =  [
            "FilePath",
            "kMDItemUseCount",
            "kMDItemLastUsedDate",
            "kMDItemUsedDates"
        ]
        spotlight.convert_to_array(data, attrs)


if __name__ == "__main__":
    unittest.main()
