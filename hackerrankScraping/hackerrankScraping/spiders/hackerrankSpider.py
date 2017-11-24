import scrapy


class HackerrankSpider(scrapy.Spider):
    name = 'hackerrank'
    start_urls = ['http://www.hackerrank.com/login']
    handle_httpstatus_list = [400]

    def parse(self, response):
        print('type of response is', len(response.text))
        form = {'login': 'abidkhan484', 'password': 'myPassword'}
        # formxpath = "//input[@data-attr2='Login']"
        return [scrapy.FormRequest.from_response(response,
                                                 formdata=form,
                                                 # formxpath=formxpath,
                                                 dont_click=True,
                                                 callback=self.after_login)]

    def after_login(self, response):
        if "authentication failed" in response.text:
            self.logger.error("Login failed")
            return
        print('response after login request', response.text)


        return [scrapy.Request('https://www.hackerrank.com/challenges/down-to-zero-ii/submissions/code/57407297',
                                    callback=self.parse_test)]

    def parse_test(self, response):
        print(response.xpath('//strong[@data-reactid="51"]').extract())
        print(response.url)
        print(dir(response), 'response directory')
        # print(response.text)
        # print(response.selector.xpath('//a[@class="btn btn-inverse view-results backbone"]'))
