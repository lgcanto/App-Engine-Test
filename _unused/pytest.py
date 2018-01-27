# Gcloud commands:
# dev_appserver.py app.yaml    -> builds the app.yaml project locally
# gcloud app deploy            -> deploys app to current selected project
# gcloud app browse            -> browse deployed project

# with open('forms.html', 'r') as myfile:
#     form=myfile.read()
# print form

text = 'tes!t'
if '!' in text:
    num = text.index('!')
    if (num+3) > len(text):
        num = len(text) - num + 1
    else:
        print text[num+3]