import scribus
from scribus import BUTTON_OK

page = 1
pagenum = scribus.pageCount()
images_content = 0
while (page <= pagenum):
    scribus.gotoPage(page)
    d = scribus.getPageItems()
    for item in d:
        if item[1] == 2:
            images_content += 1
    page += 1

scribus.messageBox('Counting images', 'Images: ' + str(images_content), BUTTON_OK)
