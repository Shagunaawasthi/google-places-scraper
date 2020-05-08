
def __filter_string(self, str):
    strOut = str.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    return strOut
def __parse(self, review):

    item = {}

    id_review = review.find('button', class_='section-review-action-menu')['data-review-id']
    username = review.find('div', class_='section-review-title').find('span').text

    try:

        review_text = self.__filter_string(review.find('span', class_='section-review-text').text)
    except Exception as e:

        review_text = None

    rating = float(review.find('span', class_='section-review-stars')['aria-label'].split(' ')[1])
   
    item['id_review'] = id_review
    item['caption'] = review_text
    item['rating']=rating


def get_reviews(self, offset):



        # scroll to load reviews
    self.__scroll()

        # wait for other reviews to load (ajax)
    time.sleep(4)

        # expand review text
    self.__expand_reviews()

        # parse reviews
    response = BeautifulSoup(self.driver.page_source, 'html.parser')
    rblock = response.find_all('div', class_='section-review-content')
    parsed_reviews = []
    for index, review in enumerate(rblock):
        if index >= offset:
            parsed_reviews.append(self.__parse(review))

    return parsed_reviews



def __expand_reviews(self):

        # use XPath to load complete reviews
    links = self.driver.find_elements_by_xpath('//button[@class=\'section-expand-review blue-link\']')
    for l in links:
        l.click()
    time.sleep(2)


def __scroll(self):

    scrollable_div = self.driver.find_element_by_css_selector('div.section-layout.section-scrollbox.scrollable-y.scrollable-show')
    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)