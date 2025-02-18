# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


class TextToHexConverter:

    # This class will implement a simple functiom that takes a text value and converts it to the hex value

    def convert_hex(self, text: str) -> str:

        return text.encode('utf-8').hex()
        # Very simple implementation since python already has the encode function

