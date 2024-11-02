import requests
import json
import cv2
import time as t

pic = cv2.imread('singaporemap.png')
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlMDE5MzA0NGYyOTA5ZjY5YTRmMTllY2QxYjg0YWZkOCIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC1uZXctMTYzMzc5OTU0Mi5hcC1zb3V0aGVhc3QtMS5lbGIuYW1hem9uYXdzLmNvbS9hcGkvdjIvdXNlci9wYXNzd29yZCIsImlhdCI6MTczMDUyMjEyMiwiZXhwIjoxNzMwNzgxMzIyLCJuYmYiOjE3MzA1MjIxMjIsImp0aSI6IlFDQVNMcmczS2pvT3hPUzciLCJ1c2VyX2lkIjo1MDg3LCJmb3JldmVyIjpmYWxzZX0.YAYhwIROdd1uRkTsQc3LQ090XyoaED-_28Nd0PUQg1s"


# Reference markers
# image size = (1200, 675), origin in top left

# pic = cv2.circle(pic,(600,40),3,(0,0,255),2)
# 1.470556, 103.817222
# "Y": 50232.13700006985,
# "X": 26208.723300821424
# (600,40)

# pic = cv2.circle(pic,(534,483),3,(0,0,255),2)
# 1.254994, 103.785515
# "Y": 26396.431464672696,
# "X": 22679.797214726106
# (534,483)

# convert x: (26208.723300821424 - 22679.797214726106) / (600 - 534) = 53.46857706205027
# 26208.723300821424 / 53.46857706205027 - 600 = c
# X / 53.46857706205027 + 109.82942242120629

# convert y: (50232.13700006985 - 26396.431464672696) / (40 - 483) = -53.80520436884234
# 50232.13700006985 / -53.80520436884234 - 40 = d
# Y / -53.80520436884234 + 973.5925323454103


trees = open('treelandmark.txt','r')
treedata = trees.readlines()

for tree in treedata:
    # data = tree.strip().split(" ")
    # print(data)
    name, lat, lng, coordx, coordy = tree.strip().split(",")
    x = float(coordx) / 53.46857706205027 + 109.82942242120629
    y = float(coordy) / -53.80520436884234 + 973.5925323454103
    cv2.circle(pic, (int(x),int(y)), 1, (0,0,255), 1)

      
# Coord conversion API
# url = "https://www.onemap.gov.sg/api/common/convert/4326to3414?latitude=1.254994&longitude=103.785515"
# headers = {"Authorization": token}
# response = requests.request("GET", url, headers=headers)
# print(response.text)

# url = "https://www.onemap.gov.sg/api/public/themesvc/getAllThemesInfo?moreInfo=Y"
# url = "https://www.onemap.gov.sg/api/public/themesvc/getThemeInfo?queryName="


cv2.imshow("Singapore Map",pic)
cv2.waitKey(0)
cv2.imwrite("singaporetrees.png",pic)



'''Sub process code'''

'''Heritage tree retrieval'''
# url = "https://www.onemap.gov.sg/api/public/themesvc/retrieveTheme?queryName="

# headers = {"Authorization": token}
      
# query = "heritagetrees"
# response = requests.request("GET", url+query, headers=headers)

# text = response.text
# jsontext = json.loads(text)
# places = jsontext['SrchResults'][1:]

# coords = []

# for place in places:
#     name = place['NAME']
#     latlng: str = place["LatLng"]
#     lat = latlng.split(",")[0]
#     lng = latlng.split(",")[1]
#     coords.append([name,lat,lng])
#     # print(f"Name: {name}\n    Lat: {lat}\n    Lon: {lng}")

# # print(coords)

# print(f"Num: {len(places)}")


'''Coord conversion of landmarks'''
# f = open("treelandmark.txt","w")

# for place in coords:
#     url = f"https://www.onemap.gov.sg/api/common/convert/4326to3414?latitude={place[1]}&longitude={place[2]}"
#     headers = {"Authorization": token}
#     response = requests.request("GET", url, headers=headers)
#     resp = json.loads(response.text)
#     place.append(resp['X'])
#     place.append(resp['Y'])
#     print(f"{place[0]} {place[1]} {place[2]} {place[3]} {place[4]}")
#     f.write(f"{place[0]},{place[1]},{place[2]},{place[3]},{place[4]}\n")
#     t.sleep(0.1)

# f.close()