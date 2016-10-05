from lxml import html,etree
import requests

def conditions(apartment):
    if((float(apartment.get('egenAndel'))<4.000) and ((float(apartment.get('pricesPerSquare')))<40.000)
        and (float(apartment.get('area')))>70 and float(apartment.get('area'))<4000000):
        print(apartment.get('boligHtml'));

#page = requests.get('/html-sider/041016.html');
parser = etree.HTMLParser()
testtree   = etree.parse('html-sider/051016.html', parser);
result = etree.tostring(testtree.getroot(),
    pretty_print=True, method="html")
tree = html.fromstring(result);


area = tree.xpath("//div[contains(@class, ' area ')]//div[1]/text()");
boligHtml = tree.xpath("//a[contains(@class, 'more')]/@href");
address = tree.xpath("//div[contains(@class, 'address')]//a/text()");
endringProsent = tree.xpath("//div[contains(@class, 'pricedevelopment')]/text()");
pricesPerSquare = tree.xpath("//div[contains(@class, 'areapaymentcash')]/text()");
egenAndel = tree.xpath("//div[contains(@class, 'paymentexpenses')]//div[1]/text()");
numberOfRooms = tree.xpath("//div[contains(@class, 'numberofrooms')]/text()");
price = tree.xpath("//div[contains(@class, 'paymentcash')]//b/text()");

#remove \n
while '\n' in egenAndel: egenAndel.remove('\n');
while '\n' in area: area.remove('\n');
for i in range(0,len(area)):
    if (pricesPerSquare[i] == "-"):
        pricesPerSquare[i] = '0';
    if (egenAndel[i] == "-"):
        egenAndel[i] = '0';
    price[i] = price[i].replace('.','')



#print('Price: ', pricesPerSquare);
#print('EgenAndel: ', egenAndel);
#print('Prosent: ', endringProsent);
#print('HTML: ', boligHtml);
##print('Address: ', address);
#print('Area: ', area)
#print('Price: ', price)

apartmentList = [];
for i in range(0, len(area)):
    apartment = {};
    apartment['area'] = area[i];
    apartment['boligHtml'] = boligHtml[i];
    apartment['address'] = address[i];
    apartment['endringProsent'] = endringProsent[i];
    apartment['pricesPerSquare'] = pricesPerSquare[i];
    apartment['egenAndel'] = egenAndel[i];
    apartment['numberOfRooms'] = numberOfRooms[i];
    apartment['price'] = price[i];

    apartmentList.append(apartment);


for apartment in apartmentList:
    conditions(apartment);
