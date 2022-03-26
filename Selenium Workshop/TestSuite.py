import unittest

import HtmlTestRunner

import Test_UNIT_BasicAuth
import Test_MultiTab


class TestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(Test_UNIT_BasicAuth.TestBasicAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_MultiTab.TestMultiTab)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="FirstTestReport",
            report_name="SmokeTest"
        )
        runner.run(smoke_test)
