"""Test the application module"""
import asyncio
import os
import unittest
from pathlib import Path


from common.app import application_entrypoint, terminate
from actor.app.app import Application
from actor.config import config

test_fun_called = asyncio.Future()  # The test will run until this future set


async def test_fun(app):
    """test case implementation"""
    app.logger.info("test_fun called")
    test_fun_called.set_result(None)


class TestApplication(Application):
    """
    The TestApplication class
    Completely inherits the original Application class, except it extends that with a `jobs()` member function for testing purposes.
    It makes possible to start a complete application, run tests and terminate it at the end of the tests.
    """

    async def jobs(self):
        """
        A fake jobs function
        It will be executed after the `start()` period is completed.
        This function may hold the testing logic, including the evaluation of test results.
        When the tests are completed, it has to call the `terminate()` function.
        """
        self.logger.info("jobs called")
        # Call the implementation of test logic

        await test_fun(self)
        # Wait for the completion of tests, and evaluate the results
        await asyncio.wait_for(test_fun_called, 1)

        # Terminate the application
        terminate()


class ApplicationTestCase(unittest.IsolatedAsyncioTestCase):
    "The Application test cases"

    def test_application_start_stop(self) -> None:
        """Test the starting and stopping of an application"""
        application_entrypoint(TestApplication, config, argv=[])
        result = True
        self.assertTrue(result)
