import vk_api
import time
import codecs


timestamp = int(time.time())


class VkSearcher:

    def __init__(self, age_min, age_max, location_code, sex_1_or_2):
        self.catalogue = codecs.open('girls.html', 'w', encoding='utf8')

        self.catalogue = codecs.open('people.html', 'w', encoding='utf8')

        self.params = {'age_min': int(age_min), 'age_max': int(age_max),
                       'location': int(location_code), 'sex': int(sex_1_or_2)}

        self.login = VkSearcher.get_login('login.txt')
        self.password = VkSearcher.get_password('pass.txt')

    @staticmethod
    def get_login(login_file):
        with open(login_file) as login_file:
            login = login_file.readline().strip()
            return login

    @staticmethod
    def get_password(password_file):
        with open(password_file) as password_file:
            password = password_file.readline().strip()
            return password

    def make_session(self, login, password):
        self.vk_session = vk_api.VkApi(login, password)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()
        return self.vk

    def search(self):
        print(f"""Properties of search:
                location: {self.params['location']}\n
                age_range: {self.params['age_min']}-{self.params['age_max']}\n
                      sex: {self.params['sex']}\n
                """)
        min_vozr, max_vozr = self.params['age_min'], self.params['age_max']
        city_number, sex = self.params['location'], self.params['sex']
        while min_vozr < max_vozr:
            month_number = 1
            while month_number <= 12:
                result = self.vk.users.search(
                    count=10,
                    fields='id, photo_max_orig, has_photo, last_seen, relation',
                    city=city_number, sex=sex, age_from=min_vozr, age_to=min_vozr+1, birth_month=month_number)
                self.result_filter(result)
                month_number += 1
            min_vozr += 2

    def result_filter(self, result):
        for item in result['items']:
            if 'relation' in item and item['relation'] == 1 and item['has_photo'] and 'last_seen' in item:
                not_far = timestamp-int(item['last_seen']['time'])
                if not_far < 2592000:
                    info = '<a href="https://vk.com/id'+str(item['id']) + \
                           '" target="_blank" style="width: 302px; height: 302px;' \
                           'display: inline-block;"><div style="display: inline-block;' \
                           ' background: url('+str(item['photo_max_orig'])+');' \
                           ' width: 300px; height: 300px; background-size: cover; ' \
                           'background-position: center center;"></div></a>'+'\n'
                    self.write_to_catalogue(self.catalogue, info)
                    print('https://vk.com/id' + str(item['id']))

    @staticmethod
    def write_to_catalogue(catalogue, info):
        catalogue.write(info)
        return catalogue


def main():
    obj = VkSearcher(age_min=37, age_max=38, location_code=55, sex_1_or_2=1)
    obj.make_session(obj.login, obj.password)
    obj.search()


if __name__ == '__main__':
    main()
