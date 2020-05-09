import vk_api
import time
import codecs


timestamp = int(time.time())


class VkSearcher:

    def __init__(self):
        # self.catalogue = codecs.open('girls.html', 'w', encoding='utf8')
        self.autorization('login.txt', 'pass.txt')
        self.catalogue = codecs.open('girls.html', 'w', encoding='utf8')

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
        min_vozr, max_vozr = self.params['age_min'], self.params['age_max']
        city_number, sex = self.params['location'], self.params['pol']
        while min_vozr <= max_vozr:
            month_number = 1
            while month_number <=12:
                self.result = self.vk.users.search(
                    count=10,
                    fields='id, photo_max_orig, has_photo, last_seen, relation',
                    city=city_number, sex=sex, age_from=min_vozr, age_to=max_vozr, birth_month=month_number
                                            )
                self.result_filter(self.result)# filtering
                month_number += 1
            min_vozr += 1

    def result_filter(self, result):
        for item in result['items']:
            if 'relation' in item and item['relation'] == 0 and item['has_photo'] == True\
            and 'last_seen' in item:
                not_far = timestamp-int(item['last_seen']['time'])
                if not_far < 2592000:
                    info = '<a href="https://vk.com/id'+str(item['id'])+\
                           '" target="_blank" style="width: 302px; height: 302px;' \
                           'display: inline-block;"><div style="display: inline-block;' \
                           ' background: url('+str(item['photo_max_orig'])+');' \
                           ' width: 300px; height: 300px; background-size: cover; ' \
                           'background-position: center center;"></div></a>'+'\n'
                    self.write_to_catalogue(self.catalogue, info)
                    print('https://vk.com/id' + str(item['id']))

    def write_to_catalogue(self, catalogue, info):
        catalogue.write(info)
        return catalogue

def main():
    obj = VkSearcher()
    obj.enter_parameters([20, 21], city_number=123, sex=1)
    obj.search()


if __name__ == '__main__':
    main()
