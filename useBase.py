from seleniumbase import BaseCase



class MyTestCase(BaseCase):
    def test_something(self):
        self.open("https://www.smzdm.com/")
        self.type("input[id='J_search_input']","冰箱\n")
        self.assert_title("冰箱_综合_什么值得买")



if __name__ == '__main__':
    BaseCase.main()
