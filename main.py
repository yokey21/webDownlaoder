# imported the requests library 
import requests

n = 10
while(n < 23):

    image_url = "http://www.math.yorku.ca/~alipm/math1019/LectureNotes/Lecture" + str(n) + ".pdf"
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url)  # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open("/Users/abyron/Desktop/CS365LEC/Lecture" + str(n) + ".pdf", 'wb') as f:
        # Saving received content as a png file in
        # binary format

        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)
    n += 1;