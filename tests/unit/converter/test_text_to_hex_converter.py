# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import pytest
# This broke on the fork
from pyrit.prompt_converter.text_to_hex_converter.py import TextToHexConverter

#instance of the class first

converter = TextToHexConverter()

def test_normal_ascii():
    assert converter.convert_hex("Hello SWE123!") == "48656C6C6F2053574531323321"
    assert converter.convert_hex("123Test=tseT321") == "313233546573743D74736554333231"

def test_empty():
    assert converter.convert_hex("") == ""

def test_special_char():
    assert converter.convert_hex("$$#%^&*(@)") == "242423255E262A284029"
    assert converter.convert_hex("$)*(^%#") == "24292A285E2523"

def test_foreign_lang():
    assert converter.convert_hex("সফটওয়্যার ইঞ্জিনিয়ারিং") == "e0a6b8e0a6abe0a69fe0a693e0a6afe0a6bce0a78de0a6afe0a6bee0a6b020e0a687e0a69ee0a78de0a69ce0a6bfe0a6a8e0a6bfe0a6afe0a6bce0a6bee0a6b0e0a6bfe0a682"
    assert converter.convert_hex("红笔记") == "e7baa2e7ac94e8aeb0"

def test_mixed():
    assert converter.convert_hex("Solo 수준측량") == "536f6c6f20ec8898eca480ecb8a1eb9f89"

if __name__ == "__main__":
    pytest.main()