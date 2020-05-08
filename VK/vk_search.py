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

    def enter_parameters(self, age_range: [], city_number: int, sex: int):
        self.params = {'age_min': age_range[0], 'age_max': age_range[1],
                       'location': city_number, 'pol': sex}
        return self.params

    def search(self):
        print(f"""Properties of search:
                location: {self.params['location']}\n
                age_range: {self.params['age_min']}-{self.params['age_max']}\n
                      sex: {self.params['pol']}\n
                """)
        min_vozr = self.params['age_min']
        max_vozr = self.params['age_max']
        city_number = self.params['location']
        sex = self.params['pol']
        while min_vozr <= max_vozr:
            month_number = 1
            result = self.vk.users.search(
                count=1000,
                fields='id, photo_max_orig, has_photo, last_seen, relation', city=city_number, sex=sex
            )
            month_number += 1
            print(result)
            # filtering












def main():
    obj = VkSearcher()
    obj.autorization('login.txt', 'pass.txt')
    obj.enter_parameters([20, 21], city_number=123, sex=1)
    obj.search()


if __name__ == '__main__':
    main()
