from report.create_docs import create_doc_with_data
from report.take_screenshot import take_screenshot_chromeTabs

#Open all the site and login with crednetials
#activate/open chrome browser
#take screenshot
#switch tab and contiue taking screenshots
# create word document
# attach all the screenshot as per label
# report created
# report created



def create_report():
    screenshots_path='../screenshots/'
    tab_count=5
    position=(10, 100)
    size=(1440, 900)

    image_files=take_screenshot_chromeTabs(position,size,tab_count,screenshots_path)

    file_name='../docs/myReport.docx'
    doc_heading="My Perosnal Report"

    create_doc_with_data(file_name,doc_heading,image_files)

# Run the main function
if __name__ == "__main__":
    create_report()


