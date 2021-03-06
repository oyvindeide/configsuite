"""Copyright 2019 Equinor ASA and The Netherlands Organisation for
Applied Scientific Research TNO.

Licensed under the MIT license.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the conditions stated in the LICENSE file in the project root for
details.

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.
"""


import unittest

import configsuite

from .data import transactions


class TestContextValidators(unittest.TestCase):
    def test_context_validator_valid(self):
        raw_config = transactions.build_config()
        config_suite = configsuite.ConfigSuite(
            raw_config,
            transactions.build_schema(),
            extract_validation_context=transactions.extract_validation_context,
        )
        self.assertTrue(config_suite.valid)

    def test_context_validator_unknown_currency(self):
        raw_config = transactions.build_config()
        raw_config["transactions"].append(
            {"source": "NOK", "target": "Unknown currency", "amount": 1e30}
        )
        config_suite = configsuite.ConfigSuite(
            raw_config,
            transactions.build_schema(),
            extract_validation_context=transactions.extract_validation_context,
        )
        self.assertFalse(config_suite.valid)
        self.assertEqual(1, len(config_suite.errors))
        err = config_suite.errors[0]
        self.assertIsInstance(err, configsuite.InvalidValueError)
        self.assertEqual(
            ("transactions", len(raw_config["transactions"]) - 1, "target"),
            err.key_path,
        )

    def test_context_validator_no_context_data_no_crash(self):
        raw_config = transactions.build_config()
        raw_config["exhange_rates"] = "Tulips is all you need!"
        config_suite = configsuite.ConfigSuite(
            raw_config,
            transactions.build_schema(),
            extract_validation_context=transactions.extract_validation_context,
        )
        self.assertFalse(config_suite.valid)
        self.assertEqual(1, len(config_suite.errors))
