from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTENT_PAGE = PROJECT_ROOT / "app" / "contenidos.html"
FEATURE_FILE = PROJECT_ROOT / "features" / "publicacion_contenido.feature"

scenarios(str(FEATURE_FILE))


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,1100")
    options.add_argument("--allow-file-access-from-files")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@given("que estoy en la gestión de contenidos de LENSEGUA")
def open_content_management(driver):
    driver.get(CONTENT_PAGE.as_uri())


@given(parsers.parse('que existe un contenido publicado titulado "{title}" en el módulo "{module}"'))
def create_published_content(driver, title, module):
    driver.get(CONTENT_PAGE.as_uri())
    Select(driver.find_element(By.ID, "module")).select_by_visible_text(module)
    driver.find_element(By.ID, "title").send_keys(title)
    driver.find_element(By.ID, "resource-url").send_keys("https://lensegua.local/recurso-validado.mp4")
    driver.find_element(By.ID, "reviewed").click()
    driver.find_element(By.ID, "publish").click()
    wait_for_message(driver, "Contenido publicado correctamente")


@when(parsers.parse('selecciono el módulo "{module}"'))
def select_module(driver, module):
    Select(driver.find_element(By.ID, "module")).select_by_visible_text(module)


@when(parsers.parse('ingreso el título "{title}"'))
def enter_title(driver, title):
    driver.find_element(By.ID, "title").send_keys(title)


@when(parsers.parse('ingreso el recurso "{resource}"'))
def enter_resource(driver, resource):
    driver.find_element(By.ID, "resource-url").send_keys(resource)


@when("confirmo que el material fue revisado")
def confirm_review(driver):
    driver.find_element(By.ID, "reviewed").click()


@when(parsers.parse('presiono el botón "{button_text}"'))
def press_button(driver, button_text):
    buttons = {
        "Guardar borrador": "save-draft",
        "Publicar contenido": "publish",
        "Desactivar contenido": "deactivate",
    }
    button = driver.find_element(By.ID, buttons[button_text])
    assert button.text == button_text
    button.click()


@then(parsers.parse('debería ver el mensaje "{expected_message}"'))
def verify_message(driver, expected_message):
    wait_for_message(driver, expected_message)
    assert driver.find_element(By.ID, "message").text == expected_message


@then(parsers.parse('el contenido debería tener el estado "{expected_status}"'))
def verify_status(driver, expected_status):
    status = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "content-status"))
    )
    assert status.text == expected_status


@then(parsers.parse('debería aparecer "{title}" en el portal estudiantil'))
def verify_student_content(driver, title):
    item = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "student-content"))
    )
    assert title in item.text


@then("el contenido no debería aparecer en el portal estudiantil")
def verify_no_student_content(driver):
    empty = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "student-empty"))
    )
    assert empty.text == "Sin contenidos disponibles"
    assert not driver.find_elements(By.ID, "student-content")


def wait_for_message(driver, expected_message):
    locator = (By.ID, "message")
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(locator, expected_message)
    )
