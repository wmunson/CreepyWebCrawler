xml_str =('''<GetSingleItemResponse xmlns="urn:ebay:apis:eBLBaseComponents">
  <Timestamp>2012-10-25T03:09:50.817Z</Timestamp>
  <Ack>Success</Ack>
  <Build>E795_CORE_BUNDLED_15430047_R1</Build>
  <Version>795</Version>
  <Item>
     <Description>...</Description>
     <ItemID>330810813385</ItemID>
     <EndTime>2012-10-25T04:32:37.000Z</EndTime>
     <Location>Paypal Prefered</Location>
     <GalleryURL>...</GalleryURL>
     <PictureURL>...</PictureURL>
     <PictureURL>...</PictureURL>
     <PrimaryCategoryID>177</PrimaryCategoryID>
     <PrimaryCategoryName>
     Computers/Tablets & Networking:Laptops & Netbooks:PC Laptops & Netbooks
     </PrimaryCategoryName>
     <BidCount>2</BidCount>
     <ConvertedCurrentPrice currencyID="USD">294.99</ConvertedCurrentPrice>
     <ListingStatus>Active</ListingStatus>
     <TimeLeft>PT1H22M47S</TimeLeft>
     <Title>
     HP Compaq ZD8000 3800Mhz Full Loaded Ready to go, nice unit & super fast Laptop
     </Title>
     <ShippingCostSummary>
     <ShippingServiceCost currencyID="USD">23.99</ShippingServiceCost>
     <ShippingType>Flat</ShippingType>
     <ListedShippingServiceCost currencyID="USD">23.99</ListedShippingServiceCost>
     </ShippingCostSummary>
     <ItemSpecifics>
        <NameValueList>
           <Name>Operating System</Name>
           <Value>Windows XP Professional</Value>
        </NameValueList>
        <NameValueList>
           <Name>Screen Size</Name>
           <Value>17.0</Value>
        </NameValueList>
        <NameValueList>
           <Name>Processor Type</Name>
           <Value>Intel Pentium 4 HT</Value>
        </NameValueList>
     </ItemSpecifics>
     <Country>US</Country>
     <AutoPay>false</AutoPay>
     <ConditionID>2500</ConditionID>
     <ConditionDisplayName>Seller refurbished</ConditionDisplayName>
   </Item>
</GetSingleItemResponse>''')

import sys
import csv

from bs4 import BeautifulSoup as Soup

doc = Soup(xml_str, "html.parser")
data = []
cols = set()
print(type(doc))
for item in doc.findAll('item'):
	d = {}
	print('item ', item)
	for sub in item:
		if hasattr(sub, 'name'):
			print('suuuub ', type(sub))
			print(dir(sub))
			d[sub.name] = sub.text
	data.append(d)
	cols = cols.union(d.keys())

# cw = csv.writer(sys.stdout)
# cw.writerow(cols)
# for row in data:
# 	cw.writerow([row.get(k, 'N/A') for k in cols])