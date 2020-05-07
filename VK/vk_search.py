import vk_api, time
import codecs
import os, sys, shutil, requests
import os.path

timestamp = int(time.time())


class VkSearcher():

    def autorization(self, login_file: str, password_file: str):
        with open(login_file) as login_file:
            login = login_file.readline().strip()

        with open(password_file) as password_file:
            password = password_file.readline().strip()

        print(login, ':', password)
        # if login and password: ...
        self.vk_session = vk_api.VkApi(login, password)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()
        return self.vk

    def enter_parameters(self, age_range: [], city_number: int, psex: int):
        self.params = {'age_min': age_range[0], 'age_max': age_range[1],
                  'location': city_number, 'pol': psex}
        return self.params


def main():
    obj = VkSearcher()
    obj.autorization('login.txt', 'pass.txt')
    obj.enter_parameters([20, 21], city_number=123, psex=1)


if __name__ == '__main__':
    main()
