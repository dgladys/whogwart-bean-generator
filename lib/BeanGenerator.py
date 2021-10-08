import requests
import time


class BeanGenerator:
    def __init__(self, url):
        self.url = url
        self.login_uri = 'index_x.php'
        self.draw_bean_uri = 'losuj_fasolke.php'

    def generate(self, person, count):
        s = requests.Session()

        s.post(self.url + self.login_uri, {
            "login": person.get_login(),
            "password": person.get_password()
        })

        for i in range(count):
            print("   * Losowanie fasolki nr. %d" % (i+1))
            s.post(self.url + self.draw_bean_uri, {"robotest": ""})
            time.sleep(0.5)
