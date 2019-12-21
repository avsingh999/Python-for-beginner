# pip install google_images_download
from google_images_download import google_images_download  
  
# 객체생성
response = google_images_download.googleimagesdownload()  
  
search_queries = [
'The smartphone also features an in display fingerprint sensor.', 
'The pop up selfie camera is placed aligning with the rear cameras.', 
'''In terms of storage Vivo V15 Pro could offer 
   up to 6GB of RAM and 128GB of onboard storage.''', 
'The smartphone could be fuelled by a 3 700mAh battery.', 
] 
  
  
def downloadimages(query): 
    # keywords는 검색어입니다
    # format는 이미지 파일 형식입니다
    # limit는 다운로드 할 이미지 수입니다.
    # print urs는 이미지 파일 URL을 인쇄하는 것입니다
    # size는 수동으로 ("large, medium, icon") 를 지정할 수있는 이미지 크기입니다
    # aspect ratio은 다운로드 할 이미지의 높이 너비 비율을 나타냅니다. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":4, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"} 
    try: 
        response.download(arguments) 
      
    # NotFound 에러 파일처리     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # 검색된 쿼리에 대한 인자 제공
        try: 
            # 주어진 인자에 따라 사진 다운로드
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()
