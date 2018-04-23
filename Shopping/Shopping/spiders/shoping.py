import scrapy
from Shopping.items import ShoppingItem
from scrapy.selector import Selector
# from scrapy.http import HtmlResponse

class Shoping(scrapy.Spider):
    
    name = 'shop' #name  of the crawler is shop
     
    def __init__(self, keyword='', page=1, *args, **kwargs):
        super(Shoping, self).__init__(*args, **kwargs)
        print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM,")
        print(*args)
        if keyword !='':
            self.start_urls = ['http://www.shopping.com/products~PG-'+str(page)+'?KW='+keyword]
        else :
            print("*************Keyword is null redirecting to home page*********************")
            self.start_urls = ['http://www.shopping.com']
 
    def parse(self, response):
        hxs = Selector(response)
        item=ShoppingItem()
        '''The span tag with class attribute 
        	equal to 'numTotalResults' gives the string with items on the page and 
        	total count 
        '''
        try:
          valueString=hxs.xpath('//span[@class="numTotalResults"]/text()').extract()
          print(valueString)
          if valueString == []:
            print("*****************No Page containing values****************")
          else:
            value= valueString[0]              
            start=value.index("of")
            item['totalCount']=value[start+2:]
            print("*****************Total results of the product***************   ")
            print(str(item['totalCount']))            
  
        except :
         	print("******************Element not found****************")
        '''
        	The div tag with attribute quicklookItem(regex quicklookItem ) inside 
        	form tag with attribute name equal to compareprd
        	gives total items in the page specified
        '''
        try :
            item['pageCount']=len(hxs.xpath('//form[@name="compareprd"]/div[contains(@id,"quickLookItem")]'))
            print("Total results on specified page "+str(item['pageCount']))
        except:
        	 print("**************Form Element not found*******************")