import random
from seleniumbase import sb_cdp


def test_client_support_cdp():
    sb = sb_cdp.Chrome()

    try:
        sb.goto("https://yaroslavl.lemanapro.ru/")
        sb.sleep(random.uniform(2, 4))
        menu_selector = 'button[data-qa="header-menu"]'
        sb.wait_for_element_visible(menu_selector, timeout=15)
        sb.click(menu_selector)
        sb.sleep(random.uniform(1, 2.5))

        support_selector = "//a[contains(text(), 'Клиентская поддержка')]"
        sb.wait_for_element_visible(support_selector, timeout=15)
        sb.click(support_selector)

        sb.assert_url_contains("/company/obratnaya-svyaz/")

        sb.assert_text("Клиентская поддержка", selector="html", timeout=10)

        print("✅ Тест пройден успешно в режиме CDP!")

    finally:
        sb.quit()