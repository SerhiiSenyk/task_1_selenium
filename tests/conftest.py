import pytest
import time
from source.driver.driver import Driver

@pytest.fixture(scope="session")
def browser():
    driver = Driver()
    yield driver
    time.sleep(3)
    driver.quit()